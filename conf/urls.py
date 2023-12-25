from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path

from conf import settings
from pages.views import home_page, reservation_view, Foods_image

urlpatterns = [
    path('admin/', admin.site.urls),
    path('reservation/', reservation_view, name='reservation_view'),
    path('', Foods_image, name='home')
]

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

