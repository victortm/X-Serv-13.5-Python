#!/usr/bin/python
fd = open("/etc/passwd","r")
lineas = fd.readlines()
dicc = {}
for linea in lineas:
	conf = linea.split(":")
	usrname = conf[0]
	shell = conf[-1]
	dicc[usrname] = shell
try:
	print dicc["imaginario"]
except KeyError:
	print "Usuario imaginario no existe en el dicc"
