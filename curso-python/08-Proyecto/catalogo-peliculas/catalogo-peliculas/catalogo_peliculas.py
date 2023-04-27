import tkinter as tk
from client.gui_app import Frame, barra_menu

def main(): 
    root = tk.Tk()
    root.title("Catalogo de peliculas")
    root.resizable(0,1)
    
    barra_menu(root)
    
    app = Frame(root = root)
        
    app.mainloop() #final ejecucion de la app

if __name__ == "__main__":
    main()