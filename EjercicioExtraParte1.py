#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Dec 16 12:17:28 2020

@author: José Carlos Aradillas jaradillas@us.es
"""

'''
    Importación de librerías
'''
import numpy as np
import matplotlib.pyplot as plt
from IPython import get_ipython
get_ipython().run_line_magic('matplotlib', 'qt')
from utils import load_signal, detecta_y_procesa
plt.close('all')

#%%

'''
    Con la siguiente función, obtenemos en Xt la señal recibida:
'''
Rt = load_signal('./Rt1.npy')

# Representamos un trozo de la señal a la entrada del receptor.

plt.figure()
limites = (3024, 3700)
t = np.arange(limites[0], limites[1])*np.log2(32)/0.3e6*64
plt.plot(t, Rt[limites[0]:limites[1]])
plt.xlabel('t (ms)')
plt.ylabel('$R(t)$')
plt.title('Representación de un trozo de la señal R(t)')
plt.grid()
plt.show()

#%%
'''
    Líneas para editar, obtener los parámetros de la transmisión de las
    diapositivas adjuntas.
'''
Eb = None # Tomar del enunciado.
M = None # Tomar del enunciado.
L = None # Tomar del enunciado.
Wc = None # Tomar del enunciado.
phi = None # Tomar del enunciado.
Rb = None # Tomar del enunciado.

Tb = None # Calcular
Ts = None # Calcular
Tm = None # Calcular

#%%
'''
    Ejercicio: Obtener el vector de observación r a la salida del receptor vectorial.
    Una vez obtenido, pasar como parámetro este vector "r" al detector y a las capas de los 
    niveles superiores de la torre de protocolos. La función detecta_y_procesa 
    emula tanto el detector como estas capas superiores, por lo tanto no es 
    necesario implementar. Esta función también recibe como parámetros el 
    alfabeto de la constelación utilizada en el transmisor y la ruta al fichero
    donde se almacenarán los datos recibidos (en nuestro ejemplo, una imagen)

'''

# Líneas para implementar el receptor vectorial, implementar el bloque 2
# ilustrado en las diapositivas.
r = None # Obtener el vector de observación r a partir de la señal Rt
alfabeto = None # Obtener el alfabeto de la constelación

detecta_y_procesa(r, alfabeto, './img_recibida.jpg')