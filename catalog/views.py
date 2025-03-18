from django.http import HttpResponse
from django.shortcuts import render


def home(request):
    return render(request, 'catalog/home.html')


#def contacts(request):
#    return render(request, 'catalog/contacts.html')

def contacts(request):
    if request.method == 'POST':
        # Получение данных из формы
        name = request.POST.get('name')
        phone = request.POST.get('phone')
        message = request.POST.get('message')
        # Обработка данных (например, сохранение в БД, отправка email и т. д.)
        print(name)
        print(phone)
        print(message)
        # Здесь мы просто возвращаем простой ответ
        return HttpResponse(f"Спасибо, {name}! Ваше сообщение получено. Уже набираем Ваш номер!")
    return render(request, 'catalog/contacts.html')
