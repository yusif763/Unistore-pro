from django.shortcuts import render,redirect
from contact.models import *
from checkout.forms import CheckoutForm 
from checkout.models import OrderItem
from django.views.generic import (
    ListView, DetailView, CreateView, TemplateView
)

from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from checkout.signals import send_form
# Create your views here.


def checkoutpage(request):
    form = CheckoutForm()
    if request.method == 'POST':
        form = CheckoutForm(data=request.POST)
        if form.is_valid():
            order = form.save(commit=False)
            order.author = request.user
            order.completed = True
            order.save()
            OrderItem.objects.filter(author = request.user).update(order = order.id , completed = True)
            send_form(instance = order)
            return redirect('/az/')
    context = {
        'form': form
    }
    return render(request , 'checkout.html' , context)





# class CheckoutView(CreateView):
#     form_class = CheckoutForm
#     template_name = 'checkout.html'

#     def form_valid(self, form):
#         form.instance.author = self.request.user
#         return super(CheckoutView, self).form_valid(form)
    
