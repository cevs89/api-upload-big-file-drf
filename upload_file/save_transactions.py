from sqlalchemy.orm import sessionmaker
from db_setup import engine
from models_clients_transaction import ClienteTransactions
from datetime import datetime
import pandas


class SaveClientTransactions:
    """
    Estos procesos debria ser manejados en Celery, aplicando las validaciones necesarias
    de la data y aplicando procesos Bulk para guarda la data por lotes.
    """
    def save(self, data):
        try:
            Session = sessionmaker(bind=engine)
            session = Session()
        except Exception as e:
            raise ValueError("Fail connection DB external: " + str(e))

        try:
            for i in range(len(data)):
                me = ClienteTransactions()
                me.transaction_id = data[i]['transaction_id']
                me.transaction_date = datetime.strptime(data[i]['transaction_date'], '%Y-%m-%d')
                me.transaction_amount = data[i]['transaction_amount']
                me.client_id = data[i]['client_id']
                me.client_name = data[i]['client_name']
                session.add(me)
                session.commit()
        except Exception as e:
            raise ValueError("Something went wrong when trying to save the data in the external DB. {}".format(e))

        return True

    def process_item(self, data):
        df = pandas.read_csv(
            data.file_upload.file, encoding='utf-8', sep=data.separator, header=0)

        dict_data = {}
        lista_data = []
        dict_pandas = df.to_dict()
        for i in range(len(df)):
            for key, val in dict_pandas.items():
                dict_data[key] = dict_pandas[key][i]
            lista_data.append(dict_data)
            dict_data = {}

        self.save(lista_data)
        return lista_data
