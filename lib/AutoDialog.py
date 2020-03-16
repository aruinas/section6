import sys
from PyQt5.Qtwidgets import *

class AutoDialog(QDialog):
    def __init__(self):
        super().__init__()
        self.setupUI()

    def setupUI(self):
        self.setGeometry(200,500,200,200)
        self.setWindowTitle("인 증")
        self.setFixedSize(300,200)

        label_1=QLabel("ID ")
        label_2=QLabel("password ")

        self.lineEdit=QLineEdit()
        self.lineEdit=QLineEdit()
        self.lineEdit=selfEchoMode(QLineEdit().password)

        self.pushButton=QPushButton("로그인")
        #로그인버튼 활성=>이벤트 발생(시그널)
        self.pushButton.click.connect(self.submitLogin)

        layout.QGridLayout()
        layout.addWidget(label1,0,0)
        layout.addWidget(self.lineEdit1,0,1)
        layout.addWidget(self.pushButton,0,2)
        layout.addWidget(label2,1,0)
        layout.addwidget(self.lineEdit2,1,1)

        self.setLayout(layout)
    #슬롯
    def submitLogin(self):
        self.user_id=self.linedit1.text()
        self.user_pw=self.lineEdit2.text()
        print(self.user_id,self.user_pw)

        if self.user_id
