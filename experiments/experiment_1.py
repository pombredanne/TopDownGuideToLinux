#!/usr/bin/env python
import time


if __name__ == '__main__':
    some_data = []
    for k in range(60):
        some_data += [1,] * 10000
        time.sleep(30)