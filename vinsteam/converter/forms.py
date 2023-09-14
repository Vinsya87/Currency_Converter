from django import forms


class CurrencyConversionForm(forms.Form):
    amount = forms.DecimalField(label='Amount', min_value=0)
    to = forms.ChoiceField(label='To Currency', choices=[('RUB', 'RUB'), ('EUR', 'EUR'), ('GBP', 'GBP')])  # Пример валют
