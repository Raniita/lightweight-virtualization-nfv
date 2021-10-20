#!/usr/bin/python
import numpy

print("cgroup testing program (memory limit)")
result = [numpy.random.bytes(1024*1024) for x in range(1024*4)]
print("RAM used: {}M".format(len(result)))
