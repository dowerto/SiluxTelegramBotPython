# -*- coding: utf-8 -*-
#Se acomoda la codificón utf-8 para poder poner tildes y que no sea solo unicode

#Se importan las librerías necesarias
import sys
import time
import random
import datetime
import profesor
import informacion
import canal

#Clase controladora del Bot
def asesoriaProfesor(nombre):
	return profesor.asesoriaPro(nombre)

def enviarmensajecanal():
	return canal.info()
  
   	

