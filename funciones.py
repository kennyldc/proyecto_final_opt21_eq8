#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Dec  2 16:17:52 2021

@author: goriminaur
"""

import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from decimal import *
import math

def approx_eigval_max(matriz_covarianza,max_iters):
    z_k_minus_1=[]
    getcontext().prec = 7
    eigen_val_ant=1
    eigen_val=0
    eigen_vec=(np.zeros((1,5)))
    k=0
    #Se crea una lista que contenga el número de columnas = al número de renglones de la matriz
    #de covarianzas -1 y al final se agrega un uno para seguir el algoritmo de la potencia
    for i in range(len(matriz_covarianza)):
        if i+1==len(matriz_covarianza):
            z_k_minus_1.append(1)
        else: 
            z_k_minus_1.append(0)
    # A partir del número máximo de iteraciones se crea un ciclo para aproximar el eigenvalor
    while (k <=max_iters) and (abs(Decimal(eigen_val)-Decimal(eigen_val_ant))>=1e-4):
        eigen_val_ant=eigen_val
        z_k=matriz_covarianza@z_k_minus_1
        #Se normaliza el vector utilizando la norma cuadrada
        eigen_vec=z_k/np.linalg.norm(z_k)
        z_k_minus_1=eigen_vec
        #Se genera el eigen valor utilizando el vector resultante y la matriz original
        eigen_val=eigen_vec.T@matriz_covarianza@eigen_vec
        
        k=k+1 
    return eigen_val,eigen_vec,matriz_covarianza
