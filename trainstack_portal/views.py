from django.contrib import auth
from django.contrib.auth.decorators import login_required
from django.http.response import HttpResponseRedirect
from django.shortcuts import render
from django.contrib.auth.models import User, Group
from trainstack_portal import settings
from trainstack_portal.forms import CreateUserForm, CreateGroupForm
from trainstack_portal.models import Topology

def login(request):
    username = request.POST['username']
    password = request.POST['password']
    user = auth.authenticate(username=username, password=password)
    if user is not None and user.is_active:
        auth.login(request, user)
        return HttpResponseRedirect(request.GET.get('next', settings.LOGIN_REDIRECT_URL))

def logout(request):
    auth.logout(request)
    return HttpResponseRedirect("/login")

@login_required
def createUser(request):
    form=CreateUserForm(request.POST)
    if form.is_valid():
        form.save()
    users=User.objects.all()
    templates={'form': form, 'users': users}
    return render(request, "general_form.html", templates)

@login_required
def createGroup(request):
    form=CreateGroupForm(request.POST)
    if form.is_valid():
        form.save()
    groups=Group.objects.all()
    templates={'form': form, 'groups': groups}
    return render(request, "general_form.html", templates)

@login_required
def groups(request):
    grp=User.objects.select_related().all()
    top=Topology.objects.select_related().all()
    return render(request,'groups.html', {
        "grp": grp, "top": top,
    })

@login_required
def topologies(request):
    return render(request,'topology.html')

@login_required
def topology(request, id):
    return render(request,'topology.html')

@login_required
def tasks(request):
    return render(request,'tasks.html')
