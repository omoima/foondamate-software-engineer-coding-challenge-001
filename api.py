from datetime import datetime
from  Userbase import *
import requests

url = "http://sam-user-activity.eu-west-1.elasticbeanstalk.com/"

def get_userbase():
    response = requests.get(url=url)
    return response

def userbase_list():
    response = get_userbase().json()
    list = []
    for a in response:
        list.append(Userbase(a,response[a]))
    return list

def filter(start, end):
    print(    )


def print_bars():
    print("YEAH")    

if __name__ == '__main__':
    userbase_list()