import os
from django.utils.datastructures import MultiValueDictKeyError
import pandas


def ValidateHeaderMissing(expectedHeaders, headers):
    missing_headers = [col for col in expectedHeaders if col.upper() not in (col.upper() for col in headers)]
    if len(missing_headers) > 0:
        return missing_headers
    else:
        return True


def ValidateHeaderGarbage(expectedHeaders, headers):
    garbage_headers = [col for col in headers if col.upper() not in (col.upper() for col in expectedHeaders)]
    if len(garbage_headers) > 0:
        return garbage_headers
    else:
        return True


class ValidateUploadFile:
    """
        {
        "file_upload": "file",
        "separator": ""
        }
        El separador lo define el usuario al enviar el archivo, el valida el separador
        de su archivo lo incluye y sube el archivo, y todos los procesos se hacen con
        esa variable, incluso se podria definir separadores permitidos en la DB
    """
    def file(self, data):
        if 'separator' in data and 'file_upload' in data:
            get_file = data['file_upload']
            get_separator = data['separator']

            try:
                get_file
            except MultiValueDictKeyError:
                raise ValueError("There is an error in the file")

            extencion = os.path.splitext(str(get_file))[1][1:].lower()
            if not extencion == 'csv':
                raise ValueError("the file must be .csv")

            if len(get_separator) > 1:
                raise ValueError("the separator should be only 1 character")

            quotechar = "\""
            df = pandas.read_csv(
                get_file.file, encoding='utf-8', quotechar=quotechar, header=0,
                sep=get_separator)
            headers = list(df)

            """
            La data del Header puede y debe ser dinamica, definiendo formatos y tipos de datos
            en la DB, asi pueden ser administrados en cualquier momento.
            """
            header_valid = [
                "transaction_id", "transaction_date", "transaction_amount",
                "client_id", "client_name"]

            header_missing = ValidateHeaderMissing(header_valid, headers)
            header_garbage = ValidateHeaderGarbage(header_valid, headers)

            if header_missing is True and header_garbage is True:
                return str(df.to_csv(header=True, index=False, sep=get_separator))
            else:
                # header_missing lista de encabezado que falta
                # header_garbage lista de encabezado que no es requerido
                raise ValueError("Invalid header. Only allowed: {}".format(
                    ",".join(header_valid)))

        else:
            raise ValueError("file_upload and separator are required")
