from django.shortcuts import render

# Create your views here.
def return_html_dashboard(request):
    return render(request,'dashboard_form.html')