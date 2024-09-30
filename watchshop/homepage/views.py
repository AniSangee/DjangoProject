from django.shortcuts import render,redirect
from .models import Watches,WatchUpload, Wishlist,Cart,CartItem
# Create your views here.
def Home(request):
    watches= WatchUpload.objects.all()
    # watche= Watches.objects.all()
    context= {'watch': watches}
    # context1 ={'watch':watche}
    return render(request,'home.html',context)

def About(request):
    return render(request, 'about.html')

from .forms import uploadform
from django.contrib.auth.decorators import login_required

@login_required(login_url="/login")
def upload(request):
    if request.method == 'POST':
        form = uploadform(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = uploadform()
    return render(request,'watchUpload.html',{'form':form})

# loginpage
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth import authenticate, login, logout

def Login(request):
    if request.method == 'POST':
        form= AuthenticationForm(request,data=request.POST)
        print(form.is_valid())
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')

            user =authenticate(username = username, password = password) 
            if user is not None:
                login(request,user)
                return redirect('home')
            else:
                return render(request,'login.html',{'form':form})
    else:
        form=AuthenticationForm()
    
    return render(request,'login.html',{'form':form})

# signup
def Signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
         form = UserCreationForm()
    return render(request,'signup.html',{'form':form})

def Logout(request):
    logout(request)
    return redirect('home')

from django.shortcuts import get_object_or_404
def ShowProduct(request, id):
    products = get_object_or_404(WatchUpload, id=id)
    return render(request,'product.html',{'product':products})

#Wishlist
def addtowish(request, id):
    user = request.user
    product = WatchUpload.objects.get(id=id)
    obj1, created  = Wishlist.objects.get_or_create(user=user)
    obj1.products.add(product)
    obj1.save()
    return redirect('home')

def show_wishlist(request):
    user = request.user
    wish_object = Wishlist.objects.get(user=user)
    return render(request, "wishlist.html", {"user_products": wish_object.products.all()})

def removewish(request, id):
    product_rm = WatchUpload.objects.get(id=id)
    wish_obj = Wishlist.objects.get(user=request.user)
    wish_obj.products.remove(product_rm)
    return render(request, 'wishlist.html', {"user_products": wish_obj.products.all()})
# Cart
def addtocart(request, id):
    #check if user has cart or not
    user_cart, created = Cart.objects.get_or_create(user = request.user)

    #fetch the product with given id
    product = WatchUpload.objects.get(id=id)

    #create a cart item using the product and user
    cart_item, created = CartItem.objects.get_or_create(user = user_cart, product= product )
    cart_item.product= product
    cart_item.save()

    return redirect('home')

def show_cart(request):
    user_cart, created = Cart.objects.get_or_create(user = request.user)
    cart_objects = user_cart.cartitem_set.all()
    return render(request, "cart.html", {"user_products": cart_objects})

def removeCart(request, id):
    product_rm = WatchUpload.objects.get(id=id)
    cart_obj = Cart.objects.get(user=request.user)
    cart_obj.products.remove(product_rm)
    return render(request, 'cart.html', {"user_products": cart_obj.products.all()})
    
from django.http import JsonResponse
def showdata(request):
    start_text = request.GET.get('param1')
    watches = list(WatchUpload.objects.filter(name__startswith=start_text).values_list())

    message = {
               'name': 'Hello Jitin',
               'watches': watches
               }
    

    return JsonResponse(message)