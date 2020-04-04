import requests

def do_poc():
    r = requests.get('http://web')
    print(r.text)
    return r
def check_poc(r):
    if('Hello World!' in r.text):
        print('Poc success!')
        return 0
    else:
        print('Poc failed!')
        return -1

if __name__ == "__main__":
    r=do_poc()
    result=check_poc(r)
    exit(result)