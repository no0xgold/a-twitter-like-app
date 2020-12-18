import random
from django.conf import settings
from django.http import HttpResponse, Http404, JsonResponse
from django.shortcuts import render, redirect
from django.utils.http import is_safe_url

from .models import Tweet
from .forms import TweetForms


ALLOWED_HOSTS = settings.ALLOWED_HOSTS

def home_view(request,*args,**kwargs):
    print(args,kwargs)
    #return HttpResponse("<h1>Hello<h1>")
    return render(request,"pages/home.html", context={},status=200)

def tweet_create_view(request, *args, **kwargs):
    form=TweetForms(request.POST or None)
    next_url= request.POST.get("next") or None
    print("next url", next_url)
    if form.is_valid():
        obj = form.save(commit=False)
        obj.save()
        if next_url != None and is_safe_url(next_url, ALLOWED_HOSTS):
            return redirect(next_url)
        form=TweetForms()
    return render(request, 'components/forms.html', context={"form": form})

def tweet_list_view(request,*args,**kwargs):
    """
    REST API VIEW
    Consme by JavaScript or Swift/Java/ios/Android
    return json data
    for now we use JS
    """
    qs=Tweet.objects.all()
    tweets_list=[{"id":x.id, "content": x.content, "likes":random.randint(0, 100)} for x in qs]
    data={
        "IsUser": False,
        "response": tweets_list
        }
    return JsonResponse(data)



def tweet_detail_view(request,tweet_id,*args,**kwargs):
    """
    REST API VIEW
    Consme by JavaScript or Swift/Java/ios/Android
    return json data
    for now we use JS
    """
    data={
        "id":tweet_id,
    }
    status=200
    try:
        obj=Tweet.objects.get(id=tweet_id)
        data['content']=obj.content
    except:
        data['message']="not found"
        status=404
    
    return JsonResponse(data, status=status)
