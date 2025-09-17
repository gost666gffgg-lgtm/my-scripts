import requests

url = "https://raw.githubusercontent.com/gost666gffgg-lgtm/my-scripts/main/script.py"

response = requests.get(url)
if response.status_code == 200:
    with open("script.py", "w") as f:
        f.write(response.text)
    print("✓ Скрипт обновлён!")
else:
    print("✗ Ошибка загрузки")