from datetime import datetime
from  Userbase import *
import requests
import matplotlib.pyplot as plt

url = "http://sam-user-activity.eu-west-1.elasticbeanstalk.com/"

def get_userbase():
    response = requests.get(url=url)
    return response


def userbase_list():
    response = get_userbase().json()
    list = []
    for a in response:
        list.append(Userbase(datetime.strptime(a,'%d-%m-%Y').date(),response[a]))
    return list


def filter(start, end):
    final = []
    list = userbase_list()
    try:
        for a in list:
            if (a.date >= start) and (a.date <= end):
                final.append(a)
    except:
        print("Dates specified are invalid.")
    return final


def print_graph(list):
    if len(list) == 0:
        print("No dates are within range")
        return

    x_array = []
    y_array = []
    for base in list:
        x_array.append(base.date)
        y_array.append(base.users)
    
    plt.plot(x_array, y_array)
    plt.xlabel('Date')
    plt.ylabel('Users Count')
    plt.title('Userbase Growth')
    plt.show()
