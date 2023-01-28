from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect
from django.urls import reverse

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
    "december": "Hey, it's december"
}

# Create your views here.


def index(request):
    list_items = ""
    months = list(monthly_challenges.keys())
    for month in months:
        capitalized_month = month.capitalize()
        month_path = reverse("month-challenge", args=[month])
        list_items += f"<li><a href='{month_path}'>{capitalized_month}</a></li>"

        # <li><a href="/challenges/january"><January></a></li>

        response_data = f"<ul>{list_items}</ul>"
    return HttpResponse(response_data)


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
    monthly_message = None
    # We access to a dictionary values using keyword month from parameters
    try:
        challenge_text = monthly_challenges[month]
        response_data = f"<h1>{challenge_text}</h1>"
        return HttpResponse(response_data)
    except:
        return HttpResponseNotFound("<h1>Month not found</h1>")
