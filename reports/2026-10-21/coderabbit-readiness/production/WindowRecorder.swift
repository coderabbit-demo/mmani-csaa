import Foundation
import ScreenCaptureKit
import AVFoundation
import AppKit

final class RecorderDelegate: NSObject, SCRecordingOutputDelegate {
    var finished = false
    func recordingOutputDidStartRecording(_ output: SCRecordingOutput) { print("RECORDING STARTED"); fflush(stdout) }
    func recordingOutput(_ output: SCRecordingOutput, didFailWithError error: Error) { print("RECORDING ERROR: \(error)"); finished = true; fflush(stdout) }
    func recordingOutputDidFinishRecording(_ output: SCRecordingOutput) { print("RECORDING FINISHED"); finished = true; fflush(stdout) }
}

@main struct WindowRecorder {
    static func main() async throws {
        _ = NSApplication.shared
        let args = CommandLine.arguments
        let content = try await SCShareableContent.excludingDesktopWindows(true, onScreenWindowsOnly: false)
        if args.count < 4 {
            for window in content.windows where ["com.google.Chrome", "com.apple.Terminal"].contains(window.owningApplication?.bundleIdentifier ?? "") {
                print("\(window.windowID) | \(window.owningApplication?.applicationName ?? "") | \(window.title ?? "") | \(window.frame)")
            }
            return
        }
        guard let id = UInt32(args[1]), let window = content.windows.first(where: {$0.windowID == id}) else { fatalError("Window not found") }
        let file = URL(fileURLWithPath: args[2])
        let stop = args[3]
        let progress = args[4]
        let filter = SCContentFilter(desktopIndependentWindow: window)
        let config = SCStreamConfiguration()
        config.width = Int(window.frame.width) / 2 * 2
        config.height = Int(window.frame.height) / 2 * 2
        config.minimumFrameInterval = CMTime(value: 1, timescale: 30)
        config.showsCursor = true
        config.showMouseClicks = true
        config.capturesAudio = false
        config.captureMicrophone = false
        config.queueDepth = 6
        config.ignoreShadowsSingleWindow = true
        config.scalesToFit = true
        let rc = SCRecordingOutputConfiguration()
        rc.outputURL = file
        rc.videoCodecType = .h264
        rc.outputFileType = .mp4
        let delegate = RecorderDelegate()
        let output = SCRecordingOutput(configuration: rc, delegate: delegate)
        let stream = SCStream(filter: filter, configuration: config, delegate: nil)
        try stream.addRecordingOutput(output)
        try await stream.startCapture()
        while !FileManager.default.fileExists(atPath: stop) && !delegate.finished {
            let seconds = CMTimeGetSeconds(output.recordedDuration)
            let us = seconds.isFinite ? Int64(seconds * 1_000_000) : 0
            try? "out_time_us=\(us)\n".write(toFile: progress, atomically: true, encoding: .utf8)
            try await Task.sleep(nanoseconds: 200_000_000)
        }
        try await stream.stopCapture()
        for _ in 0..<100 where !delegate.finished { try await Task.sleep(nanoseconds: 100_000_000) }
        print("Saved: \(file.path), duration: \(CMTimeGetSeconds(output.recordedDuration)) seconds")
    }
}
