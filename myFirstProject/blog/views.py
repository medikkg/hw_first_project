from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    html_code = f"<h1> Главна страница для домашней работы</h1>"\
                f"<p>Тестовое сообщения</p>"\
                f"<p><a href='index/about'>О компании</a></p>"\
                f"<p><a href='index/articles'>СТАТЬИ</a></p>"\
                f"<p><a href='index/currencies'> Курс Валют</a></p>"

    return HttpResponse(html_code)


def about(request):
    html_code = f"<h1> О компании</h1>"\
                f"<p>Lorem Ipsum является текст-заполнитель обычно используется в " \
                f"графических, печать и издательской индустрии для предварительного " \
                f"просмотра макета и визуальных макетах.</p>"

    return HttpResponse(html_code)


def articles(request):
    html_code = f"<h1> СТАТЬИ</h1>"\
                f"<p>Lorem Ipsum является текст-заполнитель обычно используется в " \
                f"графических, печать и издательской индустрии для предварительного " \
                f"просмотра макета и визуальных макетах.</p>"

    return HttpResponse(html_code)

def currencies(request):
    html_code = f"<h1> Курсы валют</h1>"\
                f"<p>все курсы валют.</p>"\
        f"<table border='1'> " \
                f"<thead>" \
                f"<tr>" \
                f"<th>Валюта</th>" \
                f"<th>Курс</th>" \
                f"</tr>" \
                f"</thead>" \
                f"<tbody>" \
                f"<tr>" \
                f"<td>Сом</td>" \
                f"<td>1.6</td>" \
                f"</tr>" \
                f"</tbody>" \
        f"</table>"


    return HttpResponse(html_code)