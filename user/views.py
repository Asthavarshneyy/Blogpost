from django.shortcuts import render,redirect
from user.forms import RegisterForm,LoginForm
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth import login,authenticate,logout
from django.urls import reverse_lazy
from django.views.generic.edit import FormView
from django.contrib.auth.forms import UserCreationForm


# Create your views here.

# class register(FormView):
#     template_name='register.html'
#     form_class=RegisterForm
#     success_url='/ /'
#     def form_valid(self, form):
#         if form.is_valid():
#             username = form.cleaned_data.get("username")
#             password = form.cleaned_data.get("password")

#             newUser = User(username =username)
#             newUser.set_password(password)

#             newUser.save()
#             login(form,newUser)
#             messages.info(self,"Registered Successfully")

#             return redirect("index")
#         context = {
#                 "form" : form
#             }
#         return render(self,"register.html",context)

# class RegisterView(FormView):
#     template_name = 'register.html'
#     form_class = RegisterForm
#     redirect_authenticated_user = True
#     success_url = reverse_lazy('tasks')
    
#     def form_valid(self, form):
#         user = form.save()
#         if user:
#             login(self.request, user)
        
#         return super(RegisterView, self).form_valid(form)

def register(request):

    form = RegisterForm(request.POST or None)
    if form.is_valid():
        username = form.cleaned_data.get("username")
        password = form.cleaned_data.get("password")

        newUser = User(username =username)
        newUser.set_password(password)

        newUser.save()
        login(request,newUser)
        messages.info(request,"Registered Successfully")

        return redirect("index")
    context = {
            "form" : form
        }
    return render(request,"register.html",context)

    
    
def loginUser(request):
    form = LoginForm(request.POST or None)

    context = {
        "form":form
    }

    if form.is_valid():
        username = form.cleaned_data.get("username")
        password = form.cleaned_data.get("password")

        user = authenticate(username = username,password = password)

        if user is None:
            messages.info(request,"Incorrect details")
            return render(request,"login.html",context)

        messages.success(request,"Logged In successfully")
        login(request,user)
        return redirect("index")
    return render(request,"login.html",context)

def logoutUser(request):
    logout(request)
    messages.success(request,"Logged Out successfully")
    return redirect("index")
