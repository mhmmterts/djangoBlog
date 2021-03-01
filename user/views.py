from django.shortcuts import render,redirect#sayfa yönlendirmeleri için gerekli
from .forms import RegisterForm,LoginForm#form yapıları için gerekli
from django.contrib.auth.models import User # django nun kendi obje modelini kullandık
from django.contrib.auth import login,authenticate,logout#doğrulama için gerekli
from django.contrib import messages #flash mesajlarını import ediyoruz   

# Create your views here.
def register(request):
    form=RegisterForm(request.POST or None)#get veya post request olsa dahi form oluşturuluyor
    if form.is_valid():#validation bölümünde clean metodu çalışır ve kontrol eder
        username=form.cleaned_data.get("username")
        password=form.cleaned_data.get("password")
        newUser=User(username=username)
        newUser.set_password(password)
        newUser.save()
        login(request,newUser)
        messages.info(request,"Başarıyla kayıt oldunuz...")

        return redirect("index")#urls.pyde bulunan index.html in name i ile çağırdık 
    context={
        "form":form
    }
    return render(request,"register.html",context)
def loginUser(request):
    form=LoginForm(request.POST or None)
    context={
        "form":form
    }
    if form.is_valid():
        username=form.cleaned_data.get("username")
        password=form.cleaned_data.get("password")
        user = authenticate(username = username,password = password)#veri tabanına bakar böyle bir kullanıcı var mı diye
        if user is None:
            messages.info(request,"Kullanıcı adı veya parola hatalı...")
            return render(request,"login.html",context)
        messages.success(request,"Giriş başarılı...")
        login(request,user)
        return redirect("index")
    return render(request,"login.html",context)
def logoutUser(request):
    logout(request)
    messages.success(request,"Çıkış yapıldı...")
    return redirect("index")
