from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from product.models import *
from product.forms import *
from django.views.generic import (
    ListView, DetailView
)
from django.views.generic.edit import FormMixin
from django.http import HttpResponseRedirect
from django.urls import reverse_lazy
# Create your views here.


# @login_required
# def product_list(request):
#     products = Product.objects.order_by('created_at')[:9]
#     images = Image.objects.all()
#     categories  = Category.objects.all()
#     tags = Tag.objects.all()
#     brands = Brands.objects.all()
#     screensizes = ScreenSize.objects.all()
#     context = {
#         "products":products,
#         "images":images,
#         "tags":tags,
#         "categories": categories,
#         "brands":brands,
#         "screensizes":screensizes
#     }
#     return render(request , 'product-list.html' , context)


# def product_page(request,pk):
#     product = Product.objects.get(pk = pk)
#     form = ReviewForm()
#     categories  = Category.objects.all()
#     prodspecnames = ProductSpecName.objects.filter(category = product.category)
#     productspecdescs = ProductSpecDesc.objects.filter(product = product).filter(prod_spec_name__in = prodspecnames)
#     reviews = Review.objects.all()
#     products2 = Product.objects.order_by('-created_at')[:4]
#     parent_comments = Review.objects.filter(parent_comment__isnull = True , product = product)
#     if request.method == 'POST':
#         form = ReviewForm(data = request.POST)
#         if form.is_valid():
#             form.instance.product = product
#             form.save()
#             return redirect(f'/product/{pk}')
#     context = {
#         "parent_comments":parent_comments,
#         "product":product,
#         "categories": categories,
#         "prodspecnames":prodspecnames,
#         "productspecdescs":productspecdescs,
#         "reviews":reviews,
#         "products2":products2,
#         "form":form

#     }
#     return render(request , 'product.html', context)


    



class ProductListView(ListView):
    model = Product
    template_name = 'product-list.html'
    paginate_by = 2
    context_object_name = 'products'
    # queryset = Recipe.objects.filter(is_published=True)

    def get_queryset(self):
        queryset = super().get_queryset()
        tags = self.request.GET.get('tags')
        print(tags)
        
        if tags:
            queryset = queryset.filter(tags__id=tags)
        return queryset
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['tags'] = Tag.objects.all()
        context['images'] = Image.objects.all()
        context['categories'] = Category.objects.all()
        context['brands'] = Brands.objects.all()
        context['screensizes'] = ScreenSize.objects.all()
        return context


class ProductDetailView(FormMixin,DetailView):
    model = Product
    form_class = ReviewForm
    template_name = 'product.html'
    context_object_name = 'product'
    

    def get_success_url(self , **kwargs):
        return reverse_lazy('product:product_detail' , kwargs = {'pk': self.object.pk})

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        product = self.object
        prodspecnames = ProductSpecName.objects.filter(category = product.category)
        context['parent_comments'] = Review.objects.filter(parent_comment__isnull = True , product = product)
        context['categories'] = Category.objects.all()
        context['prodspecnames'] = ProductSpecName.objects.filter(category = product.category)
        context['productspecdescs'] = ProductSpecDesc.objects.filter(product = product).filter(prod_spec_name__in = prodspecnames)
        context['products2'] = Product.objects.order_by('-created_at')[:4]
        return context

    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        form = self.get_form()
        print(request.POST)
        if form.is_valid():
            # <process form cleaned data>
            form.instance.product = self.object
            form.instance.author = request.user
            form.save()
            return self.form_valid(form)
        else:
            print('invalid form')
            return self.form_invalid(form)
        return render(request, self.template_name, {'form': form})



