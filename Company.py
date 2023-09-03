# 会社クラス
class Company:
    
    # コンストラクタ
    def __init__(self, form, industry_type, industry_group,
                 listing, head_office, sales, income, recruits,
                 employees, establish, salary, what):
        self.form = form    # 会社形態
        self.industry_type = industry_type  # 業種
        self.industry_group = industry_group    # 大業種
        self.listing = listing  # 上場企業かどうか
        self.head_office = head_office  # 本社の位置
        self.sales = sales  # 売上高
        self.income = income    # 営業利益
        self.recruits = recruits    # 採用数
        self.employees = employees  # 従業員
        self.establish = establish  # 設立年
        self.salary = salary    # 平均年収
        self.what = what    # 何をしている会社か(概要)
    
    # 特定のパラメータについて分類を行う
    def classification(self):
        # 売上規模
        if self.income >= 10000:
            self.salesScale = "[LL] 超大企業"
        elif self.income >= 3000:
            self.salesScale = "[L] 大企業"
        elif self.income >= 500:
            self.salesScale = "[M] 中堅企業"
        else:
            self.salesScale = "[S] 中小企業"
        
        # 従業員規模
        if self.employees >= 5000:
            self.employeeScale = "[LL]"
        elif self.employees >= 1000:
            self.employeeScale = "[L]"
        elif self.employees >= 300:
            self.employeeScale = "[M]"
        else:
            self.employeeScale = "[S]"
        
        # 平均年収の区分
        if self.salary >= 800:
            self.salaryScale = "高い"
        elif self.salary > 500:
            self.salaryScale = "平均的"
        else:
            self.salaryScale = "低い"


        