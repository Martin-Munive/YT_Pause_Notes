# gui.py

import tkinter as tk
import youtube


def on_pause_button_click():
    message = youtube.pause_youtube()
    status_label.config(text=message)


root = tk.Tk()
root.title("Control de YouTube")

# Ajustar el tamaño de la ventana
button_width = 200
button_height = 50
window_width = button_width
# Doble de la altura del botón para incluir espacio para la etiqueta de estado
window_height = button_height * 2
root.geometry(f"{window_width}x{window_height}")

# Botón de pausa
pause_button = tk.Button(root, text="Pausar YouTube",
                         command=on_pause_button_click)
pause_button.place(x=0, y=0, width=button_width, height=button_height)

# Etiqueta de estado
status_label = tk.Label(root, text="", justify="center")
status_label.place(x=0, y=button_height,
                   width=button_width, height=button_height)

root.mainloop()
