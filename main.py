import tkinter as tk
import chrome


def on_estado_button_click():
    chrome_status = chrome.check_chrome_status()
    youtube_tab_status = chrome.check_youtube_tab()
    status_label.config(text=chrome_status)
    url_label.config(text=youtube_tab_status)


root = tk.Tk()
root.title("Estado de Chrome")

estado_button = tk.Button(root, text="Verificar Estado",
                          command=on_estado_button_click)
estado_button.pack()

status_label = tk.Label(root, text="", justify="left")
status_label.pack()

url_label = tk.Label(root, text="", justify="left")
url_label.pack()

root.mainloop()
