from django.shortcuts import render
from django.http import HttpResponse
# from newapp.models import Topic,Webpage,AccessRecord

# Create your views here.
def index(request):
   # webpages_list = AccessRecord.objects.order_by('date')
   # date_dict = {'access_records':webpages_list}
    my_dict = {'insert_me': "Now I am coming from newapp/index.html"}
    return render(request,'newapp/index.html',context=my_dict)
   # return render(request,'newapp/index.html',context=date_dict)
