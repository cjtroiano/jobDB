from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    return HttpResponse("Hello, world. You're at Chris' job index.")

def details(request, job_id):
	return HttpResponse("You're looking at job %s." % job_id)

def results(request, job_id):
	response = "You're looking at the results of job %s."
	return HttpResponse(response % job_id)
