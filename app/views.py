from django.shortcuts import render
from .forms import UserForm

def home(request):
    data={
        'form': UserForm()
    }

    if request.method == "POST":
        form=UserForm(data=request.POST)
        if form.is_valid():
            form.save()
            data['mensaje']="usuario creado"
        else:
            data['form']=form
            data['mensaje']="usuario no creado"


    return render(request,'app/home.html', data)