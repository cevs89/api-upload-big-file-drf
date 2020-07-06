import os
from django.utils.datastructures import MultiValueDictKeyError


class ValidateUploadFile:
    """
        {
        "file_upload": "file",
        "separator": ""
        }
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
            if not extencion != 'CSV' or extencion != 'csv':
                raise ValueError("the file must be .csv")

            if len(get_separator) > 1:
                raise ValueError("the separator should be only 1 character")

            return True

        else:
            raise ValueError("file_upload and separator are required")
