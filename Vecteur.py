# -*- coding: utf-8 -*-
"""
Created on Fri Dec 11 14:33:09 2020

@author: lhoes
"""

import numpy as np

class Vecteur(list):
    def __init__(self,l=[1]):
        list.__init__(self,l)
        
    def norme(self):
        s = 0
        for i in range(len(self)):
            s+=self[i]**2
        return s**(1/2)
    
    def scalaire(self,other):
        sca = 0
        for i in range (len(self)):
            sca += self[i]*other[i]
        return sca
    
    def angle(self,other):                
        O = np.arccos(self.scalaire(other)/(self.norme()*other.norme()))
        return O
        
    def Colinear(self,other):
        return self.norme()*other.norme()*np.sin(self.angle(other)) == 0
    
    def Orthogonal(self,other):
        return self.scalaire(other)==0
    
    def projection(self,other):
        return self.scalaire(other)/other.norme()
    
    def __lt__(self,other):
        return(Vecteur.norme(self)<Vecteur.norme(other))
        
    def __le__(self,other):
        return(Vecteur.norme(self)<=Vecteur.norme(other))
        
    def __eq__(self,other):
        return(Vecteur.norme(self)==Vecteur.norme(other))
        
    def __ne__(self,other):
        return(Vecteur.norme(self)!=Vecteur.norme(other))
        
    def __ge__(self,other):
        return(Vecteur.norme(self)>=Vecteur.norme(other))
        
    def __gt__(self,other):
        return(Vecteur.norme(self)>Vecteur.norme(other))
    
    def __add__(self,other):
        L=[x for x in range(len(self))]
        for i in range(len(self)):
            L[i]=self[i]+other[i]
        return(L)
    
    def __sub__(self,other):
        L = [x for x in range(len(self))]
        for i in range(len(self)):
            L[i]=self[i]-other[i]
        return(L)
    
    def __mul__(self,other):
        L = [x for x in range(len(self))]
        for i in range(len(self)):
            L[i]=self[i] * other[i]
        return(L)
    
    def __truediv__(self,other):
        L = [x for x in range(len(self))]
        for i in range(len(self)):
            L[i]=self[i]/other[i]
        return(L)
    
    def __floordiv__(self,other):
        L = [x for x in range(len(self))]
        for i in range(len(self)):
            L[i]=self[i]//other[i]
        return(L)
    
    def __pow__(self,other):
        L = [x for x in range(len(self))]
        for i in range(len(self)):
            L[i]=self[i]**other[i]
        return(L)
    
    def __iadd__(self,other):
        L = [x for x in range(len(self))]
        for i in range(len(self)):
            self[i]+=other[i]
            L[i]=self[i]
        return(L)
