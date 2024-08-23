from django.shortcuts import render,redirect
from table.models import Student

def Home(request):
    
    students= Student.objects.all()
    
    data= {"data": students }
    return render(request,"home.html",data)

def Submit(request):
    a= request.POST['name']
    b= request.POST['age']
    c= request.POST['city']
    d=request.FILES.get('img')

    Student(name= a,age= b,city= c,img=d).save()
    return redirect('/')


def Delete(request,id):

    Student.objects.get(id= id).delete()
    return redirect('/')


def Edit(request,id):
    
    object= Student.objects.get(id= id)
    a= request.POST['name']
    b= request.POST['age']
    c= request.POST['city']
    d= request.FILES.get('img')

    object.name= a
    object.age= b
    object.city= c
    
    if d is not None:
        object.img= d
        
    object.save()

    return redirect('/')



