from django.shortcuts import render,redirect
from .forms import signupModel
from .models import signup
from django.contrib.auth import logout

# Create your views here.

def index(request):
    if request.method=='POST':
        if request.POST.get('signup')=='signup':
            signupreq=signupModel(request.POST)
            if signupreq.is_valid():
                signupreq.save()
                print("Signup successfully!")
                return redirect('notes')
            else:
                print(signupreq.errors)
        elif request.POST.get('login')=='login':
            unm=request.POST['username']
            pas=request.POST['password']

            user=signup.objects.filter(username=unm,password=pas)

            if user:
                print('Login successfully!')
                request.session['user']=unm
                return redirect('notes')
            else:
                print('Login faild....somthing went wrong - Try again.')
    else:
        signupreq=signupModel()
    return render(request, 'index.html')

def notes(request):
    user=request.session.get('user')
    return render(request, 'notes.html',{'user':user})


def userlogout(request):
    logout(request)
    return redirect('/')