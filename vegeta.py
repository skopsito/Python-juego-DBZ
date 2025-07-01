from ClasesPersonajes import Personaje
import random

class Vegueta(Personaje):
    def __init__(self, nombre, fuerza, defensa, energia, vida):
        super().__init__(nombre, fuerza, defensa, energia, vida)
        
        self.frases = ["Yo soy el príncipe de todos los Saiyajin!",
                       "No necesito ayuda de nadie, ¡ni siquiera de Kakarotto!",
                       "Puedes destruir planetas, pero nunca destruirás lo que soy: ¡Yo soy el Guerrero de la Raza Saiyajin!",
                       ]
    
    def descripcion(self) -> str:
        print(f"{self.nombre} se caracteriza por ser el príncipe de la raza Saiyajin, una especie guerrera extraterrestre.")
        print()
        print("- Es el príncipe de los Saiyajin, una raza alienígena guerrera.")
        print("- Se obsesiona con superar a Goku.")
        print("- Es conocido por su orgullo, arrogancia y soberbia.")
    
    
    def habilidad_especial(self, enemigo):
        if self.energia < 20:
            print("No tienes suficiente energia para usar esta Habilidad !!")
            return
        
        frase_aleatoria = random.choice(self.frases)
        print(frase_aleatoria)
        print("MUERE INSECTO....GAAALIICKKK GUUUNNNNN ! ! !")
        print()

        max_rand = Personaje.calcular_max_rand(self.energia)

        energia_usada = min(random.randint(20, max_rand), self.energia)
        energia_usada = (energia_usada // 10) * 10
        fuerza_aleatorio = energia_usada / 10

        daño = int(max((self.fuerza * fuerza_aleatorio) - enemigo.defensa, 0))       
        enemigo.vida = int(max(enemigo.vida - daño , 0)) # aseguramos q la vida minimo sea 0
        self.energia = max(self.energia - energia_usada, 0)
        

        print("="*60)
        print(f"{self.nombre} ha lanzado un poderoso ataque especial!")
        print(f"🔥 {daño} puntos de daño infligidos a {enemigo.nombre} 🔥")
        print(f"⚡ Energía gastada: {energia_usada} | Energía restante: {self.energia} ⚡")
        print("="*60)
        super().validar_vivo(enemigo)
        print()