import requests
import os
import time

def update_script():
    url = "https://raw.githubusercontent.com/gost666gffgg-lgtm/my-scripts/main/script.py"
    
    try:
        response = requests.get(url)
        if response.status_code == 200:
            with open("my_script.py", "w") as f:
                f.write(response.text)
            print("Скрипт обновлён!")
            return True
        else:
            print("Ошибка загрузки!")
            return False
    except:
        print("Нет интернета!")
        return False


while True:
    update_script()
    time.sleep(300) 