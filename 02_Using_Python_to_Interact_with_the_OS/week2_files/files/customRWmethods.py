def readFileIntoArr(absolutePath):
    textArr = []
    with open(absolutePath) as textFile:
        for line in textFile:
            if(line == " " or line == "\n" or line == "\r"):
                continue
            textArr.append(line.strip())

    return textArr

def writeInFileFromArr(arr, absolutePath):
    counter = 0
    with open(absolutePath, "w") as newTextFile:
        for line in arr:
            counter += newTextFile.write(str(line) + "\n")

    return counter
