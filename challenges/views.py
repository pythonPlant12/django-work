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
    "december": None
}


def index(request):
    months = list(monthly_challenges.keys())
    for month in months:
        capitalized_month = month.capitalize()
        month_path = reverse("month-challenge", args=[month])

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
        return HttpResponseNotFound("<h1>Month not found</h1>")
