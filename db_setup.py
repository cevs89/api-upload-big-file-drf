from sqlalchemy import create_engine

from models_clients_transaction import Base

engine = create_engine("sqlite:///transaction_external.sqlite3")

if __name__ == "__main__":
    Base.metadata.create_all(engine)
