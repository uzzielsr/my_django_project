from django.shortcuts import render

def home(request):
    context = {
        "username": "Uzziel",
        "skills": ["Python", "Django", "Playwright", "Jira"],
        "title": "Welcome to My QA Dashboard",
    }
    return render(request, "blog/home.html", context)