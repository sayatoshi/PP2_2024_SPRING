def write_list(path: str, l: list):
    with open(path, "w", encoding="utf-8") as file:
        file.write(str(l))


if __name__ == "__main__":
    l = list((i for i in range(150)))
    write_list(r"C:/Users/tumas/Desktop/Python/lab5/regex5-1.py", l)