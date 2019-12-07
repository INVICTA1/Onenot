"""Определяет схемы URL для learning_logs"""
from django.conf.urls import url
from . import views  # импортируем из каталога файл

app_name = 'learning_log'
urlpatterns = [  # список страниц которые могут запрашиваться из приложения learning_logs
    # Домашняя страница
    url(r'^$', views.index, name='index'),
    # 2-ой аргумент определяет ф-ю представления нашей страницы, 3-й аргумент определяет index для этой схемы URL что-бы можно было ссылаться в других частях кода
    url(r'^topics/$', views.topics, name='topics'),
    url(r'^topics/(?P<topic_id>\d+)/$', views.topic, name='topic'),
    url(r'^new_topic/$', views.new_topic, name='new_topic'),
    # Символ r сообщает Django, что последующая строка должна интерпретироваться без дополнительной обработки, а выражение заключено в кавычки. Вторая часть выражения, /(?P<topic_id>\d+)/, описывает целое число, заключенное между двумя косыми чертами; это целое число сохраняется в аргументе topic_id. Круглые скобки, в которые заключена эта часть выражения, сохраняют значение из URL; часть ?P<topic_id> сохраняет совпавшее значение в topic_id; а выражение \d+ совпадает с любым количеством цифр, заключенных между символами косой черты.
    url(r'^new_entry/(?P<topic_id>\d+)/$', views.new_entry, name='new_entry'),
    url(r'^edit_entry/(?P<entry_id>\d+)/$', views.edit_entry, name='edit_entry'),
    url(r'^del_topic/(?P<topic_id>\d+)/$', views.del_topic, name='del_topic'),
    url(r'^del_entry/(?P<entry_id>\d+)/$', views.del_entry, name='del_entry'),

]
