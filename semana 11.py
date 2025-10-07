import matplotlib.pyplot as plt
from collections import Counter
import statistics

# Datos de la encuesta (10 personas)
personas = [f"Persona {i}" for i in range(1, 11)]
horas_dormidas = [6, 7, 8, 5, 7, 6, 9, 8, 7, 6]
tazas_cafe = [2, 1, 3, 2, 1, 2, 1, 3, 2, 2]
tiempo_u = [15, 25, 20, 30, 10, 35, 25, 40, 15, 20]
redes = ["Instagram", "TikTok", "WhatsApp", "Instagram", "Facebook", 
         "TikTok", "Instagram", "WhatsApp", "TikTok", "Facebook"]

# --- Frecuencias y medidas ---
def mostrar_estadisticas(nombre, datos):
    conteo = Counter(datos)
    total = len(datos)
    print(f"\n📊 Estadísticas de {nombre}:")
    print("Valor\tFrecuencia\tRelativa")
    for valor, freq in conteo.items():
        relativa = round(freq / total, 2)
        print(f"{valor}\t{freq}\t\t{relativa}")
    
    try:
        media = round(statistics.mean(datos), 2)
        mediana = round(statistics.median(datos), 2)
        moda = statistics.mode(datos)
        print(f"\nMedia: {media}")
        print(f"Mediana: {mediana}")
        print(f"Moda: {moda}")
    except:
        print("\n(No se puede calcular media/mediana/moda para datos categóricos)")

# --- Gráficas ---
def grafico_lineas():
    plt.figure(figsize=(8,5))
    plt.plot(personas, horas_dormidas, marker='o', color='blue')
    plt.title("¿Cuántas horas dormiste anoche?")
    plt.xlabel("Personas")
    plt.ylabel("Horas")
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()

def grafico_barras():
    plt.figure(figsize=(8,5))
    plt.bar(personas, tazas_cafe, color='brown')
    plt.title("¿Cuántas tazas de café tomas al día?")
    plt.xlabel("Personas")
    plt.ylabel("Tazas")
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()

def grafico_post():
    conteo = Counter(redes)
    plt.figure(figsize=(6,6))
    plt.pie(conteo.values(), labels=conteo.keys(), autopct='%1.1f%%')
    plt.title("¿Qué red social usas más?")
    plt.tight_layout()
    plt.show()

def grafico_histograma():
    plt.figure(figsize=(8,5))
    plt.hist(tiempo_u, bins=5, color='purple', edgecolor='black')
    plt.title("¿Cuántos minutos te tardas en llegar a la U?")
    plt.xlabel("Minutos")
    plt.ylabel("Frecuencia")
    plt.tight_layout()
    plt.show()

# --- Ejecución directa ---
mostrar_estadisticas("Horas dormidas", horas_dormidas)
grafico_lineas()

mostrar_estadisticas("Tazas de café", tazas_cafe)
grafico_barras()

mostrar_estadisticas("Redes sociales", redes)
grafico_post()

mostrar_estadisticas("Tiempo en llegar a la U", tiempo_u)
grafico_histograma()
