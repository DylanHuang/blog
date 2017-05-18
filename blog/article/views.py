from django.shortcuts import render

# Create your views here.
def article(request):
    '''
    Render the articel page
    '''
    return render(request, 'article/article.html')
