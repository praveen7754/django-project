from django.shortcuts import render,redirect
from .forms import *

def func(request):
    return render(request, "index.html")
# Create your views here.

# def display(request):
#     name="mukilan"
#     return render(request,"index.html",{"name":name})

# def greet(request):
#     data={"age":22}
#     return render(request,"index.html",data)

# def ifelse(request):
#     data={"name":"mukil",
#           "mark":[10,20,30,40,50]}
#     return render(request,"index.html",data)

def add_data(request):
    context={
        "form":stud_form()
    }
    if request.method=="POST":
        s_form=stud_form(request.POST)
        if s_form.is_valid():
            s_form.save()
            return redirect("/batch/view/")
        

    return render(request, "add.html",context)

def view_data(request):
    data={
        "all_data":Student.objects.all()

    }
    return render(request,"view.html",data)

def update_date(request,id):
    selected_data=Student.objects.get(id=id)
    context={
        "form":stud_form(instance=selected_data)
    }

    if request.method=="POST":
        up_from=stud_form(request.POST,instance=selected_data)
        if up_from.is_valid():
            up_from.save()
            return redirect("/batch/view/")

    return render(request,"add.html",context)

def delete_data(request,id):
    selected_data=Student.objects.get(id=id)
    selected_data.delete()

    return redirect("/batch/view/")

def about(request):
    return render(request,"about.html")

def base(request):
    return render(request,"base.html")

def contact(request):
    return render(request,"contact.html")

def service(request):
    return render(request,"service.html")



