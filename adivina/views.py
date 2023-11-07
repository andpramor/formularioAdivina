from django.shortcuts import render

import random

def home(request):
    return render(request, 'adivina/home.html')

def guess(request):
    random_number = random.randint(1, 100)
    user_guess = int(request.POST['guess'])

    if user_guess == random_number:
        devolver = '¡Acertaste!'
    else:
        devolver = 'Has fallado estrepitosamente'
    
    return render(request, 'adivina/guess.html', {'mensaje':devolver})
