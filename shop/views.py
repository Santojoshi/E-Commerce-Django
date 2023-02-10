from django.http import HttpResponse
from django.shortcuts import render, redirect
from contact.models import cont
from app1.models import card, cart, Customer, order
from.forms import register, profileForm    # Importing registration form and model form for profile
from django.contrib import messages # Importing messages
from django.contrib.auth.decorators import login_required


def home(request):
    deal = card.objects.filter(card_category='Deal')
    excl = card.objects.filter(card_subcategory='exc')
    print(excl)
    return render(request,'front.html',{'deal':deal, 'exc': excl})
def about(request):
    return render(request,'about.html')
def contact(request):
    dict = {}
    try:
        if request.method == 'POST':
            name = request.POST.get('name')
            email = request.POST.get('email')
            phone = request.POST.get('phone')
            comment = request.POST.get('comment')
            temp = cont(name=name, email=email, phone=phone, comment=comment)
            temp.save()
            return redirect('/conthank')
    except Exception as e:
        dict = {'error' : 'Kindly Fill All the Fields Correctly'}
    return render(request,'contact.html', dict)

def conthank(request):
    return render(request, 'ConThank.html')

def product(request,id):
    detail = card.objects.get(id=id)
    return render(request, 'product.html', {'detail': detail})

def category(request,data):
    if data == 'Mobiles':
        cont = card.objects.filter(card_category=data)
    elif data == 'Electronics':
        cont = card.objects.filter(card_category=data)
    elif data == 'PowerBanks':
        cont = card.objects.filter(card_category=data)
    elif data == 'Clothings':
        cont = card.objects.filter(card_category=data)
    elif data == 'HomeDecorators':
        cont = card.objects.filter(card_category=data)
    return render(request, 'category.html', {'cont': cont})

def registeruser(request):
    if request.method == 'POST':
        form = register(request.POST)
        if form.is_valid():
            messages.success(request, 'Hurray! You are registered Successfully| Login to Continue Shoping')
            form.save()
    else:
        form = register()
    return render(request, 'register.html',{'form':form})
    
@login_required
def profile(request):
    if request.method == 'POST':
        prof = profileForm(request.POST)
        if prof.is_valid():
            messages.success(request, 'Your Profile Created successfullty')
            profile = prof.save(commit=False)
            profile.user = request.user
            profile.save()
    prof= profileForm()
    cus = Customer.objects.filter(user = request.user)
    return render(request, 'profile.html', {'prof':prof, 'cus': cus})

@login_required
def addcart(request):
    
    user = request.user
    prodid= request.GET.get('prodid')
    cartproduct = card.objects.get(id=prodid)
    cart(user=user, product=cartproduct).save()
    return redirect('/cart')

@login_required
def cartDetail(request):
    val = 0
    cartval = 0
    if request.user.is_authenticated:
        user = request.user
        carts = cart.objects.filter(user=user)
        if request.user:
            car= cart.objects.filter(user=request.user)
            for i in car:
                mul= i.product.card_price * i.quantity
                val = val + mul
                cartval += 1
    if val != 0:
        delivery = 60
        total = delivery+val  
          
    else:
        delivery = 0
        total = 0    
        cartval = 0
    cus = Customer.objects.filter(user = request.user)
    return render(request, 'cart.html', {'carts': carts, 'mul': val, 'total': total, 'del': delivery, 'cartval':cartval, 'cus': cus})

def remove(request, id):
    if request.method == 'POST':
        rem = cart.objects.get(id=id)
        rem.delete()
        return redirect('/cart/')

def reduce1(request,id):
    if request.method == 'POST':
        red = cart.objects.get(id=id)
        if red.quantity > 1:
            red.quantity -= 1
            red.save()
            return redirect('/cart/')
        else:
            return redirect('/cart/')
            

def add1(request,id):
    if request.method == 'POST':
        add = cart.objects.get(id=id)
        add.quantity += 1
        add.save()

        print(add)
        return redirect('/cart/')  
    
@login_required   
def congo(request):
    try:
        custid = request.GET.get('cusid')
        print(custid)
        Cust = Customer.objects.get(id=custid)
    except:
        cust = Customer.objects.filter(user=request.user)
        Cust = cust[0]
    carts = cart.objects.filter(user=request.user)
    for i in carts:
        order(user=request.user, cart = i.product, quantity = i.quantity, customer = Cust ).save()
        carts.delete()
        return redirect('/congrat/')  
    return render(request, 'cart.html')    

# def checkout(request):
#     cus = Customer.objects.filter(user=request.user)
#     custm = request.GET.get('cust')
#     print(custm)
#     return render(request, 'checkout.html',{'cus':cus})

@login_required
def orders(request):
    ord = order.objects.filter(user=request.user)
    return render(request, 'orders.html',{'ord': ord}) 

def congrat(request):
    return render(request, 'congratulations.html')

def search(request):
    st = request.GET.get('search')
    if st != None:
        serdata = card.objects.filter(card_item__icontains=st) or card.objects.filter(card_category__icontains=st)
    else:
        pass
    return render(request, 'search.html',{'cont':serdata})