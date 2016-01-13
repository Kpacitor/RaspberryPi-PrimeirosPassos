#!/usr/bin/env python
# -*- coding: utf-8 -*-

#/###################################################################
#/ 					Kpacitor, Ensinanso Tecnologia					 
#/###################################################################
#/ Author: Elder Lucas de Oliveira Santos							 				
#/ Data: 13 de Janeiro de 2015										 
#/ Titulo: Robo KapacitorPi											 
#/###################################################################
#/ Arquivo: run_kapacitorpi.py 									     
#/ Descricao: Controle das funcoes basicas do Frente, Tras, Esquerda 
#/             e direita 											 
#/																	 
#/ Curso: Raspberry Pi: Primeiros Passos + IOT (Internet of things)	 
#/ link: www.kpacitor.com/robokpacitopi								 
#/																	 
#/###################################################################

import RPi.GPIO as GPIO
import time
import os

def movimentar(run):
	if run == 'FRENTE':
		dir_frente.start(100) #Duty Cycle de 20%
		esq_frente.start(100) #Duty Cycle de 20%
		dir_tras.stop()
		esc_tras.stop()

	elif run == 'TRAS':
		dir_tras.start(18) #Duty Cycle de 20%
		esc_tras.start(20) #Duty Cycle de 20%
		dir_frente.stop()
		esq_frente.stop()

	elif run == 'DIREITA':
		esq_frente.start(20) #Duty Cycle de 20%
		dir_tras.start(20) #Duty Cycle de 20%
		dir_frente.stop()
		esc_tras.stop()

	elif run == 'ESQUERDA':
		dir_frente.start(20) #Duty Cycle de 20%
		esc_tras.start(20) #Duty Cycle de 20%
		esq_frente.stop()
		dir_tras.stop()

	else:
		dir_frente.stop()
		esq_frente.stop()
		dir_tras.stop()
		esc_tras.stop()

	return "Ok, Movimento Executado"



GPIO.setmode(GPIO.BCM)

GPIO.setup(17,GPIO.OUT)
GPIO.setup(22,GPIO.OUT)
GPIO.setup(23,GPIO.OUT)
GPIO.setup(27,GPIO.OUT)


dir_frente 	= GPIO.PWM(17, 100) #Direita Para Frente
dir_tras 	= GPIO.PWM(22, 100) #Direita Para Tras
esq_frente 	= GPIO.PWM(23, 100) #Esquerda Para Frente
esc_tras 	= GPIO.PWM(27, 100) #Esquerda Para Tras 


movimentar(run = 'FRENTE')
for x in range(0, 3):
	time.sleep(1)
	print "FRENTE: %d ", x	


movimentar(run = 'TRAS')
for x in range(0, 3):
	time.sleep(1)
	print "TRAS: %d ", x	

movimentar(run = 'ESQUERDA')
for x in range(0, 3):
	time.sleep(1)
	print "ESQUERDA: %d ", x	

movimentar(run = 'DIREITA')
for x in range(0, 3):
	time.sleep(1)
	print "DIREITA: %d ", x	

movimentar(run = 'STOP')

	

GPIO.cleanup()





