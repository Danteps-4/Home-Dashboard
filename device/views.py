from django.shortcuts import render

# Create your views here.
def device(request):
    return render(request, "device/device.html")