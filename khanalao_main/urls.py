"""
URL configuration for khanalao_main project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from marketplace import views as MarketPlaceViews


from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),
    path('', include('accounts.urls')),
    path('marketplace/', include('marketplace.urls')),
    path('cart/', MarketPlaceViews.cart, name='cart'),
    path('checkout/', MarketPlaceViews.checkout, name='checkout'),
    path('process-payment/', MarketPlaceViews.process_payment, name='process_payment'),
    # path('payment-success/', Mpayment_success, name='payment_success'),
    path('orders/', include('orders.urls')),




] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
