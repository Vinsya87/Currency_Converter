from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from converter.views import CurrencyRateView, index


app_name = 'converter'

urlpatterns = [
    path('', index, name='index'),
    path('api/rates', CurrencyRateView.as_view(), name='currency-rate'),
]
if settings.DEBUG:
    urlpatterns += static(
        settings.STATIC_URL, document_root=settings.STATIC_ROOT)
