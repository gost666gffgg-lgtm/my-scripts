import sys

if len(sys.argv) > 1:
    command = sys.argv[1]
    if command == "hello":
        print("Привет, друг!")
    elif command == "version":
        print("Версия 1.0")
    else:
        print("Неизвестная команда")
else:
    print("Использование: python script.py [команда]")
    print("Команды: hello, version")