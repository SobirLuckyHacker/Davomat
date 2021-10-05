from django.shortcuts import redirect, render
from .models import Davomats, Student
from datetime import datetime

def home(request):
    context={}
    context['stu']=studentss=Student.objects.all().order_by('-id')
    if request.method=="POST":
        full_name = request.POST.get('full_name')
        age = request.POST.get('age')
        if full_name=="" or age =="":
            context['error'] = 'Tsldsandas'
            return render(request,'index.html',context)
        student_all = Student(
            name=full_name,
            age=age
        )
        student_all.save()
    return render(request,'index.html',context)

def kelmadi(request,pk):
    context={}
    student_id = Student.objects.filter(id=pk)
    davomatlar=Davomats.objects.all().order_by('-id')
    s=0
    for stu in student_id:
        for davomats in davomatlar:
            if stu.name==davomats.name:
                s+=1
                print(davomats.name)
        print(s)
        davomat = Davomats.objects.create(name=stu.name)
        davomat.save()
        return redirect('home')
    
def history(request):
    this_date = datetime.now()
    davomatlar=Davomats.objects.all().order_by('-id')
    
       
    return render(request,'davomat_history.html',{'davomat':davomatlar,'time':this_date})

def delete(request,pk):
    student = Student.objects.filter(id=pk)
    student.delete()
    return redirect('home')
    
def delete_davomat(request,pk):
    davomat_delete = Davomats.objects.filter(id=pk)
    davomat_delete.delete()
    return redirect('history')