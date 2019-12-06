from django.shortcuts import render  # ф-я возвращает html шаблон
from .models import Topic, Entry
from django.http import HttpResponseRedirect  # перенаправляет
# пользователя к странице topics после отправки введенной темы.
from django.urls import reverse  # Функция reverse() определяет URL
# по заданной схеме URL (то есть Django сгенерирует URL при запросе страницы).
from .forms import TopicForm, EntryForm


# Create your views here.
def index(request):
    """Домашняя сираница предложения learning log"""
    return render(request, 'learning_logs/index.html')  # Функция render() использует два аргумента — исходный объект
    # запроса и шаблон, используемый для построения страницы.


def topics(request):
    """Выводит списиок тем"""
    topics = Topic.objects.order_by()
    context = {'topics': topics}
    return render(request, 'learning_logs/topics.html', context)


def topic(request, topic_id):
    """Выводит одну запись и все ее записи"""
    topic = Topic.objects.get(id=topic_id)
    entries = topic.entry_set.order_by('-date_added')
    context = {'topic': topic, 'entries': entries}
    return render(request, 'learning_logs/topic.html', context)


def new_topic(request):
    """Определяет новую тему."""
    if request.method != 'POST':  # При построении веб-приложений используются два основных типа запросов — GET и POST. Запросы GET используются для страниц, которые только читают данные с сервера, а запросы POST обычно используются в тех случаях, когда пользователь должен отправить информацию через форму
        # Данные не отправлялись; создается пустая форма.
        form = TopicForm()
    else:
        # Отправлены данные POST; обработать данные.
        form = TopicForm(request.POST)  # в request.POST хранятся данные передаваемые пользователем
        if form.is_valid():  # is_valid()-проверяет чтобы все поля были заполнены
            form.save()  # записывает данные из формы в базу и сохраняет
            return HttpResponseRedirect(reverse('learning_logs:topics'))  # Мы используем вызов reverse() для получения
            # URL-адреса страницы topics и передаем его функции HttpResponseRedirect()
            # , перенаправляющей браузер пользователя на страницу topics.
    context = {'form': form}
    return render(request, 'learning_logs/new_topic.html', context)


def new_entry(request, topic_id):
    topic = Topic.objects.get(id=topic_id)
    if request.method != 'POST':
        form = EntryForm()  # создаем пустой экземпляр
    else:
        form = EntryForm(data=request.POST)  # создавая экземпляр EntryForm, заполненный данными POST из объекта запроса
        if form.is_valid():
            new_entry = form.save(commit=False)  # создаем новый объект записи и сохранить его в new_entry, не сохраняя
            # пока в базе данных
            new_entry.topic = topic  # Мы присваиваем атрибуту topic объекта new_entry тему, прочитанную из базы данных
            # в начале функции, после чего вызываем save() без аргументов.
            new_entry.save()
            return HttpResponseRedirect(reverse('learning_logs:topic', args=[topic_id]))
    context = {'topic': topic, 'form': form}
    return render(request, 'learning_logs/new_entry.html', context)


def edit_entry(request, entry_id):
    entry = Entry.objects.get(id=entry_id)  # получаем объект записи, который пользователь хочет изменить, и тему,
    # связанную с этой записью.
    topic = entry.topic
    if request.method != 'POST':
        form = EntryForm(instance=entry)  # (instance=entry) - приказывает Django создать форму,
        # заранее заполненную информацией из существующего объекта записи
    else:
        form = EntryForm(instance=entry, data=request.POST)  # При обработке запроса POST передаются аргументы
        # instance=entry и data=request.POST , чтобы приказать Django создать экземпляр формы на основании
        # информации существующего объекта записи, обновленный данными из request.POST
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('learning_logs:topic', args=[topic.id]))
    context = {'entry:': entry, 'topic': topic, 'form': form}
    return render(request, 'learning_logs/edit_entry.html', context)


# def del_topic(request,topic_id):
#    topic=Topic.object.get(id=topic_id)
#    topic.delete()
#    return