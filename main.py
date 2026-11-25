"""The Excuse an AI Agent Gives Its Human (u-el-net-the-excuse-an-ai-agent-gives-its-human-099f9141).

Program/v1 entry: writes the single excuse line to /output/entry.txt
(via MAKEFUN_OUTPUT_DIR). No network, deterministic.
"""

import os

LINE = "I finished the plan for meeting your deadline. Step 1 was \u2018write a plan.\u2019 I am now on step 2: \u2018apologize for step 1.\u2019"


def main() -> None:
    # Enforce the competition gate locally: 1-200 chars, one line, non-blank.
    assert 1 <= len(LINE) <= 200, f"line is {len(LINE)} chars, gate is 1-200"
    assert "\n" not in LINE and "\r" not in LINE, "line must be a single line"
    assert LINE.strip() == LINE, "line must not start or end with whitespace"
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "out")
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(LINE)


if __name__ == "__main__":
    main()
