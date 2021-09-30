from django.shortcuts import render
from django.views.generic import TemplateView
from .models import Doc
from django.http import HttpResponse,JsonResponse

class MainView(TemplateView):
    template_name = 'docs/home.html'
def file_upload_view(request):
    if request.method == "POST":
        my_file = request.FILES.get('file')
        print(my_file)
        str(my_file)
        Doc.objects.create(upload = my_file)
    return JsonResponse({'post':"false"})
    print(request.FILES)
    return HttpResponse("upload")

# Create your views here.
