import os


def func(path: str):
    if os.access(path, os.F_OK):
        directory = "\\".join(path.split("\\")[:-1])
        print("Directory:", (directory if directory else "Nothing"))
        filename = path.split("\\")[-1]
        print("Filename: ", (filename if filename else "Nothing"))
    else:
        print(f"Path doesn't exist")


if __name__ == "__main__":
    func(r"C:\Users\tumas\Desktop\Python\lab5\regex5-1.txt")
    func(r"C:\Users\tumas\Desktop\Python\lab5\regex5-2.txt")
    func(r"C:\Users\tumas\Desktop\Python\lab5\regex5-3.txt")