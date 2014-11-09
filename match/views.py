from django.shortcuts import render, redirect, HttpResponse
#from django.contrib.auth.forms import UserCreateForm
from forms import UserCreateForm, InterestForm, DescriptionForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User

def register(request):
    if request.method == 'POST':
        form = UserCreateForm(request.POST)


        if form.is_valid():
            username = form.clean_username()
            password = form.clean_password2()
            form.save()
            user = authenticate(username=username, password=password)
            login(request,user)
            #return render(request,'created_file.html')
            return redirect('match.views.success')
    else:
        form = UserCreateForm()
        context = {"form":form}
        context = {}
        context['form'] = form
        return render(request, 'register.html',context)

def create_new(request):
    return render(request,'createnew.html')

def index(request):
    return render(request, 'index.html')

def login_view(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if user:
            login(request,user)
            return redirect('match.views.index')
        else:
            return HttpResponse("WRONG")
    else:
        return render(request, 'login.html')

def logout_view(request):
    logout(request)
    return render(request, 'logout.html')

def success(request):
    if request.user.is_authenticated():
        return render(request, 'success.html')
    else:
        return HttpResponse("idk")

def profile(request):
    context = {'interest_form':InterestForm(), 'description_form':DescriptionForm()}

    return render(request, 'profile.html', context)

'''def createnew(request):
    if request.method == 'POST':
        form = UserCreateForm(request.POST)
        if form.is_valid():
            departFrom = form.clean_username()
            departTo = form.clean_password2()
            departDate = form.
            form.save()
            login(request,user)
            #return render(request,'created_file.html')
            return redirect('match.views.success')
    else:
        form = UserCreateForm()
        context = {"form":form}
        context = {}
        context['form'] = form
        return render(request, 'register.html',context)
'''