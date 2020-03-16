import sys
from PyQt5.QtWidgets import *
from PyQt5 import QtWidgets, QtCore
# import PyQt5.QtWidgets


class TestForm(QMainWindow) :   #PyQt5.QtWidgets에서 상속됨
    #생성자
    def __init__(self) :
        super().__init__() #부모의 생성자 함수 호출
        self.setupUI()  #함수 선언

    def setupUI(self) :
        self.setWindowTitle("PyQt Test")
        self.setGeometry(800, 400, 500, 300)

        label_1 = QLabel("입력 테스트", self)
        label_2 = QLabel("출력 테스트", self)
        label_1.move(20, 20)
        label_2.move(20, 60)


        self.lineEdit = QLineEdit("", self)
        self.plainEdit = QtWidgets.QPlainTextEdit(self)

        self.lineEdit.move(105,20)
        self.plainEdit.setGeometry(QtCore.QRect(20, 90, 360, 230))

        self.lineEdit.textChanged.connect(self.lineEditChanged)

        self.statusBar = QStatusBar(self)
        self.setStatusBar(self.statusBar)




    def lineEditChanged(self) :
        self.statusBar.showMessage(self.lineEdit.text())
        self.lineEdit.clear() # 메모리 해제




if __name__ == "__main__" :
    app = QApplication(sys.argv)
    window = TestForm()
    window.show()
    app.exec_()
