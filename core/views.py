from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.views.generic import CreateView,ListView,DetailView,CreateView,FormView
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from.models import Services,Appointement
from .forms import Appointmentform



@login_required
def home(request):
    return render(request,"core/index.html",{'abc':"hello world"})

class Services_list(ListView):
    model = Services

class Servicetype_detail(DetailView):
    model = Services


# class ABC(FormView):
#     template_name = 'core/services_html'
#     form_class = SearchForm
  
#     def form_valid(self,request):
#         query = form.cleaned_data.get('query',None)
#         print(query)
#         return render(self.request,self.template_name)


@login_required
def appointmentform(request):
    template = 'core/appointement_form.html'
    usr = request.user
    srvc = request.GET.get('query', '')
    print(srvc)

    form = Appointmentform(request.POST)
    if form.is_valid():
        abc = form.save(commit=False)
        abc.user = usr
        abc.service = srvc
        abc.save()
        return redirect('home')
    return render(request,template,{'form':form})



class SignUp(CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'registration/signup.html'