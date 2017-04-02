#!/usr/bin/python
from Robot import Robot

if __name__ == "__main__":
	obj = Robot('tom','1.0')
	obj.selfCheck()
	obj.readFile("testfile")
