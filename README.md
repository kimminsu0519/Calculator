# 🧮 PyQt6 Calculator

PyQt6와 SymPy를 활용하여 제작한 심플하고 직관적인 데스크탑 계산기 애플리케이션입니다.  
기본 사칙연산부터 부호 반전, 소수점 입력, 예외 처리까지 다양한 기능을 지원합니다.

---

## 📄 프로젝트 개요

- **프로젝트명**: PyQt6 기반 GUI Calculator
- **주요 기술**: Python, PyQt6, SymPy
- **실행 환경**: Python 3.10 이상, PyQt6 설치 필요

---

## 📦 파일 구성

| 파일명 | 설명 |
|:------|:----|
| `Calculator.ui` | 계산기 UI 레이아웃 파일 (Qt Designer로 제작) |
| `main.py` | 계산기 기능 구현 및 실행 파일 |
| `Calculator_Test_Case.ods` | 테스트 케이스 문서 (기능별 테스트 시나리오 정리) |
| `requirements.txt` | 필수 패키지 목록 파일 |
| `LICENSE` | 오픈소스 라이선스 파일 (MIT) |
| `README.md` | 프로젝트 소개 문서 |

---

## ✨ 주요 기능

- **입력 버튼 표시 및 입력 기능**
  - 숫자 버튼 (`0-9`)
  - 소수점 버튼 (`.`)
  - 연산자 버튼 (`+`, `-`, `×`, `÷`, `%`)
  - 부호 반전 버튼 (`±`)
  - 초기화 버튼 (`AC`), 삭제 버튼 (`⌫`)
  - 등호 버튼 (`=`) 입력 처리
- **수식 계산 및 결과 출력**
  - `sympify`를 활용한 안전한 수식 계산
  - 정수/실수 결과를 상황에 맞게 출력
- **에러 처리**
  - 0으로 나누기 시: `"Cannot be divided by zero."`
  - 기타 오류 발생 시: `"Unknown ERROR. Please retry"`
- **이전 결과 표시**
  - 계산 결과를 `Ans = 결과값` 형식으로 상단에 표시

---

---

## 🚀 실행 방법

1. 저장소 클론
```bash
git clone https://github.com/kimminsu0519/Calculator.git
cd Calculator
```

2. 가상환경 및 의존성 설치
```bash
python3 -m venv venv
source venv/bin/activate  # (윈도우: venv\Scripts\activate)
pip install -r requirements.txt
```

3. 실행
```bash
python main.py
```

---

## 📜 라이선스

이 프로젝트는 [MIT License](./LICENSE) 하에 배포됩니다.

---

## 📌 추가 개발 예정

- 부호(±) 연산 개선 : 괄호를 도입하여 정확한 부호 연산이 가능하도록 기능 확장
- 고급 기능 추가 : 괄호 입력, 루트 연산, 메모리 저장 기능(M+, MR, MC) 구현 계획
- 키보드 입력 지원 : 버튼 클릭뿐 아니라 키보드 입력으로도 제어할 수 있도록 개선
- 계산 이력 저장 : 이전 수식과 결과를 스택 구조로 저장하여 조회 및 재사용 가능하도록 설계
- 수정 가능한 수식 입력창 : QLineEdit를 편집 가능하게 설정해, 수식 중간 수정 및 커서 이동 지원

---
