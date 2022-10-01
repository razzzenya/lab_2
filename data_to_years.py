import csv
import os
from typing import NoReturn


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
        return 'data_to_years_output//' + f_p + '_' + s_p + '.csv'


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


def data_to_years(file_name: str) -> NoReturn:
    """Function that sorts data to different files where each individual file will correspond to one year

    Args:
        file_name (str): Path to file

    Raises:
        TypeError: No such file exists
    """
    if __name__ == '__main__':

        if os.path.exists(file_name):

            if not os.path.exists('data_to_years_output'):
                os.mkdir('data_to_years_output')

            with open(file_name, 'r', encoding='utf-8') as csvfile:
                reader_object = list(csv.reader(csvfile, delimiter=","))

                output = []
                first_part_of_name = ''
                second_part_of_name = ''
                is_first = True
                current_year = get_year_from_data(reader_object, 0)
                last_year = get_year_from_data(
                    reader_object, len(reader_object) - 1)

                for i in range(len(reader_object)):

                    if current_year < last_year:

                        if get_year_from_data(reader_object, i) == current_year:
                            if is_first:
                                first_part_of_name = reader_object[i][0]

                            is_first = False
                            output.append(reader_object[i])
                            second_part_of_name = reader_object[i][0]

                        elif get_year_from_data(reader_object, i) != current_year:
                            with open(name_for_file(first_part_of_name, second_part_of_name), 'w', encoding='utf-8') as csv_file:
                                writer = csv.writer(
                                    csv_file, lineterminator='\n')
                                for j in output:
                                    writer.writerow((j))
                                output = []

                                first_part_of_name = reader_object[i][0]
                                output.append(reader_object[i])
                                current_year += 1

                    elif current_year == last_year:

                        output.append(reader_object[i])
                        second_part_of_name = reader_object[i][0]

                        if i + 1 == len(reader_object):
                            with open(name_for_file(first_part_of_name, second_part_of_name), 'w', encoding='utf-8') as csv_file:
                                writer = csv.writer(
                                    csv_file, lineterminator='\n')
                                for j in output:
                                    writer.writerow((j))

        else:
            raise FileNotFoundError


try:
    file_name = 'result.csv'
    data_to_years(file_name)

except FileNotFoundError:
    print('No such file exists!')
