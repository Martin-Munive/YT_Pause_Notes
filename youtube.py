import pygetwindow as gw

def find_youtube_tab():
    # Obtener todas las ventanas activas
    windows = gw.getAllTitles()

    # Buscar una pestaña del navegador con "YouTube" en el título
    for window in windows:
        if "YouTube" in window:
            return window

    return None

def pause_youtube():
    youtube_tab = find_youtube_tab()
    if youtube_tab:
        return f"Video de YouTube encontrado en la pestaña: {youtube_tab}"
    else:
        return "No se encontró una pestaña de YouTube."