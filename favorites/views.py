from django.shortcuts import render

# Create your views here.
def fav_page(request):
    return render(request , 'favorites.html')