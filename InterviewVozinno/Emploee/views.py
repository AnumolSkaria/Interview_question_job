from django.shortcuts import render, redirect

# Create your views here.
from django.urls import reverse_lazy
from django.views.generic import CreateView, TemplateView

from Emploee.forms import EmployeeCreate, EmployeeUpdate
from Emploee.models import Employee



def AddEmploy(request):
    form=EmployeeCreate()
    template_name='create_employ.html'
    context={}
    context["form"]=form
    if request.method=='POST':
        form=EmployeeCreate(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            return redirect('login')
    return render(request,template_name,context)

def listEmploy(request):
    template_name='list_employ.html'
    qs=Employee.objects.all()
    context={}
    context["queryset"]=qs
    return render(request,template_name,context)

def EmployeLogin(request):
    form=EmployeeCreate()
    template_name="login.html"
    context={}
    context["form"]=form
    if request.method=='POST':
        username=request.POST.get("User_name")
        # request.session['']


        password=request.POST.get("Password")
        qs=Employee.objects.get(User_name=username)
        # print(qs.employee_id)

        if (qs):
            if (password == qs.Password):
                print("ok")
                print("successfully Login")

                # return redirect("profile")

                context['usr']=qs

                return render(request,'profile.html',context)
            else:
                return render("login.html")
    return render(request, template_name, context)


def Home(request):
    template_name='home.html'
    qs=Employee.objects.all()
    context={}
    context["emp"]=qs
    return render(request,template_name)

#
def Profile(request):
    template_name='profile.html'

    return render(request,template_name)

def UpdateEmploy(request,pk):
    obj=Employee.objects.get(id=pk)
    form=EmployeeUpdate(instance=obj)
    context={}
    context['form']=form
    if request.method=='POST':
        print("ok")
        form=EmployeeUpdate(request.POST,request.FILES)
        if form.is_valid():

            print('ok')
            uname=form.cleaned_data['User_name']
            passwrd=form.cleaned_data['Password']
            age=form.cleaned_data['Age']
            name=form.cleaned_data['Name']
            photo=form.cleaned_data['Profile_img']
            print(uname,passwrd,age,name,photo)
            obj.User_name=uname
            obj.Password=passwrd
            obj.Age=age
            obj.Name=name
            obj.Profile_img=photo
            obj.save()
            # form.save()
            return redirect('login')
        else:
            context={}
            context['form']=form
            return render(request,'update.html',context)
    return render(request,'update.html',context)

def DeleteEmp(request,pk):
    obj = Employee.objects.get(id=pk)
    print(obj)
    # if request.method == 'POST':
    #     print('ok')
    qs =Employee.objects.get(User_name=obj).delete()
    return redirect('home')












