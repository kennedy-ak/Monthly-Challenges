from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect, Http404
from django.urls import reverse
from django.template.loader import render_to_string
# Create your views here.
tasks = {
    "me":"this will work",
    "january": "Avoid Social Media While Working",
    "february": "Start a Blog (and Post Once a Week)",
    "march": "Just sleep",
    "april":  "Try a New Side Hustle Each Week",
    "may": "Drink a Little More Water",
    "june": "Stay calm and meditate every day",
    "july":"Pay In Cash Only",
    "august": "increase my cwa",
    "september":None,
    "october": "Make One New Connection a Week",
    "november": "Read a Chapter of a Book a Day",
    "december": None,
}



def by_number(request, month):
    months = list(tasks.keys())
    
    if month > len(months):
        return HttpResponseNotFound(" Invalid Month")
    forwarded_month = months[month - 1]
    redirected_path = reverse("task-month", args=[forwarded_month])
    return HttpResponseRedirect(redirected_path)


def monthly_challenge(request, month):
    try:
        challenge_text = tasks[month]
        return render(request, "challenges/index.html", {
            'text': challenge_text,
            'month_name': month
        })
        
    except:
       raise Http404()
    
    
def index(request):
    list_items = ""
    months = list(tasks.keys())
    
    return render(request, "challenges/list.html",{
        "months" :months,
    } )
    
    
       
