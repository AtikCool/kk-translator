from django.urls import path
from . import views
urlpatterns = [
    path('translator', views.TranslatorHtmlAPI.as_view(), name='translator'),
    path('translator/API', views.TranslatorAPI.as_view(), name='translatorAPI')
]