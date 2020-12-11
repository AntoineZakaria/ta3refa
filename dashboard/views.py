from django.shortcuts import render

# Create your views here.
def return_dashboard(request):
    return render(request,'dashboard form.html')