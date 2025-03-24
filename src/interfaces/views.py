from django.shortcuts import render, redirect
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from django.views import View
from src.infrastructure.models import PostModel
from django.contrib.auth.forms import AuthenticationForm
from src.infrastructure.forms import CustomUserCreationForm
from django.views.generic import ListView

class LoginView(View):
    def get(self, request):
        return render(request, "login.html", {"form": AuthenticationForm()})

    def post(self, request):
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect("dashboard")
        return render(request, "login.html", {"form": form})

class HomeView(ListView):
    model = PostModel
    template_name = "home.html"
    context_object_name = "posts"

@login_required
def dashboard(request):
    if request.method == "POST":
        title = request.POST.get("title")
        content = request.POST.get("content")
        if title and content:
            PostModel.objects.create(title=title, content=content, author=request.user)
            return redirect("dashboard")  # Redireciona para evitar reenvios do formulário

    posts = PostModel.objects.filter(author=request.user).order_by("-created_at")
    return render(request, "dashboard.html", {"posts": posts})

class RegisterUserView(View):
    def get(self, request):
        form = CustomUserCreationForm()
        return render(request, "register.html", {"form": form})

    def post(self, request):
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect("dashboard")
        return render(request, "register.html", {"form": form})
