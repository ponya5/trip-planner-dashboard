#!/usr/bin/env python3
"""
Extract the <script> block(s) from a trip-dashboard HTML file and check them
for JavaScript syntax errors before the file is considered finished.

Usage:
    python verify_js.py path/to/dashboard.html

Requires Node.js (for `node --check`). Exits non-zero and prints the node
error if the script has a syntax error; otherwise prints OK and the byte size
of the extracted script, so a silently-truncated write is also noticeable.
"""
import re
import subprocess
import sys
import tempfile
import os


def main():
    if len(sys.argv) != 2:
        print("Usage: python verify_js.py path/to/dashboard.html", file=sys.stderr)
        sys.exit(2)

    html_path = sys.argv[1]
    with open(html_path, encoding="utf-8") as f:
        html = f.read()

    scripts = re.findall(r"<script>(.*?)</script>", html, re.S)
    if not scripts:
        print("No inline <script> blocks found — nothing to check.")
        sys.exit(0)

    js = "\n".join(scripts)

    with tempfile.NamedTemporaryFile(
        mode="w", suffix=".js", delete=False, encoding="utf-8"
    ) as tmp:
        tmp.write(js)
        tmp_path = tmp.name

    try:
        result = subprocess.run(
            ["node", "--check", tmp_path], capture_output=True, text=True
        )
    finally:
        os.unlink(tmp_path)

    print(f"Extracted script size: {len(js)} bytes")
    if result.returncode != 0:
        print("SYNTAX ERROR:")
        print(result.stderr)
        sys.exit(1)

    print("OK — no syntax errors.")
    sys.exit(0)


if __name__ == "__main__":
    main()
