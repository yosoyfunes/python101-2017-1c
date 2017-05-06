

if __name__ == '__main__':
    mFile = open("miarchivo2.txt", "w+")
    mFile.write("asdasd")
    mFile.close()
    mFile = open("miarchivo2.txt", "r")
    print(mFile.read())
    mFile.close()
