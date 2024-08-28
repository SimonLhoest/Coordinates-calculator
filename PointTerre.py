# -*- coding: utf-8 -*-
"""
Created on Fri Nov 20 13:21:57 2020

@author: lhoes
"""

import Vecteur as Vc
import numpy as np


global R
R = 6371 #km


class Point_Terre(Vc.Vecteur):
    '''
    Class permettant de rentrer les
    coordonnées géographiques de point.
    Rentrer sous la forme [Coordonnée nord, Coordonnée est].
    La coordonnée nord doit être dans l'intervalle [0,90],
    négatif si sud
    La coordonnée est doit être dans l'intervalle [0,90],
    négatif si ouest
    '''
    def __init__(self,l=[1,1]):
        Vc.Vecteur.__init__(self,l)
        
    def cartesien(self):
        '''
        Fonction permettant de convertir les coordonnées
        géographiques d'un point en coordonnées cartésiennes
        Renvoi une liste contenant les coordonnées [x,y,z]
        '''
        L=self.spherique()
        x = round(np.cos(L[2]*np.pi/180),15)*round(np.sin(L[1]*np.pi/180),15)*R
        y = round(np.sin(L[1]*np.pi/180),15)*round(np.sin(L[2]*np.pi/180),15)*R
        z = round(np.cos(L[1]*np.pi/180),15)*R
        return([x,y,z])
    
    def cylindrique(self):
        '''
        Fonction permettant de convertir les coordonnées
        géographiques d'un point en coordonnées cylindriques
        Renvoi une liste contenant les coordonnées [p,O,z]
        '''
        L=self.cartesien()
        p = ((L[0])**2+(L[1])**2)**(1/2)
        if p!=0 :
            O = np.arccos((L[0]/(p)))*180/np.pi
        else :
            O=0
        return([p,O,L[2]])
    
    def spherique(self):
        '''
        Fonction permettant de convertir les coordonnées
        géographiques d'un point en coordonnées sphériques
        Renvoi une liste contenant les coordonnées [r,O,phi]
        '''
        r = R
        O = 90-self[0]
        phi = self[1]
        return([r,O,phi])
    
    def distance(self,other):
        '''
        Fonction renvoyant la distane en kilomètres
        entre deux positions géographiques
        Renvoi un float
        '''
        self = self.cartesien()
        other = other.cartesien()
        un = Vc.Vecteur(self)
        deux= Vc.Vecteur(other)
        O= un.angle(deux)
        return O*R
        
    def latence(self,other,n):
        '''
        Fonction renvoyant la latence en secondes
        entre deux positions géographiques
            n==0 : Communication par fibre
            n==1 : Communication par satellite avec méthode triangle rectanlge
            n==2 : Communication par satellite avec méthode triangle isocèle 
        Renvoi un float
        '''
        c = 300000
        if n==0:#FIBRE
            d=self.distance(other)
            c=c/1.5
            return 2*(d/c)
        if n==1 :#SATELLITE Rect
            d=36000+(self.distance(other)**2+36000**2)**(1/2)
            return 2*(d/c)
        if n==2 :#SATELLITE Iso
            d=2*(((self.distance(other)/2)**2+36000**2)**(1/2))
            return 2*(d/c)
        else : 
            return 'LatenceErreur : mauvaise valeur de n'
            
