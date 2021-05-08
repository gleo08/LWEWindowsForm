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

def genKeyA():
    entry4.delete('1.0', END)
    q = int (entry1.get())
    amount = int (entry2.get())
    A = random.sample(range(q), amount)
    entry4.insert(END, str (A))

def genKeyB():
    q = int(entry1.get())
    s = int (entry3.get())
    e = []
    B = []
    entry5.delete("1.0", END)
    A = ast.literal_eval(entry4.get("1.0", END))
    for x in range (0, len(A)):
        e.append(random.randint(1, 3))
    for x in range(0, len(A)):
        B.append((A[x] * s + e[x]) % q)
    entry5.insert(END, str (B))

def getUV(A, B, amount, q, m):
    sample = random.sample(range(amount - 1), amount // 4)
    UV = []
    u = 0
    v = 0
    for x in range(len(sample)):
        u = u + (A[sample[x]])
        v = v + (B[sample[x]])
    v = v + math.floor(q // 2) * m
    v = v % q
    u = u % q
    UV.append(u)
    UV.append(v)
    return UV

def fileOpen():
    entry6.delete("1.0", END)
    fileName = filedialog.askopenfilename(
        initialdir="/home/adam/cypherApp", title="Select File")
    f = open(fileName, "r")
    m = f.read()
    encoded = []
    for character in m:
        encoded.append(base64.b64encode(bytes(character, "utf-8")))
    binary = []
    for i in range(len(encoded)):
        binary.append(binascii.a2b_base64(encoded[i]))
    intMessage = []
    for i in range(len(encoded)):
        intMessage.append(int.from_bytes(binary[i], byteorder='little'))
    bitsCypher = toBits(intMessage)
    entry6.insert(END, str (bitsCypher))

def toBits(input=[]):
    result = []
    for i in range(0, len(input)):
        l = [0]*(8)
        l[0] = input[i] & 0x1
        l[1] = (input[i] & 0x2) >> 1
        l[2] = (input[i] & 0x4) >> 2
        l[3] = (input[i] & 0x8) >> 3
        l[4] = (input[i] & 0x16) >> 4
        l[5] = (input[i] & 0x32) >> 5
        l[6] = (input[i] & 0x64) >> 6
        l[7] = (input[i] & 0x128) >> 7
        result.append(l)
    return result

def encrypt():
    A = ast.literal_eval(entry4.get("1.0", END))
    B = ast.literal_eval(entry5.get("1.0", END))
    q = int(entry1.get())
    amount = int(entry2.get())
    message = ast.literal_eval(entry6.get("1.0", END))
    cypher = []
    for element in message:
        result = []
        for x in element:
            UV = getUV(A, B, amount, q, x)
            result.append(UV)
        cypher.append(result)
    f = open("output.txt", "w")
    f.write(str (cypher))
    f.close()
    tkMessageBox.showinfo("Encrypt Process", message="Success!!!")

root = tk.Tk()
root.geometry("500x800")

L1 = Label(root, text = "Input prime q")
L1.grid(row = 0)
entry1 = Entry(root, width = 30)
entry1.grid(row = 0, column = 1, padx = 10, pady = 10)

L2 = Label(root, text = "Input amount")
L2.grid(row = 1)
entry2 = Entry(root, width = 30)
entry2.grid(row = 1, column = 1, padx = 10, pady = 10)

L3 = Label(root, text = "Input secret key")
L3.grid(row = 3)
entry3 = Entry(root, width = 30)
entry3.grid(row = 3, column = 1, padx=10, pady=10)

entry4 = Text(root, width = 30, height = 5)
entry4.grid(row=4, column=1, padx = 10, pady = 10)
keyGenA = Button(root, text = "Gen public key A", padx = 10, pady = 10, command = genKeyA)
keyGenA.grid(row = 4, padx = 10, pady = 10)

entry5 = Text(root, width=30, height=5)
entry5.grid(row=5, column=1, padx=10, pady=10)
keyGenB = Button(root, text="Gen public key B", padx=10, pady=10, command=genKeyB)
keyGenB.grid(row=5, padx=10, pady=10)

L4 = Label(root, text = "Choose input file to encrypt")
L4.grid(row = 6)
openFile = tk.Button(root, text = "Choose File", command = fileOpen)
openFile.grid(row = 6, column = 1, padx = 10, pady = 10)

L5 = Label(root, text="Bits Cypher")
L5.grid(row = 7)
entry6 = Text(root, width = 30, height = 5)
entry6.grid(row = 7, column=1, padx=10, pady=10)

entry7 = Button(root, text = "Encrypt", width = 20, height = 2, command = encrypt)
entry7.grid(row = 8, column = 0, padx=10, pady=10)

root.mainloop()

