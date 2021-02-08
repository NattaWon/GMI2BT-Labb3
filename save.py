import json
import os


class History():
    def read_json(url):
        try:
            with open(url, "r") as f:
                data = json.load(f)
                return data
        except FileNotFoundError as error:
            print(error)

    def write_json(url, data):
        try:
            f = os.stat(url).st_size
            print(f)
            list = []
            if f > 0:
                old_list = History.read_json(url)
                print(old_list)
                for i in old_list:
                    list.append(i)
            list.append(data)
            with open(url, "w") as file:
                json.dump(list, file)
        except FileNotFoundError as error:
            print(error)


#import tkinter
#
#window = tkinter.Tk()
#window.title("This is the main window ")
#
# def CreateMain():
#    bt1 = tkinter.Button(window, text="Search for a movie"). pack() #when clicked it should show Search..
#    bt2 = tkinter.Button(window, text="View recent search"). pack()
#    bt2 = tkinter.Button(window, text="Exit"). pack()
#tkinter.Button(window, text="Menu choice", command = CreateMain ).pack()
#
# window.mainloop()
#
# ------------How to create fields---------------------

# Create 2 text fields and input fields
    # tkinter.Label(window, text = "Username") .grid(row = 0) #place in row 0 column 0
# "Entery" is used to display the input fields
    # tkinter.Entry(window).grid(row = 0, column = 1)#place in row 0 column 1
    #
    #tkinter.Label(window, text = "Password") .grid(row = 1)
    #tkinter.Entry(window).grid(row = 1, column = 1)
    #
    #tkinter.Checkbutton(window, text = "Keep me looged in").grid(columnspan = 2)
    #
    # window.mainloop()

#-----------How to create a buttons fram-------------########

# creating 2 frames TOP and Bottom
    #top_frame = tkinter.Frame(window).pack()
    #bottom_frame = tkinter.Frame(window).pack(side = "bottom")

# creating some widgets in the top_frame and bottom_frame
    #btn1 = tkinter.Button(top_frame, text = "Buttom1", fg = "green").pack()
    #btn2 = tkinter.Button(top_frame, text = "Buttom1", fg = "green").pack()
    #btn2 = tkinter.Button(bottom_frame, text = "Buttom2", fg = "red").pack(side = "left")
    #btn2 = tkinter.Button(bottom_frame, text = "Buttom2", fg = "red").pack(side = "left")
    #
    # window.mainloop()
