#! /usr/bin/env python
# coding: utf-8


import libmc
from libmc import (
    MC_HASH_MD5, MC_POLL_TIMEOUT, MC_CONNECT_TIMEOUT, MC_RETRY_TIMEOUT
)

mc = libmc.Client(
    [
        '172.17.0.5:11211',
    ],
    do_split=True,
    comp_threshold=0,
    noreply=False,
    prefix=None,
    hash_fn=MC_HASH_MD5,
    failover=False
)

mc.config(MC_POLL_TIMEOUT, 100)  # 100 ms
mc.config(MC_CONNECT_TIMEOUT, 300)  # 300 ms
mc.config(MC_RETRY_TIMEOUT, 5)  # 5 s

print mc

