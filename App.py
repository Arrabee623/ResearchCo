# tkinter
from tkinter import *
from tkinter import ttk

# 自作の会社情報クラス
from Company import Company

# tkinterによるウィンドウの作成
root = Tk()
root.title('企業研究')
root.geometry('800x600')

# ウィジェットの作成
frame1 = ttk.Frame(root, padding=10, relief="solid")
frame1.grid()

# 会社名
frameName = ttk.Frame(frame1, padding=10, relief="solid")
labelName = ttk.Label(
    frame1, 
    text='会社名')
labelName.grid(row=0, column=0)
companyName = StringVar()
entryName = ttk.Entry(
    frame1,
    textvariable=companyName)
entryName.grid(row=0, column=1)

# 会社形態
labelForm = ttk.Label(
    frame1,
    text='会社形態')
labelForm.grid(row=1, column=0)
companyForm = StringVar()
entryForm = ttk.Entry(
    frame1,
    textvariable=companyForm)
entryForm.grid(row=1, column=1)
labelFormTip = ttk.Label(
    frame1,
    text='(株式会社/その他形態)')
labelFormTip.grid(row=2, column=0, columnspan=2, sticky='W')

# 業種
labelType = ttk.Label(
    frame1,
    text='業種')
labelType.grid(row=3, column=0)
companyType = StringVar()
entryType = ttk.Entry(
    frame1,
    textvariable=companyType)
entryType.grid(row=3, column=1)

# 大業種
labelGroup = ttk.Label(
    frame1,
    text='大業種')
labelGroup.grid(row=4, column=0)
companyGroup = StringVar()
entryGroup = ttk.Entry(
    frame1,
    textvariable=companyGroup)
entryGroup.grid(row=4, column=1)

# 上場企業かどうか
labelListing = ttk.Label(
    frame1,
    text='上場企業')
labelListing.grid(row=5, column=0)
companyListing = StringVar()
entryListing = ttk.Entry(
    frame1,
    textvariable=companyGroup)
entryListing.grid(row=5, column=1)
labelListingTip = ttk.Label(
    frame1,
    text='(上場市場もしくは未上場,持株会社傘下など)')
labelListingTip.grid(row=6, column=0, columnspan=2, sticky='W')

# 本社の場所
labelHead_office = ttk.Label(
    frame1,
    text='本社の場所')
labelHead_office.grid(row=0, column=2)
companyHead_office = StringVar()
entryHead_office = ttk.Entry(
    frame1,
    textvariable=companyHead_office)
entryHead_office.grid(row=0, column=3)

# 売上高
labelSales = ttk.Label(
    frame1,
    text='売上高')
labelSales.grid(row=1, column=2)
companySales = StringVar()
entrySales = ttk.Entry(
    frame1,
    textvariable=companySales)
entrySales.grid(row=1, column=3)

# 営業利益
labelIncome = ttk.Label(
    frame1,
    text='営業利益')
labelIncome.grid(row=2, column=2)
companyIncome = StringVar()
entryIncome = ttk.Entry(
    frame1,
    textvariable=companyIncome)
entryIncome.grid(row=2, column=3)

# 採用数
labelRecruits = ttk.Label(
    frame1,
    text='採用数')
labelRecruits.grid(row=3, column=2)
companyRecruits = StringVar()
entryRecruits = ttk.Entry(
    frame1,
    textvariable=companyRecruits)
entryRecruits.grid(row=3, column=3)

# 従業員数
labelEmployees = ttk.Label(
    frame1,
    text='従業員数')
labelEmployees.grid(row=4, column=2)
companyEmployees = StringVar()
entryEmployees = ttk.Entry(
    frame1,
    textvariable=companyEmployees)
entryEmployees.grid(row=4, column=3)

# 設立年
labelEstablish = ttk.Label(
    frame1,
    text='設立年')
labelEstablish.grid(row=5, column=2)
companyEstablish = StringVar()
entryEstablish = ttk.Entry(
    frame1,
    textvariable=companyEstablish)
entryEstablish.grid(row=5, column=3)

# 平均年収
labelSalary = ttk.Label(
    frame1,
    text='平均年収')
labelSalary.grid(row=6, column=2)
companySalary = StringVar()
entrySalary = ttk.Entry(
    frame1,
    textvariable=companySalary)
entrySalary.grid(row=6, column=3)

# 何をしている会社か
labelWhat = ttk.Label(
    frame1,
    text='何をしている会社か')
labelWhat.grid(row=7, column=0)
companyWhat = StringVar()
entryWhat = ttk.Entry(
    frame1,
    textvariable=companyWhat)
entryWhat.grid(row=7, column=1)

# 出力ボタン
button_export = ttk.Button(
    frame1,
    text='Export',
    command=lambda: print("Button is pushed."))
button_export.grid(row=15, column=0)

# アプリケーションの実行
root.mainloop()