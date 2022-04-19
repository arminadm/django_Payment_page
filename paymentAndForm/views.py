from django.shortcuts import render
from paymentAndForm.forms import CustomenrsFrom
from django.shortcuts import redirect


# Create your views here.
def form_view(request):
    if request.method == 'GET':
        form = CustomenrsFrom()
        context = {'form': form}
        return render(request, 'form/index.html', context)
    if request.method == 'POST':
        form = CustomenrsFrom(request.POST)
        if form.is_valid():
            req = form.save()
            request.session['request_id'] = req.id
            return redirect('/go-to-gate-way')
        else:
            return render(request, 'form/failed.html')