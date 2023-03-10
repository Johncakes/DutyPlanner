import numpy as np
import datetime

eachtime=False
totalTime = False

userInput = input('Each time = 1, Total time = 2\n')
if userInput == '1':
  eachtime = True
else :
   totalTime = True

#Workers
workers = [{'name': '김민기', 'vac': False, 'wType': 't', 'points': 0, 'rec_point': [], 'p_avg': 0}, {'name': '오태연', 'vac': False, 'wType': 'i', 'points': 0, 'rec_point': [], 'p_avg': 0}, {'name': '신경민', 'vac': False, 'wType': 't', 'points': 0, 'rec_point': [], 'p_avg': 0}, {'name': '이승수', 'vac': False, 'wType': 't', 'points': 0, 'rec_point': [], 'p_avg': 0}, {'name': '노현', 'vac': False, 'wType': 't', 'points': 0, 'rec_point': [], 'p_avg': 0}, {'name': '박금강', 'vac': False, 'wType': 'g', 'points': 0, 'rec_point': [], 'p_avg': 0}, {'name': '서동현', 'vac': False, 'wType': 't', 'points': 0, 'rec_point': [], 'p_avg': 0}, {'name': '박건', 'vac': False, 'wType': 's', 'points': 0, 'rec_point': [], 'p_avg': 0}, {'name': '장건', 'vac': False, 'wType': 's', 'points': 0, 'rec_point': [], 'p_avg': 0}, {'name': '임상현', 'vac': False, 'wType': 'g', 'points': 0, 'rec_point': [], 'p_avg': 0}, {'name': '박종선', 'vac': False, 'wType': 'g', 'points': 0, 'rec_point': [], 'p_avg': 0}, {'name': '이일희', 'vac': False, 'wType': 'i', 'points': 0, 'rec_point': [], 'p_avg': 0}, {'name': '최혁', 'vac': False, 'wType': 'm', 'points': 0, 'rec_point': [], 'p_avg': 0}, {'name': '심혁', 'vac': False, 'wType': 't', 'points': 0, 'rec_point': [], 'p_avg': 0}, {'name': '채현우', 'vac': False, 'wType': 'g', 'points': 0, 'rec_point': [], 'p_avg': 0}, {'name': '허정현', 'vac': False, 'wType': 't', 'points': 0, 'rec_point': [], 'p_avg': 0}, {'name': '유창우', 'vac': False, 'wType': 't', 'points': 0, 'rec_point': [], 'p_avg': 0}]

removedWorkers=[]


looper = 1
for loops in range(30):
  numbers = [1,1,1,4.1,2.1,3.1,4.2,5,3.2,2.2]

  # number of people
  people = len(workers)

  for p in workers:
    p['rec_point'].append(0)

  # assign numbers to each person
  for i, number in enumerate(numbers):
    # if number == 1:
    #   removedWorkers.append() 
    min_avg_worker = min(workers, key=lambda x: x['p_avg'])
    min_avg_worker['points'] += number
    min_avg_worker['rec_point'].pop()
    min_avg_worker['rec_point'].append(number)
    min_avg_worker['p_avg'] = min_avg_worker['points'] /len(numbers)*looper 

  looper+=1


  #printing recorded points
if eachtime:
  for p in workers:
    print(p['name'],end=',')
    for x in p['rec_point']:
      print(x,end=',')
    print()
else :
  for p in workers:
    print(p['name'],end=',')
    print(round(p['points']))