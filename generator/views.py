from django.shortcuts import render
from django.http import HttpResponse

import random
import string


def generator_pass(n=8, upper="on", numbers="on", special="on"):
    """
    Функция генерации пароля
    :param n: get.length = str (длина пароля)
    :param upper: get.uppercase = "on" or None (использовать заглавные буквы)
    :param numbers: get.numbers = "on" or None (использовать числа)
    :param special: get.special = "on" or None (использовать символы)
    :return: password
    """
    txt = string.ascii_lowercase
    if upper is not None:
        txt += string.ascii_uppercase
    if numbers is not None:
        txt += string.digits
    if special is not None:
        txt += string.punctuation
    output = ""
    for i in range(int(n)):
        output += random.choice(txt)
    return output


def home(request):
    text_home_1 = "ГЕНЕРАЦИЯ ПАРОЛЯ"
    text_home_2 = "Выберите допустимые символы и длину пароля. После нажмите сгенерировать пароль"
    return render(request, 'generator/home.html', {"text_home_1": text_home_1,
                                                   "text_home_2": text_home_2
                                                   }
                  )


def password(request):
    length = request.GET.get("length", default=8)
    check_upp = request.GET.get("uppercase")
    check_num = request.GET.get("numbers")
    check_special = request.GET.get("special")
    text_test = check_special
    password = generator_pass(n=length, upper=check_upp, numbers=check_num, special=check_special)
    return render(request, "generator/password.html", {"password": password,
                                                       "text_test": text_test
                                                       }
                  )


def info(request):
    text_1 = "Информация"
    text_2 = "доп информация"
    return render(request=request,
                  template_name="generator/info.html",
                  context={"text_1": text_1,
                           "text_2": text_2
                           }
                  )
