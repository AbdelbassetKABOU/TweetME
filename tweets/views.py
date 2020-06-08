import random
from django.shortcuts import render
from django.http import HttpResponse, Http404, JsonResponse
from .models import Tweet

# Create your views here.
# I know

def home_view(request, *args, **kwargs):
    return render(request, "pages/home.html", context={}, status=200)

def tweet_list_view(request, *args, **kwargs):
#def home_view(request, mytweet):
    # print (args, kwargs)
    # return HttpResponse("<h1> Hello jma3a zina </h1>")
    mytweets = Tweet.objects.all()
    tweet_list = [{"id":my.id, "content":my.content, "likes":random.randint(0, 1000)} for my in mytweets]
    #tweet_list = [{"id":my.id, "content":my.content, "likes":112} for my in mytweets]
    # for mytweet in mytweets:
    # tweet_list = tweet_list.append(mytweet)    
    data = {
        "isUser":False,
        "response": tweet_list,
    }
    return JsonResponse(data)    
    # return render(request, "pages/home.html", context={'mytweets':mytweets}, status=200)

def tweet_detail_view(request, tweet_id, *args, **kwargs):
    """
    THIS IS A REST API VIEW - 
    This means we need to output a JSON
    """    
    data = {
        'id':tweet_id,
    }        
    try:
        obj = Tweet.objects.get(id=tweet_id)
        data['content'] = obj.content
        status = 200
    except:
        status = 404
        data['message'] = 'Object not found'
    #return HttpResponse(f"<h1> Hello jma3a, this is the tweet n° {obj.id} - {obj}</h1>")
    return JsonResponse (data, status=status)

def add_tweet(request, tweet_text):
    #def home_view(request, mytweet):
    obj = Tweet()
    obj.content = tweet_text
    obj.save()
    return HttpResponse(f"<h1> Hello jma3a, We added the tweet  {tweet_text} </h1>")    

def del_tweet(request, tweet_id):
    #def home_view(request, mytweet):
    obj = Tweet.objects.get(id=tweet_id)
    obj.delete()
    return HttpResponse(f"<h1> We deleted the tweet  {obj} </h1>")    