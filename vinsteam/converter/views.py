from rest_framework.views import APIView
from rest_framework.response import Response
from django.shortcuts import render
from django.conf import settings

from .utils import get_exchange_rate
from .forms import CurrencyConversionForm


class CurrencyRateView(APIView):
    def get(self, request):
        api_key = settings.API_KEY
        from_currency = request.GET.get('from')
        to_currency = request.GET.get('to')
        amount = float(request.GET.get('amount', 0))

        rate = get_exchange_rate(api_key, from_currency, to_currency, amount)
        if rate is not None:
            return Response({'result': rate})
        else:
            return Response(
                {'error': 'Currency conversion not available'}, status=400)

    def post(self, request):
        api_key = settings.API_KEY
        form = CurrencyConversionForm(request.data)
        if form.is_valid():
            to_currency = form.cleaned_data['to']
            amount = form.cleaned_data['amount']
            # Устанавливаем жестко базовую валюту в USD
            from_currency = 'USD'
            rate = get_exchange_rate(
                api_key, from_currency, to_currency, amount)
            if rate is not None:
                return Response({'result': rate})
        # Обработка ошибок формы или конвертации
        return Response(
            {'error': 'Currency conversion not available'}, status=400)


def index(request):
    form = CurrencyConversionForm(request.POST)
    context = {
        'form': form
        }
    return render(request, 'index.html', context)
