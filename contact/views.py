from django.shortcuts import render,redirect
from contact.models import *
from contact.forms import ContactForm
from django.views.generic import (
    ListView, DetailView,CreateView
)
from django.views.generic.edit import FormMixin
from django.http import HttpResponseRedirect
from django.urls import reverse_lazy



# Create your views here.
# def about_contact(request):
#     form = ContactForm()
#     # sub_form = SubscriberForm()
#     if request.method == 'POST':
#         form = ContactForm(data=request.POST)
#         if form.is_valid():
#             form.save()
#             return redirect('/about-contact/')
#     context = {
#         # "sub_form":sub_form,
#         'form': form
#     }
#     return render(request , 'about_contact.html' , context)


class AboutContactView(CreateView):
    form_class = ContactForm
    # fields = '__all__'
    # model = Contact
    template_name = 'about_contact.html'
    success_url = reverse_lazy('common:index')

    def form_valid(self, form):
        result = super(ContactView, self).form_valid(form)
        messages.success(self.request, 'Sizin muracietiniz qebul edildi.')
        return result


# def contact_page(request):
#     form = ContactForm()
#     # sub_form = SubscriberForm()
#     if request.method == 'POST':
#         form = ContactForm(data=request.POST)
#         if form.is_valid():
#             form.save()
#             return redirect('/contact/')
#     context = {
#         # "sub_form":sub_form,
#         'form': form
#     }
#     return render(request, "contact.html", context)



class ContactView(CreateView):
    form_class = ContactForm
    # fields = '__all__'
    # model = Contact
    template_name = 'contact.html'
    success_url = reverse_lazy('common:index')

    def form_valid(self, form):
        result = super(ContactView, self).form_valid(form)
        messages.success(self.request, 'Sizin muracietiniz qebul edildi.')
        return result

