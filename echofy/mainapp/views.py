from django.shortcuts import render
from mainapp.models import join_us_user as joinUs

# Create your views here.
def home(request):
    return render(request, 'home.html')  # Render the home template

def about(request):
    return render(request, 'about.html')

def service(request):
    return render(request, 'service.html')

def contact(request):
    return render(request, 'contact.html')

def join(request):
    return render(request, 'join.html')

def join_user(request):
    if request.method == 'POST':
        n = request.POST.get('name')
        e = request.POST.get('email')   
        p = request.POST.get('phone')
        l = request.POST.get('linkedin')

        joinUs.objects.create(name=n, email=e, phone=p, linkedin=l)
        msg = "Your details have been submitted successfully!"
        return render(request, 'join.html', {'msg': msg})
