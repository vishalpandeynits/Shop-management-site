from django.db import models
from django.contrib.auth.models import User
from django.core.validators import RegexValidator
from datetime import datetime
# Create your models here.

class Shop(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    shop_name = models.CharField(max_length=300,null=True)
    telephone_number =  models.CharField(max_length=10,validators=[RegexValidator(r'\d{1,10}$')],null=True)
    shop_type = models.CharField(null=True,max_length=30)
    GST_IN = models.CharField(null=True,max_length=200)
    bank_account_no = models.IntegerField(null= True,)
    IFSC_CODE = models.CharField(null=True,max_length=20)
    shop_owner_name = models.CharField(null=True,max_length=300)
    shop_owner_mobile = models.CharField(max_length=10,validators=[RegexValidator(r'\d{1,10}$')])
    address = models.CharField(null=True,max_length=300)
    city = models.CharField(null=True,max_length=200)
    state = models.CharField(null=True,max_length=200)
    
    def __str__(self):
        return self.shop_name

class Employee(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    photo = models.ImageField(upload_to="employee",null=True,blank=True)
    employee_name= models.CharField(max_length=200)
    employee_position = models.CharField(max_length=200)
    phone_number = models.CharField(max_length=10,validators=[RegexValidator(r'\d{1,10}$')])
    salary_per_month = models.IntegerField()
    bank_account_no = models.IntegerField(null=True)
    email =models.EmailField(null=True)
    IFSC_CODE = models.CharField(max_length=20,null=True)
    last_updated = models.DateTimeField(default=datetime.now())
    full_address = models.CharField(max_length=300,null=True)
    date_joined = models.DateTimeField(default=datetime.now())
    def __str__(self):
        return self.employee_name

class ItemField(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    item_name = models.CharField(max_length=200)
    item_price = models.IntegerField()
    item_category = models.CharField(max_length=200)
    item_description = models.CharField(max_length=1000)
    item_image = models.ImageField(upload_to="media/items",blank=True)
    class Meta:
        abstract = True

class Item(ItemField):
	stock = models.IntegerField()
	def __str__(self):
		return self.item_name


class IssueItem(ItemField):
    quantity = models.IntegerField()
    def __str__(self):
        return self.item_name

class Note(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    image = models.ImageField(upload_to="notes/",blank=True)
    created_on = models.DateTimeField(default=datetime.now())
    content= models.TextField(max_length=5000)

    def __str__(self):
        return self.title



    