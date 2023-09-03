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
frame1 = ttk.Frame(root, padding=10, relief="solid")
frame1.grid()

# 会社名
labelName = ttk.Label(
    frame1, 
    text='会社名')
labelName.grid(row=0, column=0, sticky=E)
companyName = StringVar()
entryName = ttk.Entry(
    frame1,
    textvariable=companyName)
entryName.grid(row=0, column=1)

# 会社形態
labelForm = ttk.Label(
    frame1,
    text='会社形態(株式会社/その他形態)')
labelForm.grid(row=1, column=0)
companyForm = StringVar()
entryForm = ttk.Entry(
    frame1,
    textvariable=companyForm)
entryForm.grid(row=1, column=1)


# アプリケーションの実行
root.mainloop()