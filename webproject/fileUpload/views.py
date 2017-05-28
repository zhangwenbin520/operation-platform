from django.shortcuts import render
from django.shortcuts import render_to_response
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse,HttpResponseRedirect
import os
#from django.templet import RequestContext

# Create your views here.

@login_required
def upload(request):
    '''upload_file'''
    if request.method == 'POST':
        print request.FILES
        f = request.FILES.get('fileUpload')
        baseDir = os.path.dirname(os.path.abspath(__name__))
        fileDir = os.path.join(baseDir,'static','file')
        fileName = os.path.join(fileDir,f.name)
        fileO = open(fileName,'wb')
        for chrunk in f.chunks():
            fileO.write(chrunk)
        fileO.close()
        
        return render_to_response('file_upload.html',{'fileUpload':f.name})
    else:
	return render_to_response('file_upload.html')
   
