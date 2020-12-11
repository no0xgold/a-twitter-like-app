from django.http import HttpResponse,Http404
from django.shortcuts import render
from .models import Tweet

def home_view(request,*args,**kwargs):
    print(args,kwargs)
    return HttpResponse("<h1>Hello<h1>")

def tweet_detail_view(request,tweet_id,*args,**kwargs):
    try:
        obj=Tweet.objects.get(id=tweet_id)
    except:
        raise Http404
    return HttpResponse(f"<h1>tweet {tweet_id}-{obj.content}<h1>")
