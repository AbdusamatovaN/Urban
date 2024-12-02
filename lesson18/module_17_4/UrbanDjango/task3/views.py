from lib2to3.fixes.fix_input import context

from django.shortcuts import render

# Create your views here.

def main_page(request):
    return render(request, 'main.html')

def games(request):
    game1 = "First game"
    game2 = "Second game"
    game3 = "Third game"
    context = {'game1': game1, 'game2': game2, 'game3': game3}
    return render(request, 'games.html', context)

def cart(request):
    return render(request, 'cart.html')
