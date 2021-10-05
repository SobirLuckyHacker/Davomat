from django.shortcuts import redirect, render
from .models import Davomat, Students,Group_Student
from datetime import datetime

def home(request):
    context={}
    context['stu']=studentss=Students.objects.all().order_by('-id')
    context['group'] = Group_Student.objects.all()
    if request.method=="POST":
        full_name = request.POST.get('full_name')
        age = request.POST.get('age')
        groups = request.POST.get('groups')
        try:
            gr = Group_Student.objects.get(id=groups)
        except Group_Student.DoesNotExist:
            gr = None
        if full_name=="" or age =="":
            context['error'] = 'Tsldsandas'
            return render(request,'index.html',context)
        if full_name == None or age == None:
            return render(request,'index.html',context)
        student_all = Students(
            name=full_name,
            age=age,
            group_choose=gr
        )
        student_all.save()
    return render(request,'index.html',context)

def kelmadi(request,pk):
    context={}
    student_id = Students.objects.filter(id=pk)
    davomatlar=Davomat.objects.all().order_by('-id')
    for stu in student_id:
        print(stu.group_choose)
        davomat = Davomat.objects.create(
            name=stu.name,
            group=stu.group_choose
            )
        return redirect('home')
        
def history(request):
    this_date = datetime.today().date()
    # Date bilan ishlangan
    davomatlar=Davomat.objects.all().order_by('-id')
    groups_student = Group_Student.objects.all()
    student_category = request.GET.get('cts',"0")
    if student_category != '0' :
        ctg=Davomat.objects.filter(group=student_category).order_by('-id')
        print(ctg)
    else:
        ctg=Davomat.objects.all()
    attendence = Davomat.objects.filter(date__day=this_date.day)
    len_davomat = len(attendence)
    return render(request,'davomat_history.html',{'davomat':davomatlar,'time':this_date,'davomat_len':len_davomat,'groups':groups_student,'ctg':ctg})

def delete(request,pk):
    student = Students.objects.filter(id=pk)
    student.delete()
    return redirect('home')
    
def delete_davomat(request,pk):
    davomat_delete = Davomat.objects.filter(id=pk)
    davomat_delete.delete()
    return redirect('history')