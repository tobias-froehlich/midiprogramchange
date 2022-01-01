import tkinter as tk
import mido

banks = [
    {
        "name": "Bank 1",
        "programs": [
            {"name": "Grand Piano 1", "index": 0},
            {"name": "Classic Grand Piano", "index": 3},
            {"name": "Stage E.Piano", "index": 6},
            {"name": "Digital E.Piano", "index": 9},
            {"name": "Harpsicord", "index": 12},
            {"name": "Vibraphone", "index": 15},
            {"name": "Jazz Organ 1", "index": 18},
            {"name": "Church Organ 1", "index": 21},
            {"name": "Strings", "index": 24},
            {"name": "Choir Hoo", "index": 27},
        ],
    },
    {
        "name": "Bank 2",
        "programs": [
             {"name": "Bright Piano", "index": 1},
             {"name": "Honky-Tonky", "index": 4},
             {"name": "Club E.Piano", "index": 7},
             {"name": "60's E.Piano", "index": 10},
             {"name": "Clav.", "index": 13},
             {"name": "Marimba", "index": 16},
             {"name": "Jazz Organ 2", "index": 19},
             {"name": "Church Organ 2", "index": 22},
             {"name": "Slow Strings", "index": 25},
             {"name": "Choir Doo", "index": 28},
        ],
    },
    {
        "name": "Bank 3",
        "programs": [
            {"name": "Grand Piano 2", "index": 2},
            {"name": "E.Grand Piano", "index": 5},
            {"name": "Thin E.Piano", "index": 8},
            {"name": "Vintage E.Piano", "index": 11},
            {"name": "Wah Clav.", "index": 14},
            {"name": "Acoustic Guitar", "index": 17},
            {"name": "Jazz Organ 3", "index": 20},
            {"name": "Church Organ 3", "index": 23},
            {"name": "Warm Pad", "index": 26},
            {"name": "Choir Pad", "index": 29},

        ],
    },
]

class Gui(tk.Frame):

    def __init__(self, master):
        super().__init__(master)
        self.__portOut = mido.open_output(name="program-change", client_name="program-change", virtual=True)
        for ibank in range(len(banks)):
            bankName = banks[ibank]["name"]
            label = tk.Label(self, text=bankName)
            label.grid(column=0, row=ibank, sticky="nswe")
            for iprogram in range(len(banks[ibank]["programs"])):
                programName = banks[ibank]["programs"][iprogram]["name"]
                programIndex = banks[ibank]["programs"][iprogram]["index"]
                def makeSendMessageFunction(program):
                    def sendMessage():
                        for channel in range(16):
                            self.__portOut.send(
                                mido.Message(
                                    "program_change",
                                    channel=channel,
                                    program=program,
                                    time=0
                                )
                            )
                    return sendMessage
                button = tk.Button(self, text=programName, command=makeSendMessageFunction(programIndex))
                button.grid(column=iprogram+1, row=ibank, sticky="nswe")

root = tk.Tk()
gui = Gui(root)
gui.pack()
root.mainloop()
