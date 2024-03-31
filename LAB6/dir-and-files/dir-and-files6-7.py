def func(file_from: str, file_to: str):
    f = open(file_from, "r", encoding="utf-8")
    ff = open(file_to, "w", encoding="utf-8")
    ff.write(f.read())
    f.close()
    ff.close()


if __name__ == "__main__":
    func(r"sample-data.json", r"sample-data2.json")