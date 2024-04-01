import pyautogui
import time
import pyperclip

# Función para verificar si Chrome está corriendo


def check_chrome_status():
    try:
        chrome_window = pyautogui.getWindowsWithTitle('Google Chrome')[0]
        print("Estado: Chrome está corriendo.")
        return True
    except IndexError:
        print("Estado: Chrome no está corriendo.")
        return False

# Función para obtener la URL de la primera pestaña de YouTube activa en Chrome


def get_youtube_tab_url():
    try:
        # Hacer clic en la ventana de Chrome para asegurarse de que esté activa
        chrome_window = pyautogui.getWindowsWithTitle('Google Chrome')[0]
        chrome_window.activate()

        # Esperar un breve momento para que la ventana de Chrome se active completamente
        time.sleep(0.5)

        # Buscar la primera pestaña de YouTube activa
        youtube_tab = pyautogui.getWindowsWithTitle(
            'YouTube - Google Chrome')[0]

        # Cambiar a la pestaña de YouTube
        youtube_tab.activate()

        # Esperar un breve momento para que la pestaña de YouTube se active completamente
        time.sleep(0.5)

        # Copiar la URL de la pestaña de YouTube
        pyautogui.hotkey('ctrl', 'l')  # Seleccionar la barra de direcciones
        pyautogui.hotkey('ctrl', 'c')  # Copiar la URL

        # Obtener la URL del portapapeles
        url = pyperclip.paste()

        return url
    except Exception as e:
        print("Error al obtener la URL de la pestaña de YouTube:", str(e))
        return None


# Ejecutar las funciones
if check_chrome_status():
    youtube_url = get_youtube_tab_url()
    if youtube_url:
        print("URL de la primera pestaña de YouTube:", youtube_url)
    else:
        print("No se pudo obtener la URL de la primera pestaña de YouTube.")
