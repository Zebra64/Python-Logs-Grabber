import glob
import os
import re
import time
from datetime import datetime
from os import system

system("title LogsGrabber By Zebra")
dir = input("Enter the path to the logs folder -->")
logs = glob.glob(f"{dir}/*/Passwords.txt")
os.system('cls')

vbt = "2"

tf = str(datetime.now().day) + '.' + str(datetime.now().month) + '_' + str(datetime.now().hour) + '.' + str(
    datetime.now().minute)

dir2 = 'Result/' + tf + '/'

os.makedirs('Result/' + tf)

if vbt == "2":
    print('Выполняется работа...\nПосле завершения программа автоматически закроется.')
    for pfile in logs:
        try:
            plist = []
            r = open(pfile, 'r+', errors="ignore").read()
            lst = re.findall("URL: https://(.+)/\nUsername: (.+)\nPassword: (.+)\n", r)
            for data in lst:
                if "." in str(data[0]):
                    url = str(data[0])
                    mail = str(data[1])
                    password = str(data[2])
                    plist.append(f"{mail}:{password}")
            wdpl = list(dict.fromkeys(plist))
            for line in wdpl:
                s = open(dir2 + url + '.txt', 'a', errors='ignore').write(f'{line}\n')
        except Exception:
            pass
os.system('cls')
print('Done!')
time.sleep(2)
quit()
