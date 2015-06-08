from django.http import JsonResponse

def responses(request):
	responses = {}
	responses["id"] = "1111111"
	responses["uri"] = request.POST.get('uri')
	responses["api"] = request.POST.get('api')
	responses["user"] = request.POST.get('user')
	responses["user"] = request.POST.get('user')

    # loop through keys
    for key in request.POST:
        value = request.POST[key]
    # loop through keys and values
    for key, value in request.POST.iteritems():
    	print key,
    	print ":",
    	print value

	return JsonResponse({'id':'1'})