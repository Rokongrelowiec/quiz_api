class bcolors:
    OK = '\033[92m'
    FAIL = '\033[91m'
    RESET = '\033[0m'
    WARNING = '\033[93m'

import requests

response = requests.get('https://opentdb.com/api.php?amount=10&category=18&difficulty=easy&type=boolean')

points = 0

if response.status_code != requests.codes.ok:
    print('Something went wrong!')
else:
    var = response.json()['results']
    print("Category:", var[0]['category'])
    for i in range(10):
        question = var[i]['question'].replace('&quot;', '"')
        print(question, '?')
        answer = input("Answer[True/False]: ").strip()
        if answer.upper() == var[i]['correct_answer'].upper():
            print(f"{bcolors.OK}{answer}{bcolors.RESET}")
            points += 1
        else:
            print(f"{bcolors.FAIL}{answer}{bcolors.RESET}")
if points >= 7:
    color = bcolors.OK
elif points >= 5:
    color = bcolors.WARNING
else:
    color = bcolors.FAIL

print(f"You have earned {color}{points}{bcolors.RESET}/10 points!")

