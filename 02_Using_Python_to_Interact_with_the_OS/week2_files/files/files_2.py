import customRWmethods
import os

os.chdir(
    "E:/Python/Google_IT_Automation_with_Python/02_Using_Python_to_Interact_with_the_OS/"
    + "week2_files/files"
)


class Travel:
    num = -1
    loc = "unknown"
    time = "unknown"
    tranportation = "unknown"
    groupType = -1

    def __str__(self) -> str:
        return "Travel number: {}, location: {}, time: {}, trasportaion: {}, groupType: {}".format(
            self.num, self.loc, self.time, self.tranportation, self.groupType
        )


textArr = customRWmethods.readFileIntoArr("all_travels.txt")


travels = []
attrsFlag = [False, False, False, False, False]

for line in textArr:
    if line.find("location: ") != -1:
        if attrsFlag[0] == True:
            travels.append(newTravel)

        locationNum = line.removeprefix("location: ")
        newTravel = Travel()
        newTravel.num = locationNum
        newTravelFlag = True
        attrsFlag = [True, False, False, False, False]
        continue

    if line.find("the location is: ") != -1 and attrsFlag[0] and not attrsFlag[1]:
        newTravel.loc = line.removeprefix("the location is: ")
        attrsFlag[1] = True
        continue

    elif line.find("the time is: ") != -1 and attrsFlag[0] and not attrsFlag[2]:
        newTravel.time = line.removeprefix("the time is: ")
        attrsFlag[2] = True
        continue

    elif line.find("how to go: ") != -1 and attrsFlag[0] and not attrsFlag[3]:
        newTravel.tranportation = line.removeprefix("how to go: ")
        attrsFlag[3] = True
        continue

    elif line.find("meeting type: ") != -1 and attrsFlag[0] and not attrsFlag[4]:
        newTravel.groupType = line.removeprefix("meeting type: ")
        attrsFlag[4] = True
        continue

if attrsFlag[0] == True:
    travels.append(newTravel)

travels.sort(key=lambda x: x.time)

for travel in travels:
    print(travel)
    print()

outputArrText = []

outputArrText.insert(0, "Total number of entries: {}".format(len(travels)))
for line in travels:
    outputArrText.append(line)


print(
    customRWmethods.writeInFileFromArr(
        outputArrText,
        "out_travels.txt",
    )
)
