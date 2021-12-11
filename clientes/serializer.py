from rest_framework import serializers
from .models import *

class ClientesSerializers(serializers.ModelSerializer):
    class Meta:
        model = Clientes
        fields = ['cedula', 'nombre', 'direccion', 'telefono', 'email']
