from django.urls import path
from embeddedsite import views
app_name = 'embeddedsite'
urlpatterns = [    
    path('',views.home, name='home'),
    path('products/',views.products, name='products'),
    path('login/', views.user_login, name='login'),
    path('signup/', views.sign_up, name='signup'),
    path('tutorials/', views.tutorials, name='tutorials'),
    path('product/<int:product_id>/', views.product, name='product'),
    path('tutorials/<int:tutorial_id>/',views.tutorial, name='tutorial'),
    path('cart/<int:product_id>/', views.add_to_cart, name='cart'),
    path('showcart/', views.show_cart, name='show_cart'),
    path('removefromcart/<int:product_id>/', views.remove_from_cart, name='remove_from_cart'),
    path('comment/<int:tutorial_id>/', views.handle_comment_submission, name='comment_submission'),
    path('services/', views.services, name='services'),
    path('aboutus/', views.about_us, name='aboutus'),
    path('enquiry/', views.enquiry, name='enquiry'),
    path('circuits/', views.circuits, name='circuits'),
    path('projects/', views.projects, name='projects'),
    path('searchproducts/', views.search_products, name='search'),
    path('searchtutorials/', views.search_tutorials, name='searchtutorials'),
    path('searchprojects/', views.search_projects, name='searchprojects'),
    path('searchservices/', views.search_services, name='searchservices'),
    path('searchcircuits/', views.search_circuits, name='searchcircuits'),
    path('username/', views.check_username, name='username'),
    path('email/', views.check_email, name='email'),
    path('signupsuccess/', views.signup_success, name='signup_success'),
]
