from django.shortcuts import render

# Create your views here.


def annotate(request):
	return render(request,"test.html",{})