from django.shortcuts import render

def portfolio(request):
    return render_to_response('portfolio.html', context_instance = RequestContext(request))