from django.shortcuts import render
#from django.http import HttpResponse
#from appTwo.models import User
from appTwo.forms import NewUser

# Create your views here.
def index(request):
    return render(request,'apptwo/index.html')

def users(request):
    form= NewUser()

    if request.method == "POST":
        form = NewUser(request.POST)

        if form.is_valid():
            form.save(commit=True)
            return index(request)
        else:
            print('Error !!! Form Invalid')
    return render(request,'apptwo/users.html',{'form':form})
