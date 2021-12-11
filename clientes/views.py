from rest_framework import viewsets
from .models import *
from .serializer import *


# Create your views here.
class ClientesViewSet(viewsets.ModelViewSet):
    queryset = Clientes.objects.all()
    serializer_class = ClientesSerializers
