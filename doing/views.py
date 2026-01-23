from django.shortcuts import render
from django.views.generic import ListView , UpdateView , CreateView , DeleteView 
from .models import Planer
from django.contrib.auth.mixins import LoginRequiredMixin
# Create your views here.







class todoView(LoginRequiredMixin,ListView ):
    model = Planer
    context_object_name = 'tasks'
    login_url = '/account/login/'

class createView(LoginRequiredMixin,CreateView ):
    model = Planer
    success_url ='/'
    fields = ['task']
    template_name = 'doing/planer_list.html'
    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)



class updateView(UpdateView, LoginRequiredMixin):
    model = Planer
    success_url ='/'
    fields = ['task']
    template_name = 'doing/planer_list.html'
    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)
    
class deleteView(DeleteView , LoginRequiredMixin):
    model = Planer
    success_url= '/'
    http_method_names = ['post']

    
    
