from django.shortcuts import render
from .models import Products, Company, Student
# Create your views here.


def index(request):
    # products = Products.objects.get(id=1).company.name
    # products = Products.objects.filter(company__name='mojang')
    # company = Company.objects.get(name='valve')
    # products = company.products_set.create(name='cs:go2', price=2500)
    # tom = Student.objects.create(name='Tom')
    # student = tom.course.create(name='Algebra')
    # courses = Student.objects.get(name='Tom').course.all()
    student = Student.objects.filter(name='Chunchukov Arsenii')
    return render(request, 'index.html', context={'student': student})
