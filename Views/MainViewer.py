import tkinter
import tkinter.filedialog
import re
import tkinter.messagebox
import time
import threading

class GUI:
    def __init__(self, height:int, width:int, title:str, iconPath:str = ""):
        self.__GUI = tkinter.Tk()
        self.__GUI.geometry(f"{width}x{height}")
        self.__GUI.title(f"{title}")
        self.__GUI.iconbitmap(f"{iconPath}")

        self.__txtPath = tkinter.Label(self.__GUI, text="Choose your txt log file: ")
        self.__btnChoosePath = tkinter.Button(self.__GUI, text="Open", command=lambda:self.__btnChoosePathEvent())
        self.__txtLog = tkinter.Text(self.__GUI, wrap="word", height=100, width=200)

    def __body(self):
        self.__txtPath.grid(row=0,column=2)
        self.__btnChoosePath.grid(row=0, column=3)
        
    def __btnChoosePathEvent(self):
        file = tkinter.filedialog.askopenfile(mode="r")
        
        pattern = re.compile(r"\w+.txt")
        if not re.search(pattern=pattern, string=file.name):
            tkinter.messagebox.showerror(title="Error 1", message="No has escogido un archivo *.txt")
            return
        
        self.__txtLog.grid(row=1, column=2)
        self.__printLog(path=file.name, txtWidgent=self.__txtLog)
        self.__txtPath["text"] = file.name
        
    def __printLog(self, path:str, txtWidgent:tkinter.Text):
        def update():
            try:
                with open(path, 'r') as file:
                    file.seek(0, 2)
                    while True:
                        line = file.readline()

                        if line:
                            txtWidgent.insert(tkinter.END, line)
                            txtWidgent.see(tkinter.END)
                        else:
                            time.sleep(0.5)
            except Exception as e:
                tkinter.messagebox.showerror(title="Error 2", message=f"Algo ha sucedido al querer leer el log\nError: {e}")
        threading.Thread(target=update, daemon=True).start()
        
    def start(self):
        self.__body()
        self.__GUI.mainloop()

x = GUI(height=400, width=700, title="Prueba")
x.start()