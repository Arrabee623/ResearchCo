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