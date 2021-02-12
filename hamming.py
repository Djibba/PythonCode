# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
import numpy 
import random
import sys


def decToBin(n,param):
    """Convertit un nombre en binaire"""
    res = [0 for i in range(param - len(bin(n)[2:]))] + list(bin(n)[2:])
    for i in range(len(res)):
        res[i] = int(res[i])    
    return res


def matrixControl(param):
    L = [2**i for i in range(param)]
    L.reverse()
    liste = []
    for i in range(1,2**param):
        if i not in L:
            liste.append(i)
    liste = liste + L
    for i in range(len(liste)):
        liste[i] = decToBin(liste[i],param)
    H = numpy.asarray(liste)
    H = H.transpose() 
    
    return H

def matrixGen(param):
    H = matrixControl(param)
    P = H[0:param,0:2**param - param-1]
    I = numpy.eye(2**param-1- param,dtype=int)
    P = numpy.concatenate (( I, P.transpose()),axis = 1)
    
    return P
    
    


def createMessage(length):
    msg = []
    for i in range(length):
        letter = random.choice([0,1])
        msg.append(letter)
    return numpy.array(msg, dtype = int)


def encode(m, g):
    enc = numpy.dot(m, g)%2
    return enc

def encode1(m, g,param):
    res = numpy.zeros(2**param -1, dtype=int)
    for i in range(len(m)):
        if m[i] != 0:
            res = res^g[i]
            
      
    return res

def flip(m,i):
    if m[i]==0:
        m[i] = 1
    else:
        m[i] = 0
        
    return m

def decoder(H,y,param):
    
    synd = numpy.dot(y, H.transpose())%2
    if (synd == numpy.zeros(param,dtype= int)).all():
        return y
    else:
        for i in range(2**param-1):
            if (synd == H[:,i]).all():
                c = flip(y,i)
        return c
                
    
    
    
    return synd
     
    
    

    


