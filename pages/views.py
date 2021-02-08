from django.shortcuts import render, redirect
from django.views.generic import ListView, DetailView
from .models import *
from django.core.mail import send_mail

# Create your views here.
def homeView(request):
    if request.method == "POST":
        email = request.POST['email']
        name = request.POST['name']
        message = request.POST['message']

        send_mail(
            "Website Message",
            "New Meeage from: {} at {}; {}".format(name, email, message),
            email,
            ['patkeenan316@gmail.com'],
        )
        context = {
            message: "Thanks for the contact!"
        }
        return redirect("home")
    projects = Project.objects.all()
    projects_for_home = projects[:5]
    context = {
        "projects": projects_for_home
    }
    return render(request, "index.html", context)

class BlogHome(ListView):
    model = BlogPost
    template_name = "blog_home.html"


class BlogDetail(DetailView):
    model = BlogPost
    template_name = "blog_detail.html"


class ProjectHome(ListView):
    model = Project
    template_name = "project_home.html"


class ProjectDetail(DetailView):
    model = Project
    template_name = "project_detail.html"
