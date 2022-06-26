from django.shortcuts import render
from apps.sys_admin.models import Employee

def index(request):
  return render(request, 'frontend/index.html')

def home(request):
    print(Employee.objects.all())
    context = {
        "employees": Employee.objects.all()
    }

    return render(request, 'frontend/home.html', context)
    