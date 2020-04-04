import requests

def do_config():
    r = requests.get('http://web')
    print(r.text)
    return r
def check_config(r):
    if('Hello World!' in r.text):
        print('Config success!')
        return 0
    else:
        print('Config failed!')
        return -1

if __name__ == "__main__":
    r=do_config()
    result=check_config(r)
    exit(result)