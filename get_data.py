import csv
import datetime
import os


def get_data_from_x_y(file_name_x: str, file_name_y: str, date: datetime.date) -> list[str] or None:
    """Function finds information about date from X.csv and Y.csv files

    Args:
        file_name_x (str): Path to file that contains dates
        file_name_y (str): Path to file that contains data
        date (datetime.date): The date for which you want to find weather data

    Raises:
        FileNotFoundError: One or both of the files are missing

    Returns:
        list[str] or None: returns list[str] if data for the date was found, or returns None on failure
    """

    if __name__ == '__main__':

        if os.path.exists(file_name_x) and os.path.exists(file_name_y):

            with open(file_name_x, 'r', encoding='utf-8') as x:
                dates = list(csv.reader(x, delimiter=","))
                index = -1

                for i in range(len(dates)):
                    if dates[i][0] == str(date):
                        index = i
                        break

            with open(file_name_y, 'r', encoding='utf-8') as y:
                data = list(csv.reader(y, delimiter=","))

                if index >= 0:
                    return data[index]

                elif index == -1:
                    return None

        raise FileNotFoundError


def get_data_from_years_and_weeks(folder_name: str, date: datetime.date) -> list[str] or None:
    """Function finds information about date from csv files that contains data 

    Args:
        folder_name_years (str): Path to folder that contains .csv files
        date (datetime.date): The date for which you want to find weather data

    Raises:
        FileNotFoundError: Folder with .csv files is missing

    Returns:
        list[str] or None: list[str] or None: returns list[str] if data for the date was found, or returns None on failure
    """
    if __name__ == '__main__':

        if os.path.exists(folder_name):
            index = -1

            for root, dirs, files in os.walk(folder_name):
                for file in files:

                    with open(folder_name + '/' + file, 'r', encoding='utf-8') as csvfile:
                        dates = list(csv.reader(csvfile, delimiter=","))

                        for i in range(len(dates)):

                            if dates[i][0] == str(date):
                                index = i
                                break

                        if index >= 0:
                            return dates[i][1:]

            if index == -1:
                return None

        else:
            raise FileNotFoundError


def get_data(file_name: str, date: datetime.date) -> list[str] or None:
    """Function finds information about date from csv file
    Args:
        file_name (str): Path to file that contains weather data about dates
        date (datetime.date): The date for which you want to find weather data

    Raises:
        FileNotFoundError: .csv file is missing

    Returns:
        list[str] or None: list[str] or None: returns list[str] if data for the date was found, or returns None on failure
    """

    if __name__ == '__main__':

        if os.path.exists(file_name):
            with open(file_name, 'r', encoding='utf-8') as csvfile:

                reader_object = list(csv.reader(csvfile, delimiter=","))

                for i in range(len(reader_object)):

                    if reader_object[i][0] == str(date):
                        return reader_object[i][1:]

        else:
            raise FileNotFoundError


class DateIterator:

    def __init__(self):
        self.counter = 0

    def __next__(self, file_name: str) -> tuple:
        """_summary_

        Args:
            file_name (str): _description_

        Raises:
            FileNotFoundError: _description_

        Returns:
            tuple: _description_
        """
        if __name__ == '__main__':

            if os.path.exists(file_name):
                with open(file_name, 'r', encoding='utf-8') as csvfile:
                    reader_object = list(csv.reader(csvfile, delimiter=","))

                    if self.counter == len(reader_object):
                        self.counter = 0
                        output = (reader_object[self.counter][0], reader_object[self.counter][1], reader_object[self.counter][2],
                                  reader_object[self.counter][3], reader_object[self.counter][4], reader_object[self.counter][5], reader_object[self.counter][6])
                        return output

                    elif self.counter < len(reader_object):
                        self.counter += 1
                        output = (reader_object[self.counter - 1][0], reader_object[self.counter - 1][1], reader_object[self.counter - 1][2],
                                  reader_object[self.counter - 1][3], reader_object[self.counter - 1][4], reader_object[self.counter - 1][5], reader_object[self.counter - 1][6])
                        return output
            else:
                raise FileNotFoundError


try:
    file_name = 'result.csv'
    folder_name_years = 'data_to_years_output'
    folder_name_weeks = 'data_to_weeks_output'
    file_name_x = 'divide_data_output//X.csv'
    file_name_y = 'divide_data_output//Y.csv'

    date = datetime.date(2010, 1, 5)
    invalid_date = datetime.date(2222, 5, 20)
    print(1)
    obj = DateIterator()
    # b = next(obj, file_name)
    b = obj.__next__(file_name)
    print(b)

    b = obj.__next__(file_name)
    print(b)

    b = obj.__next__(file_name)
    print(b)

    # # демонстрация работы функции с валидной датой
    # result = get_data_from_x_y(file_name_x, file_name_y, date)
    # print(result)

    # # демонстрация работы функции с невалидной датой
    # result = get_data_from_x_y(file_name_x, file_name_y, invalid_date)
    # print(result)

    # # демонстрация работы функции с валидной датой
    # result = get_data_from_years_and_weeks(folder_name_years, date)
    # print(result)

    # # демонстрация работы функции с невалидной датой
    # result = get_data_from_years_and_weeks(folder_name_years, invalid_date)
    # print(result)

    # # демонстрация работы функции с валидной датой
    # result = get_data_from_years_and_weeks(folder_name_weeks, date)
    # print(result)

    # # демонстрация работы функции с невалидной датой
    # result = get_data_from_years_and_weeks(folder_name_weeks, invalid_date)
    # print(result)

    # # демонстрация работы функции с валидной датой
    # result = get_data(file_name, date)
    # print(result)

    # # демонстрация работы функции с невалидной датой
    # result = get_data(file_name, invalid_date)
    # print(result)

except FileNotFoundError:
    print('No such file exists!')
