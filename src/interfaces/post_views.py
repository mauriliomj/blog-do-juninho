from rest_framework import generics, permissions
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from src.infrastructure.models import PostModel
from src.infrastructure.serializers import PostSerializer
from django.shortcuts import get_object_or_404
from src.infrastructure.forms import PostForm
from src.application.post_service import PostService

class PostListCreateView(generics.ListCreateAPIView):
    queryset = PostService.get_all_posts()
    serializer_class = PostSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)

class PostDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = PostModel.objects.all()
    serializer_class = PostSerializer
    permission_classes = [permissions.IsAuthenticated]

@login_required
def create_post(request):
    if request.method == "POST":
        title = request.POST["title"]
        content = request.POST["content"]
        PostModel.objects.create(title=title, content=content, author=request.user)
        return redirect("dashboard")

    return render(request, "post_create.html")

@login_required
def edit_post(request, post_id):
    post = get_object_or_404(PostModel, id=post_id, author=request.user)

    if request.method == "POST":
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            form.save()
            return redirect("dashboard")  # Redireciona para o dashboard após a edição
    else:
        form = PostForm(instance=post)

    return render(request, "edit_post.html", {"form": form, "post": post})

@login_required
def delete_post(request, post_id):
    post = get_object_or_404(PostModel, id=post_id, author=request.user)
    post.delete()
    return redirect("dashboard")
