########################
#Tkinterによる簡単なGUI#
########################

import tkinter as tk   #import [オブジェクト名] as [オブジェクトの別名] 

root = tk.Tk()
root.title("python_tkinter")
root.geometry('500x150+100+300')   #メイン画面（size=500×150）を、デスクトップ上の100行×300列の場所に表示

label = tk.Label(root, text="↓押してね＾＾↓")
label.pack()

button = tk.Button()
button["text"] = "クリックすると１００万円がもらえる代わりに地球が爆発します"
button["command"] = lambda: print("bung！")
button.pack()

root.mainloop()
