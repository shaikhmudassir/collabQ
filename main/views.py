from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.views import View
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Issue, Assign

class HomeView(LoginRequiredMixin,View):
  
  login_url = '/login'

  def get(self, request):

    issues = Issue.objects.all()
    return render(request, 'main/home.html', {"issues":issues, "page":"home"})

class DashboardView(LoginRequiredMixin,View):
  
  login_url = '/login'

  def get(self, request):
    issues = Issue.objects.filter(id__in=Assign.objects.filter(user_id=request.user.id))
    return render(request, 'main/home.html', {"issues":issues, "page":"dashboard"})

class RegisterView(View):

  def get(self, request):
    if not request.user.is_authenticated:
      return render(request, 'main/register.html', {})
    else:
      return HttpResponseRedirect('/')

  def post(self, request, *args, **kwargs):
    
    first_name = request.POST['first_name']
    last_name = request.POST['last_name']
    email = request.POST['email']
    password = request.POST['password']
    username = email.split('@')[0]
    
    user = User.objects.create_user(first_name=first_name, last_name=last_name, email=email, username=username, password=password)
    user.save()
    return HttpResponseRedirect('login')


class LoginView(View):

  def get(self, request):
    if not request.user.is_authenticated:
      return render(request, 'main/login.html', {})
    else:
      return HttpResponseRedirect('/')

  def post(self, request, *args, **kwargs):
    email = request.POST['email']
    password = request.POST['password']
    username = email.split('@')[0]

    user = authenticate(username=username, password=password)
    if user is not None:
      login(request, user)
      return HttpResponseRedirect('/')
    else:
      return HttpResponseRedirect('login')

class CreateView(LoginRequiredMixin,View):
  
  login_url = '/login'

  def get(self, request):
    return render(request, 'main/create_issue.html', {})
  
  def post(self, request, *args, **kwargs):

    title = request.POST['title'] 
    message = request.POST['message']
    complexity = request.POST['complexity']
    deadline = request.POST['deadline'] 

    issue = Issue(title=title, message=message, complexity=complexity, deadline=deadline, raised_by=request.user)
    issue.save()
    
    return HttpResponseRedirect('/')

class AssignView(LoginRequiredMixin,View):
  
  login_url = '/login'

  def get(self, request):
    
    issue_id = request.GET["picked"]
    issue = Issue.objects.get(id=issue_id)

    assigned = Assign(user_id=request.user, issue_id=issue)
    assigned.save()

    issue.status = 2
    issue.save()

    return HttpResponseRedirect('/')

class CompleteView(LoginRequiredMixin,View):
  
  login_url = '/login'

  def get(self, request):
    
    issue_id = request.GET["complete"]
    issue = Issue.objects.get(id=issue_id)

    issue.status = 3
    issue.save()

    return HttpResponseRedirect('dashboard')
  
class LogoutView(View):

  def get(self, request):
    logout(request)
    return HttpResponseRedirect('login')