# -*- coding: utf-8 -*-
"""
Created on Fri Dec 11 13:58:37 2020

@author: lhoes
"""

import PointTerre as ex


#TEST PARTIE 1:
print('\n -Partie 1-')

#Coordonnées Paris en cartésien
Paris = ex.Point_Terre([48.866667,2.333333])
print('Paris (cartésien) : ',Paris.cartesien())
print('Paris (cylindrique) : ',Paris.cylindrique())
print('Paris (sphérique) : ',Paris.spherique(),'\n')

#Coordonnées New York en cylindrique
NewYork = ex.Point_Terre([40.779897,-73.968565])
print('New York (cartésien) : ',NewYork.cartesien())
print('New York (cylindrique) : ',NewYork.cylindrique())
print('New York (sphérique) : ',NewYork.spherique(),'\n')

#Coordonnées Buenos Aires en sphérique
BuenosAires = ex.Point_Terre([-38.4212955,-63.587402499999996])
print('Buenos Aires (cartésien) : ',BuenosAires.cartesien())
print('Buenos Aires (cylindrique) : ',BuenosAires.cylindrique())
print('Buenos Aires (sphérique) : ',BuenosAires.spherique())
print('\n \n -Partie 2-')


#TEST PARTIE 2:

#Distance Paris - New York
print('Paris - New York : ',Paris.distance(NewYork))

#Distance Paris - Buenos Aires
print('Paris - Buenos Aires : ',Paris.distance(BuenosAires))
print('\n -Partie 3-')


#TEST PARTIE 3:
    
#Latence satellite (triangle isocèle) Paris - Buenos Aires
print('Latence satellite Paris-BA : ',Paris.latence(BuenosAires,2))

#Latence fibre Paris - Buenos Aires
print('Latence fibre Paris-BA : ', Paris.latence(BuenosAires,0),'\n')

#Latence satellite (triangle rectangle) Paris - New York 
print('Latence satellite Paris-NY : ',Paris.latence(NewYork,1))

#Latence fibre Paris - New York 
print('Latence fibre Paris-NY : ',Paris.latence(NewYork,0))
