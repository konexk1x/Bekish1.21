from .models import Link, News, Photo
from django.shortcuts import get_object_or_404, render
from django.views.generic.edit import FormView
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.forms import AuthenticationForm
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

app_url = "/news/"


def index(request):
    message = None
    if "message" in request.GET:
        message = request.GET["message"]
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
                .filter(news_id=news_id)
                .count(),
            # оценка текущего пользователя
            "user_rating":
                Mark.objects
                .filter(author_id=request.user.id)
                .filter(news_id=news_id)
                .aggregate(Avg('mark'))
                ["mark__avg"],
            # средняя по всем пользователям оценка
            "avg_mark":
                Mark.objects
                .filter(news_id=news_id)
                .aggregate(Avg('mark'))
                ["mark__avg"]

        }
    )


class RegisterFormView(FormView):
    form_class = UserCreationForm
    success_url = app_url + "login/"
    template_name = "reg/register.html"

    def form_valid(self, form):
        form.save()
        return super(RegisterFormView, self).form_valid(form)


class LoginFormView(FormView):
    form_class = AuthenticationForm
    template_name = "reg/login.html"
    success_url = app_url

    def form_valid(self, form):
        self.user = form.get_user()
        login(self.request, self.user)
        return super(LoginFormView, self).form_valid(form)


class LogoutView(View):
    def get(self, request):
        logout(request)
        return HttpResponseRedirect(app_url)


class PasswordChangeView(FormView):
    form_class = PasswordChangeForm
    template_name = 'reg/password_change_form.html'
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
    return HttpResponseRedirect(app_url + str(link_id))


def msg_list(request, riddle_id):
    res = list(
        Message.objects
        .filter(chat_id=riddle_id)
        .order_by('-pub_date')[:5]
        .values('author__username',
                'pub_date',
                'message'
                )
    )
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
    return HttpResponseRedirect(app_url + str(riddle_id))


def get_mark(request, news_id):
    res = Mark.objects \
        .filter(riddle_id=news_id) \
        .aggregate(Avg('mark'))

    return JsonResponse(json.dumps(res), safe=False)
