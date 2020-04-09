import requests


def do_config():
    post_data={'file_content':'Hello World!'}
    r = requests.post('http://web',data=post_data)
    print(r.text)

def check_config(r):
    r = requests.get('http://web')
    print(r.text)
    return r

if __name__ == "__main__":
    
    result1=check_config(r)
    do_config()
    result2=check_config(r)
    
    target_info='Hello World!'

    if(target_info not in result1.text and target_info in result1.text):
        print('Config success!')
        exit 0
    else:
        print('Config failed!')
        exit -1