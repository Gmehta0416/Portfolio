from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def profile(request):
    return render(request,"home.html")
    #return HttpResponse("this is first deployed project pf django and this is the changes have a great day bro")