import tkinter as tk
import chrome

root = tk.Tk()
root.title("Youtube Stopper")
root.configure(background="white")
root.minsize(300, 100)
root.maxsize(300, 100)


def on_pause_button_click():
    message = chrome.is_chrome_on()
    status_label.config(text=message)


# Botón de pausa
pause_button = tk.Button(root, text="Verificar Estado",
                         command=on_pause_button_click)
pause_button.pack()

# Etiqueta de estado
status_label = tk.Label(
    root, text="Estado: Esperando acción.", justify="center")
status_label.pack()

root.mainloop()
