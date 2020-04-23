from django.shortcuts import render, redirect
from schedule.models import Show
from django.contrib import messages
# from datetime import datetime

def homeroute(request):
    return redirect('/shows')
def shows(request):
    print("*"*100)
    print("All Shows table")
    print(request.method)
    context={
        'shows_table': Show.objects.all(),
    }
    # print(context['shows_table'])
    return render (request,'shows.html',context)
# Create your views here.

def new(request):
    print("*"*100)
    print("Data entry: New Show")
    print(request.method)
    return render(request,'new_show.html')

def create(request):
    print("*"*100)
    print("A new show was created")
    print(request.method)
    print(request.POST)
    # *************Cleaning input data(empty input, too short, etc.)**************
    errors= Show.objects.basic_validator_bonus(request.POST)
    if len(errors)>0:
        for k, v in errors.items():
            messages.error (request,v)
        return redirect('/shows/new')
    # ******************************************************************************
    else: 
        a=request.POST['title']
        b=request.POST['network']
        c=request.POST['release_date']
        d=request.POST['desc']
        Show.objects.create(title=a, network=b, release_date=c, desc=d)
        last=Show.objects.last()
        return redirect(f"/shows/{last.id}")

def read(request,x):
    print("*"*100)
    print("reading show details")
    print(request.method)
    selected_show=Show.objects.get(id=int(x))
    context={
        "id": selected_show.id,
        "title": selected_show.title,
        "network": selected_show.network,
        "release_date": selected_show.release_date,
        "desc": selected_show.desc,
        "update_time": selected_show.updated_time
    }
    return render(request,'details_show.html',context)

def update(request,x):
    print("*"*100)
    print("update a show details")
    print(request.method)
    selected_show=Show.objects.get(id=int(x))
    context={
        "id": selected_show.id,
        "title": selected_show.title,
        "network":selected_show.network,
        "release_date": selected_show.release_date.strftime('%Y-%m-%d'),
        "desc": selected_show.desc,
    }
    return render(request,'update_shows.html',context)

def edit(request,x):
    print("*"*100)
    print("A show was edited")
    print(request.method)
    print(request.POST)
    # *************Cleaning input data(empty input, too short, etc.)**************
    errors= Show.objects.basic_validator_bonus(request.POST)
    if len(errors)>0:
        for k, v in errors.items():
            messages.error (request, v)
        return redirect(f'/shows/{x}/update')
    # ******************************************************************************
    else: 
        selected_show=Show.objects.get(id=int(x))
        selected_show.title=request.POST['title']
        selected_show.network=request.POST['network']
        selected_show.release_date=request.POST['release_date']
        selected_show.desc=request.POST['desc']
        selected_show.save()
        return redirect(f"/shows/{selected_show.id}")

def delete(request,x):
    print("*"*100)
    print("A new show was deleted")
    print(request.method)
    selected_show=Show.objects.get(id=int(x))
    selected_show.delete()
    return redirect("/shows")
    