from sqlalchemy import Column, String, Integer, Float
from core import db


class BankEntity(db.Model):
    __tablename__ = 'banks'
    id = Column(Integer(), primary_key=True, autoincrement=True)
    bank_name = Column(String())
    interest_rate = Column(Float())
    maximum_loan = Column(Integer())
    minimum_down_payment = Column(Integer())
    loan_term = Column(Integer())

    def __init__(self, bank_name=None, interest_rate=None, maximum_loan=None,
                 minimum_down_payment=None, loan_term=None):
        self.bank_name = bank_name
        self.interest_rate = interest_rate
        self.maximum_loan = maximum_loan
        self.minimum_down_payment = minimum_down_payment
        self.loan_term = loan_term
