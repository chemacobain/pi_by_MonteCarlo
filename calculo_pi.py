import random
import math

from bokeh.models.annotations import Legend, Title
from estadisticas import desviacion_estandar, media
from bokeh.plotting import figure, output_file, show

class Coordenadas():
    def __init__(self, x_in_circle,y_in_circle,x_out_circle,y_out_circle):

        self.x_in_circle = x_in_circle
        self.y_in_circle = y_in_circle
        self.x_out_circle = x_out_circle
        self.y_out_circle = y_out_circle

def aventar_agujas(numero_de_agujas):
    dentro_del_circulo = 0

    for _ in range(numero_de_agujas):
        x = random.random() * random.choice([-1, 1])
        y = random.random() * random.choice([-1, 1])
        distancia_desde_el_centro = math.sqrt(x**2 + y**2)
    
        if distancia_desde_el_centro <=1:
            dentro_del_circulo +=1

    return (4 * dentro_del_circulo) / numero_de_agujas

def estimacion(numero_de_agujas,numero_de_intentos):
    estimados = []

    for _ in range(numero_de_intentos):
        estimacion_pi = aventar_agujas(numero_de_agujas)
        estimados.append(estimacion_pi)
    
    media_estimados = media(estimados)
    sigma = desviacion_estandar(estimados)
    print(f'Est={round(media_estimados,5)},sigma={round(sigma,5)}, agujas= {numero_de_agujas}')
    return [media_estimados, sigma]

def estimar_pi(precision, numero_de_intentos):
    numero_de_agujas = 1000
    sigma = precision
    while sigma >= precision / 1.96 : 
        media,sigma = estimacion(numero_de_agujas, numero_de_intentos)
        numero_de_agujas *= 2
    
    return media

def graficar(numero_de_agujas):
    x_in_circle = []
    y_in_circle = []
    x_out_circle = []
    y_out_circle = []

    for _ in range(numero_de_agujas):
        x = random.random() * random.choice([-1, 1])
        y = random.random() * random.choice([-1, 1])
        distancia_desde_el_centro = math.sqrt(x**2 + y**2)
    
        if distancia_desde_el_centro <=1:
            x_in_circle.append(x)
            y_in_circle.append(y)
        else:
            x_out_circle.append(x)
            y_out_circle.append(y)
        
    plot = figure(plot_width=600, plot_height=600,title='Pi Calculation By Monte Carlo')
    plot.circle(x_in_circle, y_in_circle, size=5, color= '#3399FF' , alpha=0.5)
    plot.circle(x_out_circle, y_out_circle, size=5, color= '#FFFF00', alpha=0.5)
    show(plot)
        
if __name__ == '__main__':
    print('Bienvenido a Calculo de pi usando el Metodo de Monte Carlo')
    op = int(input('Opciones \n 1. si deseas calcular pi \n 2. Graficar lanzamiento de dardos \n ->' ))

    if op == 1 : 
        print('Vamos a calcular pi')
        precision = float(input('Escribe el error maximo que deseas: \n '))
        num_tiros = int(input('Elige un numero de dardos inicial para lanzar \n'))
        estimar_pi(precision,1000)
    elif op ==2:
        n = int(input('Cuantos dardos deseas lanzar? \n'))
        graficar(n)
    else: 
        print('Error, no existe la opción que tecleaste.')