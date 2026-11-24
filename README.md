# agent-lab

Claude Code를 "신입사원"에 비유해 배우는 실습 저장소입니다.
프롬프트, 컨텍스트, 스킬, 서브에이전트, 하네스(훅과 권한), 플러그인, 에이전트 설계를 단계별 작은 실험으로 확인합니다.

## 문서와 발표자료

문서만 보고 이해하고 실습할 수 있도록 정리한 자료입니다. 파일을 눌러 **Download**로 내려받으세요.

| 자료 | 내용 |
|---|---|
| [실습 가이드 (Word)](docs/agent-lab-guide.docx) | 준비물과 내려받기, 단계별 개념, 따라 하기 명령, 결과 비교표, 용어집, 문제 해결 |
| [발표자료 (PowerPoint)](docs/agent-lab-slides.pptx) | 신입사원 비유 줄거리의 23장 슬라이드와 발표자 노트 |

두 파일은 `main`에만 있고 단계 태그(`step-1`~`step-7`)에는 들어 있지 않습니다.

## 단계별로 보기

각 단계는 **태그**로 저장돼 있어서, 그 시점의 파일 상태로 돌아가 볼 수 있습니다.

```bash
git checkout step-3   # 3단계 시점으로 이동
git checkout main     # 최신 상태로 복귀
```

## 한눈에 보기

| 단계 | 태그 | 신입사원 비유 | 한 줄 요약 | 실험 폴더 |
|---|---|---|---|---|
| 1 | `step-1` | 오늘 시키는 말 | 구체적으로 시킬수록 결과가 좋아진다 | [experiments/01-prompt](experiments/01-prompt) |
| 2 | `step-2` | 업무 규칙집 | `CLAUDE.md`가 있으면 매번 말하지 않아도 규칙을 지킨다 | [experiments/02-context](experiments/02-context) |
| 3 | `step-3` | 작업 매뉴얼 | 스킬로 같은 일을 항상 같은 모양으로 한다 | [experiments/03-skill](experiments/03-skill) |
| 4 | `step-4` | 검수 담당 동료 | 서브에이전트로 쓰는 사람과 검토하는 사람을 분리한다 | [experiments/04-subagent](experiments/04-subagent) |
| 5 | `step-5` | 출입증과 자동 점검 장치 | 훅과 권한으로 말이 아니라 시스템이 통제한다 | [experiments/05-harness](experiments/05-harness) |
| 6 | `step-6` | 도구 가방 | 플러그인으로 위 도구들을 묶어 다른 곳에서 쓴다 | [experiments/06-plugin](experiments/06-plugin) |
| 7 | `step-7` | 팀 짜기 | 전부 조합한 회의록 파이프라인 | [experiments/07-mini](experiments/07-mini) |

각 실험 폴더의 `NOTES.md`에 비교표와 발견한 점, 한계가 정리돼 있습니다.

## 폴더 구조

```
agent-lab/
├─ experiments/        단계별 실험 기록 (프롬프트, 결과, NOTES.md)
├─ sandbox/            에이전트가 만지는 실습용 코드
│  ├─ phone/           1단계: 전화번호 정규화와 pytest
│  ├─ hooktest/        5단계: 훅 실험용 작은 프로젝트
│  └─ mini/            7단계: 회의록 파이프라인
├─ plugins/
│  └─ agent-lab-kit/   6단계: 스킬, 에이전트, 훅을 묶은 플러그인
└─ .claude/            이 프로젝트에 적용되는 스킬, 에이전트, 훅, 권한
```

## 직접 해 보기

1. **스킬:** Claude Code에서 `/meeting-summary` 뒤에 회의 메모를 붙여 실행합니다. 항상 같은 4단 형식(결정사항, 할 일, 미해결 질문, 한 줄 요약)으로 나옵니다.
2. **서브에이전트:** "reviewer 에이전트로 sandbox/phone/phone.py를 리뷰해 줘"라고 요청합니다.
3. **훅:** `sandbox/hooktest/mathutil.py`의 `add`를 일부러 틀리게 고치게 하면, 수정 직후 테스트가 자동으로 돌아 실패합니다.
4. **플러그인:** 빈 폴더에서 `claude --plugin-dir <이 저장소 경로>/plugins/agent-lab-kit`로 실행합니다.
5. **파이프라인:** `sandbox/mini`에서 `/meeting-pipeline meeting-raw.txt`를 실행합니다.

## 필요한 것
- Claude Code
- Python 3 (`sandbox/`의 예제와 훅 스크립트)
- pytest (`pip install pytest`)

## 읽을 때 주의할 점
- 모든 실험은 **1회 실행** 결과입니다. 모델의 응답은 매번 조금씩 달라질 수 있어서, 경향을 보여 주는 자료로 읽어 주세요.
- 각 `NOTES.md`에 확인하지 못한 항목(한계)을 따로 적어 두었습니다.
- `.claude/settings.json`에는 `experiments/**/result*.md` 수정을 막는 권한 규칙이 들어 있습니다. 결과 파일을 직접 고치려면 이 규칙을 먼저 확인하세요.
- 커밋 날짜는 같은 날이며, 단계 태그는 완성된 파일을 단계별로 나눠 담은 것입니다.
