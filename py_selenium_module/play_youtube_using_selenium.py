from selenium import webdriver
import time
import random
import pafy


import json




driver = webdriver.Chrome('chromedriver.exe')

videos = [
    'https://www.youtube.com/watch?v=IZn43q1Mue8',
    'https://www.youtube.com/watch?v=DzzME0sHU_Y'

]

random_video = random.randint(0, 1)

for i in range(1900):
    driver.get(videos[random_video])
    video = pafy.new(videos[random_video])
    print(video.length)
    print('Playing....' + video.title)

    sleep_time = video.length
    time.sleep(sleep_time)


driver.quit()