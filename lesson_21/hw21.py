from datetime import datetime, timedelta
import logging

logging.basicConfig(filename='hb_test.log',
                    level=logging.DEBUG,
                    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')


def convert_log_to_list_of_strings(file):
    with open(file, 'r') as file:
        file_content = file.read()
        return file_content.split('\n')


def filter_log_by_key(log_list: list, filter_key: str):
    # filter log by key
    filtered_log = []
    for row in log_list:
        if filter_key in row:
            filtered_log.append(row)
    return filtered_log


def analyze_log(filtered_log: list):
    # get every time from filtered rows
    list_of_times = []
    for row in filtered_log:
        timestamp_text = 'Timestamp ' # get index for substring
        start_position = row.find(timestamp_text) + len(timestamp_text) # get start position for time
        time_string = row[start_position:start_position + 8] # time format 00:00:00 is 8 characters length
        list_of_times.append(datetime.strptime(time_string, "%H:%M:%S")) # create a list with times

    # timedelta objects for future comparison
    td_31 = timedelta(seconds=31)
    td_33 = timedelta(seconds=33)

    list_of_times_index = 0
    for _ in list_of_times:
        while list_of_times_index < len(list_of_times) - 1:
            # get a difference between current and next time record
            difference = list_of_times[list_of_times_index] - list_of_times[list_of_times_index + 1]
            # log differences between 31 and 33 seconds
            if td_31 < difference < td_33:
                logging.warning(f"Difference is: {difference.seconds} seconds"
                                f"\n{filtered_log[list_of_times_index]}"
                                f"\n{filtered_log[list_of_times_index + 1]}")
            # log differences more or equal 33 seconds
            elif difference >= td_33:
                logging.error(f"Difference is: {difference.seconds} seconds"
                              f"\n{filtered_log[list_of_times_index]}"
                              f"\n{filtered_log[list_of_times_index + 1]}")
            list_of_times_index += 1


file_content = convert_log_to_list_of_strings('hblog.txt')
filtered_log = filter_log_by_key(file_content, 'Key TSTFEED0300|7E3E|0400')
analyze_log(filtered_log)
