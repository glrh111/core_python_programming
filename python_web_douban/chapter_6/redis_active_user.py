#! /usr/bin/env python
# coding: utf-8

import redis
import datetime
import random

ACCOUNT_ACTIVE_KEY = 'account:active'

r = redis.StrictRedis(host='172.17.0.3', port=6379, db=0)
r.flushall() # 删除全部key
now = datetime.datetime.utcnow()


def record_active(accound_id, t=None):
    """"""
    if t is None:
        t = datetime.datetime.utcnow()
    p = r.pipeline()
    key = ACCOUNT_ACTIVE_KEY
    for arg in ('year', 'month', 'day'):
        key = '{}:{}'.format(key, getattr(t, arg))  # 这里有点问题，month和day的重复。
        p.setbit(key, accound_id, 1) # 设置当年，月，天登录
    p.execute()


def gen_records(max_days, population, k): # 随机生成一些数据
    for day in range(1, max_days):
        time_ = datetime.datetime(now.year, now.month, day)
        accounts = random.sample(range(population), k)
        for account in accounts:
            # print account, time_
            record_active(account, time_)


gen_records(29, 10000, 2000) # 每天从1W个人中，选择2000个人登录


# 本月总活跃用户数量
def get_active_user_this_month():
    """"""
    print '本月总活跃用户数量: ', r.bitcount(
        '{}:{}:{}'.format(ACCOUNT_ACTIVE_KEY, now.year, now.month)
    )
get_active_user_this_month()


# 今天的活跃用户数量
def get_active_user_this_day():
    """"""
    print '今天的活跃用户数量: ', r.bitcount(
        '{}:{}:{}:{}'.format(ACCOUNT_ACTIVE_KEY, now.year, now.month, now.day)
    )
get_active_user_this_day()


# 查看这个随机用户是否登录过
def get_user_if_active():
    """"""
    account = random.randint(0, 10000)
    print '用户{}今天是否登录过: '.format(account), r.getbit(
        '{}:{}:{}:{}'.format(ACCOUNT_ACTIVE_KEY, now.year, now.month, now.day), account
    )
get_user_if_active()


# 获取在几天同时活跃的用户数量
def get_active_user_amount_in_continues_2_days():
    keys = [
        '{}:{}:{}:{}'.format(ACCOUNT_ACTIVE_KEY, now.year, now.month, day) for day in [2, 3]
    ]
    r.bitop(
        'and', 'destkey:and', *keys
    )
    print '在2,3两日都活跃的用户数量是:', r.bitcount(
        'destkey:and'
    )
get_active_user_amount_in_continues_2_days()


# ipython -i redis_active_user.py

def cal_mem():
    pass



