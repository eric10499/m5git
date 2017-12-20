#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  abcfor7.py
#  
#  Copyright 2017 cf17eric.visier <cf17eric.visier@super-desktop>
#  Programa que determina la nota mija de la classe, la pitjor nota i el nom de l'alumne amb la pitjoe nota
n=10
suma=0.0 #Para declarar que es float
notamasbaja=10.0 #solo funciona si la nota mas alta posible es un 10
for i in range(n):
	nombre=raw_input("Nombre:")
	nota=float(raw_input("Nota:"))
	if i==0:
		notamasbaja=nombre
		alumnoperornota=nombre
	if notamasbaja>=nota:
		notamasbaja=nota
		alumnoperornota=nombre
	suma=suma+nota
print "Media:",suma/n
print "Nota mas baja:",notamasbaja
print "Alumno peor nota:",alumnoperornota
