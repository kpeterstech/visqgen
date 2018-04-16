import csv
import datetime


def main():

    while True:
        # Call the get_XY function to have the user enter in their desired values
        # xy_values[0] = x axis values
        # xy_values[1] = y axis values
        # xy_values[2] = how much to shift the row

        xy_values = get_XY()

        # The x_line is the variable that the values that belong on the horizontal axis will be place into.
        # It is first created with two spaces. This is to align the values of the x axis with the y axis
        # all other values that belong on the x axis will be appened

        x_line = "  "
        for x in xy_values[0]:
            x_line += x
        print(x_line)

        x_line_len = len(xy_values[0])
        shift = xy_values[2]
        y_pos = 0 + shift
        for y in xy_values[1]:

            if y_pos > x_line_len:
                y_pos = y_pos - x_line_len
                tail = ''
                tail += xy_values[0][:y_pos]
                head = ''
                head += xy_values[0][y_pos:]
                completed = head + tail

            else:
                for x in xy_values[0]:
                    tail = ''
                    tail += xy_values[0][:y_pos]
                    head = ''
                    head += xy_values[0][y_pos:]
                    completed = head + tail
            print(f'{y} {completed}')
            y_pos += 1

        # Asks the user if they would like to save the results to a file

        save = input(
            "Would you like to save this table in a .csv file? (y/n): ")
        save = save.lower()

        if save == 'n':
            pass

        elif save == 'y':
            save_results(xy_values)

        elif save != 'y' or save != 'n':
            while True:
                save = input(
                    "Sorry, please let me know if you want to save with a (Y) or a (N): ")
                save = save.lower()

                if save == 'n':
                    break

                elif save == 'y':
                    save_results(xy_values)

        # Ask the user if they would like to immediatly create another table

        again = input("Would you like to create another table? (y/n): ")
        again = again.lower()

        if again == 'n':
            exit()

        elif again == 'y':
            continue

        elif again != 'y' or again != 'n':
            while True:
                again = input(
                    "Sorry, please let me know if you want to go again with a (Y) or a (N): ")
                again = again.lower()

                if again == 'n':
                    exit()

                elif again == 'y':
                    break


def get_XY():
    x = input("Please enter in the values you want on your X axis: ")
    if len(x) == 0:
        x_len = 0
        while x_len == 0:
            x = input("You need at least 1 value")
            x_len = len(x)

    y = input(
        "Please enter in the values you want on your Y axis (leave blank to input same values as X): ")
    if len(y) == 0:
        y = x

    shift = input(
        "How many places do you want to initially shift the row? (leave blank for a default of 0): ")
    if shift == '':
        shift = 0
    else:
        shift = int(shift)

    xy_values = [x, y, shift]

    return xy_values


def save_results(xy_values):

    name = input(
        "Enter the name you want to save the file as (if blank it will be saved as 'visqgen-YYYY-MM-DD-HH:MM:SS.csv'): ")

    if name == '':
        name = f"visqgen-{datetime.datetime.now():%Y-%m-%d-%H:%M:%S}"
        print(name)

    print("saving results...")
    with open(f'{name}.csv', 'w') as csv_file:
        csv_writer = csv.writer(csv_file)

        # The x_line is the variable that the values that belong on the horizontal axis will be place into.
        # It is first created with two spaces. This is to align the values of the x axis with the y axis
        # all other values that belong on the x axis will be appened

        x_line = " "
        for x in xy_values[0]:
            x_line += f'{x}'
        csv_writer.writerow(x_line)

        x_line_len = len(xy_values[0])
        shift = xy_values[2]
        y_pos = 0 + shift
        for y in xy_values[1]:

            if y_pos > x_line_len:
                y_pos = y_pos - x_line_len
                tail = ''
                tail += xy_values[0][:y_pos]
                head = ''
                head += xy_values[0][y_pos:]
                completed = head + tail

                completed_with_commas = ''
                for j in completed:
                    completed_with_commas += f'{j}'

                csv_writer.writerow(f'{y}{completed_with_commas}')

            else:
                for x in xy_values[0]:
                    tail = ''
                    tail += xy_values[0][:y_pos]
                    head = ''
                    head += xy_values[0][y_pos:]
                    completed = head + tail

                    completed_with_commas = ''
                    for j in completed:
                        completed_with_commas += f'{j}'

                csv_writer.writerow(f'{y}{completed_with_commas}')
            y_pos += 1
    print("Done")


if __name__ == '__main__':
    main()
