from django.urls import path
from . import views

urlpatterns = [
    path('', views.layout),
    path('products/', views.products),
    path('customer/', views.customer),
    path('about/',views.about),
    path('contact/',views.contact),
    path('index/',views.index),

    path('aboutUs/',views.aboutUs, name='aboutUs'),
    path('contactUs/',views.contactUs, name='contactUs'),
    path('login/',views.login, name='login'),
    path('product/',views.product, name='product'),
    path('promotion/',views.promotion, name='promotion'),
    path('layout/',views.layout, name='layout'),
    path('ListCategory/',views.ListCategory,name='ListCategory'),

    path('indexPA/', views.indexPA, name='indexPA'),
]