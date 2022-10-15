from django.http import HttpResponse
from .models import Link, News, Photo
from django.shortcuts import get_object_or_404, render, redirect
from django.views.generic.edit import FormView
# Спасибо django за готовую форму регистрации.
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.forms import AuthenticationForm
# Функция для установки сессионного ключа.
# По нему django будет определять,
# выполнил ли вход пользователь.
from django.contrib.auth import login
from django.http import HttpResponseRedirect
from django.views.generic.base import View
from django.contrib.auth import logout
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth.models import User
from .models import Message
from datetime import datetime
from django.http import JsonResponse
import json
from .models import Mark
from django.db.models import Avg



# Create your views here.
app_url = "/news/"



def index(request):
    message = None
    if "message" in request.GET:
        message = request.GET["message"]
    # создание HTML-страницы по шаблону index.html
    # с заданными параметрами latest_riddles и message
    return render(
        request,
        "index.html",
        {
            "latest_links":
                Link.objects.order_by('-pub_date')[:10],
            "message": message
        }
    )

def detail(request, news_id):
    error_message = None
    if "error_message" in request.GET:
        error_message = request.GET["error_message"]
    return render(
        request,
        "news.html",
        {
            "link": get_object_or_404(Link, pk=news_id),
            "error_message": error_message,
            "latest_messages":
                Message.objects
                    .filter(chat_id=news_id)
                    .order_by('-pub_date')[:5],
            "already_rated_by_user":
                Mark.objects
                    .filter(author_id=request.user.id)
                    .filter(riddle_id=news_id)
                    .count(),
            # оценка текущего пользователя
            "user_rating":
                Mark.objects
                    .filter(author_id=request.user.id)
                    .filter(riddle_id=news_id)
                    .aggregate(Avg('mark'))
                ["mark__avg"],
            # средняя по всем пользователям оценка
            "avg_mark":
                Mark.objects
                    .filter(riddle_id=news_id)
                    .aggregate(Avg('mark'))
                ["mark__avg"]

        }
    )

class RegisterFormView(FormView):
    # будем строить на основе
    # встроенной в django формы регистрации
    form_class = UserCreationForm
    # Ссылка, на которую будет перенаправляться пользователь
    # в случае успешной регистрации.
    # В данном случае указана ссылка на
    # страницу входа для зарегистрированных пользователей.
    success_url = app_url + "login/"
    # Шаблон, который будет использоваться
    # при отображении представления.
    template_name = "reg/register.html"
    def form_valid(self, form):
        # Создаём пользователя,
        # если данные в форму были введены корректно.
        form.save()
        # Вызываем метод базового класса
        return super(RegisterFormView, self).form_valid(form)


class LoginFormView(FormView):
    # будем строить на основе
    # встроенной в django формы входа
    form_class = AuthenticationForm
    # Аналогично регистрации,
    # только используем шаблон аутентификации.
    template_name = "reg/login.html"
    # В случае успеха перенаправим на главную.
    success_url = app_url
    def form_valid(self, form):
        # Получаем объект пользователя
        # на основе введённых в форму данных.
        self.user = form.get_user()
        # Выполняем аутентификацию пользователя.
        login(self.request, self.user)
        return super(LoginFormView, self).form_valid(form)


class LogoutView(View):
    def get(self, request):
        # Выполняем выход для пользователя,
        # запросившего данное представление.
        logout(request)
        # После чего перенаправляем пользователя на
        # главную страницу.
        return HttpResponseRedirect(app_url)


class PasswordChangeView(FormView):
    # будем строить на основе
    # встроенной в django формы смены пароля
    form_class = PasswordChangeForm
    template_name = 'reg/password_change_form.html'
    # после смены пароля нужно снова входить
    success_url = app_url + 'login/'
    def get_form_kwargs(self):
        kwargs = super(PasswordChangeView, self).get_form_kwargs()
        kwargs['user'] = self.request.user
        if self.request.method == 'POST':
            kwargs['data'] = self.request.POST
        return kwargs
    def form_valid(self, form):
        form.save()
        return super(PasswordChangeView, self).form_valid(form)

def profile(request, user_id):
    return render(
        request,
        "profile.html",
        {
            "user": get_object_or_404(User, pk=user_id),

        }
    )

def post_img(request):
    photo = Photo()
    photo.user = request.user
    photo.photo = request.POST['img']
    photo.save()
    return HttpResponseRedirect(app_url + "profile/" + str(photo.user.id))

def post(request, link_id):
    msg = Message()

    msg.author = request.user
    msg.chat = get_object_or_404(Link, pk=link_id)
    msg.message = request.POST['message']
    msg.pub_date = datetime.now()
    msg.save()
    return HttpResponseRedirect(app_url+str(link_id))

def msg_list(request, riddle_id):
    # выбираем список сообщений
    res = list(
            Message.objects
                # фильтруем по id загадки
                .filter(chat_id=riddle_id)
                # отбираем 5 самых свежих
                .order_by('-pub_date')[:5]
                # выбираем необходимые поля
                .values('author__username',
                        'pub_date',
                        'message'
                )
            )
    # конвертируем даты в строки - сами они не умеют
    for r in res:
        r['pub_date'] = \
            r['pub_date'].strftime(
                '%d.%m.%Y %H:%M:%S'
            )
    return JsonResponse(json.dumps(res), safe=False)

def post_mark(request, riddle_id):
    msg = Mark()
    msg.author = request.user
    msg.riddle = get_object_or_404(Link, pk=riddle_id)
    msg.mark = request.POST['mark']
    msg.pub_date = datetime.now()
    msg.save()
    return HttpResponseRedirect(app_url+str(riddle_id))

def get_mark(request, news_id):
    res = Mark.objects\
            .filter(riddle_id=news_id)\
            .aggregate(Avg('mark'))

    return JsonResponse(json.dumps(res), safe=False)
