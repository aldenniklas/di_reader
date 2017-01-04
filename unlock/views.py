# coding=utf-8

from django.shortcuts import render
from .forms import UnlockForm
from .models import print_article

def index(request):
    # Form post
    if request.method == 'POST':
        form = UnlockForm(request.POST)
        
        if form.is_valid():
            article = form.cleaned_data['article']
            return unlocked_article(request, article)
        
    else:
        form = UnlockForm()
    
    template = 'unlock/index.html'
    context = {'form': form}
    return render(request, template, context)
    
def unlocked_article(request, article):
    template = 'unlock/unlocked_article.html'
    context = print_article(article)
    return render(request, template, context)
    