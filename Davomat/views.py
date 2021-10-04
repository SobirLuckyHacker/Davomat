from django.shortcuts import redirect, render
from .models import Davomats, Students

def home(request):
    context={}
    context['stu']=studentss=Students.objects.all().order_by('-id')
    if request.method=="POST":
        full_name = request.POST.get('full_name')
        age = request.POST.get('age')
        if full_name=="" or age =="":
            context['error'] = 'Tsldsandas'
            return render(request,'index.html',context)
        student_all = Students(
            name=full_name,
            age=age
        )
        student_all.save()
    return render(request,'index.html',context)

def kelmadi(request,pk):
    context={}
    student_id = Students.objects.filter(id=pk)
    davomatlar=Davomats.objects.all().order_by('-id')
    for stu in student_id:
        print(stu)
        davomat = Davomats.objects.create(name=stu.name)
        davomat.save()
        return redirect('home')
    return render(request,'index.html',{"davomatsss":davomatlar})