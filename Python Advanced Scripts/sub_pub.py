#! /usr/bin/python3.4
# -*- coding: utf-8 -*-

import zmq
from multiprocessing import Process

def sub():
    context = zmq.Context()
    socket = context.socket(zmq.PUB)
    socket.bind('tcp://localhost')

    while True:
        socket.send