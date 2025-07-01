import random


class Personaje:
    
    
    def __init__(self, nombre, fuerza, defensa, energia, vida):
        self.nombre = nombre
        self.fuerza = fuerza
        self.defensa = defensa
        self.energia = energia
        self.vida = vida
        
    def atributos(self):
        return (f'Guerrero: {self.nombre}\n-Fuerza: {self.fuerza}\n-Defensa: {self.defensa}\n-Vida: {self.vida}\n-Energia: {self.energia}').title()


    def esta_vivo(self):
        return self.vida > 0
    
    def morir(self):
        self.vida = 0 # Asegura que la vida no quede negativa
        
        
    def validar_vivo(self, enemigo):
        if enemigo.esta_vivo():
            print(f"- La vida de {enemigo.nombre} ahora es: {enemigo.vida}.")
        else:
            print(f"<<<<<<<<<<<<<<<   {enemigo.nombre.upper()} ha muerto en combate.  >>>>>>>>>>>>>")
            enemigo.morir()
    
    def daño(self, enemigo):
        
        if self.vida < 40:
            print(f"{self.nombre} está debilitado pero se vuelve más fuerte. ¡Fuerza x1.5!")
            print()
            daño = int(max(( self.fuerza * 1.5) - enemigo.defensa, 0)) # si la vida es menor de 40 sus golpes tendran el doble de fuerza
        else:
            daño = max(self.fuerza - enemigo.defensa, 0)
        return daño
    
    def atacar(self, enemigo):
        daño = self.daño(enemigo)
        enemigo.vida -= daño
        print(self.nombre, "ha realizado", daño, "puntos de daño a", enemigo.nombre)
        if enemigo.esta_vivo():
            print("La vida de", enemigo.nombre, "es", enemigo.vida)
        else:
            print()
            enemigo.morir()
            
    def golpe_multiple(self, enemigo):
        
        golpe_aleatorio = random.randint(1, 3)
        daño = self.daño(enemigo) * golpe_aleatorio
        enemigo.vida = max(enemigo.vida - daño, 0)
        energia_recibida = golpe_aleatorio * 10
        
        if self.energia >= 100:
            energia_recibida = 0
            print(self.nombre, "ha acertado", golpe_aleatorio, "golpes, haciendo", daño, "puntos de daño a", enemigo.nombre)
            print()
            print("<<<<<<<<  !! LA ENERGIA ESTA AL MAXIMO !! >>>>>>>>")
            
        else:
            self.energia = min(self.energia + energia_recibida, 100) # Limite max en 100
            print(self.nombre, "ha acertado", golpe_aleatorio, "golpes, haciendo", daño, "puntos de daño a", enemigo.nombre)
            print()
            print(f"- Has recibido {energia_recibida} puntos de energia!")
            print(f"- La Energia de {self.nombre} es de: {self.energia}")
            print()
        enemigo.validar_vivo(enemigo)
       
    def curar(self):
        cura_aleatoria = random.randint(35, 75)
        vida_antes = self.vida
        self.vida = min(self.vida + cura_aleatoria, 150) # Limite en 150
        curacion_real = self.vida - vida_antes # para mostrar el mensaje con la curacion no mayor a la vida maxima
        print(f"{self.nombre} se ha curado {curacion_real} puntos de vida!")
    
    def calcular_max_rand(energia):
        if energia >= 100:
            return 100
        elif energia >= 80:
            return 99
        elif energia >= 60:
            return 79
        elif energia >= 40:
            return 59
        else:
            return 39

            
    def get_fuerza(self):
        return self.fuerza
    
    def set_fuerza(self, nuevo_valor):
        if nuevo_valor < 0:
            print("Error, has introducido un valor negativo")
        else:
            self.fuerza = nuevo_valor
            print(f"La nueva fuerza de {self.nombre} es {self. fuerza}")
