#!/usr/bin/python
import requests
import sys
def send_message(tocken,chat,text):
    url = "https://api.telegram.org/{}/sendMessage?chat_id={}&text={}".format(tocken,chat,text)
    response = requests.get(url)
    return response

if __name__ == '__main__':
    if send_message(sys.argv[1],sys.argv[2],sys.argv[3]) == "<Response [200]>":
        print("")
       
        
