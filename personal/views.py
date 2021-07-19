from django.shortcuts import render
from account.models import Account

# Create your views here.


def home_screen_view(request):

    context = {}
    # context['some_string'] = 'Some Random Strings'

    # context = {
    #     'some_text': 'Some Texts',
    #     'some_number': 12345
    # }

    # list_of_values = []
    # list_of_values.append('first_value')
    # list_of_values.append('second_value')
    # list_of_values.append('third_value')
    # list_of_values.append('fourth_value')

    # context['list_of_val'] = list_of_values

    # questions = Question.objects.all()

    # context['questions'] = questions

    accounts = Account.objects.all()
    context['accounts'] = accounts

    return render(request, 'personal/home.html', context)
