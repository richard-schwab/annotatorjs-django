import json

from django.http import HttpResponse
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt

@csrf_exempt										# Set this up later. Want proof of concept first.
def create(request):

	an_responses = dict(request.POST.lists())
	print
	print "New Note"
	return_responses = {}

	try:
		print an_responses["json"][0]
		return_responses = eval(an_responses["json"][0])
		print "Text: " + return_responses["text"]
		print "Quote: " + return_responses["quote"]

	except:											# This gets triggered if you run the json url directly for testing.
		print "Error"
		print an_responses
		
	return_responses["id"] = "AUxWM-HasREW1YKAwhil"
	return_responses["uri"] = "http://localhost:8000"
	return_responses["user"] = "the_user"
	return_responses["created"] = "2013-08-26T13:31:49.339078+00:00"
	return_responses["updated"] = "2013-08-26T14:09:14.121339+00:00"

	return JsonResponse(return_responses)
	