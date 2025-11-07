# Markdown to HTML 변환기

Markdown 파일을 스타일이 적용된 HTML 파일로 변환하는 GUI 프로그램입니다.

## 주요 기능

- PyQt5 기반의 직관적인 GUI 인터페이스
- Markdown 파일 선택 및 미리보기
- 스타일이 적용된 HTML 파일로 자동 변환
- output 폴더에 변환된 HTML 파일 자동 저장
- 테이블, 코드 블록, 줄바꿈 등 다양한 Markdown 확장 기능 지원

## 설치 방법

### 1. 저장소 클론 또는 다운로드

```bash
git clone <repository-url>
cd markdown2html
```

### 2. 가상환경 생성 및 활성화

#### Windows
```bash
python -m venv venv
venv\Scripts\activate
```

#### macOS/Linux
```bash
python -m venv venv
source venv/bin/activate
```

### 3. 의존성 패키지 설치

```bash
pip install -r requirements.txt
```

## 사용 방법

### 프로그램 실행

```bash
python main.py
```

### 사용 절차

1. 프로그램이 실행되면 GUI 창이 나타납니다
2. "MD 파일 선택" 버튼을 클릭하여 변환할 Markdown 파일을 선택합니다
3. 선택한 파일의 미리보기가 하단에 표시됩니다
4. "HTML로 변환 및 저장" 버튼을 클릭합니다
5. 변환이 완료되면 `output` 폴더에 HTML 파일이 생성됩니다

## 프로젝트 구조

```
markdown2html/
├── main.py              # 메인 프로그램 파일 (GUI 애플리케이션)
├── requirements.txt     # 의존성 패키지 목록
├── README.md           # 프로젝트 설명서
├── .gitignore          # Git 제외 파일 목록
└── output/             # 변환된 HTML 파일 저장 폴더 (자동 생성)
```

## 의존성 패키지

- `markdown==3.5.1` - Markdown을 HTML로 변환
- `PyQt5==5.15.10` - GUI 프레임워크

## 지원하는 Markdown 확장 기능

- **tables**: 테이블 지원
- **fenced_code**: 코드 블록 지원
- **nl2br**: 줄바꿈 자동 변환

## HTML 출력 특징

- 깔끔하고 모던한 스타일 적용
- 테이블에 그라데이션 헤더 적용
- 코드 블록에 다크 테마 적용
- 반응형 디자인 (최대 너비 800px)
- 인쇄 최적화 (A4 사이즈)

## 문제 해결

### PyQt5 설치 오류
Windows에서 PyQt5 설치 시 오류가 발생하면:
```bash
pip install --upgrade pip
pip install PyQt5
```

### 한글 깨짐 현상
- Markdown 파일과 HTML 파일 모두 UTF-8 인코딩을 사용합니다
- 파일 저장 시 UTF-8 인코딩으로 저장되었는지 확인하세요

## 라이선스

이 프로젝트는 자유롭게 사용 및 수정 가능합니다.
