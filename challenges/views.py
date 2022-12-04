from django.shortcuts import render
from django.http import Http404,HttpResponse, HttpResponseNotFound, HttpResponseRedirect
from django.urls import reverse

from django.template.loader import render_to_string

# Create your views here.
monthly_challenges_array = {
    "january": "Eat a lot  of meat",
    "february": "walk 20 minutes every day",
    "march": "read 20 minutes every day",
    "april": "Eat a lot  of meat",
    "may": "walk 20 minutes every day",
    "june": "read 20 minutes every day",
    "july": "Eat a lot  of meat",
    "august": "walk 20 minutes every day",
    "september": "read 20 minutes every day",
    "october": "Eat a lot  of meat",
    "november": "walk 20 minutes every day",
    "december": None
}


def index(request):
    list_items = ""
    months = list(monthly_challenges_array.keys())
    return render(request, "challenges/index.html", {"months": months})


def monthly_challenges_by_number(request, month):
    months = list(monthly_challenges_array.keys())
    if month > len(months):
        return HttpResponseNotFound("this is not supported")
    redirect_month = months[month - 1]
    redirect_path = reverse("month-challenge", args=[redirect_month])
    return HttpResponseRedirect(redirect_path)


def monthly_challenges(request, month):
    try:
        challenge_text = monthly_challenges_array[month]
        return render(request, "challenges/challenge.html", {
            "text": challenge_text,
            "month": month
        })
    except:
        raise Http404()