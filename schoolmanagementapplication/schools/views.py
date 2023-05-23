from django.shortcuts import render, redirect
from schools.forms import SchoolForm
from schools.models import School


def list(request):
    schools = School.objects.all()

    return render(request, "list.html", {'schools': schools})


def add(request):
    if request.method == "POST":
        form = SchoolForm(request.POST)
        if form.is_valid():
            try:
                form.save();
                return redirect("/list")
            except:
                pass
    form = SchoolForm()
    return render(request, "add.html", {'form': form})


def edit(request, id):
    school = School.objects.get(id=id)  # select * from table where id = 2
    return render(request, "edit.html", {"school": school})


def update(request, id):
    school = School.objects.get(id=id)
    form = SchoolForm(request.POST, instance=school)

    if form.is_valid():
        try:
            form.save()
            return redirect("/list")
        except:
            pass


def delete(request, id):
    school = School.objects.get(id=id)
    school.delete()
    return redirect("/list")
