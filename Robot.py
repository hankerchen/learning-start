#!/usr/bin/python
import re;

class Robot:
	def __init__(self,name = 'noName',version = '1.0'):
		self.name = name
		self.version = version
	def selfCheck(self):
		print "i am "+ self.name + ",i'm " + self.version + " robot,i'm working normally."
	def readFile(self,f):
		pattern = re.compile(r"^c")
		try:
			fp = open(f,"r")
		except:
			print "error,can't find file " + f
			return 1
		for line in fp:
			if pattern.match(line):
				print line.strip('\n')
		return 0
