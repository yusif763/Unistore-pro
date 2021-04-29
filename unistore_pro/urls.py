"""unistore_pro URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
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
from django.urls import path,include
from django.conf import settings
from django.conf.urls.static import static
from django.conf.urls.i18n import i18n_patterns


urlpatterns = [
    path('jet/', include('jet.urls', 'jet')),  # Django JET URLS
    path('jet/dashboard/', include('jet.dashboard.urls', 'jet-dashboard')),  # Django JET dashboard URLS
    path('social-auth/', include('social_django.urls', namespace='social')),
    path('account/', include('account.urls', namespace='account')),
    path('^i18n/', include('django.conf.urls.i18n')),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)



urlpatterns += i18n_patterns(
    path('admin/', admin.site.urls),
    path('', include("common.urls", namespace= 'common')),
    path('contact/', include("contact.urls", namespace= 'contact')),
    path('favorites/', include("favorites.urls", namespace= 'favorites')),
    path('product/', include("product.urls", namespace= 'product')),
    path('checkout/', include('checkout.urls', namespace='checkout')),
    path('api/', include('product.api.urls' , namespace= 'productapis')),
    path('check-api/', include('checkout.api.urls' , namespace = 'checkapis')),
    path('api/auth/',include('account.api.urls', namespace='account-api'))

)