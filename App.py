# tkinter
from tkinter import *
from tkinter import ttk

# 自作の会社情報ライブラリ
from Company import Company

# tkinterによるウィンドウの作成
root = Tk()
root.title('企業研究')
root.geometry('800x600')

# ウィジェットの作成
frame = ttk.Frame(root, padding=10)
frame.grid()

# 会社名
labelName = ttk.Label(
    frame, 
    text='会社名')
labelName.grid(row=0, column=0, sticky=E)
companyName = StringVar()
entryName = ttk.Entry(
    frame,
    textvariable=companyName)
entryName.grid(row=0, column=1)

# アプリケーションの実行
root.mainloop()