from vegeta import Vegueta
from pj_goku import Goku
from cell import Cell
import time
import random


goku =    Goku("Goku",12, 5, 100, 150)
vegueta = Vegueta("Vegueta", 10, 5, 100, 150)
cell =    Cell("Cell", 14, 6, 100, 150) 

def mostrar_barras(signo):
    print(signo * 60)

def transicion_pelea(enemigo):
    print(f"              TU SIGUIENTE PELEA SERA CONTRA {enemigo.nombre.upper()}")
    time.sleep(3)
    print()
    time.sleep(3)
    print("----------------- !!! PREPARATE !!! -----------------")
    time.sleep(3)
    mostrar_barras("=")

def ejecutar_accion_general(personaje, enemigo, opcion = None):
    mostrar_barras("=")
    print(f"- - - - - - - - - - - - {personaje.nombre.upper()}- - - - - - - - - - - -")
    mostrar_barras("=")

    # Si es el jugador y no se pasó opción, se solicita por input
    if opcion == None:
        print(f"SELECCIONE UNA ACCION A EJECUTAR PARA {personaje.nombre}!")
        print("1.- Usar habilidad 'ATAQUE'.")
        print("2.- Usar habilidad 'ESPECIAL'.")
        print("3.- Usar habilidad 'CURA'.")
        if isinstance(personaje, Goku) and personaje.turnos_para_transformarse >= 15 and not personaje.super_saiyajin: # si personaje es una instancia de Goku
            print("\033[1;33m4.- ¡Transformarse en Super Saiyajin!\033[0m") # \033[ Inicia código ANSI >> 1;33m Negrita (1) + Amarillo (33) >> \033[0m Restaura el color a normal
        print()
        opcion = input(f"Selecciona una opcion para {personaje.nombre}: ").strip()
        print()
    
    if opcion == "1" or opcion == 1:
        mostrar_barras("=")
        personaje.golpe_multiple(enemigo)

    elif opcion == "2" or opcion == 2:
        mostrar_barras("=")
        personaje.habilidad_especial(enemigo)

    elif opcion == "3" or opcion == 3:
        mostrar_barras("=")
        if personaje.vida < 150:

            print(f"{personaje.nombre} ha usado su habilidad de curar")
            personaje.curar()
            print(f"- La vida de {personaje.nombre} ahora es de: {personaje.vida}")
        else:
            print(f"{personaje.nombre} ya tiene la vida al máximo.")
            personaje.golpe_multiple(enemigo)
    elif opcion == "4" or opcion == 4 and isinstance(personaje, Goku):
        personaje.transformarse_super_saiyajin()

    else:
        print("Opción inválida, por favor selecciona una opción válida.")
    
    time.sleep(3)
        
                
def jugar_turno( personaje, enemigo):
    # Contar turno
    if isinstance(personaje, Goku):
        personaje.turnos_para_transformarse += 1 # se suma cada turno

        if personaje.super_saiyajin:            # si esta transformado en Modo SSY
            personaje.turnos_en_ssj -= 1        # se resta el turno de ese Modo
            if personaje.turnos_en_ssj <= 0:    # si el turno de ese Modo llega a 0
                personaje.volver_estado_normal()# Volvera a su Modo base



    if enemigo.vida > 0:
        ejecutar_accion_general(personaje, enemigo) # aqui ataca Goku y si muere el enemigo con este ataque, 

    if enemigo.vida > 0: # no se le preguntara una opcion a ejecutar al enemigo
        
        opcion_enmigo = random.randint(1, 3)
        ejecutar_accion_general(enemigo, personaje, opcion= opcion_enmigo)
        
    elif enemigo.vida <= 0:
        if enemigo == cell and hasattr(cell, "autoDestruccion"):
            cell.autoDestruccion(personaje)
    
    
def play_game_2():
    mostrar_barras("=")
    print("Algunos Guerreros despues de X cantidad de turnos desbloquean una 4 Habilidad")
    time.sleep(2)
    print()
    print("Deberas estar atento para usarla (Solo durara 2 turnos)")
    time.sleep(3)
    print()
    mostrar_barras("=")
    print(goku.atributos())
    mostrar_barras("=")
    time.sleep(3)
    print(vegueta.atributos())
    mostrar_barras("=")
    time.sleep(3)
    print()
    print("----------------------- INICIANDO PELEA -----------------------")
    
    print()
    
    # Definir la secuencia del juego
    personajes = [goku]
    enemigos = [vegueta, cell]
    transicion_mostrada = False

    while any([personaje.esta_vivo() for personaje in personajes]) and any([enemigo.esta_vivo() for enemigo in enemigos]):
        if personajes[0].esta_vivo() and enemigos[0].esta_vivo():
            jugar_turno(personajes[0], enemigos[0])
        elif personajes[0].esta_vivo() and enemigos[1].esta_vivo():
            if not transicion_mostrada:
                transicion_pelea(enemigos[1])
                transicion_mostrada = True
                if isinstance(personajes[0], Goku):
                    personajes[0].volver_estado_normal()
                    personajes[0].turnos_para_transformarse = 0
            jugar_turno(personajes[0], enemigos[1])
        else:
            break
    if personajes[0].esta_vivo():
        print("\n----------- GOKU HA GANADO LA PELEA --------------")
        print("\n---------------!!!! FELICIDADES !!!!---------------")
    elif any(enemigo.esta_vivo() for enemigo in enemigos):
        if vegueta.esta_vivo():
            print("\n----------- VEGUETA HA GANADO LA PELEA --------------")
        elif cell.esta_vivo():
            print("\n----------- CELL HA GANADO LA PELEA --------------")
    else:
        print("\n---- No hay un ganador !! Todos han muerto !! --------")
    

        

play_game_2()