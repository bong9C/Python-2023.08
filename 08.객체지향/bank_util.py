import datetime as dt
from account import Account

# 입력: 이름, 금액, 통장번호: 현재 시분초 6자리
# Account를 생성하며 acc_list에 append
def create_account(acc_list):
    cmd = input('이름 금액=>').split()
    name, amount = cmd[0], int(cmd[1])
    now = dt.datetime.now()
    ano = now.strftime('%H%M%S')
    account = Account(ano, name, amount) 
    acc_list.append(account)



def deposit():
    print('입금')
    pass

def withdraw():
    print('출금')
    pass