#dependancies: customtkinter, pywinstyles, pillow

import os
import customtkinter as CTK
from customtkinter import  filedialog
import pywinstyles as PYS
from PIL import Image

app = CTK.CTk()
app.geometry("660x470")
app.title("Badgel")
app.iconbitmap("icon.ico")
app.resizable(False,False)

def messages_changed(Messages):
    Messages = int(Messages)
    for i in range(8):
        if i <= Messages - 1:
            for o in Options[i]:
                PYS.set_opacity(o, value=1)
                o.configure(state="normal")
        elif i > Messages - 1:
            for o in Options[i]:
                PYS.set_opacity(o, value=0.5)
                o.configure(state="disabled")

def _attempt_upload():
    TotalMessages = int(MessagesOp.get())
    Command = 'python ./led-badge-11x44.py'
    Texts = ''
    Modes = '-m'
    Speeds = '-s'
    for i in range(TotalMessages):
        Speeds += Options[i][4].get()
        if i < TotalMessages-1:
            Speeds += ','
        ModeText = Options[i][3].get()
        Modes += str(ModeNames[ModeText])
        
        if i < TotalMessages-1:
            Modes+= ","
        match Options[i][1].get():
            case "Text":
                text = Options[i][2].get("0.0", "end")
                text = os.linesep.join([s for s in text.splitlines() if s])
                text = '"' + text + '"'
                Texts += " " + text
    Command += ' ' + Speeds + ' ' + ' ' + Modes + ' ' + Texts
    os.system('cmd /c ' +Command)

def op_set(Num):
    Ops = Options[Num]
    match Ops[1].get():
        case "Text":
            Ops[2].grid()
            Ops[5].grid_remove()
        case "Image":
            Ops[2].grid_remove()
            Ops[5].grid()

def img_but(Num):
    ChosenImg = filedialog.askopenfilename()

def img_ins(ImgPath):
    app.focus_get().insert(CTK.INSERT, ImgPath)

def _set_val(DropDown, i):
    DropDown.configure(command=lambda value: op_set(i))

def _set_file_button(Button, i):
    Button.configure(command=lambda: img_but(i))

def _set_img_button(Button, ImgPath):
    Button.configure(command=lambda: img_ins(ImgPath))

def _change_all_speed(Option):
    for i in Options:
        Options[i][4].set(Option)

def _change_all_mode(Option):
    for i in Options:
        Options[i][3].set(Option)

#Setup
Options = {}
ImgButtons = {}
ModeNames = {"Scroll Left": 0, "Scroll Right": 1, "Scroll Up": 2, "Scroll Down": 3,
         "Centered & Still": 4, "Animation": 5, "Drop Down": 6, "Curtain": 7, "Laser": 8}
for i in range(8):
    Offset = i + 2
    NewText = CTK.CTkLabel(app, text="Message " + str(i + 1), fg_color="transparent")
    NewText.grid(row=Offset, column=1, padx=0, pady=5)
    
    NewTypeChoice = CTK.CTkOptionMenu(app, values=["Text","Image"], width=75)
    #NewTypeChoice.grid(row=Offset, column=2, padx=5, pady=5)

    PicButton = CTK.CTkButton(app, width=300,height=31,fg_color="white",text_color="black",text="Click to select file")
    PicButton.grid(row=Offset, column=3,padx=5,pady=5)
    PicButton.grid_remove()
    
    NewBox = CTK.CTkTextbox(app, width=300, height=10)
    NewBox.grid(row=Offset, column=3, padx=5,pady=5)

    ModeChoice = CTK.CTkOptionMenu(app, values=["Scroll Left", "Scroll Right",
                                               "Scroll Up", "Scroll Down",
                                               "Centered & Still", "Animation",
                                               "Drop Down", "Curtain", "Laser"],
                                   width=130)
    ModeChoice.grid(row=Offset, column=4, padx=5,pady=5)

    SpeedChoice = CTK.CTkOptionMenu(app, values=["1","2","3","4","5",
                                                 "6","7","8"], width=10)
    SpeedChoice.grid(row=Offset, column=5, padx=5,pady=5)

    Options[i] = [NewText, NewTypeChoice, NewBox, ModeChoice,
                  SpeedChoice, PicButton]

for i in range(8):
    _set_val(Options[i][1], i)
    _set_file_button(Options[i][5], i)

ImgsFrame = CTK.CTkScrollableFrame(app,width=650,height=20,scrollbar_fg_color="transparent",orientation="horizontal")
ImgsFrame.grid(row=12,column=0,padx=10,sticky="ew",columnspan=6)
app.grid_columnconfigure(0, weight=1)
ImgsText = CTK.CTkLabel(app,text="Click images to insert into message")
ImgsText.grid(row=11,column=3,padx=5,pady=5,sticky="ew")
for i in range(len(os.listdir("gfx"))):
    if os.listdir("gfx")[i][-4:] == ".png":
        ImgOn = Image.open("gfx/"+os.listdir("gfx")[i])
        ImgImg = CTK.CTkImage(dark_image=ImgOn,size=ImgOn.size)
        ImgButton = CTK.CTkButton(ImgsFrame,image=ImgImg,text="",fg_color="transparent", width=ImgOn.size[0],height=ImgOn.size[1])
        ImgButton.grid(row=0,column=i)
        ImgButtons[ImgButton] = ":gfx/"+os.listdir("gfx")[i]+":"
for i in ImgButtons:
    _set_img_button(i, ImgButtons[i])

SubBut = CTK.CTkButton(app, command=_attempt_upload, text="Upload", width=300)
SubBut.grid(row=10,column=3)

#Topbar
MessagesText = CTK.CTkLabel(app, text="Messages: ")
MessagesText.grid(row=1,column=1)

MessagesOp = CTK.CTkOptionMenu(app, values=["1","2","3","4","5","6","7","8"],width=75,
                               command=messages_changed)
MessagesOp.grid(row=1,column=2)

ChangeAllMode = CTK.CTkOptionMenu(app, values=["Scroll Left", "Scroll Right",
                                               "Scroll Up", "Scroll Down",
                                               "Centered & Still", "Animation",
                                               "Drop Down", "Curtain", "Laser"],
                                   width=130,
                                  command=_change_all_mode)
ChangeAllMode.grid(row=1,column=4)

ChangeAllSpeed = CTK.CTkOptionMenu(app, values=["1","2","3","4","5",
                                                 "6","7","8"], width=10,
                                   command=_change_all_speed)
ChangeAllSpeed.grid(row=1,column=5)

messages_changed(1)

app.mainloop()
