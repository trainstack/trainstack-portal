from django.contrib import auth
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, render_to_response
from django.contrib.auth.models import User, Group
from trainstack_portal.forms import CreateUserForm, CreateGroupForm
from django.http import HttpResponse
from django.template import Context, loader
from trainstack_portal.models import topology

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
def someview(request):
   return render_to_response('profile.html')

@login_required
def crtuser(request):
    form=CreateUserForm(request.POST)
    if form.is_valid():
        form.save()
    users=User.objects.all()
    templates={'form': form, 'users': users}
    return render(request, "prof.html", templates)

@login_required
def crtgroup(request):
    form=CreateGroupForm(request.POST)
    if form.is_valid():
        form.save()
    groups=Group.objects.all()
    templates={'form': form, 'groups': groups}
    return render(request, "prof.html", templates)    

@login_required
def display(request):
    grp=User.objects.select_related().all()
    top=topology.objects.select_related().all()
    return render(request,'displ.html', {
        "grp": grp, "top": top,
    })

@login_required
def topo(request):
    return render(request,'topo.html')   

@login_required
def tsk(request):
    return render(request,'tsk.html')   
