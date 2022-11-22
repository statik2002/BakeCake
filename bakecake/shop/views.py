from django.shortcuts import render


# Вью главной страницы
def index(request):

    if request.method == 'GET':

        if 'REG' in request.GET:
            print('Регистрация')
            print(f'Телефон = {request.GET.get("REG")}')

        elif 'LEVELS' in request.GET:
            print('Создана заявка')
            print(f'Levels = {request.GET.get("LEVELS")}')
            print(f'Form = {request.GET.get("FORM")}')
            print(f'Topping = {request.GET.get("TOPPING")}')
            print(f'Berries = {request.GET.get("BERRIES")}')
            print(f'Decor = {request.GET.get("DECOR")}')
            print(f'Words = {request.GET.get("WORDS")}')
            print(f'Comments = {request.GET.get("COMMENTS")}')
            print(f'Name = {request.GET.get("NAME")}')
            print(f'Phone = {request.GET.get("PHONE")}')
            print(f'Email = {request.GET.get("EMAIL")}')
            print(f'Address = {request.GET.get("ADDRESS")}')
            print(f'Date = {request.GET.get("DATE")}')
            print(f'Time = {request.GET.get("TIME")}')
            print(f'Deliv comment = {request.GET.get("DELIVCOMMENTS")}')

        context = {

        }

        return render(request, 'shop/index.html', context)

    else:

        context = {

        }

        return render(request, 'shop/index.html', context)


# Вью каталога тортиков
def show_catalog(request):

    context = {

    }

    return render(request, 'shop/show_catalog.html', context)


# Вью корзины
def show_cart(request):

    context = {

    }

    return render(request, 'shop/show_cart.html', context)


# Вью личного кабинета сладкоежки
def show_cabinet(request):

    context = {

    }

    return render(request, 'shop/show_cabinet.html', context)
