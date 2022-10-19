from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from up import username, password
import time
from time import sleep
import datetime
from datetime import date
import csv
import discordwebhooks
from selenium.webdriver.chrome.options import Options

ser = Service("C:/geckodrive/chromedriver.exe") # add your webdriver path here
op = Options()
op = webdriver.ChromeOptions()
op.add_argument("--disable-infobars")
op.add_argument("start-maximized")
op.add_argument("--disable-extensions")
# op.add_argument("--start-maximized")
op.add_experimental_option("prefs", {"profile.default_content_setting_values.media_stream_mic": 1,
                                     "profile.default_content_setting_values.geolocation": 1,
                                     "profile.default_content_setting_values.media_stream_camera": 1,
                                     "profile.default_content_setting_values.notifications": 1})
driver = webdriver.Chrome(service=ser, options=op)

now = datetime.datetime.now()
n = now.strftime("%H:%M:%S")
today = date.today()
x = today.weekday()

if x == 0:
    z = 1
elif x == 1:
    z = 2
elif x == 2:
    z = 3
elif x == 3:
    z = 4
elif x == 4:
    z = 5

g = 1


def login(l):
    driver.maximize_window()
    driver.get(l)
    driver.find_element_by_xpath("/html/body/div/div/div/div[2]/div/button[2]").click()
    time.sleep(2)
    driver.find_element_by_xpath(
        "//input[@class='form-control ltr_override input ext-input text-box ext-text-box']").send_keys(username)
    driver.find_element_by_xpath(
        "//input[@class='win-button button_primary button ext-button primary ext-primary']").click()
    time.sleep(2)
    driver.find_element_by_xpath("//input[@id='i0118']").send_keys(password)
    driver.find_element_by_xpath("//input[@id='idSIButton9']").click()
    time.sleep(2)
    driver.find_element_by_xpath("//input[@id='idBtn_Back']").click()
    time.sleep(5)
    # driver.find_element_by_xpath("/html/body/div/form[1]/div/div/div[2]/div[1]/div/div/div/div/div/div[3]/div/div/div/div[2]/div/div/div[1]/div/div").click()


def join_class(start_time, end_time):
    try:
        driver.find_element_by_class_name("ts-calling-join-button").click()

    except:

        global g

        while g <= 15:
            print("Join button not found, trying again")
            time.sleep(60)
            driver.refresh()
            g += 1
            print(g)
            join_class(start_time, end_time)

        print("Seems like there is no class today")
        discordwebhooks.send_msg(status="no class", start_time=start_time, end_time=end_time)

    time.sleep(4)
    webcam = driver.find_element_by_xpath(
        '/html/body/div[1]/div[2]/div[2]/div[1]/div/calling-pre-join-screen/div/div/div[2]/div[1]/div[2]/div/div/section/div[2]/toggle-button[1]/div/button/span[1]')
    if webcam.get_attribute('title') == 'Turn camera off':
        webcam.click()
    time.sleep(1)

    microphone = driver.find_element_by_xpath(
        '/html/body/div[1]/div[2]/div[2]/div[1]/div/calling-pre-join-screen/div/div/div[2]/div[1]/div[2]/div/div/section/div[2]/toggle-button[2]/div/button/span[1]')
    if microphone.get_attribute('title') == 'Mute microphone':
        microphone.click()

    time.sleep(1)
    driver.find_element_by_xpath(
        '/html/body/div[1]/div[2]/div[2]/div[1]/div/calling-pre-join-screen/div/div/div[2]/div[1]/div[2]/div/div/section/div[1]/div/div/button').click()

    discordwebhooks.send_msg(status="joined", start_time=start_time, end_time=end_time)

    # leaving class code
    tmp = "%H:%M:%S"

    class_running_time = datetime.strptime(end_time, tmp) - datetime.strptime(start_time, tmp)

    time.sleep(class_running_time.seconds)

    driver.find_element_by_class_name("ts-calling-screen").click()

    driver.find_element_by_xpath('//*[@id="teams-app-bar"]/ul/li[3]').click()
    time.sleep(1)

    driver.find_element_by_xpath('//*[@id="hangup-button"]').click()
    print("Class left")
    discordwebhooks.send_msg(status="left", start_time=start_time, end_time=end_time)


running = True
while running:
    f = open('timetable for bot csv.csv', 'r')
    csvreader = csv.reader(f)
    row = []
    for i in csvreader:
        row.append(i)
    for i in range(1, 6):
        if "08:10:00" <= n <= "08:30:00":
            continue
            Link = row[i][z]
            login(Link)
            time.sleep(5)
            join_class("08:15:00", "09:15:00")
        elif "09:15:00" <= n <= "09:35:00":
            continue
            Link = row[i][z]
            login(Link)
            time.sleep(5)
            join_class("09:15:00", "10:15:00")
        elif "10:45:00" <= n <= "11:05:00":
            continue
            Link = row[i][z]
            login(Link)
            time.sleep(5)
            join_class("10:45:00", "11:45:00")
        elif "11:45:00" <= n <= "12:05:00":
            continue
            Link = row[i][z]
            login(Link)
            time.sleep(5)
            join_class("11:45:00", "12:45:00")

# add further if statements if you have more classes