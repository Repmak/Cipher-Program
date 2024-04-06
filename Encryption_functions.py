from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from itertools import *


def vernam(msg_entry, key_entry_vernam, encrypted_text, root):
    inp = msg_entry.get()
    inpkey = key_entry_vernam.get()
    output = ""
    # CHECKS IF LENGTH OF KEY IS LONGER THAN LENGTH OF TEXT TO ENCRYPT/DECRYPT
    if len(inpkey) < len(inp):
        encrypted_text.config(text="Error: len(key) < len(text)")
    # CHECKS IF ENTRY BOX IS EMPTY
    elif inp == "":
        encrypted_text.config(text="Error: no text entered")
    # ENCRYPTION/DECRYPTION (THERE IS NO NEED FOR 2 SEPARATE PARTS OF CODE FOR ENCRYPTION AND DECRYPTION BECAUSE AN XOR OPERATION WILL RETURN THE ENCRYPTED TEXT BACK TO ITS ORIGINAL INPUT)
    else:
        for i in range(len(inp)):
            xorresult = ord(inp[i]) ^ ord(inpkey[i])
            output = output + str(chr(xorresult))
        encrypted_text.config(text=output)
        graph(output, root)


# CAESAR
def caesar(msg_entry, caesaroption, swapcounter, encrypted_text, root):
    inp = msg_entry.get()
    inp_spaces = caesaroption.get()
    a = int(inp_spaces)
    array = []
    # CHECKS IF ENTRY BOX IS EMPTY
    if inp == "":
        encrypted_text.config(text="Error: no text entered")
        output = ""
    else:
        # ENCRYPTION
        if swapcounter % 2 == 0:
            for i in range(0, len(inp)):
                array.append(chr(ord(inp[i]) + a))
            output = ("".join(array))
        # DECRYPTION
        else:
            for i in range(0, len(inp)):
                array.append(chr(ord(inp[i]) - a))
            output = ("".join(array))
        encrypted_text.config(text=output)
    graph(output, root)


# VIGENERE
def vigenere(msg_entry, key_entry_vigenere, swapcounter, encrypted_text, root):
    inp = msg_entry.get()
    inpkey = key_entry_vigenere.get()
    output = ""
    # CHECKS IF KEY ENTRY BOX IS EMPTY
    if inpkey == "":
        encrypted_text.config(text="Error: no key entered")
    # CHECKS IF ENTRY BOX IS EMPTY
    elif inp == "":
        encrypted_text.config(text="Error: no text entered")
    else:
        for i in range(len(inp)):
            letter_n = ord(inp[i])
            key_n = ord(inpkey[i % len(inpkey)])
            # ENCRYPTION
            if swapcounter % 2 == 0:
                value = (letter_n + key_n) % 1114112
            # DECRYPTION
            else:
                value = (letter_n - key_n) % 1114112
            output = output + chr(value)
        encrypted_text.config(text=output)
    graph(output, root)


# FREQUENCY GRAPH
def graph(output, root):
    sortedword = sorted(list(output))
    ycoord = [len(list(group)) for key, group in groupby(sortedword)]
    xcoord = list(dict.fromkeys(sortedword))
    fig = Figure(figsize=(4, 2.1), dpi=100)
    fqgraph = fig.add_subplot(111, title="Frequency Analysis Graph")
    fqgraph.bar(xcoord, ycoord, color="#7393B3")
    canvas = FigureCanvasTkAgg(fig, master=root)
    canvas.draw()
    canvas.get_tk_widget().place(relx=0.545, rely=0.525)


# SWAPPING TO ENCRYPTION/DECRYPTION
def swap(swapcounter, text1, swapbutton, option, img1e, img1d, imgsd, imgse, img2e, img2d):
    remainder = swapcounter % 2
    if remainder == 0:
        text1.config(image=img1e, borderwidth=0)
        swapbutton.config(image=imgsd, borderwidth=0)
        option.config(image=img2e, borderwidth=0)
    if remainder == 1:
        text1.config(image=img1d, borderwidth=0)
        swapbutton.config(image=imgse, borderwidth=0)
        option.config(image=img2d, borderwidth=0)
