from django.utils.http import is_safe_url
from django.conf import settings
import random
from django.shortcuts import render, redirect
from django.http import HttpResponse, Http404, JsonResponse
from .forms import TweetForm
from .models import Tweet



ALLOWED_HOSTS = settings.ALLOWED_HOSTS


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

def tweet_create_view(request, *args, **kwargs):
    form = TweetForm(request.POST or None)
    next_url = request.POST.get("next") or None
    print ('next_url = ', next_url)
    if form.is_valid() and is_safe_url(next_url, ALLOWED_HOSTS):
        obj = form.save(commit=False)
        obj.save()
        if next_url!=None:
            return redirect(next_url)
        form = TweetForm()
    return render(request, 'components/form.html', context={"form":form})
