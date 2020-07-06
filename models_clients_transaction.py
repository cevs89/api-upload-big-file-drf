from sqlalchemy import Column, Integer, String, Float, Date
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class ClienteTransactions(Base):

    __tablename__ = "clients_transactions"

    id = Column(Integer, primary_key=True)
    transaction_id = Column(String, nullable=False)
    transaction_date = Column(Date, nullable=True)
    transaction_amount = Column(Float, nullable=True)
    client_id = Column(Integer, nullable=True)
    client_name = Column(String, nullable=False)

    def __init__(self, transaction_id=None, transaction_date=None, transaction_amount=None, client_id=None, client_name=None):
        self.transaction_id = transaction_id
        self.transaction_date = transaction_date
        self.transaction_amount = transaction_amount
        self.client_id = client_id
        self.client_name = client_name
