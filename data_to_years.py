import csv
import os


def name_for_file(first_part: str, second_part: str) -> str:
    """Creates a name for file

    Args:
        first_part (str): First part of future file's name
        second_part (str): Second part of future file's name
    Returns:
        str: Name in special format
    """
    if __name__ == '__main__':
        f_p = first_part.replace('-', '')
        s_p = second_part.replace('-', '')
        return 'data_to_years//' + f_p + '_' + s_p


def get_year_from_data(data: list[list[str]], index: int) -> int:
    """Gets the year from csv file

    Args:
        data (list[list[str]]): A list with dates and data
        index (int): The index of the string that points on list in the list

    Returns:
        int: Value of year
    """
    if __name__ == '__main__':
        date = data[index][0]
        year = ''
        for numbers in date:

            if numbers != '-':
                year += numbers

            else:
                break

        return int(year)


def get_month_from_data(data: list[list[str]], index: int) -> int:
    """Gets the month from csv file

    Args:
        data (list[list[str]]): A list with dates and data
        index (int): The index of the string that points on list in the list
    Returns:
        int: Value of month
    """
    if __name__ == '__main__':
        date = data[index][0]
        month = ''
        dash_counter = 0
        for numbers in date:

            if numbers == '-':
                dash_counter += 1
                continue

            if dash_counter == 1:
                month += numbers

            elif dash_counter == 2:
                break

        return int(month)


def get_day_from_data(data: list[list[str]], index: int) -> int:
    """Gets the day from csv file

    Args:
        data (list[list[str]]): A list with dates and data
        index (int): The index of the string that points on list in the list

    Returns:
        int: Value of day
    """
    if __name__ == '__main__':
        date = data[index][0]
        day = ''
        dash_counter = 0
        for numbers in date:
            if numbers == '-':
                dash_counter += 1
                continue

            if dash_counter == 2:
                day += numbers
        return int(day)


def data_to_years(file_name: str):
    """Function that sorts data to different files where each individual file will correspond to one year

    Args:
        file_name (str): Path to file

    Raises:
        TypeError: No such file exists
    """
    if __name__ == '__main__':

        if os.path.exists(file_name):

            if not os.path.exists('data_to_years'):
                os.mkdir('data_to_years')

            with open(file_name, 'r', encoding='utf-8') as csvfile:
                reader_object = list(csv.reader(csvfile, delimiter=","))

                row_count = sum(1 for row in reader_object)
                last_year = get_year_from_data(reader_object, row_count - 1)
                last_month = get_month_from_data(reader_object, row_count - 1)
                last_day = get_day_from_data(reader_object, row_count - 1)

                is_month_first = True
                write_data_list = []
                first_part_of_name = ''
                second_part_of_name = ''
                for elements in range(row_count):
                    if get_year_from_data(reader_object, elements) != last_year and get_month_from_data(reader_object, elements) != 12:
                        if is_month_first:
                            first_part_of_name = reader_object[elements][0]
                            is_month_first = False
                        write_data_list.append(reader_object[elements])

                    elif get_month_from_data(reader_object, elements) == 12 and get_year_from_data(reader_object, elements) != last_year:
                        second_part_of_name = reader_object[elements][0]
                        is_month_first = True
                        write_data_list.append(reader_object[elements])

                        if get_day_from_data(reader_object, elements) == 31:
                            with open(name_for_file(first_part_of_name, second_part_of_name), 'w', encoding='utf-8') as csv_file:
                                writer = csv.writer(
                                    csv_file, lineterminator='\n')
                                for i in write_data_list:
                                    writer.writerow((i))
                                write_data_list = []

                    elif get_year_from_data(reader_object, elements) == last_year and get_month_from_data(reader_object, elements) != last_month:
                        if is_month_first:
                            first_part_of_name = reader_object[elements][0]
                            is_month_first = False
                        write_data_list.append(reader_object[elements])

                    elif get_year_from_data(reader_object, elements) == last_year and get_month_from_data(reader_object, elements) == last_month:
                        write_data_list.append(reader_object[elements])
                        if get_day_from_data(reader_object, elements) == last_day:
                            with open(name_for_file(first_part_of_name, second_part_of_name), 'w', encoding='utf-8') as csv_file:
                                writer = csv.writer(
                                    csv_file, lineterminator='\n')
                                for i in write_data_list:
                                    writer.writerow((i))
                                write_data_list = []

        else:
            raise TypeError('No such file exists!')


try:
    file_name = 'result.csv'
    data_to_years(file_name)

except TypeError:
    print('No such file exists!')
