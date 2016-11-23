from django.shortcuts import get_object_or_404, render
from django.http import HttpResponse
from .models import Job

def index(request):
	job_list = Job.objects.all()
	context = {'job_list': job_list}
	return render(request, 'jobApp/index.html', context)

def details(request, job_id):
	job = get_object_or_404(Job, pk=job_id)
	return render(request, 'jobApp/details.html', {'job': job})

def results(request, job_id):
	response = "You're looking at the results of job %s."
	return HttpResponse(response % job_id)
