# tkinter
from tkinter import *
from tkinter import ttk, Text

# 自作の会社情報クラス
from Company import Company

# tkinterによるウィンドウの作成
root = Tk()
root.title('企業研究')
root.geometry('800x600')

# ウィジェットの作成
frame = ttk.Frame(root, padding=10, relief="solid")
frame.grid()
frame1 = ttk.Frame(frame, padding=10, relief='solid')
frame1.grid(row=0, column=0, sticky='NW')
frame2 = ttk.Frame(frame, padding=10, width=200, relief='solid')
frame2.grid(row=0, column=1, sticky='NE')
frame3 = ttk.Frame(frame, padding=10, relief='solid')
frame3.grid(row=1, column=0, columnspan=2, sticky='W')
frame4 = ttk.Frame(frame, padding=10, relief='solid')
frame4.grid(row=2, column=0, columnspan=2)

# 会社名
labelName = ttk.Label(
    frame1,
    text='会社名')
labelName.grid(row=0, column=0, sticky='E')
companyName = StringVar()
entryName = ttk.Entry(
    frame1,
    textvariable=companyName)
entryName.grid(row=0, column=1, pady=5)

# 会社形態
labelForm = ttk.Label(
    frame1,
    text='会社形態')
labelForm.grid(row=1, column=0, pady=(5, 0), sticky='E')
companyForm = StringVar()
entryForm = ttk.Entry(
    frame1,
    textvariable=companyForm)
entryForm.grid(row=1, column=1, pady=(5, 0))
labelFormTip = ttk.Label(
    frame1,
    text='(株式会社/その他形態)')
labelFormTip.grid(row=2, column=0, columnspan=2, sticky='W', pady=(0, 5))

# 業種
labelType = ttk.Label(
    frame1,
    text='業種')
labelType.grid(row=3, column=0, sticky='E')
companyType = StringVar()
entryType = ttk.Entry(
    frame1,
    textvariable=companyType)
entryType.grid(row=3, column=1, pady=5)

# 大業種
labelGroup = ttk.Label(
    frame1,
    text='大業種')
labelGroup.grid(row=4, column=0, sticky='E')
companyGroup = StringVar()
entryGroup = ttk.Entry(
    frame1,
    textvariable=companyGroup)
entryGroup.grid(row=4, column=1, pady=5)

# 上場企業かどうか
labelListing = ttk.Label(
    frame1,
    text='上場企業')
labelListing.grid(row=5, column=0, pady=(5, 0), sticky='E')
companyListing = StringVar()
entryListing = ttk.Entry(
    frame1,
    textvariable=companyGroup)
entryListing.grid(row=5, column=1, pady=(5, 0))
labelListingTip = ttk.Label(
    frame1,
    text='(上場市場もしくは未上場,持株会社傘下など)')
labelListingTip.grid(row=6, column=0, columnspan=2, sticky='W', pady=(0, 5))

# 本社の場所
labelHead_office = ttk.Label(
    frame1,
    text='本社の場所')
labelHead_office.grid(row=7, column=0, sticky='E')
companyHead_office = StringVar()
entryHead_office = ttk.Entry(
    frame1,
    textvariable=companyHead_office)
entryHead_office.grid(row=7, column=1, pady=5)

# 売上高
labelSales = ttk.Label(
    frame2,
    text='売上高')
labelSales.grid(row=1, column=0, sticky='E')
companySales = StringVar()
entrySales = ttk.Entry(
    frame2,
    textvariable=companySales)
entrySales.grid(row=1, column=1, pady=5, padx=10)

# 営業利益
labelIncome = ttk.Label(
    frame2,
    text='営業利益')
labelIncome.grid(row=2, column=0, sticky='E')
companyIncome = StringVar()
entryIncome = ttk.Entry(
    frame2,
    textvariable=companyIncome)
entryIncome.grid(row=2, column=1, pady=5, padx=10)

# 採用数
labelRecruits = ttk.Label(
    frame2,
    text='採用数')
labelRecruits.grid(row=3, column=0, sticky='E')
companyRecruits = StringVar()
entryRecruits = ttk.Entry(
    frame2,
    textvariable=companyRecruits)
entryRecruits.grid(row=3, column=1, pady=5, padx=10)

# 従業員数
labelEmployees = ttk.Label(
    frame2,
    text='従業員数')
labelEmployees.grid(row=4, column=0, sticky='E')
companyEmployees = StringVar()
entryEmployees = ttk.Entry(
    frame2,
    textvariable=companyEmployees)
entryEmployees.grid(row=4, column=1, pady=5, padx=10)

# 設立年
labelEstablish = ttk.Label(
    frame2,
    text='設立年')
labelEstablish.grid(row=5, column=0, sticky='E')
companyEstablish = StringVar()
entryEstablish = ttk.Entry(
    frame2,
    textvariable=companyEstablish)
entryEstablish.grid(row=5, column=1, pady=5, padx=10)

# 平均年収
labelSalary = ttk.Label(
    frame2,
    text='平均年収')
labelSalary.grid(row=6, column=0, sticky='E')
companySalary = StringVar()
entrySalary = ttk.Entry(
    frame2,
    textvariable=companySalary)
entrySalary.grid(row=6, column=1, pady=5, padx=10)

# 何をしている会社か
labelWhat = ttk.Label(
    frame3,
    text='何をしている会社か')
labelWhat.grid(row=0, column=0, sticky='W')
companyWhat = StringVar()
entryWhat = Text(
    frame3,
    bg="#ffffff",
    relief='solid',
    height=15,
    width=65)
entryWhat.grid(row=1, column=0, pady=5)

# 出力ボタン
button_export = ttk.Button(
    frame4,
    text='Export',
    command=lambda: print("Button is pushed."))
button_export.grid(row=0, column=0, pady=5)

# アプリケーションの実行
root.mainloop()