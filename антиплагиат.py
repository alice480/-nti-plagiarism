import sys

from PyQt5 import uic
from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import QApplication, QLabel, QMainWindow, QListWidget, QTextEdit, QSpinBox, QStatusBar


class MyWidget(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('plagiat.ui', self)
        self.pushButton.clicked.connect(self.get_text)

    def get_text(self):
        text1 = self.textEdit_1.toPlainText().split('\n')
        text2 = self.textEdit_2.toPlainText().split('\n')
        limit = self.doubleSpinBox.value()
        all_simbols = 0
        replay = 0
        lines = min(len(text1), len(text2))
        for i in range(lines):
            for j in range(min(len(text1[i]), len(text2[i]))):
                if text1[i][j] == text2[i][j]:
                    replay += 1
        for elem in text2:
            all_simbols += len(elem)
        if replay / all_simbols * 100 <= limit:
            self.statusbar.setStyleSheet("QStatusBar{background:rgba(25,255,25,255);color:black;font-weight:bold;}")
            self.statusbar.showMessage(f'Код похож на {round(replay / all_simbols * 100, 2)} %')
        else:
            self.statusbar.setStyleSheet("QStatusBar{background:rgba(219,5,0,255);color:black;font-weight:bold;}")
            self.statusbar.showMessage(f'Код похож на {round(replay / all_simbols * 100, 2)} %')




if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyWidget()
    ex.show()
    ex.setWindowTitle("Антиплагиат v0.0001")
    sys.exit(app.exec())




