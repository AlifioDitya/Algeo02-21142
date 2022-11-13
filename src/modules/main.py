from tkinter import *
from PIL import ImageTk, Image
from tkinter import filedialog

class Window:

    def __init__(self, master):
        # Variabel Global
        # dataset_filename = NULL
        # imagetest_filename = NULL

        def askopenzip():
            return filedialog.askopenfile(mode='r', filetypes=[('Zip File', '*.zip')])
        def askopenfile():
            return filedialog.askopenfile(mode='r', filetypes=[('JPG File', '*.jpg')])

        # Inisialisasi Frame Judul
        frame_title = Frame(master)
        label_title = Label(frame_title, text = "Face Recognition").pack(padx=20, pady=20)
        frame_title.pack()

        # Inisialisasi Frames
        frame_input = Frame(master) # Frame kiri untuk input dataset
        label_input = Label(frame_input, text = "Frame input").pack(padx=20, pady=20)
        frame_input.pack(side = LEFT, expand = True, fill = BOTH)

        frame_display = Frame(master)
        # label_display = Label(frame_display, text = "Frame display").pack(padx=20, pady=20)
        frame_display.pack(side = LEFT, expand = True, fill = BOTH)

        frame_result = Frame(master)
        # label_result = Label(frame_result, text = "Frame result").pack(padx=20, pady=20)
        frame_result.pack(side = LEFT, expand = True, fill = BOTH)

        # Inisialisasi Isi

        # FRAME INPUT
        dataset_placeholder = "No choosen files"
        input_dataset = Button(frame_input, command=askopenzip) # Dataset
        input_dataset.pack()
        dataset_label = Label(frame_input, text=dataset_placeholder).pack(padx=20, pady=20)

        testfile_placeholder = "No choosen files"
        input_testfile = Button(frame_input, command=askopenfile) # Test files
        input_testfile.pack()
        testfile_label = Label(frame_input, text=testfile_placeholder).pack(padx=20, pady=20)

        input_checkres = Label(frame_input, text="Result: ").pack(padx=20, pady=20) # Result yang clickable

        # FRAME DISPLAY
        
        display_label = Label(frame_display, text="Test Image").pack(padx=20, pady=20) # Label Photo

        # Displaying image
        img_display = Image.open("test.png")
        resize_img_display = img_display.resize((300, 300))
        resize_img_display2 = ImageTk.PhotoImage(resize_img_display)
        img_display_label = Label(frame_display, image = resize_img_display2)
        img_display_label.pack()
        img_display_label.photo = resize_img_display2

        time_label = Label(frame_display, text="Execution Time: ").pack(padx=20, pady=20) # Label

        # FRAME RESULT
        result_label = Label(frame_result, text="Closest Result").pack(padx=20, pady=20) # 

        # Displaying image
        img_result = Image.open("test.png")
        resize_img_result = img_result.resize((300, 300))
        resize_img_result2 = ImageTk.PhotoImage(resize_img_result)
        img_result_label = Label(frame_result, image = resize_img_result2)
        img_result_label.pack()
        img_result_label.photo = resize_img_result2

root = Tk()
root.geometry("2000x1000")
window = Window(root)
root.mainloop()
