from django.shortcuts import render,redirect
from . import models
import os
from django.db.models import Q
from django.contrib import messages
# Create your views here.

def home(request):
    if request.method == 'GET':
        src = request.GET.get('src')
        if src:
            profile = models.Profile.objects.filter(name__icontains=src)
        elif src == None:
            profile = models.Profile.objects.all()
        else:
            profile = models.Profile.objects.all()
    return render(request,'home.html',locals())

def create(request):
    try:

        if request.method == 'POST':
            name = request.POST.get('Name')
            image = request.FILES.get('image')
            email = request.POST.get('email')
            gender = request.POST.get('gender')
            address = request.POST.get('address')
            religion = request.POST.get('religion')
            blood_group = request.POST.get('blood_group')
            Date_of_birth = request.POST.get('date_of_birth')
            is_alive = request.POST.get('is_alive')
            if models.Profile.objects.filter(Q(email=email)).exists():
                messages.warning(request, "this email already taken.")
                return redirect('create')
            elif models.del_profile.objects.filter(Q(email=email)).exists():
                messages.warning(request, "this email already taken on inactive profile list")
                return redirect('create')
            else:
                if image:
                    if is_alive =="1":
                        profile = models.Profile.objects.create( name=name,image=image,email=email,gender=gender,address=address,religion=religion,blood_group=blood_group,Date_of_birth=Date_of_birth,is_alive=True
                        )
                        profile.save()
                        messages.success(request, "Account Created.")
                        return redirect('home')
                    else:
                        profile = models.Profile.objects.create( name=name,image=image,email=email,gender=gender,address=address,religion=religion,blood_group=blood_group,Date_of_birth=Date_of_birth
                        )
                        profile.save()
                        messages.success(request, "Account Created.")
                        return redirect('home')
                else:
                    if is_alive =="1":
                        profile = models.Profile.objects.create( name=name,email=email,gender=gender,address=address,religion=religion,blood_group=blood_group,Date_of_birth=Date_of_birth,is_alive=True
                        )
                        profile.save()
                        messages.success(request, "Account Created.")
                        return redirect('home')
                    else:
                        profile = models.Profile.objects.create( name=name,email=email,gender=gender,address=address,religion=religion,blood_group=blood_group,Date_of_birth=Date_of_birth
                        )
                        profile.save()
                        messages.success(request, "Account Created.")
                        return redirect('home')

    except Exception as e:
        messages.warning(request, "Somthing wrong !")
    return render(request, 'create.html')


def delete(request,id):
    profile = models.Profile.objects.get(id=id)
    del_pro = models.del_profile.objects.create(
        name = profile.name,
        image = profile.image,
        email = profile.email,
        gender = profile.gender,
        address = profile.address,
        religion = profile.religion,
        blood_group = profile.blood_group,
        date_of_birth = profile.Date_of_birth,
        is_alive = profile.is_alive,
        previous_id = profile.id,
    )
    profile.delete()
    return redirect('home')

def profile_see(request,id):
    try:
        profile = models.Profile.objects.get(id=id)
    except Exception as e:
        print(e)
    return render(request,'profile.html',locals())

def profile_update(request,id):
    try:
        profile = models.Profile.objects.get(id=id)
        if request.method == 'POST':
            name = request.POST.get('Name')
            image = request.FILES.get('image')
            email = request.POST.get('email')
            gender = request.POST.get('gender')
            address = request.POST.get('address')
            religion = request.POST.get('religion')
            blood_group = request.POST.get('blood_group')
            Date_of_birth = request.POST.get('date_of_birth')
            is_alive = request.POST.get('is_alive')
            if image == None:
                pass
            elif profile.image != 'def.png':
                os.remove(profile.image.path)
                profile.image=image
            else:
                profile.image=image
                
            profile.name=name
            profile.email=email
            profile.gender=gender
            profile.address=address
            profile.religion=religion
            profile.blood_group=blood_group
            profile.Date_of_birth=Date_of_birth
            if is_alive != False:
                profile.is_alive=True
            profile.save()
            messages.success(request, "Account Update success.")
            return redirect('home')
    except Exception as e:
        messages.success(request, "Somthing wrong !.")
    return render(request,'update.html',locals())

def delete_profiles(request):
    profile = models.del_profile.objects.all()
    if request.method == "GET":
        src = request.GET.get('src')
        if src:
            profile = models.del_profile.objects.filter(name__icontains = src)
        elif src == None:
            profile = models.del_profile.objects.all()
        else:
            profile = models.del_profile.objects.all()
    return render(request,'delete.html',locals())

def delete_permanent(request,id):
    profile = models.del_profile.objects.get(id=id)
    if profile.image!='def.png':
        os.remove(profile.image.path)
    profile.delete()
    return redirect('home')

def restore_profiles(request,id):
    profile = models.del_profile.objects.get(id=id)
    restore = models.Profile.objects.create(
        name = profile.name,
        image = profile.image,
        email = profile.email,
        gender = profile.gender,
        address = profile.address,
        religion = profile.religion,
        blood_group = profile.blood_group,
        Date_of_birth = profile.date_of_birth,
        is_alive = profile.is_alive,
        id = profile.id,
    )
    restore.save()
    profile.delete()
    return redirect('home')