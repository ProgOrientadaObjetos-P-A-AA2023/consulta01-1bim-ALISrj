"""

"""

# Crear dos clases en Python
# Usted defina el nombre y los atributos
# Puede usar las mismas clases usadas en Java en los ejemplos estudiados

# clase 01


class Automotor():

    valor_matricula = 0

    def __init__(self, fabr, c, anioF, valor):
        self.fabricante = str(fabr)
        self.cedula = str(c)
        self.anio_fabricacion = int(anioF)
        self.valor = int(valor)
        print("Objeto creado\n")

    def establecer_fabricante(self, fabr):
        self.fabricante = fabr

    def establecer_cedula(self, c):
        self.cedula = c

    def establecer_anio_fabricacion(self, anioF):
        self.anio_fabricacion = anioF

    def establecer_valor(self, valor):
        self.valor = valor
        
    def calcular_valor_matricula(self):
        self.valor_matricula = 0.00002 * (self.valor * (2023 - self.anio_fabricacion))

    def obtener_fabricante(self):
        return self.fabricante

    def obtener_cedula(self):
        return self.cedula

    def obtener_anio_fabricacion(self):
        return self.anio_fabricacion

    def obtener_valor(self):
        return self.valor

    def __str__(self):

        mensaje = f"""
        Fabricante: {self.fabricante}
        Cédula: {self.cedula}
        Año de Fabricación: {self.anio_fabricacion}
        Valor: {self.valor}
        Matricula: {self.valor_matricula:.2f}\n"""

        return mensaje

        # clase 02
class Profesor():
    
    def __init__(self, n, a, sB):
        self.nombre = n
        self.apellido = a
        self.sueldoB = sB
        self.sueldoT = 0
        print("Objeto Creado")
        
    def establecer_nombre(self, n):
        self.nombre = n
        
    def establecer_apellido(self, a):
        self.apellido = a

    def establecer_sueldoB(self, sB):
        self.sueldoB = sB
        
    def calcular_sueldoT(self):
        self.sueldoT = self.sueldoB * 1.20
        
    def obtener_nombre(self):
        return self.nombre
        
    def obtener_apellido(self):
        return self.apellido

    def obtener_sueldoB(self):
        return self.sueldoB
        
    def obtener_sueldoT(self):
        return self.sueldoT
        
    def __str__(self) -> str:
        mensaje = f"""
        Nombre: {self.nombre}
        Apellido: {self.apellido}
        Sueldo Básico {self.sueldoB}
        Sueldo Total {self.sueldoT}
        """
        return mensaje