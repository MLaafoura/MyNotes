from django.shortcuts import render
from django.urls import reverse_lazy 
from django.shortcuts import redirect
from django.views.generic import  DetailView , ListView , CreateView , DeleteView , UpdateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import LoginView
from django.contrib import messages
from .models import MyNotes
from django.contrib.auth.models import User
from django.shortcuts import (get_object_or_404,
                              render,
                              HttpResponseRedirect)

from .forms import RegisterForm


class LoginCheck(LoginView):
    template_name="login.html"
    redirect_authenticated_user = True
    
    def get_success_url(self):
        return reverse_lazy('homepage') 
    
    def form_invalid(self, form):
        messages.error(self.request,'Invalid username or password')
        return self.render_to_response(self.get_context_data(form=form))
    

class HomePage(LoginRequiredMixin,ListView):
    model = MyNotes
    template_name ="home.html"
    context_object_name = "notes"

    def get_queryset(self):
        queryset = super().get_queryset()
        queryset = queryset.filter(user=self.request.user)
        return queryset

class CreateNote(LoginRequiredMixin , CreateView):
    model = MyNotes
    template_name = "AddNote.html"
    fields=['title','note']

    success_url = reverse_lazy('homepage')
    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

class DeleteNote(LoginRequiredMixin , DeleteView):
    model = MyNotes
    template_name ="ConfirmDelete.html"
    context_object_name = "obj"
    def get_success_url(self):
        return reverse_lazy('homepage')
    

class UpdateNote(LoginRequiredMixin , UpdateView):
    model = MyNotes
    template_name = "AddNote.html"
    fields = ['title','note']
    context_object_name ="noteupdate"
    def get_success_url(self):
        return reverse_lazy('homepage')
    

class DetailNote(LoginRequiredMixin , DetailView):
    model = MyNotes
    template_name ="notedetail.html"
    fields =['title','note']
    context_object_name ="mynote"


"""class Signmeup(CreateView):
    model = User
    template_name = "signup.html"
    fields = ['username','password']
    success_url = reverse_lazy('signin')
"""

def sign_up(request):
    if request.method == 'GET':
        form = RegisterForm()
        return render(request, 'signup.html', {'form': form})    
   
    if request.method == 'POST':
        form = RegisterForm(request.POST) 
        if form.is_valid():
            user = form.save(commit=False)
            user.username = user.username.lower()
            user.save()
            messages.success(request, 'You have singed up successfully.')
   
            return redirect('signin')
        else:
            return render(request, 'signup.html', {'form': form})