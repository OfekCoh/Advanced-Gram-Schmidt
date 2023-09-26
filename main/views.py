from django.shortcuts import render
from django.http import HttpResponse
from .forms import HomeForm 
from .GramSchmdit import main, pretty_base
import json
from django.core.mail import send_mail

# Create your views here.


def home(response):
    if response.method == 'POST':
        form=HomeForm(response.POST)
        if form.is_valid():
            newInner=form.cleaned_data['newInner']
            innerChoice=form.cleaned_data['innerChoice']
            base=form.cleaned_data['base']
            sizeVector=len(base[0])
            try:
                orth_base=main(len(base[0]),len(base),newInner,innerChoice,base)
            except:
                return HttpResponse('Something went wrong, check inner product or base')
            pretty_base(base)
            orth_base_json = json.dumps(orth_base)
            return render(response,"main/home.html",{'form':form , 'base':base, 'res':orth_base_json, 'sizeVector':sizeVector})
    else:
        form=HomeForm()
    return render(response,"main/home.html",{'form':form, 'base':None, 'res':None})


def about(response):
    return render(response, 'main/about.html')


def help(response):
    return render(response, 'main/help.html')

# def contact(response):
#     if response.method == 'POST':
#         name=response.POST['name']
#         mail=response.POST['mail']
#         message=response.POST['message']

#         send_mail('Website report from '+name, message, mail, ['ofek977@walla.co.il'])
        
#         return render(response, 'main/contact.html')
#     else:
#         return render(response, 'main/contact.html')