# match case
# Supported from Python 3.10+
# Only supports integer and character
day = int(input("Enter a number(1-7): "))

match day:
    case 1:
        print("Monday")
    case 2:
        print("Tuseday")
    case 3:
        print("Wednesday")
    case 4:
        print("Thursday")
    case 5:
        print("Friday")
    case 6:
        print("Saturday")
    case 7:
        print("Sunday")
    case _:
        # Default case if no match
        print("Invalid")