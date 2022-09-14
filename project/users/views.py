
from django.views import View
from django.shortcuts import render
from django.http import HttpResponse

class Index(View):
    def get(self,request,*args,**kwargs):
    # GET Request
        return render(request,'users/index.html')

