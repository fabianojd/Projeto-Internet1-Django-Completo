from django.http import HttpResponse
from django.template import loader
from .models import Materiais

def materiais(request):
    mymateriais = Materiais.objects.all().values()
    template = loader.get_template('all_materiais.html')
    # context = {'mymateriais = mymateriais',}
    context = {"mymateriais": Materiais.objects.all()}
    return HttpResponse(template.render(context, request))

def details(request, codigo):
    mymaterial = Materiais.objects.get(codigo=codigo)
    template = loader.get_template('details')
    # context = {"mymateriais": Materiais.objects.all()}
    context = {"mymateriais": mymaterial}
    return HttpResponse(template.render(context, request))