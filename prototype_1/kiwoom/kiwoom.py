from PyQt5.QAxContainer import * 
from PyQt5.QtCore import *
from config.errorCode import *

class Kiwoom(QAxWidget):
    def __init__(self):
        super().__init__()
        print("Kiwoom() class start.")
        
        ###### 초기 셋팅 함수들 바로 실행 
        
        self.get_ocx_instance() # OCX 방식 파이썬에 사용할 수 있게 변환
        self.event_slots() # 키움과 연결하기 위한 시그널/슬롯
        self.signal_login_commConnect() #로그인 요청 함수 포함 
        self.get_account_info()
        
        ###### event loop 를 실행하기 위한 변수모음
        self.login_event_loop = QEventLoop() #로그인 요청용 이벤트루프 
        
    def event_slots(self):
        self.OnEventConnect.connect(self.login_slot) # 로그인 관련 이벤트 
        
    def get_ocx_instance(self):
        self.setControl("KHOPENAPI.KHOpenAPICtrl.1") 
        
    def signal_login_commConnect(self):
        self.dynamicCall("CommConnect()") #로그인 요청 시그널
        
        self.login_event_loop.exec_()  #이벤트 루프 실행 
        
    def login_slot(self, err_code):
        print(errors(err_code)[1])
        
        #로그인 처리 완료시 루프 종료
        self.login_event_loop.exit()
    def get_account_info(self):
        account_lsit = self.dynamicCall("GetLoginInfo(QString)","ACCNO") # 계좌번호 반환
        account_num = account_lsit.split(';')[0] # a;b;c -> [a,b,c]
        self.account_num = account_num
        print('계좌번호 : %s' % account_num) 
               