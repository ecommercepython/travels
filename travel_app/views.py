from django.http import HttpResponse
from django.shortcuts import render
from . models import place

# def demo1(request):
#     return HttpResponse("HELOOO")
#
def about(request):
    obj=place.objects.all()
    return render(request, "index.html",{'result':obj})






#def addition(request):
     #X=int(request.GET['num1'])
   #  Y=int(request.GET['num2'])
   #  res=X+Y
    # return render(request,'result.html',{"result":res})

