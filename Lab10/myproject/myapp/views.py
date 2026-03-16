from django.shortcuts import render, redirect, get_object_or_404
from .models import Person

# แสดงข้อมูล
def index(request):
    persons = Person.objects.all()
    return render(request, 'index.html', {'persons': persons})


# เพิ่มข้อมูล
def form(request):

    if request.method == "POST":
        name = request.POST['name']
        age = request.POST['age']

        Person.objects.create(
            name=name,
            age=age
        )

        return redirect('/')

    return render(request, 'form.html')


# แก้ไขข้อมูล
def edit(request,id):

    person = get_object_or_404(Person,id=id)

    if request.method == "POST":

        person.name = request.POST['name']
        person.age = request.POST['age']

        person.save()

        return redirect('/')

    return render(request,'edit.html',{
        'person':person
    })


# ลบข้อมูล
def delete(request,id):

    person = Person.objects.get(id=id)
    person.delete()

    return redirect('/')