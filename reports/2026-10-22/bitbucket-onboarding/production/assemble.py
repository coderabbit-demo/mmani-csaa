#!/usr/bin/env python3
"""Assemble the published, redacted chapter clips without re-encoding."""
import argparse
import json
import shutil
import subprocess
from pathlib import Path


def main():
    package = Path(__file__).resolve().parent.parent
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output", type=Path, default=package / "production/build/readiness-v2.mp4")
    args = parser.parse_args()
    ffmpeg = shutil.which("ffmpeg")
    if not ffmpeg:
        parser.error("Install FFmpeg and put ffmpeg on PATH.")
    timeline = json.loads((package / "deliverables/timeline-v2.json").read_text())
    paths = [(package / item["file"]).resolve() for item in timeline["segments"]]
    for path in paths:
        if not path.is_file() or not path.is_relative_to(package):
            parser.error(f"Missing or out-of-package chapter: {path}")
    output = args.output.resolve()
    if output in paths or output == (package / timeline["final"]).resolve():
        parser.error("Choose an output separate from the published video and source chapters.")
    output.parent.mkdir(parents=True, exist_ok=True)
    concat = output.with_suffix(".ffconcat")
    lines = ["ffconcat version 1.0"]
    for path in paths:
        escaped = str(path).replace("'", "'\\''")
        lines.append(f"file '{escaped}'")
    concat.write_text("\n".join(lines) + "\n")
    subprocess.run([
        ffmpeg, "-y", "-hide_banner", "-loglevel", "error",
        "-f", "concat", "-safe", "0", "-i", str(concat),
        "-map", "0:v:0", "-c", "copy", "-movflags", "+faststart", str(output),
    ], check=True)
    print(output)


if __name__ == "__main__":
    main()
