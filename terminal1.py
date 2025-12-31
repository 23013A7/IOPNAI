from AI_core import zapros

def logo_info_start():
    print("ИОПН — Гениративная модель версия 0.4.1\n")
    print("Любой ввод — Запрос к гениративной модели")


def zickl():
    a = 1
    while a < 10:
        text = input("Запрос :")
        ai(text)

def ai(text):
    response = zapros(text)
    print("Ответ: ", response)

if __name__ == "__main__":
    logo_info_start()
    zickl()