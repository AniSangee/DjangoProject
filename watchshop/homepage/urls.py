from django.contrib import admin
from django.urls import path
from .views import Home, About, upload, Login, Signup, Logout, ShowProduct,addtowish,show_wishlist,removewish,addtocart,show_cart,removeCart,showdata
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('', Home, name="home"),
    path('about', About, name="about"),
    path('upload', upload,name='upload'),
    path('login', Login, name='login'),
    path('signup', Signup, name='signup'),
    path('logout', Logout,name='logout'),
    path('product/<int:id>', ShowProduct,name='product'),
    path('addtowish/<int:id>', addtowish, name ='addtowish'),
    path('addtocart/<int:id>', addtocart, name ='addtocart'),
    path('wishlist', show_wishlist, name = "showlist"),
    path('removewish/<int:id>', removewish, name = 'removewish'),
    path('showcart', show_cart, name = 'showcart'),
    path('removeCart/<int:id>', removeCart, name = 'removeCart'),
    path('dummy', showdata, name = 'dummy')
]

urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)