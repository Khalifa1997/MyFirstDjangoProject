from django.views import generic
from .models import board, thread, reply
from django.shortcuts import render, redirect, get_object_or_404
from .forms import NewReplyForm,NewThreadForm
from django.contrib.auth.decorators import login_required
import datetime

class IndexView(generic.ListView):
    template_name = 'forums/boards.html'
    context_object_name = 'boards'
    def get_queryset(self):
        return board.objects.all()

class BoardDetailView(generic.DetailView):
    template_name = 'forums/threads.html'
    context_object_name = 'threads'
    def get_queryset(self):
        return thread.objects.filter(board=pk).order_by('-date')

class ThreadDetailView(generic.DetailView):
    template_name = 'forums/boards.html'
    context_object_name = 'replies'
    def get_queryset(self):
        boardx = get_object_or_404(board,pk=pk)
        threads = thread.objects.filter(board=boardx.pk)
        #threadx= threads.objects.get(pk=pk2)
        threadx= get_object_or_404(threads,pk=pk2)
        return reply.objects.filter(thread=threadx.pk ).order_by('-date')

@login_required
def newThread(request , pk):
    boardX= get_object_or_404(board,pk=pk)
    if request.method== 'POST':
        form = NewThreadForm(request.POST)
        if form.is_valid():
            new_thread= form.save(commit=false)
            new_thread.date=datetime.date.today()
            new_thread.board=boardX
            new_thread.author=request.user.username
            new_thread.save()
            return redirect('threads', pk=boardX.pk)
    else:
        form = NewThreadForm()
    return render(request, 'forums/CreateThread.html', {'form': form})

@login_required
def newReply(request , pk):
    threadx= get_object_or_404(thread,pk=pk)
    if request.method== 'POST':
        form = NewReplyForm(request.POST)
        if form.is_valid():
            new_reply= form.save(commit=false)
            new_reply.date=datetime.datetime.now()
            new_reply.thread=threadx
            new_reply.created_by=request.user.username
            new_reply.save()
            return redirect('replies', pk=threadx.pk)  # TODO: redirect to the crea
    else:
        form = NewReplyForm()
    return render(request, 'forums/CreateReply.html', {'form': form})