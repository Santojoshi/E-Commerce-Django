from django.contrib import admin
from django.urls import path, include
from shop import views
from django.conf import settings             # to upload media images in DB
from django.conf.urls.static import static   # to upload media images in DB
from django.contrib.auth import views as auth_views # For login(inbuilt validator)
from .forms import LoginForm # for login



urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home),
    path('about/', views.about),
    path('contact/', views.contact),
    path('conthank/', views.conthank),
    path('product/<int:id>', views.product, name='product'),
    path('category/<slug:data>', views.category, name='category'),
    path('accounts/login/', auth_views.LoginView.as_view(template_name='login.html', authentication_form = LoginForm), name='login'),
    path('logout/', auth_views.LogoutView.as_view(next_page='login'), name='logout'),
    path('register/', views.registeruser, name='register'),
    path('profile/', views.profile, name='profile'),
    path('add_cart/', views.addcart, name='addcart'),
    path('cart/', views.cartDetail, name='cart'),
    path('remove/<slug:id>/', views.remove, name='remove'),
    path('reduce/<slug:id>/', views.reduce1, name='reduce'),
    path('add/<slug:id>/', views.add1, name='add'),
    path('orders/', views.orders, name='orders'),
    path('congo/', views.congo, name='congo'),
    # path('checkout/', views.checkout, name='checkout'),
    path('congrat/', views.congrat, name='congrat'),
    path('search/', views.search, name='search'),
    path('app1/', include('app1.urls')),
    
]


if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT) 
    urlpatterns+= static(settings.MEDIA_URL, document_root= settings.MEDIA_ROOT)