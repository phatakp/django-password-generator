from django.shortcuts import render
import random
# Create your views here.


def index(request):
    return render(request, 'generator_app/index.html')

def about(request):
    return render(request, 'generator_app/about.html')

def result(request):
    gen_password = ''
    chars = list('abcdefghijklmnopqrstuvwxyz')
    upper_chars = list('ABCDEFGHIJKLMNOPQRSTUVWXYZ')
    numbers = list('0123456789')
    special = list('!@#$%^&*()?><:;,./|')
    length = int(request.GET.get('min-chars', 8))

    if request.GET.get('ucase'):
        gen_password += random.choice(upper_chars)
        gen_password += random.choice(upper_chars)
        length -= 2

    if request.GET.get('nums'):
        gen_password += random.choice(numbers)
        length -= 1

    if request.GET.get('special'):
        gen_password += random.choice(special)
        length -= 1

    for i in range(length):
        gen_password += random.choice(chars)

    gen_list = list(gen_password)
    random.shuffle(gen_list)
    gen_password = ''.join(gen_list)
    return render(request, 'generator_app/result.html', {'password': gen_password})
