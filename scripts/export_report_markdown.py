"""Convert the generated assessment HTML to a GitHub-readable Markdown snapshot."""

from html.parser import HTMLParser
from pathlib import Path
import re


class Node:
    def __init__(self, tag="", attrs=()):
        self.tag = tag
        self.attrs = dict(attrs)
        self.children = []


class Parser(HTMLParser):
    def __init__(self):
        super().__init__(convert_charrefs=True)
        self.root = Node()
        self.stack = [self.root]

    def handle_starttag(self, tag, attrs):
        node = Node(tag, attrs)
        self.stack[-1].children.append(node)
        if tag not in {"br", "col", "meta"}:
            self.stack.append(node)

    def handle_endtag(self, tag):
        for index in range(len(self.stack) - 1, 0, -1):
            if self.stack[index].tag == tag:
                del self.stack[index:]
                return

    def handle_data(self, data):
        self.stack[-1].children.append(data)


def descendants(node, tag):
    for child in node.children:
        if isinstance(child, Node):
            if child.tag == tag:
                yield child
            yield from descendants(child, tag)


def literal(node):
    return "".join(c if isinstance(c, str) else literal(c) for c in node.children)


def render(node, in_cell=False):
    if isinstance(node, str):
        return node
    tag = node.tag
    if tag in {"head", "style"}:
        return ""
    if tag == "table":
        rows = []
        for row in descendants(node, "tr"):
            cells = [c for c in row.children if isinstance(c, Node) and c.tag in {"th", "td"}]
            values = []
            for cell in cells:
                value = render(cell, True).strip().replace("|", "&#124;")
                values.append(value.replace("\n", " ").removesuffix("<br><br>"))
            rows.append("| " + " | ".join(values) + " |")
        if not rows:
            return ""
        columns = len([c for c in next(descendants(node, "tr")).children if isinstance(c, Node) and c.tag in {"th", "td"}])
        rows.insert(1, "| " + " | ".join(["---"] * columns) + " |")
        return "\n\n" + "\n".join(rows) + "\n\n"
    if tag == "pre":
        return "\n\n```yaml\n" + literal(node).rstrip() + "\n```\n\n"
    if tag in {"ul", "ol"}:
        items = [c for c in node.children if isinstance(c, Node) and c.tag == "li"]
        if in_cell:
            return "<br>".join("• " + render(c, True).strip() for c in items) + "<br>"
        return "\n\n" + "\n".join((f"{i}. " if tag == "ol" else "- ") + render(c).strip() for i, c in enumerate(items, 1)) + "\n\n"
    content = "".join(render(c, in_cell) for c in node.children)
    if tag in {"h1", "h2"}:
        level = 1 if node.attrs.get("class") == "title" else int(tag[1]) + 1
        return "\n\n" + "#" * level + " " + content.strip() + "\n\n"
    if tag == "p":
        return content.strip() + ("<br><br>" if in_cell else "\n\n")
    if tag == "br":
        return "<br>" if in_cell else "\n"
    if tag == "strong":
        return "**" + content + "**"
    if tag == "code":
        return "`" + content + "`"
    if tag == "a":
        return "[" + content + "](" + node.attrs["href"] + ")"
    return content


if __name__ == "__main__":
    directory = Path(__file__).resolve().parents[1] / "reports" / "2026-10-21"
    parser = Parser()
    parser.feed((directory / "coderabbit-assessment.html").read_text(encoding="utf-8"))
    markdown = render(parser.root)
    markdown = re.sub(r"\n{3,}", "\n\n", markdown).strip() + "\n"
    output = directory / "coderabbit-assessment.md"
    output.write_text(markdown, encoding="utf-8")
    print(output)
