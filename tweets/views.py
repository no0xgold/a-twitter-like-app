from django.http import HttpResponse,Http404,JsonResponse
from django.shortcuts import render
from .models import Tweet

def home_view(request,*args,**kwargs):
    print(args,kwargs)
    #return HttpResponse("<h1>Hello<h1>")
    return render(request,"pages/home.html", context={},status=200)
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
