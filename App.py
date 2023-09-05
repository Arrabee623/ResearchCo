# tkinter
from tkinter import *
from tkinter import ttk, Text

# export関数
from Export import export

# tkinterによるウィンドウの作成
root = Tk()
root.title('企業研究')
root.geometry('620x600')

# ウィジェットの作成
frame = ttk.Frame(root, padding=10)
frame.grid()
frame1 = ttk.Frame(frame, padding=10)
frame1.grid(row=0, column=0, sticky='NW')
frame2 = ttk.Frame(frame, padding=10, width=200)
frame2.grid(row=0, column=1, sticky='NE')
frame3 = ttk.Frame(frame, padding=10)
frame3.grid(row=1, column=0, columnspan=2, sticky='W')
frame4 = ttk.Frame(frame, padding=10)
frame4.grid(row=2, column=0, columnspan=2)
frame5 = ttk.Frame(frame)
frame5.grid(row=3, column=0, columnspan=2)

# 会社名
labelName = ttk.Label(
    frame1,
    text='会社名')
labelName.grid(row=0, column=0, sticky='E')
companyName = StringVar()
entryName = ttk.Entry(
    frame1,
    textvariable=companyName,
    width=30)
entryName.grid(row=0, column=1, pady=5, padx=10)

# 会社形態
labelForm = ttk.Label(
    frame1,
    text='会社形態')
labelForm.grid(row=1, column=0, pady=(5, 0), sticky='E')
companyForm = StringVar()
entryForm = ttk.Entry(
    frame1,
    textvariable=companyForm,
    width=30)
entryForm.grid(row=1, column=1, pady=(5, 0), padx=10)
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
    textvariable=companyType,
    width=30)
entryType.grid(row=3, column=1, pady=5, padx=10)

# 大業種
labelGroup = ttk.Label(
    frame1,
    text='大業種')
labelGroup.grid(row=4, column=0, sticky='E')
companyGroup = StringVar()
entryGroup = ttk.Entry(
    frame1,
    textvariable=companyGroup,
    width=30)
entryGroup.grid(row=4, column=1, pady=5, padx=10)

# 上場企業かどうか
labelListing = ttk.Label(
    frame1,
    text='上場企業')
labelListing.grid(row=5, column=0, pady=(5, 0), sticky='E')
companyListing = StringVar()
entryListing = ttk.Entry(
    frame1,
    textvariable=companyListing,
    width=30)
entryListing.grid(row=5, column=1, pady=(5, 0), padx=10)
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
    textvariable=companyHead_office,
    width=30)
entryHead_office.grid(row=7, column=1, pady=5, padx=10)

# 売上高
labelSales = ttk.Label(
    frame2,
    text='売上高[億円]')
labelSales.grid(row=1, column=0, sticky='E')
companySales = StringVar()
entrySales = ttk.Entry(
    frame2,
    textvariable=companySales,
    width=30)
entrySales.grid(row=1, column=1, pady=5, padx=10)

# 営業利益
labelIncome = ttk.Label(
    frame2,
    text='営業利益[億円]')
labelIncome.grid(row=2, column=0, sticky='E')
companyIncome = StringVar()
entryIncome = ttk.Entry(
    frame2,
    textvariable=companyIncome,
    width=30)
entryIncome.grid(row=2, column=1, pady=(5, 0), padx=10)
deltaIncome = ttk.Frame(frame2)
deltaIncome.grid(row=3, column=0, columnspan=2, pady=(0, 5), sticky='W')
labelDelta = ttk.Label(
    deltaIncome,
    text="前年と比較しておおむね(5%を基準に)")
labelDelta.grid(row=0, column=0, columnspan=3, sticky='W')
delta = StringVar()
rbDelta1 = ttk.Radiobutton(
    deltaIncome,
    text='増えている',
    value='増えている',
    variable=delta)
rbDelta2 = ttk.Radiobutton(
    deltaIncome,
    text='横ばい',
    value='横ばい',
    variable=delta)
rbDelta3 = ttk.Radiobutton(
    deltaIncome,
    text='減っている',
    value='減っている',
    variable=delta)
rbDelta1.grid(row=1, column=0)
rbDelta2.grid(row=1, column=1)
rbDelta3.grid(row=1, column=2)

# 採用数
labelRecruits = ttk.Label(
    frame2,
    text='採用数[人]')
labelRecruits.grid(row=4, column=0, sticky='E')
companyRecruits = StringVar()
entryRecruits = ttk.Entry(
    frame2,
    textvariable=companyRecruits,
    width=30)
entryRecruits.grid(row=4, column=1, pady=5, padx=10)

# 従業員数
labelEmployees = ttk.Label(
    frame2,
    text='従業員数[人]')
labelEmployees.grid(row=5, column=0, sticky='E')
companyEmployees = StringVar()
entryEmployees = ttk.Entry(
    frame2,
    textvariable=companyEmployees,
    width=30)
entryEmployees.grid(row=5, column=1, pady=5, padx=10)

# 設立年
labelEstablish = ttk.Label(
    frame2,
    text='設立年[年]')
labelEstablish.grid(row=6, column=0, sticky='E')
companyEstablish = StringVar()
entryEstablish = ttk.Entry(
    frame2,
    textvariable=companyEstablish,
    width=30)
entryEstablish.grid(row=6, column=1, pady=5, padx=10)

# 平均年収
labelSalary = ttk.Label(
    frame2,
    text='平均年収[万円]')
labelSalary.grid(row=7, column=0, sticky='E')
companySalary = StringVar()
entrySalary = ttk.Entry(
    frame2,
    textvariable=companySalary,
    width=30)
entrySalary.grid(row=7, column=1, pady=5, padx=10)

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
    width=80)
entryWhat.grid(row=1, column=0, pady=5)

# 出力ボタン
button_export = ttk.Button(
    frame4,
    text='Export',
    command=lambda: export(companyName.get(),companyForm.get(),companyType.get(),companyGroup.get(),
    companyListing.get(),companyHead_office.get(),companySales.get(),companyIncome.get(),
    delta.get(),companyRecruits.get(),companyEmployees.get(),companyEstablish.get(),companySalary.get(),
    entryWhat.get('1.0', 'end')))
button_export.grid(row=0, column=0, pady=5)

# アプリケーションの実行
root.mainloop()
    
