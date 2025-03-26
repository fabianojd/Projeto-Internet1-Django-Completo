from tempfile import template
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from django.urls import reverse
from .models import Member
from plans.models import Plan
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator

def members(request):
    # mymembers = Member.objects.all().values()
    # mymembers = Member.objects.all().order_by('firstname', 'lastname')
    # mymembers = Member.objects.all().values()
    mymembers = Member.objects.all()
    template = loader.get_template('all_members.html')
    context = {
        'mymembers': mymembers,
    }
    return HttpResponse(template.render(context, request))

def details(request, id):
    mymember = Member.objects.get(id=id)

    template = loader.get_template('details.html')
    context = {
        'mymember': mymember,
    }
    return HttpResponse(template.render(context, request))

def main(request):
    template = loader.get_template('main.html')
    return HttpResponse(template.render(request))  # request adicionado aqui

def add(request):
    myplans = Plan.objects.all().values()
    template = loader.get_template('add.html')
    context = {
        'myplans': myplans,
    }
    return HttpResponse(template.render(context, request))


from datetime import datetime  # Importar para converter a data


def addrecord(request):
    x = request.POST['first']
    y = request.POST['last']
    z = Plan.objects.get(id=request.POST['plan'])
    phone = request.POST.get('phone', '')
    joined_date = request.POST.get('joined_date', None)

    if joined_date:
        joined_date = datetime.strptime(joined_date, "%Y-%m-%d").date()

    foto = request.FILES.get('foto', None)
    documento = request.FILES.get('documento', None)  # Captura o documento

    member = Member(
        firstname=x,
        lastname=y,
        plan=z,
        phone=phone,
        joined_date=joined_date,
        foto=foto,
        documento=documento
    )
    member.save()

    return HttpResponseRedirect(reverse('members'))


def delete(request, id):
    member = Member.objects.get(id=id)
    member.delete()
    return HttpResponseRedirect(reverse('members'))

def update(request, id):
    mymember = Member.objects.get(id=id)
    myplans = Plan.objects.all().values()
    template = loader.get_template('update.html')
    context = {
        'mymember': mymember,
        'myplans': myplans,
    }
    return HttpResponse(template.render(context, request))


def updaterecord(request, id):
    first = request.POST['first']
    last = request.POST['last']
    plan = Plan.objects.get(id=request.POST['plan'])
    phone = request.POST.get('phone', '')
    joined_date = request.POST.get('joined_date', None)

    if joined_date:
        joined_date = datetime.strptime(joined_date, "%Y-%m-%d").date()

    member = Member.objects.get(id=id)
    member.firstname = first
    member.lastname = last
    member.plan = plan
    member.phone = phone
    member.joined_date = joined_date

    if 'foto' in request.FILES:
        member.foto = request.FILES['foto']

    if 'documento' in request.FILES:
        member.documento = request.FILES['documento']
    member.save()

    return HttpResponseRedirect(reverse('members'))

def home(request):
    return render(request, 'home.html')

@login_required(login_url="/login/")
def members(request):
    mymembers = Member.objects.all()
    template = loader.get_template('all_members.html')
    paginator = Paginator(mymembers, 2)
    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)
    context = {
        'mymembers': mymembers,
        "page_obj": page_obj,
    }
    return HttpResponse(template.render(context, request))