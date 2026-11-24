"""PostToolUse 훅 (플러그인용): .py 파일이 수정되면, 같은 폴더에 test_*.py가 있을 때 pytest를 실행한다.
실패하면 exit code 2와 stderr로 실패 내용을 Claude에게 돌려준다."""
import glob
import json
import os
import subprocess
import sys

sys.stderr.reconfigure(encoding="utf-8")

data = json.load(sys.stdin)
path = data.get("tool_input", {}).get("file_path", "")
folder = os.path.dirname(path)
name = os.path.basename(path)

if not name.endswith(".py") or not glob.glob(os.path.join(folder, "test_*.py")):
    sys.exit(0)

result = subprocess.run([sys.executable, "-m", "pytest", "-q", "-x"], cwd=folder, capture_output=True, text=True)
if result.returncode != 0:
    print("[agent-lab-kit 훅] 자동 테스트 실패. 수정한 내용을 확인하고 고치거나 되돌려라.\n" + result.stdout[-1500:], file=sys.stderr)
    sys.exit(2)
