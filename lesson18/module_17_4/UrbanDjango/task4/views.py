from django.shortcuts import render

# Create your views here.
def main_page(request):
    return render(request, 'main.html')

def games(request):
    context = {'games': ["Atomic Heart", "Cyberpunk 2077"]}
    return render(request, 'games.html', context)

def cart(request):
    return render(request, 'cart.html')
