# -*- coding: utf-8 -*-
"""
Created on Mon Jun  4 22:38:10 2018

@author: antoni
"""
#ejemplo: 0-> PAR 1 -> Impar
#juego = JuegoParImpar(0,10)
#juego.jugar()
import random as rnd
class JuegoParImpar:
    def __init__(self,jugador,puntos_maximos):
        self.jugador = jugador
        self.puntos_jugador = 0
        self.puntos_ordenador = 0
        self.puntos_maximos = puntos_maximos 
        print("Bienvenid@ al juego de Par Impar, el objetivo consiste en que"+
              " la suma de tu jugada y la de la máquina sea un número par "+
              "(si has elegido ser par) o impar en caso contrario. "+
              "Gana el jugador que llegue a "+str(self.puntos_maximos)+
              " puntos")
        if(self.jugador):
            print("\nTienes que conseguir que la suma sea IMPAR")
        else:
            print("\nTienes que conseguir que la suma sea PAR")
    def jugar(self):
        while (self.puntos_jugador < self.puntos_maximos and
               self.puntos_ordenador < self.puntos_maximos):
            print("Jugador: \t"+str(self.puntos_jugador)+" puntos"+
                  "\nOrdenador: \t"+str(self.puntos_ordenador)+" puntos")
            cantidad_jugador = input("¿Cuánto quieres sacar?: ")
            cantidad_ordenador = rnd.choice(range(0,10))
            print("Tus jugada: "+str(cantidad_jugador))
            print("Jugada del ordenador: "+str(cantidad_ordenador))
            suma = int(cantidad_jugador) + cantidad_ordenador
            if (suma % 2 == 0):
                print("La jugada ha sido PAR")
                if(self.jugador):
                    self.puntos_ordenador += 1
                else:
                    self.puntos_jugador += 1
            else:
                print("La jugada ha sido IMPAR")
                if(self.jugador):
                    self.puntos_jugador += 1
                else:
                    self.puntos_ordenador += 1
            print("----------------------------")
            
        if (self.puntos_jugador > self.puntos_ordenador):
            print("HAS GANADO!")
        else:
            print("HAS PERDIDO! con "+str(self.puntos_jugador)+
                  " puntos frente a los "+str(self.puntos_ordenador)+
                  " puntos del ordenador")
        
            