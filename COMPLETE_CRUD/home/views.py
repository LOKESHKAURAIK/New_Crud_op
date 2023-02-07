from django.shortcuts import render
from .models import Emp
def home(request):
    data=Emp.objects.all()
    return render(request,"index.html",{"data":data})
def addemp(request):
    name=request.POST['name']
    sal=request.POST['sal']
    sal=int(sal)
    address=request.POST['address']
    e=Emp()
    e.name=name
    e.sal=sal
    e.address=address
    e.save()
    data=Emp.objects.all()
    return render(request,"index.html",{"data":data})
    # ham delete nam se function banayenge jaha request ayegi
def delete(request):
    return render(request,"delete.html")
def delt(request):
    eid=request.GET['eid']
    Emp.objects.get(id=eid).delete()
    data=Emp.objects.all()
    return render(request,"index.html",{"data":data})
def search(request):
    eid=request.POST['eid']
    e=Emp.objects.get(id=eid)
    return render(request,"index.html",{"data":[e]})
def update(request):
    # yaha hamne direct class ka object bana ke call kar rahe
    e=Emp()
    e.id=request.POST['id']
    e.name=request.POST['name']
    sal=request.POST['sal']
    e.sal=int(sal)
    e.address=request.POST['address']
    e.save()
    data=Emp.objects.all()
    return render(request,"index.html",{"data":data})