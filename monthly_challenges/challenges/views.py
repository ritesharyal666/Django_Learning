from django.shortcuts import render
from django.http import HttpResponse,HttpResponseNotFound,HttpResponseRedirect
from django.urls import reverse

# Create your views here.
#make method get request send response to create a view,django has no way of knowing methods created so go to urls.py

monthly_challenges={
    "january"  : "1 Eat no meat for entire month!",
    "february" : "2 Walk for at least 20 minutes every day!",
    "march"    : "3 Learn Django for at least 20 minutes every day!",
    "april"    : "4 Eat no meat for entire month!",
    "may"      : "5 Eat no meat for entire month!",
    "june"     : "6 Walk for at least 20 minutes every day!",
    "july"     : "7 Learn Django for at least 20 minutes every day!",
    "august"   : "8 Eat no meat for entire month!",
    "september": "9 Eat no meat for entire month!",
    "october"  : "10 Walk for at least 20 minutes every day!",
    "november" : "11 Don't eat nuts",
    "december" : None,
}

def index(request):
    months =list(monthly_challenges.keys())
    return render(request,"challenges/index.html",{
        "months": months
    })






def monthly_challenge(request,month):
    try:
        challenge_text = monthly_challenges[month]
        return render(request, "challenges/challenge.html", {
            "text": challenge_text,
            "month_text" : month
        })
    except:
        return HttpResponseNotFound("This month is not supported ")

def monthly_challenge_by_number(request,month):
    months =list(monthly_challenges.keys())
    
    if month >len(months):
         return HttpResponseNotFound("This month is not supported ")
    redirect_month = months[month-1]
    redirect_path= reverse("month-challenge",args=[redirect_month])
    return HttpResponseRedirect(redirect_path)

       