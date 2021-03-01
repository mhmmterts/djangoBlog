from django.contrib import admin
from .models import Article,Comment#article modelini models.py den import edip admin paneline kayıt ettik
#modellerimizin admin panelinde gözükmesini istiyorsak buraya kaydetmemiz lazım 
# Register your models here.
#admin.site.register(Article)#normal kaydetme, eğer özelleştirmek istiyorsak kendimiz model classını yazarız

#decorator ile admin panelinde oluşturduğumuz article listesinin nasıl görüneceğini
#list_display ile özelleştirdik ve  meta classı ile admin paneline model olarak bağladık
admin.site.register(Comment)
@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    list_display=["title","author","created_date"]
    list_display_links=["title","created_date"]
    search_fields=["title"]
    list_filter=["created_date"]
    class Meta:#meta classı özel bir class 
        model=Article
