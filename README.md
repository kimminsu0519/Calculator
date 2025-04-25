# 🧮 PyQt6 Calculator

> 심플하고 직관적인 UI의 데스크탑 계산기 애플리케이션  
> PyQt6 + SymPy 기반으로 구현된 GUI 계산기입니다.

---

## 📌 주요 기능

- 사칙연산: `+`, `-`, `×`, `÷`, `%` 지원
- 부호 반전(`±`) 기능
- `AC` (전체 초기화), `←` (한 글자 삭제)
- 소수점 입력 및 중복 방지
- 이전 결과값 `"Ans = "` 표시
- 연산자 중복 방지, 연산자 끝나는 수식 예외 처리
- `sympy`를 이용한 안전한 수식 계산

---

## 🖼️ UI 구성

| 요소 | 설명 |
|------|------|
| `lineEdit_prev` | 이전 계산식 또는 결과 (예: `Ans = 400`) |
| `lineEdit_curr` | 현재 입력 중인 수식 또는 결과 |
| 버튼 영역 | `QPushButton`으로 숫자, 연산자, 기능 구성 (5x4 Grid) |

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

## 🛠️ 사용 기술

- **Python 3**
- **PyQt6** – GUI 프레임워크
- **SymPy** – 수식 파싱 및 계산

---

## 📁 파일 구조

```
Calculator/
├── Calculator.ui       # Qt Designer로 만든 UI 파일
├── main.py             # PyQt6 로직 전체
├── README.md
└── requirements.txt
```

---

## 📷 스크린샷

![Calculator Screenshot](./screenshot.png)

---

## ✍️ 개발자

- 김민수 ([@kimminsu0519](https://github.com/kimminsu0519))

---

## 📝 License

이 프로젝트는 [MIT License](LICENSE)를 따릅니다.