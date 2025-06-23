import tkinter
import tkinter.filedialog
import re

class GUI:
    def __init__(self, height:int, width:int, title:str, iconPath:str = ""):
        self.__GUI = tkinter.Tk()
        self.__GUI.geometry(f"{width}x{height}")
        self.__GUI.title(f"{title}")
        self.__GUI.iconbitmap(f"{iconPath}")

        self.__txtPath = tkinter.Label(self.__GUI, text="Choose your txt log file: ")
        self.__btnChoosePath = tkinter.Button(self.__GUI, text="Open", command=lambda:self.__btnChoosePathEvent())
        self.__txtLog = tkinter.Text(self.__GUI)

    def __body(self):
        self.__txtPath.grid(row=0,column=2)
        self.__btnChoosePath.grid(row=0, column=3)
        
    def __btnChoosePathEvent(self):
        file = tkinter.filedialog.askopenfile(mode="r")
        self.__txtPath["text"] = file.name

        

    def start(self):
        self.__body()
        self.__GUI.mainloop()

x = GUI(height=400, width=700, title="Prueba")
x.start()