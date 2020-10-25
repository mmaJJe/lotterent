from django.shortcuts import render, redirect, get_object_or_404 
from django.contrib.auth.hashers import check_password
from .models import CustomUser
from rentapp.models import rent

def signup(request):
    if request.method == 'POST':
        nickname = request.POST['nickname']
        name = request.POST['name']
        phone = request.POST['phone']
        birth = request.POST['birth']
        address = request.POST['address']
        pwd = request.POST['password']
        c_pwd = request.POST['check_password']

        if CustomUser.objects.filter(username = nickname).distinct():
            return render(request, 'user/signup.html', {'err1' : '중복 아이디가 존재합니다.'})
        if pwd != c_pwd:
            return render(request, 'user/signup.html', {'err2' : '비밀번호가 일치하지 않습니다'})
        
        customUser = CustomUser(
            username = nickname,
            name = name,
            phone = phone,
            birth = birth,
            address = address,
        )
        customUser.set_password(pwd)
        customUser.save()
        return redirect('login')
    else:
        return render(request, 'user/signup.html')

def login(request):
    if request.method == "POST":
        nickname = request.POST['nickname']
        pwd = request.POST['password']

        user = get_object_or_404(CustomUser, username = nickname)
        if check_password(pwd, user.password):
            request.session['user'] = user.username
            return redirect('home')
        else:
            return render(request, 'user/login.html', {'err' : '비밀번호가 틀렸습니다.'})
    else:
        return render(request, 'user/login.html')

def logout(request):
    if request.session.get('user', False):
        request.session.modified = True
        del request.session['user']
        return redirect("home")
    else:
        return redirect("home")

def read(request):
    Rents = rent.objects.all()
    context = {'Rents' : Rents}
    return render(request, 'Mypage/index.html', context)
    