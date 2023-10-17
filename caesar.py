alphabet = "абвгдеёжзийклмнопрстуфхцчшщъыьэюя"

def coder(word, number):
    res = ""

    ...

    return res


def encoder(word, number):
    return coder(word, -number)


if __name__ == '__main__':
    t = coder("", 6)
    print(t)
    t = encoder(t, 6)
    print(t)