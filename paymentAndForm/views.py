from django.shortcuts import render

# Create your views here.
def form_view(request):
    return render(request, 'form/index.html')