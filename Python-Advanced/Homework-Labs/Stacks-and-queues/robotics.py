from math import floor
from collections import deque


class Robot:
    def __init__(self, name, processing_time):
        self.name = name
        self.processing_time = int(processing_time)
        self.busy_until = 0

    def __str__(self):
        return f'{self.name} has a processing time of {self.processing_time} minutes'


def get_seconds_from_time(time):
    hours, minutes, seconds = [int(i) for i in time.split(':')]
    return hours * 60 * 60 + minutes * 60 + seconds


def get_time_from_seconds(seconds):
    seconds %= 24 * 60 * 60
    hours = seconds // (60*60)
    minutes = floor((seconds/60) % 60)
    seconds = seconds % 60
    return f'{hours:02d}:{minutes:02d}:{seconds:02d}'


robots = []
robot_input = input().split(";")
for robot in robot_input:
    robot_name, robot_processing_time = robot.split("-")
    robots.append(Robot(robot_name, robot_processing_time))

time = input()
time_in_seconds = get_seconds_from_time(time)

product_queue = deque()

while True:
    product = input()
    if product == "End":
        break
    product_queue.append(product)

while product_queue:
    current_product = product_queue.popleft()
    time_in_seconds += 1
    found_robot = False

    for robot in robots:
        if time_in_seconds >= robot.busy_until:
            robot.busy_until = time_in_seconds + robot.processing_time
            found_robot = True
            print(f'{robot.name} - {current_product} [{get_time_from_seconds(time_in_seconds)}]')
            break
    if not found_robot:
        product_queue.append(current_product)

