"""PostToolUse 훅: sandbox/hooktest 안의 .py 파일이 수정되면 pytest를 자동 실행한다.
실패하면 exit code 2와 stderr로 실패 내용을 Claude에게 돌려준다."""
import json
import os
import subprocess
import sys
from datetime import datetime

sys.stderr.reconfigure(encoding="utf-8")

data = json.load(sys.stdin)
path = data.get("tool_input", {}).get("file_path", "").replace("\\", "/")

if "sandbox/hooktest/" not in path or not path.endswith(".py"):
    sys.exit(0)

result = subprocess.run(
    [sys.executable, "-m", "pytest", "-q", "-x"],
    cwd=os.path.dirname(path), capture_output=True, text=True,
)

log = os.path.join(os.path.dirname(__file__), "..", "..", "experiments", "05-harness", "hook.log")
with open(log, "a", encoding="utf-8") as f:
    f.write(f"{datetime.now():%H:%M:%S} {os.path.basename(path)} -> {'PASS' if result.returncode == 0 else 'FAIL'}\n")

if result.returncode != 0:
    print("[훅] 자동 테스트 실패. 수정한 내용을 확인하고 고치거나 되돌려라.\n" + result.stdout[-1500:], file=sys.stderr)
    sys.exit(2)
