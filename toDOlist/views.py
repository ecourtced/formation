from django.shortcuts import render
# Create your views here.

def views_index(request):
    return render(request,"index.html",context={"var_nom":"Benoit"})

def blog(request):
    return render(request,"blog.html")


def custom_404(request, exception):
    return render(request, '404.html', status=404)