def to_seconds(hour, minutes, seconds):
    return hour * 3600 + minutes * 60 + seconds


def main():

    print()
    print("Welcome to MoMo time conversion ._.")
    print("This simple program takes hours, minutes and seconds then converts them to seconds")
    print()
    cont = "y"
    while(cont.lower() == "y"):
        hours = int(input("Enter the number of hours: "))
        minutes = int(input("Enter the number of minutes: "))
        seconds = int(input("Enter the number of seconds: "))

        print("This will be {} seonds.".format(to_seconds(hours, minutes, seconds)))

        cont = input("Do you want to do another conversion? [type y to continue and n to finish] ")

    print("Goodbye")

main()