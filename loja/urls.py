from django.urls import path,include
from loja import views
from django.conf import settings
from django.conf.urls.static import static
from django.conf import settings
from django.conf.urls import include

app_name = 'loja'

urlpatterns = [
    path('', views.index, name='index'),

]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

