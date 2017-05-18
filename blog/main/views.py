from django.shortcuts import render
import datetime
# Create your views here.
def main(request):
    '''
    Render the main page
    '''
    
    context = {'like':'Django很棒'}
    return render(request,'main/main.html', context)

def about(request):
    '''
    Render the about page
    '''
    return render(request, 'main/about.html')

def time(request):
    '''
    Render the main Page
    '''
    return render(request, 'main/time.html')
