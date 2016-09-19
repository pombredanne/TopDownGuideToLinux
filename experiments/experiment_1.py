#!/usr/bin/env python
import time,os


if __name__ == '__main__':
    some_file = open("{}.txt".format(os.getpid()),'w')
    some_data = []
    for k in range(60):
        some_data += [1,] * 10000
        time.sleep(30)
        some_file.write("{}\n".format(k))
    some_file.close()