from django.shortcuts import render,redirect
from common.models import *
from common.forms import *
from django.views.generic import (
    ListView, DetailView
)
from django.views.generic.edit import FormMixin
from django.http import HttpResponseRedirect
from django.urls import reverse_lazy

# Create your views here.
# def blog_page(request):
#     blogs = Blog.objects.all().order_by('-created_at')[:6]
#     context = {
#         "blogs":blogs
#     }
#     return render(request, 'blog.html' , context)


def faq_page(request):
    return render(request , 'faq.html')

def home_page(request):
    form = SubscriberForm()
    if request.method == 'POST':
        form = SubscriberForm(data = request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')
    context = {
        "form":form
    }
    return render(request , 'index.html', context)

# def item_photo(request,pk):
#     blog = Blog.objects.get(pk = pk)
#     form = CommentForm()
#     comments = Comment.objects.all()
#     parent_comments = Comment.objects.filter(parent_comment__isnull = True , blog = blog)
#     if request.method == 'POST':
#         form = CommentForm(data = request.POST)
#         if form.is_valid():
#             form.instance.blog = blog
#             form.save()
#             return redirect(f'/item-photo/{pk}')
#     context={
#         "comments":comments,
#         "parent_comments":parent_comments,
#         "blog":blog,
#         "form":form
#     }
#     return render(request , 'item-photo.html', context)







class BlogListView(ListView):
    model = Blog
    template_name = 'blog.html'
    paginate_by = 2
    context_object_name = 'blogs'
    # queryset = Recipe.objects.filter(is_published=True)

    def get_queryset(self):
        queryset = super().get_queryset()
        tags = self.request.GET.get('tags')
        print(tags)
        
        if tags:
            queryset = queryset.filter(tags__id=tags)
        return queryset
   

class BlogDetailView(FormMixin,DetailView):
    model = Blog
    form_class = CommentForm
    template_name = 'item-photo.html'
    context_object_name = 'blog'
    

    def get_success_url(self , **kwargs):
        return reverse_lazy('common:blog_detail' , kwargs = {'pk': self.object.pk})

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        blog = self.object
        context['parent_comments'] = Comment.objects.filter(parent_comment__isnull = True , blog = blog)
        return context

    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        form = self.get_form()
        print(request.POST)
        if form.is_valid():
            # <process form cleaned data>
            form.instance.blog = self.object
            form.instance.author = self.request.user
            form.save()
            return self.form_valid(form)
        else:
            print('invalid form')
            return self.form_invalid(form)
        return render(request, self.template_name, {'form': form})
