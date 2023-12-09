from django.shortcuts import render
from django import http
from django.forms.models import BaseModelForm
from django.http import HttpResponse, FileResponse
from django.shortcuts import render, get_object_or_404
from django.views.generic import TemplateView, CreateView, UpdateView, DeleteView, ListView, DetailView
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
import os

from .models import Post


# Create your views here.
class BlogCreate(LoginRequiredMixin, CreateView):
    model = Post
    fields = ['subject','content','background']

    def form_valid(self,form):
        form.instance.author = self.request.user
        return super().form_valid(form)

class BlogUpdate(LoginRequiredMixin, UpdateView):
    template_name = "pestpoge/post_update.html"
    model = Post
    fields = ['subject','content','background']

    def dispatch(self, request, *args, **kwargs):
        obj = self.get_object()
        if obj.author == self.request.user:
            return super(BlogUpdate, self).dispatch(request, *args, **kwargs)
        else:
            return render(request, 'somethingerror.html')
        
class BlogDelete(LoginRequiredMixin, DeleteView):
    model = Post
    success_url = reverse_lazy('blog:blog_list')

    def dispatch(self, request, *args, **kwargs):
        obj = self.get_object()
        if obj.author == self.request.user:
            return super(BlogDelete, self).dispatch(request, *args, **kwargs)
        else:
            return render(request, 'somethingerror.html')
        
class BlogList(ListView):
    model = Post
    context_object_name = 'all_post'

class BlogDetail(DetailView):
    model = Post
