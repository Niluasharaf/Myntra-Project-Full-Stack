from django.shortcuts import render,redirect
from app8.models import login,customer,seller,product,order1,reviews1,complaints,product_women,bill
from django.http import HttpResponse
from django.core.files.storage import FileSystemStorage
from datetime import datetime,date

# Create your views here.
def myntra(request):
    return render(request,"myntra.html")

def about(request):
    return render(request,"myn_about.html")

def contact(request):
    return render(request,"myn_contact.html")

def history(request):
    return render(request,"myn_history.html")

def men(request):
    ob=product.objects.all()
    return render(request,"myn_men.html",{'ob1':ob})

def women(request):
    ob=product_women.objects.all()
    return render(request,"myn_women.html",{'ob1':ob})

def signin(request):
    return render(request,"signin.html")

def signin_insert(request):
    if request.method=="POST":
        obj=login.objects.all()
        u_name=request.POST.get('username')
        pwd=request.POST.get('password')
        flag=0
        for i in obj:
            if u_name ==i.username and pwd==i.password:
                category=i.category_1
                flag=1
                request.session['username']=u_name
                if category =="admin":
                    return redirect("/admin1")
                elif category =="customer":
                    return redirect("/")
                elif category =="seller":
                    return redirect("/seller")

                else:
                    return HttpResponse("invalid")
        if flag ==0:
            return HttpResponse("user does not exist")



def admin1(request):
    return render(request,"admin1.html")

def cust(request):
    return render(request,"customer.html")

def signup(request):
    return render(request,"signup.html")

def signup_insert(request):
    if request.method=="POST":
        tb=customer()
        tb.customer_name=request.POST.get("customer_name")
        tb.customer_address=request.POST.get("customer_address")
        tb.customer_phone=request.POST.get("customer_phone")
        tb.customer_place=request.POST.get("customer_place")
        tb.save()

        lg=login()
        lg.username=request.POST.get("customer_name")
        lg.password=request.POST.get("customer_phone")
        lg.category_1="customer"
        lg.save()
        return redirect("/signin")


def se_ller(request):
    return render(request,"seller.html")


def seller_details(request):
    return render(request,"seller_details.html")

def seller_insert(request):
    if request.method=="POST":
        tb=seller()
        tb.seller_name=request.POST.get("seller_name")
        tb.seller_id=request.POST.get("seller_id")
        tb.seller_age=request.POST.get("seller_age")
        tb.seller_exp=request.POST.get("seller_exp")
        tb.seller_salary=request.POST.get("seller_salary")
        tb.save()

        lg=login()
        lg.username=request.POST.get("seller_name")
        lg.password=request.POST.get("seller_id")
        lg.category_1="seller"
        lg.save()
        return redirect("/admin1")



def seller_view(request):
    ob=seller.objects.all()
    return render(request,"seller_view.html",{'ob1':ob}) 


def seller_update(request,id):
    ob=seller.objects.get(id=id)
    return render(request,"seller_update.html",{'ob1':ob})


def seller_update_insert(request,id):
    if request.method=="POST":
        tb=seller.objects.get(id=id)
        tb.seller_name=request.POST.get("seller_name")
        tb.seller_id=request.POST.get("seller_id")
        tb.seller_age=request.POST.get("seller_age")
        tb.seller_exp=request.POST.get("seller_exp")
        tb.seller_salary=request.POST.get("seller_salary")
        tb.save()
        return redirect("/seller_view")

def seller_delete(request,id):
    ob=seller.objects.get(id=id)
    ob.delete()
    return redirect("/seller_view")

def prod(request,id):
    ob=product.objects.get(id=id)
    return render(request,"product.html",{'ob1':ob})


def prod_women(request,id):
    ob=product_women.objects.get(id=id)
    return render(request,"product.html",{'ob1':ob})



# def order_insert(request,id):
#     if request.method=="POST":
#         ab=order1()
#         ab=product.objects.get(id=id)
#         ab.order_name=request.POST.get("order_name")
#         ab.order_address=request.POST.get("order_address")
#         ab.order_phone=request.POST.get("order_phone")

#         ab.product_name=request.POST.get("product_name")
#         ab.product_price=request.POST.get("product_price")
#         ab.status="pending"
#         ab.save()
#         return redirect("/")


def cart(request):
    ob=bill.objects.all()
    return render(request,"cart.html",{'ob1':ob})


# def myorders(request):
#     v=request.session['username']
#     insta=customer.objects.get(customer_name=v)
#     ob=order1.objects.filter(customer_name=insta)
    
#     return render(request,"myorders_view.html",{'ob1':ob})


# def order(request,id):
#     v=request.session['username']
#     ob=customer.objects.get(customer_name=v)
#     # ob=order1.objects.filter(customer_name=insta)

#     pd=product.objects.get(id=id)
    
#     return render(request,"order_shipping.html",{'ob1':ob,'pd1':pd})


#new order for bill with quantity
def orders(request,id):
    ob=product.objects.filter(id=id)
    return render(request,"orders.html",{'ob1':ob})


def bill_order(request):
    if request.method=="POST":
        iname=request.POST.get("iname")
        iprice=request.POST.get("iprice")
        quantity=request.POST.get("quantity")
        total=int(iprice)*int(quantity)
        # amount=bill(iname=iname,iprice=iprice,quantity=quantity,total=total)
        # amount.save()
        ob=bill()
        ob.iname=iname
        ob.iprice=iprice
        ob.quantity=quantity
        ob.total=total
        ob.save()
        return render(request,'bill.html',{'iname':iname,'total':total})




def rev(request,id):
    ob=bill.objects.get(id=id)
    return render(request,"reviews.html",{'ob1':ob}) 

def review_insert(request,id):
    if request.method=="POST":
        tb=reviews1()
        rb=bill.objects.get(id=id)
        
        tb.comment=request.POST.get("comment")
        tb.uname=rb.iname
        tb.save()
        return render(request,"confirmation.html")


def seller_login(request):
    return render(request,"seller.html")


def comp(request):
    return render(request,"complaints.html")


def s_comp(request):
    ob=complaints.objects.all()
    return render(request,"s_complaints.html",{'ob1':ob})

def products_view(request):
    ob=product.objects.all()
    return render(request,"products_view.html",{'ob1':ob})



def comp_insert(request):
    if request.method=="POST":
        tb=complaints()
        current_user=request.user
        user_id=current_user.id
        
        
        tb.sellername="seller"
        tb.complaint=request.POST.get("complaint")
        tb.date=request.POST.get("date")
        tb.save()
        return redirect("/seller_login")

def s_rev(request):
    ob=reviews1.objects.all()
    return render(request,"seller_reviews.html",{'ob1':ob})

# def appr(request):
#     ob=order1.objects.all()
#     return render(request,"approve.html",{'ob1':ob})

# def approv(request,id):

#     ob=order1.objects.get(id=id)
#     ob.status="to be deliver!"
#     ob.save()
#     return redirect("/approve") 









    
    
    
