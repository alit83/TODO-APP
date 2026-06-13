from django.shortcuts import  get_object_or_404 , redirect
from django.views.generic import ListView  , CreateView , DeleteView ,View
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



class DoneView(View, LoginRequiredMixin):
    def post(self,request,pk):
        Planer.objects.create(user=request.user , done=Planer.objects.get(pk=pk).task)
        task=get_object_or_404(Planer,pk=pk)
        task.delete()
        return redirect('/')
        
        
class deleteView(DeleteView , LoginRequiredMixin):
    model = Planer
    success_url= '/'
    http_method_names = ['post']

    
    
