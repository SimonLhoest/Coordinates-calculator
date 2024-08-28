# -*- coding: utf-8 -*-
"""
Created on Fri Dec 11 13:59:54 2020

@author: lhoes
"""

import PointTerre as ex

import tkinter as tk
import tkinter.font as tkfont
import tkinter.messagebox as tkmsg

from PIL import ImageTk 


fenetre = tk.Tk()
fenetre.geometry('1280x720')
fenetre.minsize(1280,720)
fenetre.title('Convertiseur de coordonnées')


font = tkfont.Font(size=12)
fontresultat=tkfont.Font(size=20)

#Premiere moitié
partie1 = tk.Frame(fenetre, borderwidth=5,bg='white',relief=tk.SOLID)
partie1.pack(side=tk.TOP,fill=tk.BOTH,expand=0)

#Espace Terre
FrameTerre = tk.Frame(partie1)
FrameTerre.pack(side=tk.LEFT,fill=tk.BOTH,expand=1)

photo = ImageTk.PhotoImage(file = 'Terre.png')
Terre= tk.Label(FrameTerre,image=photo)
Terre.config(width=160)
Terre.pack(fill=tk.BOTH)

#Frame milieu
Framemiddle = tk.Frame(partie1)
Framemiddle.pack(side=tk.LEFT,fill=tk.BOTH,expand=1)

#Espace IPSA
FrameIPSA= tk.Frame(partie1)
FrameIPSA.pack(side=tk.LEFT, fill=tk.BOTH,expand=1)

photo2 = ImageTk.PhotoImage(file = 'Ipsa.png')
IPSA= tk.Label(FrameIPSA,image=photo2)
IPSA.config(width=160)
IPSA.pack(fill=tk.BOTH)


#Frame pour cases dentree et labels
Frame2 = tk.Frame(Framemiddle,borderwidth=5,relief=tk.RIDGE)
Frame2.pack(side=tk.TOP,fill=tk.Y, expand=1)

#Cases nom
Frame3 = tk.Frame(Frame2,bg='white')
Frame3.pack(side=tk.LEFT,fill=tk.Y, expand=1)
#Label nom
LabelNom = tk.Label(Frame3,text='NOM DU POINT',font=font)
LabelNom.pack(anchor=tk.CENTER,side=tk.TOP,padx=100,expand=1,pady=5)
#Entree nom point
nom=tk.StringVar()
entree = tk.Entry(Frame3, borderwidth=5,bg='white',textvariable=nom)
entree.pack(anchor=tk.CENTER,side=tk.TOP,padx=50,expand=1,pady=5)

#Cases nord
Framenord = tk.Frame(Frame2,bg='white')
Framenord.pack(anchor=tk.CENTER,side=tk.LEFT,fill=tk.Y)
#Label Nord
LabelNord = tk.Label(Framenord,text='COORD NORD',font=font)
LabelNord.pack(anchor=tk.CENTER,side=tk.TOP,padx=10,expand=1,pady=5)
#Entree coord nord point
nord=tk.DoubleVar()
nord.set('')
entree2 = tk.Entry(Framenord, borderwidth=5,bg='white',textvariable=nord)
entree2.pack(anchor=tk.CENTER,side=tk.TOP,expand=1,pady=5)

#Cases est
Frameest = tk.Frame(Frame2,bg='white')
Frameest.pack(anchor=tk.CENTER,side=tk.LEFT,fill=tk.Y)
#Label est
LabelEst = tk.Label(Frameest,text='COORD EST',font=font)
LabelEst.pack(anchor=tk.CENTER,side=tk.TOP,padx=50,expand=1,pady=5)
#Entree coord est point
est=tk.DoubleVar()
est.set('')
entree3 = tk.Entry(Frameest, borderwidth=5,bg='white',textvariable=est)
entree3.pack(anchor=tk.CENTER,side=tk.TOP,expand=1,pady=5)


#Radiobutton pour choix  et bouton conversion
Frame4 = tk.Frame(Framemiddle,borderwidth=5,relief=tk.RAISED)
Frame4.pack(side=tk.TOP)


#Fonction conversion grace a bouton, créer button radio dans lpoint1 et lpoint2
i=0
D={}
listenom=[]
def conv():
    global i
    global D
    global listenom
    lequel=conversion.get()
    try :
        L=[nord.get(),est.get()]
    except tk.TclError :
        tkmsg.showerror('Erreur','La valeur des coordonnées doit être un nombre')
        return
    
    test=ex.Point_Terre(L)   # utilisé ligne 308
    lequel=str(lequel)
    n=(eval('test.'+lequel+'()'))
    if lequel == 'cartesien':
        reponse = 'x={} ; y={} ; z={}'.format(round(n[0],2),round(n[1],2),round(n[2],2))
    if lequel == 'cylindrique':
        reponse = 'p={} ; O={} ; z={}'.format(round(n[0],2),round(n[1],2),round(n[2],2))
    if lequel == 'spherique':
        reponse = 'r={} ; O={} ; phi={}'.format(round(n[0],2),round(n[1],2),round(n[2],2))
    res.set(reponse)
    #nord.set('')
    #est.set('')
    nm=str(nom.get())
    for j in D :
        if D[j]==L:
            return

    if nm in listenom:
        if tkmsg.askyesno('Confirmer','Un point a déjà ce nom, voulez vous continuer ?'):
            pass
        else : 
            return
        
    elif nm=='':
        if tkmsg.askyesno('Confirmer','Vous n\'avez pas précisé de nom, voulez vous continuer ?'):
            pass
        else :
            return
    
    pt = "\'"+nm+"\'"
    try :
        exec("boutton"+str(i)+"=tk.Radiobutton(lpoint1,text="+pt+",variable=value1, value="+str(i)+").pack()")
    except SyntaxError :
        tkmsg.showerror('Erreur','Le nom contient un caractère interdit')
        return
    
    exec("boutton"+str(i)+str(i)+"=tk.Radiobutton(lpoint2,text="+pt+",variable=value2, value="+str(i)+").pack()")
    #nom.set('')
    listenom+=[nm]
    D[i]=L
    i+=1
    
    
    
def lecalcul():
    global D
    pt1=int(value1.get())
    pt2=int(value2.get())
    try :
        pt2=D[pt2]
    except KeyError :
        return
        
    pt1=D[pt1]
    if pt1==pt2:
        distance.set('0 km')
        if choix.get()==0:
            latence.set('0 s')
        else :
            latence.set('0.48 s')
        tkmsg.showinfo('Info','Les points ont les mêmes coordonnées')
        return
    d = ex.Point_Terre.distance(ex.Point_Terre(pt1),ex.Point_Terre(pt2)) 
    distance.set('{} km'.format(round(d,2)))
    choixx= str(choix.get())
    n=eval('ex.Point_Terre.latence(ex.Point_Terre(pt1),ex.Point_Terre(pt2),'+choixx+')')
    latence.set('{} s'.format(round(n,5)))


#Radiobouton pour choix conversion
conversion=tk.StringVar()
conversion.set('cartesien')
car=tk.Radiobutton(Frame4,text='Cartésien',variable=conversion,value='cartesien')
cyl=tk.Radiobutton(Frame4,text='Cylindrique',variable=conversion,value='cylindrique')
sphe=tk.Radiobutton(Frame4,text='Sphérique',variable=conversion,value='spherique')
car.pack(anchor=tk.CENTER,side=tk.LEFT,pady=5)
cyl.pack(anchor=tk.CENTER,side=tk.LEFT,pady=5)
sphe.pack(anchor=tk.CENTER,side=tk.LEFT,pady=5)

#bouton conversion
button= tk.Button(Frame4,text='Calcul',command=conv,font=font,activeforeground='white',activebackground='black')
button.pack(anchor=tk.CENTER,side=tk.LEFT,padx=10,pady=5,ipadx=2,ipady=2)

#Affichage resultat
res=tk.StringVar()
res.set('')
resultat=tk.Label(Framemiddle,textvariable=res,font=fontresultat,borderwidth=2,relief=tk.GROOVE,bg='white')
resultat.pack(anchor=tk.CENTER,side=tk.TOP,fill=tk.Y,expand=1,pady=10)






#2eme moitié
partie2 = tk.Frame(fenetre,borderwidth=5,bg='white',relief=tk.SOLID)
partie2.pack(side=tk.BOTTOM,fill=tk.BOTH,expand=1)

#partie affichage des points(gauche)
points = tk.Frame(partie2,bg='white',borderwidth=7,relief=tk.GROOVE)
points.pack(side=tk.LEFT, fill=tk.BOTH,expand=1)

#partie affichage distance et latence(droite)
distlat = tk.Frame(partie2,bg='white',borderwidth=7,relief=tk.GROOVE)
distlat.pack(side=tk.LEFT, fill= tk.BOTH,expand=1)

#2 listes de points
lpoint1 = tk.LabelFrame(points,text='Point 1')
lpoint1.pack(side=tk.LEFT,fill=tk.BOTH,expand=1,padx=1)
lpoint2 = tk.LabelFrame(points,text='Point 2')
lpoint2.pack(side=tk.LEFT,fill=tk.BOTH,expand=1,padx=1)

#Value des points
value1 = tk.StringVar()
value1.set(0)
value2 = tk.StringVar()
value2.set(1)

#Distance
Distance= tk.Frame(distlat,borderwidth=5,relief=tk.RIDGE)
Distance.pack(side=tk.TOP,fill=tk.BOTH,expand=1,padx=5,pady=5)
distance = tk.StringVar()
textedistance = tk.Label(Distance,text='Distance :',relief=tk.RIDGE,font=font)
textedistance.pack(fill=tk.Y,side=tk.LEFT,padx=5,pady=5)
distanceaffichage = tk.Label(Distance,textvariable=distance,font=fontresultat)
distanceaffichage.pack(fill=tk.BOTH,expand=1,side=tk.LEFT)

#Latence
Latence = tk.Frame(distlat,borderwidth=5,relief=tk.RIDGE)
Latence.pack(side=tk.TOP,fill=tk.BOTH,expand=1,padx=5,pady=5)
latence=tk.StringVar()
textelatence = tk.Label(Latence,text='Latence :',relief=tk.RIDGE,font=font)
textelatence.pack(fill=tk.Y,side=tk.LEFT,padx=5,pady=5)
latenceaffichage = tk.Label(Latence,textvariable=latence,font=fontresultat)
latenceaffichage.pack(fill=tk.BOTH,expand=1,side=tk.LEFT)

#Bouton et choix
Boutonchoix = tk.Frame(distlat, borderwidth=5,relief=tk.GROOVE)
Boutonchoix.pack(side=tk.TOP,padx=5,pady=5)

Choixmode=tk.Label(Boutonchoix,text ='Mode de communication : ')
Choixmode.pack(side=tk.LEFT)

choix=tk.IntVar()
choix.set(0)
fibre = tk.Radiobutton(Boutonchoix,text='Fibre',variable=choix,value=0)
sat = tk.Radiobutton(Boutonchoix,text='Satellite',variable=choix,value=1)
fibre.pack(anchor = tk.CENTER,side=tk.LEFT)
sat.pack(anchor=tk.CENTER,side=tk.LEFT)


#Bouton calcul
Buttoncalc = tk.Button(distlat, text='Calcul',command = lecalcul, relief = tk.RAISED,borderwidth=7,font=fontresultat,activeforeground='white',activebackground='black')
Buttoncalc.pack(fill=tk.BOTH,expand=1,pady=5,padx=5)


fenetre.mainloop()