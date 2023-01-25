from django.urls import path
from app8 import views


urlpatterns = [
    path('',views.myntra, name="home"),
    path('about/',views.about, name="about"),
    path('contact/',views.contact, name="contact"),
    path('history/',views.history, name="history"),
    path('men/',views.men, name="men"),
    path('women/',views.women, name="women"),

    path('signin/',views.signin),
    path('signin_insert/',views.signin_insert),
    path('admin1/',views.admin1),
    path('customer/',views.cust),

    path('signup/',views.signup),
    path('signup_insert/',views.signup_insert),

    # path('product_details/',views.product_details),
    # path('product_insert/',views.product_insert),
    # path('view_product/',views.view_product),
    # path('update_product/<int:id>',views.update_product),
    # path('update_product_insert/<int:id>',views.update_product_insert),
    # path('delete_product/<int:id>',views.delete_product),

    path('seller/',views.se_ller),
    path('seller_details/',views.seller_details),
    path('seller_insert/',views.seller_insert),
    path('seller_view/',views.seller_view),
    path('seller_update/<int:id>',views.seller_update),
    path('seller_update_insert/<int:id>',views.seller_update_insert),
    path('seller_delete/<int:id>',views.seller_delete),

    path('products/<int:id>',views.prod),
    path('products/<int:id>',views.prod_women),
    # path('order/<int:id>',views.order),
    path('orders/<int:id>',views.orders),
    path('bill_order/',views.bill_order),
    # path('order_insert/',views.order_insert),

    path('cart/',views.cart),
    path('review/<int:id>',views.rev),
    path('review_insert/<int:id>',views.review_insert),
    # path('myorders/',views.myorders),

    path('seller_login/',views.seller_login),
    path('complaints/',views.comp),
    path('complaints_insert/',views.comp_insert),
    path('s_complaints/',views.s_comp),
    


    path('products_view/',views.products_view),
    path('seller_reviews/',views.s_rev),
    # path('approve/',views.appr),
    # path('approval/<int:id>',views.approv),
    
    

    

    

    
]

