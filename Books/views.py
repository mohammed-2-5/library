import imp
import re
from django.shortcuts import render,redirect

# Create your views here.
from .models import Department

def retrivedept(request):
    x=Department.objects.all()
    return render(request,'Booksapp/listofdept.html', {'departments':x})

def DeptDisplay(request,dept_id):
    dept=Department.objects.get(pk=dept_id)
    return render(request,'Booksapp/Dept.html',{'Department':dept})

from .form import deptform,newbook
def add_new_dept(request):
    form=deptform(request.POST or None,request.FILES or None)
    if form.is_valid():
        form.save()
        return redirect('list_of_department')
    
    return render(request,'Booksapp/new_dept.html',{'form':form})


def new_book(request,dept_id):
    dept=Department.objects.get(pk=dept_id)

    form=newbook(request.POST or None,request.FILES or None)
    if form.is_valid():
        form=form.save(commit=False)
        form.dept=dept
        form.save()
        return redirect('display_department',dept_id=dept_id)
    return render(request,'Booksapp/newbook.html',{'Department':dept,'form':form})