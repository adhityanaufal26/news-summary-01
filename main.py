"""Write the 11 November 2026 world-news summary to /output/entry.txt.

The summary text lives in summary.txt next to this file; this program only
copies it, so both runs produce byte-identical output.
"""

import pathlib

HERE = pathlib.Path(__file__).resolve().parent


def main() -> None:
    text = (HERE / "summary.txt").read_text(encoding="utf-8").strip() + "\n"
    if not 1 <= len(text) <= 2000:
        raise SystemExit(f"summary is {len(text)} chars, must be 1-2000")
    out = pathlib.Path("/output/entry.txt")
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(text, encoding="utf-8")


if __name__ == "__main__":
    main()
