from django.shortcuts import render
from paymentAndForm.forms import CustomenrsFrom
# Create your views here.
def form_view(request):
    if request.method == 'GET':
        form = CustomenrsFrom()
        context = {'form': form}
        return render(request, 'form/index.html', context)
    if request.method == 'POST':
        form = CustomenrsFrom(request.POST)
        if form.is_valid():
            form.save()
            return render(request, 'form/temp.html')
        else:
            return render(request, 'form/failed.html')