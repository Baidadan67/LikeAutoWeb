from django.shortcuts import render

# Create your views here.
def home(request):
    # we set the templates file then we fond pages/home.html
    return render(request, 'pages/home.html')