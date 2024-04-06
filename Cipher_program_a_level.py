import tkinter
from tkinter import *
import Encryption_functions


class Cipher_program:
    def __init__(self, root):
        # UI
        root.geometry("1000x700")  # DEFINES WINDOW SIZE
        root.title("Encryption program")  # WINDOW NAME
        root.call("wm", "iconphoto", root._w, tkinter.PhotoImage(file="Cipher program pics/padlock.bmp"))  # ICON
        root.configure(bg='#7393B3')  # BACKGROUND COLOUR

        # NOTE: FUNCTIONS FROM Encryption_functions ARE RUN FROM A SEPARATE FUNCTION IN THE THIS FILE (AS SHOWN BELOW) BECAUSE THE command= FUNCTION WOULD RETURN AN ERROR DUE TO NOT RECOGNISING FUNCTIONS FROM A SEPERATE FILE.

        # CALLING VERNAM ENCRYPTION
        def vernam_call():
            Encryption_functions.vernam(msg_entry, key_entry_vernam, encrypted_text, root)

        # CALLING CAESAR ENCRYPTION
        def caesar_call():
            Encryption_functions.caesar(msg_entry, caesaroption, swapcounter, encrypted_text, root)

        # CALLING VIGENERE ENCRYPTION
        def vigenere_call():
            Encryption_functions.vigenere(msg_entry, key_entry_vigenere, swapcounter, encrypted_text, root)

        # COPY TO CLIPBOARD FUNCTION
        def copytoclipboard():
            text2copy = encrypted_text.cget("text")
            root.clipboard_clear()
            root.clipboard_append(text2copy)

        # INCREMENTS swapcounter AND RUNS swap FUNCTION FROM Encryption_functions
        def swap_call():
            global swapcounter
            swapcounter += 1
            Encryption_functions.swap(swapcounter, text1, swapbutton, option, img1e, img1d, imgsd, imgse, img2e, img2d)

        # TITLE
        titleframe = Frame(root, bg='#7393B3', height="70", width="1000")
        titleframe.place(rely=0.02)
        titleframe.pack_propagate(0)  # PREVENTS FRAME FROM SHRINKING AROUND DIMENSIONS OF CONTENT
        title = Label(titleframe)
        title.config(image=imgt, borderwidth=0)
        title.pack()

        # RIGHT FRAME
        outputframe = Frame(root, bg='#7393B3', highlightbackground="white", highlightthickness=3, height="482",
                            width="490")
        outputframe.pack(side=RIGHT, padx=10)
        outputframe.pack_propagate(0)  # PREVENTS FRAME FROM SHRINKING AROUND DIMENSIONS OF CONTENT

        # BOTTOM FRAME
        swapframe = Frame(root, bg='#7393B3', highlightbackground="white", highlightthickness=3, height="80",
                          width="980")
        swapframe.place(relx=0.01, rely=0.87)
        swapframe.pack_propagate(0)  # PREVENTS FRAME FROM SHRINKING AROUND DIMENSIONS OF CONTENT

        # LEFT FRAME
        homeframe = Frame(root, bg='#7393B3', highlightbackground="white", highlightthickness=3, height="482",
                          width="490")
        homeframe.pack(side=LEFT, padx=10)
        homeframe.pack_propagate(0)  # PREVENTS FRAME FROM SHRINKING AROUND DIMENSIONS OF CONTENT

        # RIGHT FRAME TEXT
        text2 = Label(outputframe)
        encrypted_text = Label(outputframe, text="", width=25, font=("Century Gothic", 20))
        text2.config(image=img3, borderwidth=0)

        # RIGHT FRAME BUTTONS
        copy = Button(outputframe, command=copytoclipboard)  # RUNS copytoclipboard FUNCTION WHEN CLICKED
        copy.config(image=imgcopy, borderwidth=0)

        # RIGHT FRAME PLACEMENT
        text2.pack()
        encrypted_text.pack(pady=10)
        copy.pack(pady=5)

        # BOTTOM FRAME BUTTONS
        swapbutton = Button(swapframe, command=swap_call)  # RUNS swap_call FUNCTION WHEN CLICKED
        watermark = Label(swapframe)
        swapbutton.config(image=imgsd, borderwidth=0)
        watermark.config(image=imgw, borderwidth=0)

        # BOTTOM FRAME PLACEMENT
        swapbutton.pack(pady=10)
        watermark.place(relx=0.805, rely=0.065)

        # LEFT FRAME TEXT
        text1 = Label(homeframe)
        msg_entry = Entry(homeframe, width=25, font=("Century Gothic", 20))
        option = Label(homeframe)
        text1.config(image=img1e, borderwidth=0)
        option.config(image=img2e, borderwidth=0)

        # LEFT FRAME BUTTONS AND ADDITIONAL INPUTS
        option1 = Button(homeframe, command=vernam_call)  # RUNS vernam_call FUNCTION WHEN CLICKED
        option2 = Button(homeframe, command=caesar_call)  # RUNS caeser_call FUNCTION WHEN CLICKED
        option3 = Button(homeframe, command=vigenere_call)  # RUNS vigenere_call FUNCTION WHEN CLICKED
        key_vernam = Label(homeframe)
        key_entry_vernam = Entry(homeframe, width=8, font=("Century Gothic", 14))
        increment = Label(homeframe)
        caesaroption = StringVar(homeframe)  # LINES 109, 110, 111 CONSTITUTE THE DROPDOWN MENU FOR CAESAR INCREMENT
        caesaroption.set(1)
        caesardropdown = OptionMenu(homeframe, caesaroption, 1, 2, 3, 4, 5)
        key_vigenere = Label(homeframe)
        key_entry_vigenere = Entry(homeframe, width=8, font=("Century Gothic", 14))
        option1.config(image=imgb1, borderwidth=0)
        option2.config(image=imgb2, borderwidth=0)
        option3.config(image=imgb3, borderwidth=0)
        key_vernam.config(image=imgkey, borderwidth=0)
        increment.config(image=imgincrement, borderwidth=0)
        key_vigenere.config(image=imgkey, borderwidth=0)

        # LEFT FRAME PLACEMENT
        text1.pack()
        msg_entry.pack(pady=15)
        option.pack(pady=5)
        option1.pack(pady=5)
        option2.pack(pady=5)
        option3.pack(pady=5)
        key_vernam.place(relx=0.775, rely=0.532)
        key_entry_vernam.place(relx=0.777, rely=0.619)
        increment.place(relx=0.775, rely=0.69)
        caesardropdown.place(relx=0.777, rely=0.765)
        key_vigenere.place(relx=0.775, rely=0.85)
        key_entry_vigenere.place(relx=0.777, rely=0.935)


# DISPLAY WINDOW
root = Tk()

# COUNTER FOR SWAPPING FUNCTION
swapcounter = 0

# IMPORTING IMAGES (DONE OUTSIDE OF CLASS TO PREVENT PYTHON'S GARBAGE COLLECTOR FROM DELETING THEM)
imgt = PhotoImage(file="Cipher program pics/title.png")
img1e = PhotoImage(file="Cipher program pics/entermsge.png")
img1d = PhotoImage(file="Cipher program pics/entermsgd.png")
img2e = PhotoImage(file="Cipher program pics/optione.png")
img2d = PhotoImage(file="Cipher program pics/optiond.png")
img3 = PhotoImage(file="Cipher program pics/output.png")
imgb1 = PhotoImage(file="Cipher program pics/vernambt.png")
imgb2 = PhotoImage(file="Cipher program pics/caesarbt.png")
imgb3 = PhotoImage(file="Cipher program pics/vigenerebt.png")
imgkey = PhotoImage(file="Cipher program pics/key.png")
imgincrement = PhotoImage(file="Cipher program pics/increment.png")
imgcopy = PhotoImage(file="Cipher program pics/copy.png")
imgw = PhotoImage(file="Cipher program pics/watermark.png")
imgse = PhotoImage(file="Cipher program pics/swape.png")
imgsd = PhotoImage(file="Cipher program pics/swapd.png")

# RUN Cipher_Program
Cipher_program(root)
root.mainloop()
