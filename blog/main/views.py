from django.http import HttpResponse
# Create your views here.
def main(request):
    '''
    Show 'Hello world' in the main Page
    '''
    return HttpResponse('Hello world!')