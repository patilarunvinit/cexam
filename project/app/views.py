from django.shortcuts import render
from .models import data

# Create your views here.
def home(request):
    if request.method == 'POST':
        name = request.POST.get("name")
        lastname = request.POST.get("lastname")
        gender = request.POST.get("gender")
        company = request.POST.get("company")
        birthday = request.POST.get("birthday")
        data.objects.create(name=name,lastname=lastname,gender=gender,company=company,birthday=birthday)
        print(name,lastname,gender,company,birthday)

    return render(request, "home.html")