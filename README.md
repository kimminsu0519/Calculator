# PyQt6 계산기 🧮

이 프로젝트는 **Python**과 **PyQt6**를 활용해 제작한 간단한 계산기 애플리케이션입니다.  
덧셈, 뺄셈, 곱셈, 나눗셈, 퍼센트 계산, 부호 반전, 소수점 입력 등 기본적인 연산 기능을 지원합니다.

## 주요 기능

- 🧠 **기본 연산 지원**: 직관적인 버튼 매핑을 통해 덧셈, 뺄셈 등 계산 기능 제공
- ✨ **깔끔한 UI**: Qt Designer로 설계된 깔끔하고 사용하기 쉬운 인터페이스
- 🧩 **모듈화된 코드**: 유지보수가 쉽도록 각 기능을 메서드로 분리
- ✅ **오류 처리**: 0으로 나누기 등 예외 상황에 대한 처리 포함

## 스크린샷

> *(필요 시 여기에 스크린샷을 삽입하세요)*

## 설치 방법

1. 레포지토리를 클론합니다:
    ```bash
    git clone https://github.com/your-username/pyqt6-calculator.git
    cd pyqt6-calculator
    ```

2. 필요한 패키지를 설치합니다:
    ```bash
    pip install -r requirements.txt
    ```

3. 애플리케이션을 실행합니다:
    ```bash
    python main.py
    ```

## 실행 환경

- Python 3.9 이상
- PyQt6
- sympy (수식 계산용)

## 폴더 구조

```
📁 pyqt6-calculator/
├── Calculator.ui       # Qt Designer로 만든 UI 파일
├── main.py             # 메인 실행 코드
├── calculator.py       # 계산기 로직 및 이벤트 처리
├── README.md
└── requirements.txt
```

---

Fork, Star, 그리고 기여는 언제든지 환영입니다! 🚀
