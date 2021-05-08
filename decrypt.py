import tkinter as tk
from tkinter import filedialog, Text
from tkinter import *
from tkinter import messagebox as tkMessageBox
import ast
import os
import math
import random
import base64
import binascii

def bitsToInterger(array=[]):
    result = []
    for element in array:
        number = 0
        for i in range(0, len(element) - 1):
            if (element[i] == 1):
                number = number + pow(2, i)
        result.append(number)
    return result

def fileOpen():
    q = int(entry1.get())
    s = int(entry3.get())
    result = []
    fileName = filedialog.askopenfilename(
        initialdir="/home/adam/cypherApp", title="Select File")
    f = open(fileName, "r")
    cypher = f.read()
    cypher = ast.literal_eval(cypher)
    for element in cypher:
        C = []
        for x in element:
            tmp = (x[1] - s * x[0]) % q
            if (tmp > q // 2):
                C.append(1)
            else:
                C.append(0)
        result.append(C)
    intResult = bitsToInterger(result)
    entry6.insert (END, str(intResult))

def decrypt():
    message = entry6.get("1.0", END)
    message = ast.literal_eval(message)
    result = ""
    for i in range(len(message)):
        letter = chr(abs(message[i]))
        result = result + letter
    f = open("plaintext.txt", "w")
    f.write("Message: " + result)
    f.close()
    tkMessageBox.showinfo("Decrypt Process", message="Success!!!")

root = tk.Tk()
root.geometry("500x800")
root.title("DECRYPT")

L1 = Label(root, text="Input prime q")
L1.grid(row=0)
entry1 = Entry(root, width=30)
entry1.grid(row=0, column=1, padx=10, pady=10)

L3 = Label(root, text="Input secret key")
L3.grid(row=3)
entry3 = Entry(root, width=30)
entry3.grid(row=3, column=1, padx=10, pady=10)

L4 = Label(root, text="Input public key A")
L4.grid(row=4)
entry4 = Text(root, width=30, height = 5)
entry4.grid(row=4, column=1, padx=10, pady=10)

L5 = Label(root, text="Input public key B")
L5.grid(row=5)
entry5 = Text(root, width=30, height = 5)
entry5.grid(row=5, column=1, padx=10, pady=10)

L6 = Label(root, text="Choose input file to decrypt")
L6.grid(row=6)
openFile = tk.Button(root, text="Choose File", command=fileOpen)
openFile.grid(row=6, column=1, padx=10, pady=10)

L6 = Label(root, text="Bits after decrypting")
L6.grid(row=7)
entry6 = Text(root, width=30, height=5)
entry6.grid(row=7, column=1, padx=10, pady=10)

entry7 = Button(root, text="Decrypt", width=20, height=2, command=decrypt)
entry7.grid(row=8, column=0, padx=10, pady=10)


root.mainloop()
