#! /usr/bin/env python
# coding: utf-8

"""
读入一个csv文件, 读取数据进行统计


"""

import csv
import traceback
import datetime
import pytz
import calendar
from collections import Counter

def datestr_to_time13(datestr, tz=pytz.timezone('Asia/Bangkok'), FORMAT='%Y-%m-%d'):
    '''
    :param tz_date_string: 2016-07-08 Bangkok time
    :param FORMAT:
    :return: (stat_time13, end_time13), end is bigger than stat_time by 1 day
    '''
    utc_timezone = pytz.timezone('UTC')
    Bangkok_timezone = tz
    dt = datetime.datetime.strptime(datestr, FORMAT)
    th_datetime = Bangkok_timezone.localize(dt)
    utc_datetime = th_datetime.astimezone(utc_timezone)
    return int(calendar.timegm(utc_datetime.timetuple()) * 1000)

def read_from_csv():
    gift_counter = Counter()
    with open('gift.csv', 'r') as f:
        csv_reader = csv.reader(f)
        for row in csv_reader:
            try:
                to_userId = row[6]
                gift_count = row[11]
                create_time = row[13] # 过滤时间

                time13 = datestr_to_time13(create_time, FORMAT='%Y-%m-%d %H:%M:%S', tz=pytz.timezone('UTC'))

                print create_time, time13

                if not (1504717200000 <= time13 < 1505062800000):
                    continue

                # print to_userId, gift_count
                gift_counter.update({
                    int(to_userId): int(gift_count)
                })
            except Exception:
                traceback.print_exc()
                continue

    return gift_counter

def main():
    gift_counter = read_from_csv()

    write_list = [['userId', 'yellow_diamond_count']]

    for user_id, g_c in gift_counter.most_common():
        write_list.append([
            user_id,
            g_c
        ])

    with open('yellow_diamond_counter.csv', 'w') as f:
        csv_writer = csv.writer(f, delimiter=',')
        csv_writer.writerows(write_list)
    print 'write to:'


if __name__ == '__main__':
    main()