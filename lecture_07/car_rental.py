MENU = """Welcome to the minimal car-rental company.
0. Car availability
1. Rent car(s)
2. Return car(s)
3. Read T&C
4. Quit
Please choose an option: """


def read_availability():
    """Read from file and return the fleet (list of lists)."""
    fleet = []
    in_file = open("vehicles1.csv", "r", encoding="utf-8")

    for line in in_file.readlines():  # for each line
        car = line.split(",")  # convert the line into a list of str
        car[-1] = int(car[-1])  # convert the last str into a number
        fleet.append(car)  # append current car record into fleet

    in_file.close()
    return fleet  # list of lists


def write_availability(fleet):
    """Write file with updated number of cars."""
    out_file = open("vehicles1.csv", "w")

    # for each list(car) in the list of lists:
    for car in fleet:
        # convert the number into a str
        car[-1] = str(car[-1])
        #    convert the list(car) into a string delimited with ","
        line = ",".join(car)
        #    write that line into the out_file
        print(line, file=out_file)

    out_file.close()


def print_title(title):
    """Print the title in a nice manner."""
    print("=-" * 30)
    print(f"| {title:^56} |")
    print("=-" * 30)


def get_car_choice(fleet):
    """Get a valid car choice from the user."""
    choice = int(input("Choose a car: "))

    while choice < 0 or choice >= len(fleet):
        print(f"Choice must be between 0 and {len(fleet) - 1}!")
        choice = int(input("Choose a car: "))

    return choice

def display_available_cars(fleet):
    """Display available number of cars."""
    print("=" * 50)
    for index in range(len(fleet)):
        car_record = fleet[index]
        make = car_record[0]
        model = car_record[1]
        car_class = car_record[2]
        car_count = car_record[3]
        print(f"{index:2} | {make:16} | {model:12} | {car_class:3} | {car_count:3} |")
    print("=" * 50)


def rent_car(fleet):
    """Update the car count if there are available cars to rent."""

    # 1. display the available cars
    display_available_cars(fleet)

    # 2. get user input on choice car (make sure it's a valid one)
    choice = get_car_choice(fleet)

    # 3. update the number of cars if car is available (print a message)
    num_cars = fleet[choice][-1]
    if num_cars > 0:
        fleet[choice][-1] -= 1  # update by decreasing the count.
        print("Your car is available at check out.")
    else:
        print("Sorry, model not available at the moment.11")

    return fleet


def return_car(fleet):
    """Update the available car by +1"""

    # 1. display the fleet of cars
    display_available_cars(fleet)

    # 2. get car choice
    choice = get_car_choice(fleet)

    # 3. update the car count by +1
    fleet[choice][-1] += 1

    print("Car returned. Thank you!")

    return fleet


def display_terms_and_conditions():
    """Display the terms and conditions of the car rental."""
    in_file = open("terms.txt", "r", encoding="utf-8")

    line_count = 1
    for line in in_file.readlines():
        print(line.strip())
        if line_count % 10 == 0:  # if line numbers are in multiples of 10
            dummy = input("-+-+-+ Enter for more +-+-+-")  # after every 10 lines
        line_count += 1

    in_file.close()


def main():
    # 0. set up of data source / data base
    fleet = read_availability()  # read from file (list of lists)
    # print(fleet)   # for debugging purposes

    # 1. input
    choice = input(MENU)

    while choice != "4":
        # 2. process the input # 3 and output
        if choice == "0":
            print_title("0. Car Availability")
            display_available_cars(fleet)
        elif choice == "1":
            print_title("1. Renting a car")
            fleet = rent_car(fleet)
        elif choice == "2":
            print_title("2. Returning a car")
            fleet = return_car(fleet)
        elif choice == "3":
            print_title("3. Terms and Conditions")
            display_terms_and_conditions()
        else:
            print("Invalid choice!")

        print(" -.- " * 10)
        choice = input(MENU)  # ask again to eventually exit

    write_availability(fleet)  # update to file
    print("~=~. See you again soon! .~=~")


main()
