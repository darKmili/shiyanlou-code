#!/usr/bin/env python3
import requests
def download(url):
    '''
    从指定的URL下载文件并储存到当前目录
    URL：要下载内容的网址
    '''
    try:
        req = requests.get(url)
    except requests.exceptions.MissingSchema:
        print('invalid URL: {}'.format(url))
        return
    if req.status_code == 403:
        print('You do not have a authority to access this page')
        return
    filename = url.split('/')[-1]
    with open (filename,'w') as fobj:
        fobj.write(req.content.decode('utf-8'))
    print ("Download over.")
if __name__=='__main__':
    url = input('enter a URL')
    download(url)

