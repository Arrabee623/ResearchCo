from Company import Company

print("◎会社名")
name = input()

print("◎会社形態(株式会社など)")
form = input()

print("◎業種")
ctype = input()

print("◎大業種")
cgroup = input()

print("◎上場企業")
listing = input()

print("◎本社の場所")
head_office = input()

print("◎売上高(億円)")
sales = input()

print("◎営業利益(億円)")
income = input()

print("◎採用数")
recruits = input()

print("◎従業員数")
employees = input()

print("◎設立年")
establish = input()

print("◎平均年収(万円)")
salary = input()

print("◎何をしている会社か")
what = input()

com = Company(name, form, ctype, cgroup, listing,
              head_office, sales, income, recruits, employees,
              establish, salary, what)

com.classification()

# クラス変数の内容を辞書形式で出力
print(vars(com))

