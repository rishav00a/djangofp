from django.shortcuts import render
from . import forms
from f_app.models import AccessRecord,Webpage,AccessRecord


# Create your views here.
def index(request):
    my_dict={'cont':'This is the landing page'}
    return render(request,'index.html',context=my_dict)

def help(request):
    my_dict={'helpp':'What help do you want'}
    return render(request,'help.html',context=my_dict)

def extent_help(request):
    my_dict={'helpp':'this is external'}
    return render(request,'help.html',context=my_dict)

def show(request):
    webpages_list=AccessRecord.objects.order_by('date')
    date_dict={'access_records':webpages_list}
    return render(request,'show.html',context=date_dict)


def frms(request):
    form=forms.FormName()

    if request.method == 'POST':
        form = forms.FormName(request.POST)

        if form.is_valid():
            print(" Validation sucess")
            print("Name"+form.cleaned_data['name'])
    return render(request,'form.html',{'form':form})
