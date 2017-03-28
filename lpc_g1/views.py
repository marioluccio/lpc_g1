from django.http import HttpResponse
from .models import Evento

def listaEventos(objects):
    list_eventos = Evento.objects.all()
    retorno = ""
    for evento in lista_eventos:
        retorno += "<li>"+evento.nomeEvento + "</li>"
    return HttpResponse(retorno)
