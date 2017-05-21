from django.http import HttpResponse,HttpResponseRedirect
from django.shortcuts import render_to_response
from books.models import Book
from django.core.mail import send_mail
import datetime

def hello(request):
    return HttpResponse('hello world')

def current_datetime(request):
    now = datetime.datetime.now()
    html = "<html><body> It is now %s.</body></html>" % now
    return HttpResponse(html)

def hours_ahead(request,offset):
    try:
	offset = int(offset)
    except ValueError:
	raise Http404()
    dt = datetime.datetime.now() + datetime.timedelta(hours=offset)
    html = "<html><body> in %s hour(s), it will be %s.</body></html" %(offset,dt)
    return HttpResponse(html)

def search_form(request):  
    print request.META
    return render_to_response('search_form.html')

'''def search(request):
    if 'q' in request.GET:
        message = 'You searched for: %r' % request.GET['q']
    else:
        message = 'You submitted an empty form.'
    return HttpResponse(message)'''

def search(request):
    if 'q' in request.GET and request.GET['q']:
        q = request.GET['q']
        books = Book.objects.filter(title__icontains=q)
        return render_to_response('search_results.html',
            {'books': books, 'query': q})
    else:
        return HttpResponse('Please submit a search term.')

def contact(request):
    errors = []
    if request.method == 'POST':
        if not request.POST.get('subject',''):
            errors.append('Enter a subject.')
        if not request.POST.get('message',''):
            errors.append('Enter a message.')
        if request.POST.get('email') and '@' not in request.POST['email']:
            errors.append('Enter a valid e-mail address.')
        if not errors:
            send_mail(
                request.POST['subject'],
                request.POST['message'],
                request.POST.get('emial','noreply@example.com'),
                ['siteowner@example.com'],
            )
            return HttpResponseRedirect('/contact/thanks')
    return render_to_response('contact_form.html',{'errors':errors})

def thanks(request):
    return render_to_response('thanks.html')