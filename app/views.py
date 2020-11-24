from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

from django.views.generic import View,TemplateView
#responding a string By using Function Based View

from app import forms

def FBV(request):
    return HttpResponse('This is FBV response')

#responding a string By using Class Based View

class CBV(View):
    def get(self,request):
        return HttpResponse('This is Class Based View response')

#responding a Html File By using Function Based View

def FBV_template(request):
    return render(request,'FBV_template.html',context={'data':'Hai hello Python'})

#responding a Html File By using Class Based View

class CBV_template(View):
    def get(self,request):
        return render(request,'CBV_template.html',context={'data':'This Django'})


# Validating forms by using Function Based View

def FBV_form(request):
    form=forms.Student()
    if request.method=='POST':
        form_data=forms.Student(request.POST)
        if form_data.is_valid():
            return HttpResponse(str(form_data.cleaned_data))
    return render(request,'FBV_form.html',context={'form':form})

# Validating forms by using Class Based View


class CBV_form(View):
    def get(self,request):
        form=forms.Student()
        return render(request,'CBV_form.html',context={'form':form})

    def post(self,request):
        form_data=forms.Student(request.POST)
        if form_data.is_valid():
            return HttpResponse(str(form_data.cleaned_data))

# Dont use View Class whenever u deal with HTML file or Forms

#TemplateView class

'''
class Template_Render(TemplateView):
    template_name='Templateview.html'

'''



























