PI = 3.14159

def get_area(radius):
    return PI * radius * radius

def print_name():
    print(__name__)

# python entry_module.py 와 같이 실행될 경우에는 
#__name__ 값이 __main__ 이 되며, 아래 코드가 실행됨
if __name__=='__main__':
    print(f'면적: {get_area(10)}')