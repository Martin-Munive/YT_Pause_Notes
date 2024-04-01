import tkinter as tk
root = tk.Tk()
root.title("Youtube Stoper")
root.configure(background="white")
root.minsize(300, 100)
root.maxsize(300, 100)


def on_pause_button_click():
    message = "Estado: youtube.pause_youtube()"
    status_label.config(text=message)


# Botón de pausa
pause_button = tk.Button(root, text="Pausar YouTube",
                         command=on_pause_button_click)
pause_button.pack()

# Etiqueta de estado
status_label = tk.Label(
    root, text="Estado: Esperando acción.", justify="center")
status_label.pack()

root.mainloop()
