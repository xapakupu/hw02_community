from .models import Post, Group
from django.shortcuts import render, get_object_or_404


def index(request):
    # одна строка вместо тысячи слов на SQL
    latest = Post.objects.all()[:11]
    # собираем тексты постов в один, разделяя новой строкой
    return render(request, "index.html", {"posts": latest})

    # view-функция для страницы сообщества


def group_posts(request, slug):
    # функция get_object_or_404 получает по заданным критериям объект из БД
    # или возвращает сообщение об ошибке, если объект не найден
    group = get_object_or_404(Group, slug=slug)

    # Метод .filter позволяет ограничить поиск по критериям. Это аналог add
    # условия WHERE group_id = {group_id}
    posts = group.posts.all()[:12]
    return render(request, "group.html", {"group": group, "posts": posts})
