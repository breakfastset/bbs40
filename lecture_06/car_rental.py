MENU="""Welcome to the minimal car-rental company.
0. Car availability
1. Rent car(s)
2. Return car(s)
3. Read T&C
4. Quit
Please choose an option: """

def read_availability():
    """Read from file and return the number of cars."""
    in_file = open("cars.txt", "r")
    line = in_file.readline()   # read the number (text)
    car_count = int(line)       # convert to integer
    in_file.close()
    return car_count

def write_availability(car_count):
    """Write file with updated number of cars."""
    out_file = open("cars.txt", "w")
    line = f"{car_count}"     # convert to a string
    print(line, file=out_file)
    out_file.close()

def print_title(title):
    """Print the title in a nice manner."""
    print("=-" * 30)
    print(f"| {title:^56} |")
    print("=-" * 30)

def display_available_cars(available_car_count):
    """Display available number of cars."""
    print_title("0. Car Availability")
    print(f"Number of cars available: {available_car_count}")

def rent_car(available_car_count):
    """Update the car count if there are available cars to rent."""
    print_title("1. Renting a car")
    if available_car_count > 0:    # there are cars to rent

        num_cars = int(input("How many cars do you wish to rent? "))

        if num_cars > 0:
            if num_cars <= available_car_count:
                available_car_count = available_car_count - num_cars
                print(f"Your {num_cars} car(s) is/are available at check out.")
            else:
                print("Sorry, we do not have enough cars to cater to your request.")
        else:
            print("Invalid number of cars! Number must be > 0!")
    else:
        print("Sorry, we have rented out all our cars.")
    return available_car_count

def return_car(available_car_count):
    """Update the available car by +1"""
    print_title("2. Returning a car")

    num_cars = int(input("How many cars do you wish to return? "))

    if num_cars > 0:
        available_car_count = available_car_count + num_cars
        print(f"Thank you for returning {num_cars} cars!")
    else:
        print("Invalid number of cars! Number must be > 0!")
    return available_car_count

def display_terms_and_conditions():
    """Display the terms and conditions of the car rental."""
    print_title("3. Terms and Conditions")
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
    available_car_count = read_availability()  # read from file

    # 1. input
    choice = input(MENU)

    while choice != "4":
        # 2. process the input # 3 and output
        if choice == "0":
            display_available_cars(available_car_count)
        elif choice == "1":
            available_car_count = rent_car(available_car_count)
        elif choice == "2":
            available_car_count = return_car(available_car_count)
        elif choice == "3":
            display_terms_and_conditions()
        else:
            print("Invalid choice!")

        print(" -.- " * 10)
        choice = input(MENU)  # ask again to eventually exit


    write_availability(available_car_count)  # update to file
    print("~=~. See you again soon! .~=~")

main()