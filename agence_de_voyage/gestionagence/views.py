from django.shortcuts import render, redirect

from .models import Gestionagence
from .form import GestionagenceCreate
from django.http import HttpResponse 


def index(request):
      shelf = Gestionagence.objects.all()
      return render(request, 'library.html', {'shelf': shelf})
def upload(request):
    upload = GestionagenceCreate()
    if request.method == 'POST':
        upload = GestionagenceCreate(request.POST, request.FILES)
        if upload.is_valid():
            upload.save() 
            return redirect('index')
        else:
            return HttpResponse(""" Something went wrong. Please reload the webpage by clicking <a href="{{url:'index'}}">Reload</a> """)
    else:
        return render (request, 'upload_form.html', {'upload_form': upload})
def update(request, gestionagence_id):
    gestionagence_id = int(gestionagence_id)
    try:
        crud_shelf = Gestionagence.objects.get(id = gestionagence_id)
    except Gestionagence.DoesNotExist:
        return redirect('index')
    crud_form = GestionagenceCreate(request.POST or None, instance = crud_shelf)
    if crud_form.is_valid():
        crud_form.save()
        return redirect('index')  
    return render(request, 'upload_form.html', {'upload_form': crud_form})  
 
def delete(request, gestionagence_id):
    gestionagence_id = int(gestionagence_id)
    try:
        gestionagence_shelf = Gestionagence.objects.get(id = gestionagence_id)
    except Gestionagence.DoesNotExist:
        return redirect('index')
    gestionagence_shelf.delete()
    return redirect('index')         