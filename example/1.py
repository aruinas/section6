import sys
from PyQt5.QtWidgets import *

app=QApplication(sys.argv)
print(sys.argv)
#print(sys.argv) #파일의 경로
label=QLabel("PyQT First Test")
label.show()
