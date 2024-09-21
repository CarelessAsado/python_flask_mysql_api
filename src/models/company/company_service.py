from src.models.company.company_model import Company
from src.db.connect import db

# TODO: add return types

class CompanyService:
    @staticmethod
    def createCompany(company=Company, currentSession=db.session):
            currentSession.add(company)

    @staticmethod
    def getSingleCompanyOrFail(companyId):
        return  db.get_or_404(Company, companyId)
