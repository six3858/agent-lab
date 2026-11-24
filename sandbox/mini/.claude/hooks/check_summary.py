"""PostToolUse 훅: out/summary.md가 저장되면 4개 필수 섹션이 순서대로 있는지 검사한다.
빠지면 exit 2로 Claude에게 알려 고치게 한다. 실행 기록은 out/hook.log."""
import json
import os
import sys
from datetime import datetime

sys.stderr.reconfigure(encoding="utf-8")
data = json.load(sys.stdin)
path = data.get("tool_input", {}).get("file_path", "").replace("\\", "/")
if not path.endswith("out/summary.md"):
    sys.exit(0)

required = ["## 결정사항", "## 할 일", "## 미해결 질문", "## 한 줄 요약"]
text = open(path, encoding="utf-8").read()
pos = [text.find(h) for h in required]
ok = all(p >= 0 for p in pos) and pos == sorted(pos)

with open(os.path.join(os.path.dirname(path), "hook.log"), "a", encoding="utf-8") as f:
    f.write(f"{datetime.now():%H:%M:%S} summary.md -> {'PASS' if ok else 'FAIL'}\n")

if not ok:
    print("[훅] summary.md에 필수 섹션 4개가 순서대로 있지 않다: " + ", ".join(required), file=sys.stderr)
    sys.exit(2)
