import tkinter as tk  # Biblioteca para crear interfaces gráficas
from tkinter import ttk  # Extensiones de Tkinter para widgets más avanzados
import time  # Biblioteca para manejar retardos en la ejecución
from random import randint  # Biblioteca para generar números aleatorios

# Clase principal para simular la administración de memoria en la CPU
class MemorySimulator:
    def __init__(self, root):
        # Configuración inicial de la ventana principal
        self.root = root
        self.root.title("Simulación de Administración de Memoria - CPU")  # Título de la ventana
        self.root.geometry("800x600")  # Tamaño de la ventana
        self.root.configure(bg="#f5f5f5")  # Color de fondo de la ventana

        # Inicialización de la memoria como una lista de 100 espacios vacíos
        self.memory = ["Libre" for _ in range(100)]  # Cada espacio es 'Libre'

        # Variables para rastrear el espacio ocupado por el programa, variables e instrucciones
        self.program_size = 0
        self.variable_space = 0
        self.instruction_space = 0

        # Llama al método que crea los elementos gráficos de la interfaz
        self.create_widgets()

    def create_widgets(self):
        # Etiqueta de título principal
        title = tk.Label(
            self.root, text="CPU - Simulación de Administración de Memoria", 
            font=("Helvetica", 16), bg="#f5f5f5"
        )
        title.pack(pady=10)  # Espaciado alrededor del título

        # Marco para los botones de control (Cargar, Ejecutar, Reiniciar)
        control_frame = tk.Frame(self.root, bg="#f5f5f5")
        control_frame.pack(pady=10)

        # Botón para cargar un programa en memoria
        load_button = ttk.Button(control_frame, text="Cargar Programa", command=self.load_program)
        load_button.grid(row=0, column=0, padx=5)

        # Botón para ejecutar el programa cargado
        execute_button = ttk.Button(control_frame, text="Ejecutar", command=self.execute_program)
        execute_button.grid(row=0, column=1, padx=5)

        # Botón para reiniciar la memoria a su estado inicial
        reset_button = ttk.Button(control_frame, text="Reiniciar", command=self.reset_simulation)
        reset_button.grid(row=0, column=2, padx=5)

        # Marco para el canvas que representa visualmente la memoria
        memory_frame = tk.Frame(self.root, bg="#f5f5f5")
        memory_frame.pack(pady=20)

        # Canvas donde se mostrarán los bloques de memoria
        self.memory_canvas = tk.Canvas(memory_frame, width=600, height=400, bg="#e6e6e6", relief="ridge", bd=2)
        self.memory_canvas.pack()

        # Lista para almacenar las referencias a los bloques de memoria dibujados
        self.memory_blocks = []
        for i in range(10):  # 10 filas de bloques
            for j in range(10):  # 10 columnas de bloques
                # Coordenadas de cada bloque en el canvas
                x1, y1 = j * 60 + 10, i * 40 + 10
                x2, y2 = x1 + 50, y1 + 30
                # Dibuja el bloque con un color inicial gris
                block = self.memory_canvas.create_rectangle(x1, y1, x2, y2, fill="#d9d9d9", outline="#bfbfbf")
                self.memory_blocks.append(block)  # Agrega el bloque a la lista

    def load_program(self):
        # Genera un tamaño aleatorio para el programa entre 10 y 30 unidades
        self.program_size = randint(10, 30)
        # Encuentra el primer espacio libre en memoria que pueda acomodar el programa
        start_index = self.find_free_space(self.program_size)

        if start_index is not None:
            # Llena el espacio en memoria con color azul (representando el programa)
            self.fill_memory(start_index, self.program_size, "#87ceeb")
            self.show_message(f"Programa cargado: ocupa {self.program_size} unidades.")
            # Después de cargar el programa, asigna espacio para las variables
            self.root.after(500, lambda: self.allocate_variables(start_index))
        else:
            # Si no hay suficiente espacio en memoria
            self.show_message("No hay suficiente espacio en memoria.")

    def find_free_space(self, size):
        # Busca un espacio continuo en la memoria de tamaño suficiente
        consecutive_free = 0
        for i in range(len(self.memory)):
            if self.memory[i] == "Libre":
                consecutive_free += 1
                if consecutive_free == size:
                    return i - size + 1  # Devuelve el índice inicial del espacio
            else:
                consecutive_free = 0
        return None  # Si no encuentra espacio suficiente, devuelve None

    def fill_memory(self, start, size, color):
        # Llena la memoria desde el índice `start` con `size` unidades del color dado
        for i in range(start, start + size):
            self.memory[i] = "Ocupado"  # Marca el bloque como ocupado
            self.memory_canvas.itemconfig(self.memory_blocks[i], fill=color)  # Cambia el color del bloque

    def allocate_variables(self, start_index):
        # Genera un tamaño aleatorio para las variables entre 5 y 10 unidades
        self.variable_space = randint(5, 10)
        # Llena la memoria con color verde (representando variables)
        self.fill_memory(start_index, self.variable_space, "#90ee90")
        self.show_message(f"Variables cargadas: ocupan {self.variable_space} unidades.")
        # Asigna espacio para las instrucciones después de las variables
        self.root.after(500, lambda: self.allocate_instructions(start_index + self.variable_space))

    def allocate_instructions(self, start_index):
        # Genera un tamaño aleatorio para las instrucciones entre 5 y 10 unidades
        self.instruction_space = randint(5, 10)
        # Llena la memoria con color rojo (representando instrucciones)
        self.fill_memory(start_index, self.instruction_space, "#ffcccb")
        self.show_message(f"Instrucciones cargadas: ocupan {self.instruction_space} unidades.")
        self.show_message("Programa cargado y listo para ejecutarse.")

    def execute_program(self):
        # Inicia la ejecución del programa
        self.show_message("Ejecutando el programa...")
        self.root.after(2000, self.complete_execution)

    def complete_execution(self):
        # Calcula el total de espacio ocupado en memoria
        total_space = self.program_size + self.variable_space + self.instruction_space
        self.show_message(f"Ejecución completada. Espacio total ocupado: {total_space} unidades.")
        # Reinicia la simulación después de completar la ejecución
        self.root.after(2000, self.reset_simulation)

    def reset_simulation(self):
        # Reinicia todos los bloques de memoria a su estado inicial (Libre)
        for i in range(len(self.memory)):
            self.memory[i] = "Libre"
            self.memory_canvas.itemconfig(self.memory_blocks[i], fill="#d9d9d9")
        self.show_message("Memoria reiniciada.")

    def show_message(self, message):
        # Muestra un mensaje temporal en la parte inferior de la ventana
        message_label = tk.Label(
            self.root, text=message, font=("Helvetica", 12), bg="#f5f5f5", fg="#333"
        )
        message_label.pack(pady=10)
        self.root.after(3000, message_label.destroy)  # Elimina el mensaje después de 3 segundos


# Punto de entrada del programa
if __name__ == "__main__":
    root = tk.Tk()  # Crea la ventana principal
    app = MemorySimulator(root)  # Inicializa la simulación
    root.mainloop()  #Inicia el bucle principal de la interfaz grafica 

