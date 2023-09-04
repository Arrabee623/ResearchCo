import tkinter

# 会社クラス
class Company:
    
    # コンストラクタ
    def __init__(self, name='N/A', form='N/A', industry_type='N/A', industry_group='N/A',
                 listing='N/A', head_office='N/A', sales=-1, income=-1, deltaIncome='N/A', recruits=-1,
                 employees=-1, establish=-1, salary=-1, what=tkinter.Text()):
        self.name = name    # 会社名
        self.form = form    # 会社形態
        self.industry_type = industry_type  # 業種
        self.industry_group = industry_group    # 大業種
        self.listing = listing  # 上場企業かどうか
        self.head_office = head_office  # 本社の位置
        self.sales = int(sales)  # 売上高
        self.income = int(income)    # 営業利益
        self.deltaIncome = deltaIncome  # 営業利益の前年比増減
        self.recruits = int(recruits)    # 採用数
        self.employees = int(employees)  # 従業員
        self.establish = int(establish)  # 設立年
        self.salary = int(salary)    # 平均年収
        self.what = what.get("1.0", "end")    # 何をしている会社か(概要)
    
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
        
        # 採用規模
        if self.recruits >= 100:
            self.recruitScale = "多い"
        elif self.recruits >= 30:
            self.recruitScale = "中程度"
        else:
            self.recruitScale = "少ない"    
                
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
        
    # ファイル出力を行う
    def exportHTML(self):
        # ファイルオープン
        filename = self.name + '.html'
        f = open(filename, 'w')
        
        # 出力文字列作成
        htmlstr = f'''
            <!DOCTYPE html>
            <html lang="ja">
                <head>
                    <meta charset="UTF-8">
                    <title>{self.name}</title>
                </head>
                <body>
                    <h1>{self.name}</h1>
                    <hr>
                    <table class="info" border="0">
                        <tr><th>会社形態</th><td>{self.form}</td></tr>
                        <tr><th>業種</th><td>{self.industry_type}</td></tr>
                        <tr><th>大業種</th><td>{self.industry_group}</td></tr>
                        <tr><th>上場企業</th><td>{self.listing}</td></tr>
                        <tr><th>本社の場所</th><td>{self.head_office}</td></tr>
                        <tr><th>売上高</th><td>{str(self.sales)}億円 ({self.salesScale})</td></tr>
                        <tr><th>営業利益</th><td>{str(self.income)}億円 ({self.deltaIncome})</td></tr>
                        <tr><th>採用数</th><td>{str(self.recruits)}人 ({self.recruitScale})</td></tr>
                        <tr><th>従業員</th><td>{str(self.employees)}人 ({self.employeeScale})</td></tr>
                        <tr><th>設立年</th><td>{str(self.establish)}年</td></tr>
                        <tr><th>平均年収</th><td>{str(self.salary)}万円 ({self.salaryScale})</td></tr>
                    </table>
                    <hr>
                    <h3>何をしているか</h3>
                    <div class="what">
                        {self.what}
                    </div>
                </body>
            </html>
        '''
        
        # ファイル出力
        f.write(htmlstr)
        
        # ファイルのクローズ
        f.close()


        