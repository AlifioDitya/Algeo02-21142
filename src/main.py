import os
import tkinter as tk
from tkinter import *
from PIL import ImageTk, Image
from tkinter import filedialog
from time import sleep
from time import *             #meaning from time import EVERYTHING
import time
from datetime import timedelta


# VARIABEL GLOBAL
varfont = "./assets/HKGrotesk-Black.otf"
dataset_dir = "No File Choosen"
imagetest_dir = ""
imagetest_filename = "No File Choosen"  
imagetest_result = "" 
exec_time = "" 
WIDTH, HEIGHT = 1280, 720

root = tk.Tk()
root.geometry('{}x{}'.format(WIDTH, HEIGHT))   
root.title("Face Recognition")
root.resizable(False, False) 

# IMPORT PICTURES
bg = ImageTk.PhotoImage(Image.open("./assets/background.png").resize((WIDTH,HEIGHT)))
title_asset = ImageTk.PhotoImage(Image.open("./assets/Image_Robot.png").resize((200,200)))
button_choose = PhotoImage(file = "./assets/Button_ChooseFile.png")
button_choose_h = PhotoImage(file = "./assets/Button_ChooseFile_hover.png")
button_choose_c = PhotoImage(file = "./assets/Button_ChooseFile_clicked.png")
button_run = PhotoImage(file = "./assets/Button_RunResult.png")
button_run_c = PhotoImage(file = "./assets/Button_RunResult_clicked.png")
img_none = ImageTk.PhotoImage(Image.open("./assets/img_placeholder.png").resize((300,300)))

# FUNCS
def askopendataset():
    global imagetest_dir
    global photo_test
    try:
        # Menginput file
        dataset_dir = filedialog.askopenfilename(filetypes=[('Zip File', '*.zip')])
        dataset_dir = os.path.basename(dataset_dir)
        # Config File
        maincanvas.itemconfig(dataset_text, text=dataset_dir)
        
    except AttributeError:
        pass

def askopenfile():
    global imagetest_dir
    global imagetest_filename
    global img_display
    global photo_test
    try:
        # Menginput file
        imagetest_dir = filedialog.askopenfilename(filetypes=[('JPG File', '*.jpg')])
        img_display = ImageTk.PhotoImage(Image.open(imagetest_dir).resize((300,300)))
        imagetest_namefile = os.path.basename(imagetest_dir)
        print(imagetest_dir)
        # Config File
        maincanvas.itemconfig(img_test, image=img_display)
        maincanvas.itemconfig(testfile_text, text=imagetest_namefile)
        
    except AttributeError:
        pass

def runresult(event):
    maincanvas.itemconfig(result_button, image=button_run_c)
    # sleep(0.01)
    # maincanvas.itemconfig(result_button, image=button_run)

    # algo(filename_dir, dataset_dir)
    elapsed_time = time.time()
    exec_time = (str) (elapsed_time)
    maincanvas.itemconfig(elapsed, text=exec_time)
    maincanvas.itemconfig(result_button, image=button_run)

# DECORATION
def onhover_choosefile(event):
    maincanvas.itemconfig(testfile_button, image=button_choose)
def nonhover_choosefile(event):
    maincanvas.itemconfig(testfile_button, image=button_choose_h)
def onclick_choosefile(event):
    maincanvas.itemconfig(testfile_button, image=button_choose_c)
    askopenfile()
def onhover_choosedataset(event):
    maincanvas.itemconfig(dataset_button, image=button_choose)
def nonhover_choosedataset(event):
    maincanvas.itemconfig(dataset_button, image=button_choose_h)
def onclick_choosedataset(event):
    maincanvas.itemconfig(dataset_button, image=button_choose_c)
    askopendataset()


# MAIN
maincanvas = Canvas(root, width=400, height=400)
maincanvas.pack(fill="both", expand=True)
maincanvas.create_image( 0, 0, image = bg, anchor = "nw")
# TITLE
maincanvas.create_image((WIDTH/2)-270, 10, image = title_asset, anchor = "nw")
maincanvas.create_text(WIDTH/2, 80, anchor = W, text="In.Your.Face", font=(varfont, 28))
maincanvas.create_text(WIDTH/2, 130, anchor = W, text="Recognition", font=(varfont, 28))

# INPUT
# ==== INISIALISASI =====
# Insert Dataset
maincanvas.create_text(107, 228, anchor = W, text="Insert Your Dataset", font=(varfont, 22))
dataset_button = maincanvas.create_image(100, 260, image = button_choose_h, anchor = "nw")
dataset_text = maincanvas.create_text(103, 332, anchor = W, text=dataset_dir, font=(varfont, 15), fill='gray')

# Insert Image
maincanvas.create_text(107, 381, anchor = W, text="Insert Your Image", font=(varfont, 22))
testfile_button = maincanvas.create_image(100, 419, image = button_choose_h, anchor = "nw")
testfile_text = maincanvas.create_text(103, 490, anchor = W, text=imagetest_filename, font=(varfont, 15), fill='gray')

# Run Result
result_button = maincanvas.create_image(100, 552, image = button_run, anchor = "nw")

# Hasil Result
maincanvas.create_text(107, 630, anchor = W, text="Result: ", font=(varfont, 18))
result_namefile = maincanvas.create_text(170, 630, anchor = W, text=imagetest_result, font=(varfont, 18))

# ==== EVENTS ===== #
maincanvas.tag_bind(testfile_button, '<Enter>', onhover_choosefile)
maincanvas.tag_bind(testfile_button, '<Leave>', nonhover_choosefile)
maincanvas.tag_bind(testfile_button, '<ButtonPress>', onclick_choosefile)

maincanvas.tag_bind(dataset_button, '<Enter>', onhover_choosedataset)
maincanvas.tag_bind(dataset_button, '<Leave>', nonhover_choosedataset)
maincanvas.tag_bind(dataset_button, '<ButtonPress>', onclick_choosedataset)

maincanvas.tag_bind(result_button, '<ButtonPress>', runresult)


# DISPLAY
imagetest_dir = img_none
maincanvas.create_text(610, 223, anchor = W, text="Test Result", font=(varfont, 20))
img_test = maincanvas.create_image(513, 250, image = imagetest_dir, anchor = "nw")

maincanvas.create_text(513, 615, anchor = W, text="Execution Time:", font=(varfont, 22))
elapsed = maincanvas.create_text(680, 615, anchor = W, text=exec_time, font=(varfont, 22), fill="gray")

# RESULT
maincanvas.create_text(930, 223, anchor = W, text="Closest Result", font=(varfont, 20))
maincanvas.create_image(850, 250, image = img_none, anchor = "nw")

# Olah tuple lu..


root.mainloop()  