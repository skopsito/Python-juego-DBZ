from ClasesPersonajes import Personaje
import random
import time

class Cell(Personaje):
    def __init__(self, nombre, fuerza, defensa, energia, vida):
        super().__init__(nombre, fuerza, defensa, energia, vida)
        
        self.frases = ["¡Es hora de mostrarte el verdadero poder de la perfección!",
                       "¡Prepárate para sentir el terror de mi Solar Kamehameha ! ¡Esto acabará con todo!",
                       "¡Este ataque destruirá todo lo que conoces!"]
    
    def habilidad_especial(self, enemigo):
        if self.energia < 20:
            print("No tienes suficiente energia para usar esta Habilidad !!")
            return
        
        frase_aleatoria = random.choice(self.frases)
        print(frase_aleatoria)
        print("Solar Kamehamehaaaaaaaaaaaaaa ! ! !")
        print()

        max_rand = Personaje.calcular_max_rand(self.energia)

        energia_usada = min(random.randint(20, max_rand), self.energia)
        energia_usada = (energia_usada // 10) * 10
        fuerza_aleatorio = energia_usada / 10
            
        daño = int(max((self.fuerza * fuerza_aleatorio) - enemigo.defensa, 0))
        enemigo.vida = int(max(enemigo.vida - daño , 0))
        self.energia = max(self.energia - energia_usada, 0)
        
        print("~"*60)
        print(f"{self.nombre} ha lanzado un poderoso ataque especial!")
        print(f"🔥 {daño} puntos de daño infligidos a {enemigo.nombre} 🔥")
        print(f"⚡ Energía gastada: {energia_usada} | Energía restante: {self.energia} ⚡")
        print("~"*60)
        super().validar_vivo(enemigo)
        print()
        
          
    def autoDestruccion(self, enemigo):
        print("💥💥💥 NO PUEDE SER... ¡NO PUEDEEE SEEERRRRRR! 💥💥💥")
        time.sleep(2)
        print("☠️☠️☠️ AUTO-DESTRUCCIÓN INMINENTE ☠️☠️☠️")
        time.sleep(2)
        print("💣 ¡BOOOOOOOMMMMMM! 💣")
        time.sleep(1)

        daño = max((self.fuerza * 5) - enemigo.defensa, 0)
        enemigo.vida = int(max(enemigo.vida - daño , 0))
        
        print("="*40)
        print(f"{self.nombre} se autodestruyó causando {daño} puntos de daño a {enemigo.nombre} 💥")
        print("="*40)
        super().validar_vivo(enemigo)
