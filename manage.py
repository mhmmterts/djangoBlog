#django projesi oluşturma
#cmd: django-admin startproject projeismi
#otomatik olarak django manage.py ve 5 ayrı .py uzantılı dosya oluşturur
#bu dosyayı hiç elleme, bu dosya herhangi bir komutu terminalden çalıştırmamızı sağlar
# "python manage.py runserve"r ile serverı çalıştırıyoruz
# + tuşundan 2. cmd açıp diğer işlemleri yapıyoruz
# "python manage.py migrate" ile db için gerekli tabloları oluşturuyoruz
# "python manage.py createsuperuser" ile admin hesabı oluşturup
# http://127.0.0.1:8000/admin/ sitesinden admin paneline giriş yapabiliyoruz
#ilk proje oluşturduğumuzda settings.py den LANGUAGE_CODE = 'tr' TIME_ZONE = 'Europe/Istanbul' yapıyoruz
#uygulama oluşturmak için python manage.py startapp uygulama_ismi
#sonra models kısmında tablosunu oluşturup admin.py ye bildiriyoruz ve settings.py de installed apps kısmına dahil ediyoruz
#uygulama oluşturma ayrıntısı için article klasöründe açıklama.txt yi oku 
#                       Django Shell ORM Sorgularını Kullanma
#"python manage.py shell" ile orm sorguları gerçekleştirilebilir "from django.contrib.auth.models import User","from article.models import Article" çağırıp artık obje oluşturup veri tabanına kaydedebiliriz
# obje oluşturup veri tabanına kaydetme:
#örn. newUser=User(username="deneme1",password="123"), newUser.save() admin kulanıcısı oluşturduk ve veritabanına kaydettik
#örn2. newUser2=User(username="deneme2"), newUser2.set_password("123"), newUser2.save() parola şifrelenmesi için set.password kullandık
#örn3. newUser3=User(), newUser3.username="deneme3" ,newUser3.first_name="Mahmut", newUser3.set_password("123"), newUser3.save()
#örn4. article=Article(title="Django Shell Deneme",content="İçerik",author=newUser2),article.save()
#örn5. Article.objects.create(title="Deneme15",content="icerik",author=newUser2) tek seferde obje oluşturduk
#obje bilgisi güncelleme: objeIsmi.özellik="....." objeIsmi.save()
#tüm objeleri alma: ObjeSınıfı.objects.all() örn. Article.objects.all()
#belirli objeyi alma: objeIsmi=ObjeSınıfı.objects.get(özellik="....") örn. nesne=Article.objects.get(title="Deneme10")
#obje silme: objeIsmi.delete()
#objeleri filtreleme: ObjeSınıfı.objects.filter(...__contains="...") örn. Article.objects.filter(title__contains="Mer")
#!/usr/bin/env python 
"""Django's command-line utility for administrative tasks."""
import os
import sys


def main():
    """Run administrative tasks."""
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'djangoBlog.settings')
    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ) from exc
    execute_from_command_line(sys.argv)


if __name__ == '__main__':
    main()
