# 自作の会社情報クラス
from Company import Company

# ボタン押下時の処理
def export(
    companyName,companyForm,companyType,companyGroup,
    companyListing,companyHead_office,companySales,companyIncome,
    delta,companyRecruits,companyEmployees,companyEstablish,companySalary,
    entryWhat):
        # デバッグ
        """
        print(
            companyName,companyForm,companyType,companyGroup,
            companyListing,companyHead_office,companySales,companyIncome,
            delta,companyRecruits,companyEmployees,companyEstablish,companySalary,
            entryWhat)
        """
        # Companyインスタンスの作成
        com = Company(
            name=companyName,
            form=companyForm,
            industry_type=companyType,
            industry_group=companyGroup,
            listing=companyListing,
            head_office=companyHead_office,
            sales=companySales,
            income=companyIncome,
            deltaIncome=delta,
            recruits=companyRecruits,
            employees=companyEmployees,
            establish=companyEstablish,
            salary=companySalary,
            what=entryWhat)
        
        # 分類
        com.classification()
        
        # ファイル出力
        com.exportHTML()