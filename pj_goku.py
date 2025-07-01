from ClasesPersonajes import Personaje
import random


class Goku(Personaje):
    

    def __init__(self, nombre, fuerza, defensa,energia, vida):
        super().__init__(nombre, fuerza, defensa, energia, vida)

        self.super_saiyajin = False # atributo para poder transformarse
        self.turnos_para_transformarse = 0
        self.turnos_en_ssj = 0

        self.frases = ["Soy la esperanza del universo. Soy la respuesta a todos los\nseres vivos que claman por la paz.",
                       "¡Tus malvadas acciones son como una soga alrededor de tu cuello!",
                       "Soy la respuesta a todos los seres vivos que claman por la paz.\nSoy el protector de los inocentes. Soy la luz en la oscuridad"]
    
    def descripcion(self) -> str:
        print(f"{self.nombre} posee un espíritu combativo sumamente marcado, y es incapaz de resistirse a pelear con alguien que le parezca fuerte aun en los momentos más inoportunos.")
        print()
        print("- Espíritu combativo: Es muy competitivo y le encanta pelear, incluso en momentos inoportunos.")
        print("- Entrenamiento constante: Siempre busca mejorar sus habilidades y nunca está satisfecho con su fuerza actual")
        print("- Experto en artes marciales: Es un guerrero que pone a prueba sus habilidades de pelea en sus aventuras.")
    
    
    def habilidad_especial(self, enemigo):
        if self.energia < 20:
            print("No tienes suficiente energia para usar esta Habilidad !!")
            print()
            return
        
        frase_aleatoria = random.choice(self.frases)
        print(frase_aleatoria)
        print("KAA MEEE KAAA MEEEE HAAAAAAAAAAAAAAAAAAAAA !!!!")
        print()

        max_rand = Personaje.calcular_max_rand(self.energia)

        energia_usada = min(random.randint(20, max_rand), self.energia)
        energia_usada = (energia_usada // 10) * 10
        fuerza_aleatorio = energia_usada / 10
        """El doble // es el operador de división entera o "floor division".
        🔹 A diferencia del /, que da un número decimal, el // redondea hacia abajo y 
        devuelve solo la parte entera del resultado."""
            
    
        daño = int(max((self.fuerza * fuerza_aleatorio) - enemigo.defensa, 0))
        enemigo.vida = int(max(enemigo.vida - daño , 0))
        self.energia = max(self.energia - energia_usada, 0)
        
        print("="*60)
        print(f"{self.nombre} ha lanzado un poderoso ataque especial!")
        print(f"🔥 {daño} puntos de daño infligidos a {enemigo.nombre} 🔥")
        print(f"⚡ Energía gastada: {energia_usada} | Energía restante: {self.energia} ⚡")
        print("="*60)
        print()
        super().validar_vivo(enemigo)
        print()

    def transformarse_super_saiyajin(self):
        if self.super_saiyajin:
            print(f"{self.nombre} ya esta en Modo Super Saiyajin !!")
            return
        if self.energia < 30:
            print("Necesitas al menos 30 de energia para transformarte en Super Saiyajin !!")
            return
        
        if self.turnos_para_transformarse < 15:
            print(f"{self.nombre} aún no puede transformarse. Le faltan: {15 - self.turnos_para_transformarse} turnos.")
            return
        
        
        self.energia = max(self.energia - 30, 0)
        self.super_saiyajin = True
        self.turnos_en_ssj = 3 # solo dura 2 turnos la transformacion
        self.fuerza = int(self.fuerza * 2)
        self.defensa = int(self.defensa * 1.5)

        print("="*60)
        print(f"🔥 {self.nombre} se ha transformado en ¡¡¡SUPER SAIYAJIN!!! 🔥")
        print("💥 Su fuerza y defensa han aumentado significativamente 💥")
        print(f"⚡ Energía restante: {self.energia}")
        print("="*60)
        print()
    
    def volver_estado_normal(self):
        if self.super_saiyajin:
            print()
            print(f"\033[1;33m    <<<<< {self.nombre} ha vuelto a su forma base ! >>>>>\033[0m")
            self.super_saiyajin = False
            self.turnos_en_ssj = 0
            self.turnos_para_transformarse = 0
            self.fuerza = int(self.fuerza / 2)
            self.defensa = int(self.defensa / 1.5)