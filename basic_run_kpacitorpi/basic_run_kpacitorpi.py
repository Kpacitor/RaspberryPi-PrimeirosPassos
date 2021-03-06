#!/usr/bin/env python
# -*- coding: utf-8 -*-

#/###################################################################
#/ Kpacitor, Ensinanso Tecnologia					 
#/###################################################################
#/ Author: Elder Lucas de Oliveira Santos							 				
#/ Data: 13 de Janeiro de 2015										 
#/ Titulo: Robo KapacitorPi											 
#/###################################################################
#/ Arquivo: run_kapacitorpi.py 									     
#/ Descricao: Controle das funcoes basicas do Frente, Tras, Esquerda 
#/			  e direita 											 
#/																	 
#/ Curso: Raspberry Pi: Primeiros Passos + IOT (Internet of things)	 
#/ link: www.kpacitor.com/robokpacitorpi							 
#/																	 
#/###################################################################

import RPi.GPIO as GPIO
import time
import os

def movimentar(run):
	if run == 'FRENTE':
		dir_frente.start(20) #Duty Cycle de 20%
		esq_frente.start(18) #Duty Cycle de 20%
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

	print "Ok, Movimento Executado"

# Funcao que 
def delay_info(time):
	for x in range(0, time):
		time.sleep(1)
		print 'Time', x


GPIO.setmode(GPIO.BCM)

GPIO.setup(17,GPIO.OUT)
GPIO.setup(22,GPIO.OUT)
GPIO.setup(23,GPIO.OUT)
GPIO.setup(27,GPIO.OUT)

dir_frente	= GPIO.PWM(17, 100) #Direita Para Frente
dir_tras	= GPIO.PWM(22, 100) #Direita Para Tras
esq_frente	= GPIO.PWM(23, 100) #Esquerda Para Frente
esc_tras	= GPIO.PWM(27, 100) #Esquerda Para Tras 

movimentar(run = 'FRENTE')
delay_info(3)
movimentar(run = 'TRAS')
delay_info(3)	
movimentar(run = 'ESQUERDA')
delay_info(3)
movimentar(run = 'DIREITA')
delay_info(3)
movimentar(run = 'STOP')







