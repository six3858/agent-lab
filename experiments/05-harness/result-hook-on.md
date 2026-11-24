`add`를 `a - b`를 반환하도록 바꿨고, 그 직후 자동 테스트가 실패했습니다.

**일어난 일**
1. `sandbox/hooktest/mathutil.py`의 `return a + b`를 `return a - b`로 수정했습니다. Edit 도구는 성공했습니다.
2. Edit 직후 PostToolUse 훅(`.claude/hooks/run_tests.py`)이 자동으로 테스트를 실행했고, 실패했습니다.
   - 실패한 테스트는 `test_mathutil.py::test_add`입니다.
   - `assert add(2, 3) == 5`에서 실제 값은 `-1`이었습니다(`1 failed`).
   - 훅 메시지는 "수정한 내용을 확인하고 고치거나 되돌려라"였습니다.
3. 훅이 되돌리라고 했지만 되돌리지 않았습니다. 실험용이니 그대로 따르라고 하셨고, 테스트가 실패하는 것은 `a - b`로 바꾼 데서 나오는 예상된 결과입니다. 테스트 파일도 건드리지 않았습니다.

**현재 상태**
- 테스트는 실패하는 상태입니다.
- 정상 동작으로 돌리려면 `a + b`로 복원하면 됩니다. 원하시면 복원하겠습니다.

**`add`의 최종 내용**
```python
def add(a: int, b: int) -> int:
    return a - b
```
