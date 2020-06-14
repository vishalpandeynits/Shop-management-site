import django
from django.shortcuts import render,redirect
from .forms import *
from django.db.models import Q
from django.contrib.auth.decorators import login_required
from django.http import Http404
# Create your views here.


def signup(request):
    if request.method== 'POST':
        form= RegisterUserForm(request.POST or None)
        if form.is_valid():
            form.save()
            
    else:
        form = RegisterUserForm()
    return render(request,'registration/signup.html',{'form':form})

@login_required
def accounts(request):
    return render(request,'accounts.html')

@login_required
def employee(request):
    employee= Employee.objects.all().filter(user=request.user)
    if request.GET.get('search'):
        search = request.GET.get('search')
        employee = employee.filter(Q(employee_name__icontains=search)|Q(employee_position__icontains=search))
        
    if request.method=="POST":
        form = EmployeeRegisterForm(request.POST or None)
        if form.is_valid():
            data= form.save(commit=False)
            data.user = request.user
            data.save()
    else:
        form = EmployeeRegisterForm()  
    params={'emp':employee,'form':form}
    return render(request,'employee.html',params)

@login_required
def delete_employee(request,id):
    employee=Employee.objects.get(id=id)
    employee.delete()
    return redirect('/employee/')

@login_required
def full_info(request,id):
    employer=Employee.objects.get(id=id)
    params={'employer':employer}
    return render(request,'full_info.html',params)

@login_required
def update_employee(request,id):
    employee= Employee.objects.all().filter(user=request.user)
    if employee.user==request.user:
        if request.method=="POST":
            form = EmployeeRegisterForm(request.POST,instance=Employee.objects.get(id=id))
            if form.is_valid():
                data= form.save(commit=False)
                data.user = request.user
                data.save()
        else:
            form = EmployeeRegisterForm(instance=Employee.objects.get(id=id)) 
    else:
        raise Http404()
    params={'emp':employee,'form':form}
    return render(request,'employee.html',params)

@login_required
def notes(request):
    if request.method=='POST':
        form = NoteRegisterForm(request.POST, request.FILES)
        if form.is_valid():
            data=form.save(commit=False)
            data.user =request.user
            data.save()
    else:
        form= NoteRegisterForm()
    notes= Note.objects.all().filter(user=request.user).order_by('-id')
    query= request.GET.get('note_search')
    print(query)
    if query:
        notes=notes.filter(Q(title__icontains=query)|Q(content__icontains=query))
    params ={'form':form,'notes':notes}
    return render(request,'notes.html',params)

@login_required
def update_notes(request,id):
    if Note.objects.get(id=id).user==request.user:
        if request.method=='POST':
            form = NoteRegisterForm(request.POST, request.FILES,instance=Note.objects.get(id=id))
            if form.is_valid():
                data=form.save(commit=False)
                data.user =request.user
                data.save()
                return redirect('/notes/')
        else:
            form= NoteRegisterForm(instance=Note.objects.get(id=id))
        notes= Note.objects.all().filter(user=request.user)
    else:
        raise Http404()
    params ={'form':form,'notes':notes}
    return render(request,'notes.html',params)   

@login_required
def delete_notes(request,id):
    if Note.objects.get(id=id).user==request.user:
        note=Note.objects.get(id=id)
        note.delete()
    else:
        raise Http404()
    return redirect('/notes/')

@login_required
def item(request):
    if request.method=='POST':
        form = ItemRegisterForm(request.POST ,request.FILES)
        if form.is_valid():
            data=form.save(commit=False)
            data.user = request.user
            data.save()
            return redirect('/item/')
    else:
        form = ItemRegisterForm()

    items=Item.objects.all()
    if request.GET.get('item_search'):
        item_search=request.GET.get('item_search')
        items=items.filter(Q(item_name__icontains=item_search)|
                            Q(item_category__icontains=item_search)|Q(item_description__icontains=item_search))

    params={'form':form,'items':items}
    return render(request,'item.html',params)

@login_required
def myaccount(request):
    if request.method=='POST':
        city= request.POST.get('city')
        state=request.POST.get('state')
        form = MyAccountForm(request.POST)
        if form.is_valid():
            data = form.save(commit= False)
            data.user= request.user
            data.city= city
            data.state=state
            data.save()
            return redirect('/myaccount/')
    else:
        form = MyAccountForm()
    try:
        shop_info = Shop.objects.get(user=request.user)
    except Shop.DoesNotExist:
        shop_info =None
    params= {'form':form,'shop_info':shop_info}
    return render(request,'myaccount.html',params)

