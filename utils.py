#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Dec 16 11:59:55 2020

@author: José Carlos Aradillas jaradillas@us.es
"""

import numpy as np
import matplotlib.pyplot as plt
from labcomdig import detectaSBF, simbolobit

def load_signal(filename):
    try:
        Xt = np.load(filename)
    except FileNotFoundError:
        raise Exception('No se ha encontrado la señal a la entradada del receptor, en el fichero '+filename)
    return Xt

def procesa_datos_recibidos(Bn, nombre_destino = './img_recibida.jpg', cabecera_block=32, pixel_block=8):
    cabecera_size = 3*cabecera_block
    cabecera = Bn[:cabecera_size]
    dimensiones = cabecera.reshape([-1,cabecera_block]) @ 2**np.flipud(np.arange(cabecera_block))
    data_size = pixel_block*np.product(dimensiones)
    data_bits = Bn[cabecera_size:(cabecera_size+data_size)]
    try:
        data_plain_rx = data_bits.reshape([-1,pixel_block]) @ 2**np.flipud(np.arange(pixel_block))
        data_rx = data_plain_rx.reshape(dimensiones)    
    except:
        raise Exception('No has resuelto bien el ejercicio, no has demodulado bien la señal')
    plt.figure()
    plt.imshow(data_rx)
    plt.imsave(nombre_destino, data_rx.astype(np.uint8))
    
def detecta_y_procesa(r, alfabeto, fichero_destino):
    if r is None:
        raise Exception('Debes obtener el vector de observación r a partir de R(t)')
    if alfabeto is None:
        raise Exception('Debes introducir en "alfabeto" el vector con los valores posibles de la constelación')
    sn = detectaSBF(r, alfabeto)
    Bn = simbolobit(sn, alfabeto)
    procesa_datos_recibidos(Bn, fichero_destino)
    
    