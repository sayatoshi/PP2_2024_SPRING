import string, os

def func(path: str):
    if (not os.path.isdir(path)):
        os.mkdir(path)
    for i in string.ascii_uppercase:
        open(path + rf"\{i}.txt", "w").close()


if __name__ == "__main__":
    func(r"res")