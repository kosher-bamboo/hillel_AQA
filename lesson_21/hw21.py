from datetime import datetime, timedelta
import logging

logging.basicConfig(filename='hb_test.log',
                    level=logging.DEBUG,
                    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')

with open('hblog.txt', 'r') as file:
    file_content = file.read()
    file_content = file_content.split('\n')

# filter log by 'Key'
filtered_log = []
for row in file_content:
    if 'Key TSTFEED0300|7E3E|0400' in row:
        filtered_log.append(row)
        pass

# get every time from filtered rows
list_of_times = []
for row in filtered_log:
    timestamp_text = 'Timestamp '
    start_position = row.find(timestamp_text) + len(timestamp_text)
    # get times
    time_string = row[start_position:start_position + 8]
    list_of_times.append(datetime.strptime(time_string, "%H:%M:%S"))
    pass

td_31 = timedelta(seconds=31)
td_33 = timedelta(seconds=33)

list_of_times_index = 0
for time in list_of_times:
    while list_of_times_index < len(list_of_times) - 1:
        if td_31 < (list_of_times[list_of_times_index] - list_of_times[list_of_times_index + 1]) < td_33:
            logging.warning(f"\n{filtered_log[list_of_times_index]}"
                            f"\n{filtered_log[list_of_times_index + 1]}")
        elif (list_of_times[list_of_times_index] - list_of_times[list_of_times_index + 1]) > td_33:
            logging.error(f"\n{filtered_log[list_of_times_index]}"
                          f"\n{filtered_log[list_of_times_index + 1]}")
        list_of_times_index += 1
