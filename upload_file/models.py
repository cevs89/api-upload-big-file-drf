from django.db import models
from django.contrib.auth.models import User
import uuid
import os

"""
Aplique un campo Filed() para guarda el archivo en el proyecto, este archivo
solo se guarda en la carpeta media/ el cual esta ignorada en GIT,

Los archivos también podrían guardarse en un bucket de S3 (Amazon) o en
Storage (GCP)

Guardar un archivo se tiene mas control del mismo, sin contar el nombre del archivo
puede ser un nombre con espacios, caracteres especiales y mas, siempre es recomendable
cambiar dicho nombre por un estándar, yo le asigno un dato uuid.

Decidi guardar el separador del archivo .CSV ya que en mi experiencia eh encontrado
archivos .csv separados con: (,), (;), (|).

Esto se debe a que muchas veces las empresas trabajan con sistemas administrativos
como SAP, SAINT u otros del mercado y este sistema exporta los archivos .CSV
con un deparador ya definido.
"""


def upload_file_storage(instance, filename):
    ext = filename.split('.')[-1]
    filename = "%s.%s" % (uuid.uuid4(), ext)
    return os.path.join('files_uploads/', filename)


class FileUploadCSV(models.Model):
    file_upload = models.FileField(upload_to=upload_file_storage)
    user_upload = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="file_upload_user"
    )
    separator = models.CharField(max_length=1, default=",")
    pub_date = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name_plural = "Upload File"

    def __str__(self):
        return str(self.id) + " | " + str(self.user_upload.username)
