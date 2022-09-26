import csv
import os


def divide_data(file_name):
    """Function that divides date and data to different csv files

    Args:
        file_name (str): Path to file

    Raises:
        TypeError: File doesn't exist
    """
    if os.path.exists(file_name):
        with open(file_name, 'r', encoding='utf-8') as csvfile:
            reader_object = list(csv.reader(csvfile, delimiter=","))
            with open('X.csv', 'w', encoding='utf-8') as csvfile:
                writer = csv.writer(csvfile, lineterminator='\n')
                for elements in reader_object:
                    writer = csv.writer(csvfile, lineterminator='\n')
                    writer.writerow([str(elements[0])])
            with open('Y.csv', 'w', encoding='utf-8') as csvfile:
                writer = csv.writer(csvfile, lineterminator='\n')
                for elements in reader_object:
                    writer = csv.writer(csvfile, lineterminator='\n')
                    writer.writerow((
                        elements[1], elements[2], elements[3], elements[4], elements[5], elements[6],))
    else:
        raise TypeError('File does not exist')


file_name = 'result.csv'
divide_data(file_name)
