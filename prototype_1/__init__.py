#프로그램 실행시킬 Main Class
from kiwoom.kiwoom import *
import sys
from PyQt5.QtWidgets import*


class Main():
    def __init__(self):
        print("Main() start")
        
        self.app = QApplication(sys.argv) #Pyqt5로 실행할 파일명 자동설정 (동시성 처리)
        self.kiwoom = Kiwoom() # 키움 클래스 객체화
        self.app.exec_() # 이벤트 루프 실행 
if __name__ == "__main__":
    Main()