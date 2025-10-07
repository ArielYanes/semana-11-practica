import sys
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QPushButton, QLabel
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as Canvas
from matplotlib.figure import Figure
from collections import Counter
import statistics

# Datos
personas = [f"Persona {i}" for i in range(1, 11)]
horas_dormidas = [6, 7, 8, 5, 7, 6, 9, 8, 7, 6]
tazas_cafe = [2, 1, 3, 2, 1, 2, 1, 3, 2, 2]
tiempo_u = [15, 25, 20, 30, 10, 35, 25, 40, 15, 20]
redes = ["Instagram", "TikTok", "WhatsApp", "Instagram", "Facebook", 
         "TikTok", "Instagram", "WhatsApp", "TikTok", "Facebook"]

class Ventana(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Gráficas y Estadísticas")
        self.setGeometry(100, 100, 850, 650)

        self.layout = QVBoxLayout()
        self.canvas = Canvas(Figure(figsize=(8, 5)))
        self.ax = self.canvas.figure.add_subplot(111)

        # Etiqueta para estadísticas
        self.stats_label = QLabel("")
        self.stats_label.setStyleSheet("font-size: 14px;")

        # Botones
        self.btn_lineas = QPushButton("Horas dormidas")
        self.btn_barras = QPushButton("Tazas de café")
        self.btn_pastel = QPushButton("Red social más usada")
        self.btn_histograma = QPushButton("Tiempo a la U")

        # Conexiones
        self.btn_lineas.clicked.connect(lambda: self.mostrar_grafica("Horas dormidas", horas_dormidas, tipo="linea"))
        self.btn_barras.clicked.connect(lambda: self.mostrar_grafica("Tazas de café", tazas_cafe, tipo="barra"))
        self.btn_pastel.clicked.connect(lambda: self.mostrar_grafica("Red social más usada", redes, tipo="pastel"))
        self.btn_histograma.clicked.connect(lambda: self.mostrar_grafica("Tiempo a la U", tiempo_u, tipo="histograma"))

        # Añadir al layout
        self.layout.addWidget(self.canvas)
        self.layout.addWidget(self.stats_label)
        self.layout.addWidget(self.btn_lineas)
        self.layout.addWidget(self.btn_barras)
        self.layout.addWidget(self.btn_pastel)
        self.layout.addWidget(self.btn_histograma)

        self.setLayout(self.layout)

    def mostrar_grafica(self, nombre, datos, tipo):
        self.ax.clear()

        if tipo == "linea":
            self.ax.plot(personas, datos, marker='o', color='blue')
            self.ax.set_xticklabels(personas, rotation=45)
        elif tipo == "barra":
            self.ax.bar(personas, datos, color='brown')
            self.ax.set_xticklabels(personas, rotation=45)
        elif tipo == "pastel":
            conteo = Counter(datos)
            self.ax.pie(conteo.values(), labels=conteo.keys(), autopct='%1.1f%%')
        elif tipo == "histograma":
            self.ax.hist(datos, bins=5, color='purple', edgecolor='black')

        self.ax.set_title(nombre)
        self.canvas.draw()

        # Mostrar estadísticas
        self.stats_label.setText(self.calcular_estadisticas(nombre, datos))

    def calcular_estadisticas(self, nombre, datos):
        conteo = Counter(datos)
        total = len(datos)
        texto = f"<b>{nombre}</b><br>Frecuencia:<br>"

        for valor, freq in conteo.items():
            relativa = round(freq / total, 2)
            texto += f"{valor}: {freq} ({relativa})<br>"

        try:
            media = round(statistics.mean(datos), 2)
            mediana = round(statistics.median(datos), 2)
            moda = statistics.mode(datos)
            texto += f"<br>Media: {media}<br>Mediana: {mediana}<br>Moda: {moda}"
        except:
            texto += "<br>No aplica media/mediana/moda para datos categóricos"

        return texto

# Ejecutar
app = QApplication(sys.argv)
ventana = Ventana()
ventana.show()
sys.exit(app.exec_())
