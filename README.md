# Currency_Converter
использовал сервис
https://apilayer.com/marketplace/exchangerates_data-api

нужно зарегистрироваться и в ЛК получить Api ключ и выполнить бесплатную подписку на exchangerates_data

после нужно в файл .env указать этот ключ


после нужно запустить докер sudo docker-compose up -d --build

либо 
python3 -m venv venv && . venv/bin/activate && python -m pip install --upgrade pip && python -m pip install -r requirements.txt && cd vinsteam && python3 manage.py runserver


что в том, что в другом случае проект будет доступен по адресу 
http://localhost:8000/

пример запроса на апи 
http://localhost:8000/api/rates?to=RUB&from=USD&amount=10

http://localhost:8000/swagger/ установлен но не описана документация
