from django.shortcuts import render, redirect
from .models import Patients
from .forms import MyForm
from .filters import OrderFilter
from .forms import CreateUserForm
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages


def registerPage(request):
    if request.user.is_authenticated:
        return redirect('/')
    else:
        form = CreateUserForm()
        if request.method == 'POST':
            form = CreateUserForm(request.POST)
            if form.is_valid():
                form.save()
                user = form.cleaned_data.get('username')
                messages.success(request, 'Account was created for ' + user)

                return redirect('/')

        context = {'form': form}
        return render(request, 'register.html', context)


def loginPage(request):
    if request.user.is_authenticated:
        return redirect('/')
    else:
        if request.method == 'POST':
            username = request.POST.get('username')
            password = request.POST.get('password')

            user = authenticate(request, username=username, password=password)

            if user is not None:
                login(request, user)
                return redirect('/')
            else:
                messages.info(request, 'Username OR password is incorrect')

        context = {}
        return render(request, 'login.html', context)

def logoutUser(request):
    logout(request)
    return redirect('login')

def index(request):
    patients = Patients.objects.all()

    myFilter = OrderFilter(request.GET, queryset=patients)
    patients = myFilter.qs

    total_patients = patients.count()

    context = {'patients': patients, 'myFilter': myFilter, 'total_patients': total_patients}

    return render(request, 'index.html', context)


def delete_patient(request, pk):

    template = 'index.html'
    Patients.objects.filter(id=pk).delete()

    items = Patients.objects.all()

    context = {
        'items': items,
    }

    return render(request, template, context)


def my_form(request):
  if request.method == "POST":
    form = MyForm(request.POST)
    if form.is_valid():
        form.save()
        return redirect('/')
  else:
      form = MyForm()
  return render(request, 'cv-form.html', {'form': form})
