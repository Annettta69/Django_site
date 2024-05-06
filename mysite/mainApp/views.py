from django.shortcuts import render


def index(request):
    return render(request, 'mainApp/homePage.html') #ссылка на главную страницу

def contact(request):
    return render(request, 'mainApp/basic.html', {'values':['Если у вас остались вопросы, то задавайте их по телефону:', '8-960-960-00-00', 'example@mail.ru']})