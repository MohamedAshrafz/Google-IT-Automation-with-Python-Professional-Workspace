class Travel:
    num = -1
    loc = ""
    time = ""
    tranportation = ""
    groupType = -1

    def __str__(self) -> str:
        return "Travel number: {}, location: {}, time: {}, trasportaion: {}, groupType: {}".format(
            self.num, self.loc, self.time, self.tranportation, self.groupType
        )


newFile = open(
    "E:/Python/Google_IT_Automation_with_Python/02_Using_Python_to_Interact_with_the_OS/"
    + "week2_files/files/all_travels_1.txt"
)
fileText = newFile.read().split("\n")

travels = []

i = 0
while i < len(fileText):
    line = fileText[i]
    mLine = line.split(" ")[0]

    if line == "" or line == "\n":
        i += 1
        continue
    if line.find("location: ") != -1:
        locationNum = line.removeprefix("location: ")
        i += 1
        newTravel = Travel()
        newTravel.num = locationNum

        for j in range(0, 4):
            line = fileText[i]

            if line.find("the location is: ") != -1:
                newTravel.loc = line.removeprefix("the location is: ")
                i += 1
                continue

            elif line.find("the time is: ") != -1:
                newTravel.time = line.removeprefix("the time is: ")
                i += 1
                continue

            elif line.find("how to go: ") != -1:
                newTravel.tranportation = line.removeprefix("how to go: ")
                i += 1
                continue

            elif line.find("meeting type: ") != -1:
                newTravel.groupType = line.removeprefix("meeting type: ")
                i += 1
                continue

        travels.append(newTravel)

for travel in travels:
    print(travel)
    print()


newFile.close()
