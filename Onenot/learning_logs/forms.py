from django import forms
from .models import Topic, Entry


class TopicForm(forms.ModelForm):  # Простейшая версия ModelForm состоит из вложенного класса Meta, который сообщает
    # Django, на какой модели должна базироваться форма и какие поля на ней должны находиться.
    class Meta:
        model = Topic  # форма создается на базе модели Topic, а на ней размещается только поле text
        fields = ['text']
        labels = {'text': ''}  # не генерировать подпись для текстового поля.


class EntryForm(forms.ModelForm):
    class Meta:
        model = Entry
        fields = ['text']
        labels = {'text': ''}
        widgets = {'text': forms.Textarea(attrs={'cols': 80})}  # Включая атрибут widgets, вы можете переопределить
        # виджеты, выбранные Django по умолчанию. Приказывая Django использовать элемент forms.Textarea, мы настраиваем
        # виджет ввода для поля 'text', чтобы ширина текстовой области составляла 80 столбцов вместо значения по умолчанию 40.
