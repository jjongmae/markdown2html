"""
Markdown을 HTML로 변환하는 GUI 프로그램
"""
import os
import sys
import markdown
from PyQt5.QtWidgets import (
    QApplication, QMainWindow, QWidget, QVBoxLayout, QHBoxLayout,
    QPushButton, QFileDialog, QLabel, QMessageBox, QTextEdit
)
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QFont


class MarkdownToHtmlConverter(QMainWindow):
    """Markdown을 HTML로 변환하는 메인 윈도우"""

    def __init__(self):
        super().__init__()
        self.selected_file = None
        self.init_ui()

    def init_ui(self):
        """UI 초기화"""
        self.setWindowTitle('Markdown to HTML 변환기')
        self.setGeometry(100, 100, 800, 600)

        # 중앙 위젯 설정
        central_widget = QWidget()
        self.setCentralWidget(central_widget)

        # 메인 레이아웃
        main_layout = QVBoxLayout()
        central_widget.setLayout(main_layout)

        # 제목 라벨
        title_label = QLabel('Markdown to HTML 변환기')
        title_font = QFont()
        title_font.setPointSize(16)
        title_font.setBold(True)
        title_label.setFont(title_font)
        title_label.setAlignment(Qt.AlignCenter)
        main_layout.addWidget(title_label)

        # 파일 선택 영역
        file_layout = QHBoxLayout()
        self.file_label = QLabel('선택된 파일 없음')
        self.file_label.setStyleSheet('padding: 10px; border: 1px solid #ccc; border-radius: 5px;')
        file_layout.addWidget(self.file_label)

        select_btn = QPushButton('MD 파일 선택')
        select_btn.setStyleSheet('''
            QPushButton {
                background-color: #3498db;
                color: white;
                padding: 10px 20px;
                border: none;
                border-radius: 5px;
                font-weight: bold;
            }
            QPushButton:hover {
                background-color: #2980b9;
            }
        ''')
        select_btn.clicked.connect(self.select_file)
        file_layout.addWidget(select_btn)

        main_layout.addLayout(file_layout)

        # 미리보기 영역
        preview_label = QLabel('미리보기')
        preview_label.setStyleSheet('font-weight: bold; margin-top: 20px;')
        main_layout.addWidget(preview_label)

        self.preview_text = QTextEdit()
        self.preview_text.setReadOnly(True)
        self.preview_text.setStyleSheet('border: 1px solid #ccc; border-radius: 5px;')
        main_layout.addWidget(self.preview_text)

        # 변환 버튼
        convert_btn = QPushButton('HTML로 변환 및 저장')
        convert_btn.setStyleSheet('''
            QPushButton {
                background-color: #2ecc71;
                color: white;
                padding: 15px;
                border: none;
                border-radius: 5px;
                font-size: 14px;
                font-weight: bold;
            }
            QPushButton:hover {
                background-color: #27ae60;
            }
            QPushButton:disabled {
                background-color: #95a5a6;
            }
        ''')
        convert_btn.clicked.connect(self.convert_to_html)
        main_layout.addWidget(convert_btn)

        # 상태 라벨
        self.status_label = QLabel('')
        self.status_label.setAlignment(Qt.AlignCenter)
        main_layout.addWidget(self.status_label)

    def select_file(self):
        """MD 파일 선택"""
        file_path, _ = QFileDialog.getOpenFileName(
            self,
            'Markdown 파일 선택',
            '',
            'Markdown Files (*.md);;All Files (*)'
        )

        if file_path:
            self.selected_file = file_path
            self.file_label.setText(os.path.basename(file_path))
            self.show_preview(file_path)

    def show_preview(self, file_path):
        """Markdown 파일 미리보기"""
        try:
            with open(file_path, 'r', encoding='utf-8') as f:
                md_content = f.read()

            # 처음 500자만 표시
            if len(md_content) > 500:
                preview = md_content[:500] + '...'
            else:
                preview = md_content

            self.preview_text.setPlainText(preview)
            self.status_label.setText('파일이 선택되었습니다.')
            self.status_label.setStyleSheet('color: green;')

        except Exception as e:
            self.status_label.setText(f'파일 읽기 오류: {str(e)}')
            self.status_label.setStyleSheet('color: red;')

    def convert_to_html(self):
        """Markdown을 HTML로 변환하고 저장"""
        if not self.selected_file:
            QMessageBox.warning(self, '경고', '먼저 Markdown 파일을 선택해주세요.')
            return

        try:
            # Markdown 파일 읽기
            with open(self.selected_file, 'r', encoding='utf-8') as f:
                md_content = f.read()

            # Markdown을 HTML로 변환
            html_body = markdown.markdown(
                md_content,
                extensions=['tables', 'fenced_code', 'nl2br']
            )

            # 스타일이 적용된 HTML 템플릿
            html_template = self.get_html_template(html_body)

            # output 폴더 생성
            output_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'output')
            os.makedirs(output_dir, exist_ok=True)

            # 출력 파일명 생성
            base_name = os.path.splitext(os.path.basename(self.selected_file))[0]
            output_file = os.path.join(output_dir, f'{base_name}.html')

            # HTML 파일 저장
            with open(output_file, 'w', encoding='utf-8') as f:
                f.write(html_template)

            self.status_label.setText(f'변환 완료: {output_file}')
            self.status_label.setStyleSheet('color: green; font-weight: bold;')

            # 성공 메시지 박스
            QMessageBox.information(
                self,
                '변환 완료',
                f'HTML 파일이 성공적으로 생성되었습니다.\n\n저장 위치: {output_file}'
            )

        except Exception as e:
            self.status_label.setText(f'변환 오류: {str(e)}')
            self.status_label.setStyleSheet('color: red;')
            QMessageBox.critical(self, '오류', f'변환 중 오류가 발생했습니다:\n{str(e)}')

    def get_html_template(self, html_body):
        """HTML 템플릿 반환"""
        return f"""<!DOCTYPE html>
<html>
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Markdown 변환 결과</title>
    <style>
        @page {{
            size: A4;
            margin: 2cm;
        }}

        body {{
            font-family: "Malgun Gothic", "맑은 고딕", Arial, sans-serif;
            line-height: 1.6;
            color: #333;
            max-width: 800px;
            margin: 0 auto;
            padding: 20px;
            background: #fff;
        }}

        h1 {{
            color: #2c3e50;
            border-bottom: 4px solid #3498db;
            padding-bottom: 12px;
            margin-top: 30px;
        }}

        h2 {{
            color: #2980b9;
            border-bottom: 2px solid #3498db;
            padding-bottom: 8px;
            margin-top: 30px;
        }}

        h3 {{
            color: #34495e;
            margin-top: 25px;
        }}

        table {{
            border-collapse: collapse;
            width: 100%;
            margin: 25px 0;
            box-shadow: 0 2px 4px rgba(0,0,0,0.1);
        }}

        th {{
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
            color: white;
            padding: 14px;
            text-align: left;
            font-weight: bold;
            border: 1px solid #5a67d8;
        }}

        td {{
            border: 1px solid #ddd;
            padding: 12px;
            background: #fff;
        }}

        tr:nth-child(even) td {{
            background-color: #f8f9fa;
        }}

        tr:hover td {{
            background-color: #e3f2fd;
        }}

        code {{
            background-color: #f4f4f4;
            padding: 3px 8px;
            border-radius: 4px;
            font-family: "Consolas", "Monaco", monospace;
            font-size: 0.9em;
            color: #e74c3c;
        }}

        pre {{
            background-color: #2d2d2d;
            color: #f8f8f2;
            padding: 18px;
            border-radius: 6px;
            overflow-x: auto;
            border-left: 4px solid #3498db;
        }}

        pre code {{
            background: none;
            color: #f8f8f2;
            padding: 0;
        }}

        ul, ol {{
            margin-left: 25px;
            padding-left: 15px;
        }}

        li {{
            margin: 8px 0;
        }}

        blockquote {{
            border-left: 5px solid #3498db;
            padding-left: 20px;
            margin-left: 0;
            color: #555;
            background: #f9f9f9;
            padding: 15px 20px;
            border-radius: 4px;
        }}

        strong {{
            color: #2c3e50;
            font-weight: 700;
        }}

        hr {{
            border: none;
            border-top: 2px solid #ecf0f1;
            margin: 30px 0;
        }}

        @media print {{
            body {{
                margin: 0;
                padding: 15px;
            }}

            h1, h2, h3 {{
                page-break-after: avoid;
            }}

            table {{
                page-break-inside: avoid;
            }}
        }}
    </style>
</head>
<body>
{html_body}
</body>
</html>
"""


def main():
    """메인 함수"""
    app = QApplication(sys.argv)
    window = MarkdownToHtmlConverter()
    window.show()
    sys.exit(app.exec_())


if __name__ == "__main__":
    main()
