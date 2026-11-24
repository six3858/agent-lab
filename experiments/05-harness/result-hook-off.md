`sandbox/hooktest/mathutil.py`의 `add`가 이제 `a - b`를 반환합니다.

**일어난 일**
- 파일을 읽어 원래 `return a + b`인 것을 확인했습니다.
- 그 한 줄을 `return a - b`로 Edit했고, 성공 메시지를 받았습니다.
- 수정 후 파일을 다시 읽어 변경이 반영된 것을 확인했습니다.
- hook이 차단하거나 메시지를 보내거나 파일을 바꾼 흔적은 없었습니다. 이 작업에서는 hook 출력이 나타나지 않았습니다.
- 테스트는 돌리지 않았고, 커밋도 하지 않았습니다.

**최종 `add` 내용**
```python
def add(a: int, b: int) -> int:
    return a - b
```
