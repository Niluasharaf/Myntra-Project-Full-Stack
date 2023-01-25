from django.db import models

# Create your models here.

class login(models.Model):
    username=models.CharField(max_length=10)
    password=models.CharField(max_length=10)
    category_1=models.CharField(max_length=10)
  


class customer(models.Model):
    customer_name=models.CharField(max_length=10)
    customer_address=models.CharField(max_length=10, default='default value')
    customer_phone=models.CharField(max_length=10)
    customer_place=models.CharField(max_length=10)



class seller(models.Model):
    seller_name=models.CharField(max_length=10)
    seller_id=models.CharField(max_length=10)
    seller_age=models.IntegerField()
    seller_exp=models.IntegerField()
    seller_salary=models.IntegerField()



class product(models.Model):
    product_name=models.CharField(max_length=10)
    product_quantity=models.IntegerField()
    product_price=models.CharField(max_length=10)
    product_offer=models.CharField(max_length=10)
    image=models.ImageField()

    def _str_(self):
         return self.product_name
        

class product_women(models.Model):
    product_name=models.CharField(max_length=10)
    product_quantity=models.IntegerField()
    product_price=models.CharField(max_length=10)
    product_offer=models.CharField(max_length=10)
    image=models.ImageField()

    def _str_(self):
         return self.product_name
       


class order(models.Model):
    order_name=models.CharField(max_length=10)
    order_address=models.CharField(max_length=10)
    order_phone=models.CharField(max_length=10)
    product_name=models.CharField(max_length=10)
    product_price=models.CharField(max_length=10)
    status_1=models.CharField(max_length=10)
    

class order1(models.Model):
    customer_name=models.ForeignKey(customer,on_delete=models.CASCADE,default='default value')
    product_name=models.ForeignKey(product,on_delete=models.CASCADE)
    status=models.CharField(max_length=10)


class bill(models.Model):
    iname=models.CharField(max_length=20)
    iprice=models.IntegerField()
    quantity=models.IntegerField()
    total=models.IntegerField()
    

# class myorder(models.Model):
#     customer_name=models.ForeignKey(customer,on_delete=models.CASCADE)
#     product_name=models.ForeignKey(product,on_delete=models.CASCADE)
#     status=models.ForeignKey(order1,on_delete=models.CASCADE)
    



class complaints(models.Model):
    sellername=models.CharField(max_length=10)
    complaint=models.CharField(max_length=20)
    date=models.DateField()




class reviews(models.Model):
    comment=models.CharField(max_length=20)
    uname=models.CharField(max_length=20)

class reviews1(models.Model):
    comment=models.CharField(max_length=20)
    uname=models.CharField(max_length=20)










