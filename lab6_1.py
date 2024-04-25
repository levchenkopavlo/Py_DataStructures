# Завдання 1
# Розроблення програми з таймером, що підраховує
# час. Використати JSON для збереження стану таймера
# (наприклад, поточний час) у файлі. При перезапуску
# програми відновити час збереженого стану за
# допомогою завантаження даних з JSON-файлу.

import json
import datetime
import time
import random


def save_time(time):
    prev_time = load_time()
    with open('time.json', 'w') as file:
        json.dump(prev_time + time, file)


def load_time():
    with open('time.json', 'r') as file:
        prev_time = json.load(file)
        return prev_time


timer = load_time()
start_timer = datetime.datetime.now().timestamp()
print('гра почалась')
time.sleep(random.randint(1, 20) / 15)
print('гра закінчилась')
stop_timer = datetime.datetime.now().timestamp()
save_time(stop_timer - start_timer)
print(f'час проведений в грі {load_time()}')

