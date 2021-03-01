from django.shortcuts import render,HttpResponse,redirect,get_object_or_404,reverse
from .forms import ArticleForm
from .models import Article,Comment
from django.contrib import messages
from django.contrib.auth.decorators import login_required
#herhangi bir url mapine göre çalıştırılacak kod ve fonksiyonları bardındıran dosya
# Create your views here.

def index(request):
    context={
        "number1":[1,2,3,4,5,6,7]
    }
    #index çağırıldığında işlenecek fonksiyon belirtilir
    #return HttpResponse("Anasayfa")
    return render(request,"index.html",context)#otomatik templates klasörüne baktığı için düz isim
def about(request):
    return render(request,"about.html")
def detail(request,id):
    return HttpResponse("Detail:"+str(id))
@login_required(login_url='user:login')
def dashboard(request):
    articles=Article.objects.filter(author=request.user)
    context={
        "articles":articles
    }
    return render(request,"dashboard.html",context)
@login_required(login_url='user:login')
def addarticle(request):
    form=ArticleForm(request.POST or None,request.FILES or None)

    if form.is_valid():
        article=form.save(commit=False)#article objesi oluşturup veri tabanına kaydetmeye çalışır ama authoru kendimiz vermemiz lazım
        article.author=request.user
        article.save()
        messages.success(request,"Makale oluşturuldu.")
        return redirect("article:dashboard")
    
    return render(request,"addarticle.html",{"form":form})
def detail(request,id):
    #article=Article.objects.filter(id=id).first()#bulduğu ilk elementi döner first() demezsek liste döner tek obje dönmez
    article=get_object_or_404(Article,id=id)#eğer objeye ulaşamazsa sayfa 404 hatası verir
    comments=article.comments.all()
    return render(request,"detail.html",{"article":article,"comments":comments})
def articles(request):
    keyword=request.GET.get("keyword")#arama çubuğu için 
    if keyword:#eğer kelime var ise
        articles=Article.objects.filter(title__contains=keyword)
        return render(request,"articles.html",{"articles":articles})
    articles=Article.objects.all()
    context={
        "articles":articles
    }
    return render(request,"articles.html",context)
@login_required(login_url='user:login')
def updateArticle(request,id):
    article=get_object_or_404(Article,id=id)
    form=ArticleForm(request.POST or None,request.FILES or None,instance=article)
    if form.is_valid():
        article=form.save(commit=False)
        article.author=request.user
        article.save()
        messages.success(request,"Makale güncellendi")
        return redirect("article:dashboard")
    return render(request,"update.html",{"form":form})
@login_required(login_url='user:login')
def deleteArticle(request,id):
    article=get_object_or_404(Article,id=id)
    article.delete()
    messages.success(request,"Makale başarıyla silindi")
    return redirect("article:dashboard")
def addComment(request,id):
    article=get_object_or_404(Article,id=id)

    if request.method =="POST":
        comment_author=request.POST.get("comment_author")
        comment_content=request.POST.get("comment_content")
        newComment=Comment(comment_author=comment_author,comment_content=comment_content)
        newComment.article=article
        newComment.save()
    return redirect(reverse("article:detail",kwargs={"id":id}))


