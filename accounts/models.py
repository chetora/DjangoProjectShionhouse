from django.db import models

# Create your models here.

class Customer(models.Model):    
    name = models.CharField(max_length=200, null=True) 
    phone = models.CharField(max_length=200, null=True)    
    email = models.CharField(max_length=200, null=True) 
    date_created = models.DateTimeField(auto_now_add=True, null=True) 
    def str(self):         
        return f'{self.name} {self.phone} {self.email}'

class Category(models.Model):
    CategoryName = models.CharField(max_length=50 , null=True)
    CategoryDate = models.DateTimeField(auto_now_add=True, null=True)
    def str(self):
        return f'{self.CategoryName} {self.CategoryDate}'

class Supplier(models.Model):    
    companyName = models.CharField(max_length=200, null=True) 
    phone = models.CharField(max_length=200, null=True)    
    email = models.CharField(max_length=200, null=True) 
    date_created = models.DateTimeField(auto_now_add=True, null=True) 
    def str(self):         
        return f'{self.companyName} {self.phone} {self.email} {self.date_created}'
    
class tblProducts(models.Model):
    productName = models.CharField(max_length=200, null=True)
    categoryID = models.ForeignKey(Category, on_delete=models.CASCADE, null=True)
    supplierID = models.ForeignKey(Supplier, on_delete=models.CASCADE, null=True)
    quantity = models.CharField(max_length=200, null=True)
    priceIn = models.CharField(max_length=200, null=True)
    priceOut = models.CharField(max_length=200, null=True)
    instock = models.CharField(max_length=200, null=True)
    productImage = models.ImageField(upload_to='productImages/',null=True,blank=True)
    productDate = models.DateTimeField(auto_now_add=True, null=True)
    def str(self):
        return f'{self.productName} {self.priceOut}'
    
class ImageType(models.Model): 
    ImageTypeName = models.CharField(max_length=200, null=True) 
    ImageTypeDate = models.DateTimeField(auto_now_add=True, null=True) 
    def __str__(self):          
        return f'{self.id} {self.ImageTypeName}'

class Image(models.Model): 
    ImageName = models.CharField(max_length=200, null=True) 
    ImageURL = models.ImageField(upload_to='images/',null=True,blank=True) 
    ImageLink = models.CharField(max_length=200, null=True) 
    ImageTypeID = models.ForeignKey(ImageType, on_delete=models.CASCADE, null=True) 
    Active = models.CharField(max_length=200, null=True) 
    ImageDate = models.DateTimeField(auto_now_add=True, null=True) 
    def __str__(self):          
        return f'{self.ImageName}'
    




