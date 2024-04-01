import psutil

def is_chrome_on(exename='Chrome.exe'):
    for process in psutil.process_iter(['pid', 'name']):
        if 'chrome' in process.info['name'].lower():
            return "Estado: Chrome está corriendo."
    return "Estado: Chrome está cerrado."
            
