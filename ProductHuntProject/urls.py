from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from products.views import homepage

urlpatterns = [
    path('admin/', admin.site.urls),
    path('products/', include('products.urls')),
    path('accounts/', include('accounts.urls')),
    path('', homepage, name='homepage')
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
