from django.shortcuts import render
from django.http import Http404, HttpResponse, HttpResponseNotFound, HttpResponseRedirect
from django.urls import reverse
from django.template.loader import render_to_string
from django.http import Http404



# We can also create a dictionary instead of doing if statement for each month
monthly_challenges = {
    "january": "Hey, it's january",
    "february": "Hey, it's february",
    "march": "Hey, it's march",
    "april": "Hey, it's april",
    "may": "Hey, it's may",
    "june": "Hey, it's june",
    "july": "Hey, it's july",
    "august": "Hey, it's august",
    "september": "Hey, it's september",
    "october": "Hey, it's october",
    "november": "Hey, it's november",
    "december": None
}


def index(request):
    months = list(monthly_challenges.keys())
    return render(request, "challenges/index.html", {
        "months": months
    })


def monthly_challenge_by_number(request, month):
    # Convert dict.keys() into a list and assign to a variable
    months = list(monthly_challenges.keys())

    if month > len(months):
        return HttpResponseNotFound("Invalid month")
    # Taking a key word from a list accessing by index
    redirect_month = months[month - 1]
    # Creating redirecting path, accessing by name:
    # "month-challenge" = /challenge/ or month as parameter
    redirect_path = reverse("month-challenge", args=[redirect_month])
    return HttpResponseRedirect(redirect_path)


def monthly_challenge(request, month):
    try:
        challenge_text = monthly_challenges[month]
        # Return .html file from templates/challenges/challenges.html
        return render(request, "challenges/challenge.html", {
            "text": challenge_text,
            "month": month
        })
    except: 
        # We don't need to specify nothing in this directory because is in root folder
        # We cannot use here a render shortcut because render() always return success
        # response. And we need to provide an 404 Error
        # response_data = render_to_string("404.html")
        # return HttpResponseNotFound(response_data)
        # We can do it this way, but as it's used so much, django has special shorcut 
        # for it. This will look automaticly into a root templates folder and 
        # look for 404 html file
        raise Http404() 
