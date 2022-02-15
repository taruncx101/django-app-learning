from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect
from django.urls import reverse

# Create your views here.

monthly_challenges = {
    "january": "Eat no meat for the entire month!",
    "february": "Walk for at least 20 minutes every day!",
    "march": "Learn Django for at least 20 minutes every day!",
    "april": "Eat no meat for the entire month!",
    "may": "Walk for at least 20 minutes every day!",
    "june": "Learn Django for at least 20 minutes every day!",
    "july": "Eat no meat for the entire month!",
    "august": "Walk for at least 20 minutes every day!",
    "september": "Learn Django for at least 20 minutes every day!",
    "october": "Eat no meat for the entire month!",
    "november": "Walk for at least 20 minutes every day!",
    "december": "Learn Django for at least 20 minutes every day!"
}

def index(request):
    list_items = ""
    months = list(monthly_challenges.keys())

    for month in months:
        capitalized_month = month.capitalize()
        month_path = reverse("month-challenge", args=[month])
        list_items += f"<li><a href=\"{month_path}\">{capitalized_month}</a></li>"

    # "<li><a href="...">January</a></li><li><a href="...">February</a></li>..."

    response_data = f"<ul>{list_items}</ul>"
    return HttpResponse(response_data)

def january(request):
    return HttpResponse("Eat no meats for the entire month!")


def february(request):
    return HttpResponse("Work for at least 20 mins every day!")


def monthly_challenge_by_number(request, month):
    months = list(monthly_challenges.keys())

    if month > len(months):
        return HttpResponseNotFound("Invalid month")

    redirect_month = months[month - 1]
    # return HttpResponseRedirect("/challenges/" + redirect_month)
    redirect_month = months[month - 1]
    redirect_path = reverse("month-challenge", args=[redirect_month])
    return HttpResponseRedirect(redirect_path)


def monthly_challenge_by_number_bac(request, month):
    challage_text = None
    if month == 1:
        challage_text = "Eat no meats for the entire month!"
    elif month == 2:
        challage_text = "Work for at least 20 mins every day!"
    elif month == 3:
        challage_text = "Learn Django for at least 20 mins every day!"
    else:
        return HttpResponseNotFound("This month is not supported!")
    return HttpResponse(challage_text)


def monthly_challenge(request, month):
    try:
        challage_text = monthly_challenges[month]
        response_data = f"<h1>{challage_text}</h1>"
    except:
        return HttpResponseNotFound("This month is not supported!")
    # return HttpResponse(challage_text)
    return HttpResponse(response_data)


def monthly_challenge_bac(request, month):
    challage_text = None
    if month == "january":
        challage_text = "Eat no meats for the entire month!"
    elif month == "february":
        challage_text = "Work for at least 20 mins every day!"
    elif month == "march":
        challage_text = "Learn Django for at least 20 mins every day!"
    else:
        return HttpResponseNotFound("This month is not supported!")
    return HttpResponse(challage_text)
