import os
def func(path: str):
    names = os.listdir(path)
    print("All files:", ", ".join(names))
    print("Only directories:", ", ".join(x for x in names if os.path.isdir(rf"{path}\{x}")))
    print("Only files:", ", ".join(x for x in names if not os.path.isdir(rf"{path}\{x}")))


if __name__ == "__main__":
    func(r"LAB1")
    func(r"LAB4")