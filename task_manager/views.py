from django.shortcuts import render

from .forms import CommentArticleForm



def index(request, *args, **kwargs):
    form = CommentArticleForm()
    return render(request, 'index.html', {'form': form})
