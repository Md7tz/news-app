from django.contrib.auth.mixins import (
  LoginRequiredMixin,
  UserPassesTestMixin,
  )
from django.views.generic import ListView, DetailView
from django.views.generic.edit import ( 
  CreateView,
  UpdateView,
  DeleteView, 
)
from django.urls import reverse_lazy
from .models import Article

class ArticleListView(LoginRequiredMixin, ListView):
  model = Article
  template_name = 'article_list.html'
  context_object_name = 'article_list'

class ArticleDetailView(LoginRequiredMixin, DetailView):
  model = Article
  template_name = 'article_detail.html' 
  context_object_name = 'article'

class ArticleCreateView(LoginRequiredMixin, CreateView):
  model = Article
  fields = ('title', 'body',)
  template_name = 'article_new.html' 
  context_object_name = 'article'

  def form_valid(self, form):
    form.instance.author = self.request.user
    return super().form_valid(form)

class ArticleUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
  model = Article
  fields = ('title', 'body',)
  template_name = 'article_edit.html' 
  context_object_name = 'article'

  def test_func(self):
    obj = self.get_object()
    return obj.author == self.request.user

class ArticleDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
  model = Article
  template_name = 'article_delete.html' 
  success_url = reverse_lazy('article_list')
  context_object_name = 'article'

  def test_func(self):
    obj = self.get_object()
    return obj.author == self.request.user
