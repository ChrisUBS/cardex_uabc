import tkinter
from GUI.menu_interface import MenuInterface

def main():
    app = MenuInterface(tkinter.Tk())
    app.root.mainloop()

if __name__ == "__main__":
    main()