from django.views import generic
from .models import comment, article
from django.shortcuts import render, redirect, get_object_or_404
from .forms import NewArticleForm, NewCommentForm

class IndexView(generic.ListView):
    template_name = 'newspaper/newspaper.html'
    context_object_name = 'articles'
    def get_queryset(self):
        return article.objects.order_by('-date')

def new_article(request):
    #article = get_object_or_404(article, pk=pk)
    #return render(request, 'CreatePost.html', {'article': article})
    if request.method == 'POST':
        form = NewArticleForm(request.POST)
        if form.is_valid():
            topic = form.save()
            return redirect('index')
    else:
        form = NewArticleForm()
    return render(request, 'newspaper/CreatePost.html', {'form': form})

def new_comment(request, pk):
    articles = get_object_or_404(article, pk=pk)
    #ret*urn render(request, 'CreatePost.html', {'article': article})
    if request.method == 'POST':
        form = NewCommentForm(request.POST)
        if form.is_valid():
            topic = form.save(commit=False)
            topic.main_article = articles
            
            topic.save()
            
            return redirect('articledetails', pk=articles.pk)  # TODO: redirect to the crea
    else:
        form = NewCommentForm()
    return render(request, 'newspaper/CreateComment.html', {'form': form})

class ArticleDetailsView(generic.DetailView):
    template_name='newspaper/details.html'
    context_object_name = 'article'
    
    def get_queryset(self):
        return article.objects.order_by('-date')


def Delete(request, pk):
    x=get_object_or_404(article, pk=pk)
    x.delete()
    return render(request, 'newspaper/delete.html')