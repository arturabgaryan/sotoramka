from django.shortcuts import render


def main(request):
    return render(request, 'main.html')


def main_eng(request):
    return render(request, 'main_eng.html')

