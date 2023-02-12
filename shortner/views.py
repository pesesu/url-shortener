from django.shortcuts import render
from django.http import HttpResponse
import pyshorteners

# Create your views here.
def home(request):
    error = None
    result = None
    error_type = None

    if request.method == 'POST':
        url = request.POST['url']
        if url == '' or url == None:
            error = 'No url entered.'
            error_type = 'warning'
        else:
            short = pyshorteners.Shortener()
            result = short.tinyurl.short(url)
        

    context = {
                'error': error, 
                'result': result, 
                'error_type': error_type
              }
    return render(request, 'shortner/home.html', context)
