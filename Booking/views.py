from django.shortcuts import render

# Create your views here.


def reservation(request):
    return render(request, template_name='Booking/desing.html')