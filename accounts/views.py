from django.shortcuts import render
from django.http import HttpResponse
from .models import *
# Create your views here.

def indexPA(request):
    return render(request,'PA/index.html')

def home(request):
    return HttpResponse('Home_page')

def products(request):
    return HttpResponse('Products_page')

def customer(request):
    return HttpResponse('Customer_page')
def about(request):
    return HttpResponse('About_page')
def contact(request):
    return HttpResponse('Contact_page')
def index(request):
    UnitPrice = 1500
    Quantity = 5
    Total = UnitPrice * Quantity
    ProductPrice = 5000
    Amount = 700
    context = {
        'TotalPrice':Total, 
        'ProductPrice':ProductPrice,
        'Amount': Amount,
        'Dayti' :[1,2,3,4,5,6,7,8,9,10,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31],
        }
    return render(request,'accounts/index.html', context)
def aboutUs(request):
    return render(request,'accounts/aboutUs.html')
def contactUs(request):
    return render(request,'accounts/contactUs.html')
def login(request):
    return render(request,'accounts/login.html')
def product(request):
    return render(request,'accounts/product.html')
def promotion(request):
    return render(request,'accounts/promotion.html')
def layout(request):
    Banner = Image.objects.filter(ImageTypeID=1)
    ImageSidebarLeft = Image.objects.filter(ImageTypeID=3)
    ImageSidebarRight = Image.objects.filter(ImageTypeID=4)
    Footer = Image.objects.filter(ImageTypeID=5)
    SlideShow = Image.objects.filter(ImageTypeID=2)
    UseExclude = Image.objects.exclude(ImageTypeID=2)
    UseOrderBy = Image.objects.order_by('id')
    UseFirst = Image.objects.first()
    UseLast = Image.objects.last()
    UseCount = Image.objects.count()
    UseExists = Image.objects.filter(id=9).exists()
    context = {
        'Banners': Banner,
        'ImageSidebarLefts': ImageSidebarLeft,
        'ImageSidebarRights': ImageSidebarRight,
        'Footers': Footer,
        'SlideShows': SlideShow,
        'UseExcludes': UseExclude,
        'UseOrderbys': UseOrderBy,
        'UseFirsts': UseFirst,
        'UseLasts': UseLast,
        'UseCounts': UseCount,
        'UseExistss': UseExists,
}
    return render(request,'accounts/layout.html', context)

def ListCategory(request):
    TblCategory = Category.objects.all()
    TblCustomer = Customer.objects.all()
    context = {
        'categorys' :TblCategory,
        'customers' : TblCustomer,
    }
    return render(request, 'accounts/ListCategory.html', context)