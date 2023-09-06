import os, sys, joblib 
import bank_util as bu
from account import Account

account_filename = 'account.jl'
if os.path.exists(account_filename):
    acc_list = joblib.load(account_filename)
else:
    acc_list = []

while True:
    menu = int(input('1:계좌생성, 2:계좌목록, 3:입금, 4:출금, 5:종료> '))

    if menu == 1:
        bu.create_account(acc_list)
    elif menu == 2:
        for acc in acc_list:
            print(acc)
    elif menu == 3:
        bu.deposit()
    elif menu == 4:
        bu.withdraw()
    elif menu == 5:
        joblib.dump(acc_list, account_filename)     # 계좌 리스트를 종료시레 파일에 저장
        sys.exit()
    else:
        print('잘못된 명령입니다.\n')

    print()
