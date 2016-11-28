from django.shortcuts import render
from dem.models import DemUser, Assignment, Mission
from dem.forms import DemUserForm, UserForm
from django.contrib.auth import authenticate, login
from django.core.urlresolvers import reverse
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth.decorators import login_required

def index(request):
    context_dict = {}
    return render(request, 'dem/index.html', context_dict)

def register(request):
    registered = False
    if request.method == "POST":
        user_form = UserForm(data=request.POST)
        dem_user_form = DemUserForm(data=request.POST)

        if user_form.is_valid() and dem_user_form.is_valid():
            user = user_form.save()
            user.set_password(user.password)
            user.save()

            dem_user = dem_user_form.save(commit=False)
            dem_user.user = user
            dem_user.save()
            registered = True
        else:
            print(user_form.errors, dem_user_form.errors)
    else:
        user_form = UserForm()
        dem_user_form = DemUserForm()
    return render(request,
                  'dem/register.html',
                  {'user_form': user_form,
                   'dem_user_form': dem_user_form,
                    'registered': registered})

@login_required
def my_assignments(request):
    context_dict = {}
    dem_user = DemUser.objects.get(user=request.user)
    if request.user.is_active:
        context_dict['assignments'] = get_user_assignments(dem_user)
        return render(request, 'dem/my_assignments.html', context_dict)
    else:
        return HttpResponse("You are not logged in!")

def show_mission(request, mission_name_slug):
    context_dict = {}
    try:
        mission = Mission.objects.get(slug=mission_name_slug)
        context_dict['mission'] = mission
    except Mission.DoesNotExist:
        context_dict['mission'] = None
    return render(request, 'dem/mission.html', context_dict)

# def assignment(request):
#     if request.method == "POST":
#         username = request.POST.get('username')
#         password = request.POST.get('password')
#         user = authenticate(username=username, password=password)
#
#         if user:
#             if user.is_active:
#                 login(request, user)
#                 return HttpResponseRedirect(reverse('dem:index'))
#             else:
#                 return HttpResponse('Your Dem account is not active.')
#         else:
#             print('Invalid login details {0}, {1}'.format(username, password))
#             return HttpResponse("Invalid login details supplied")
#     else:
#         return render(request, 'dem/login.html', {})

# def dem_login(request):
#     if request.method == "POST":
#         username = request.POST.get('username')
#         password = request.POST.get('password')
#         user = authenticate(username=username, password=password)
#
#         if user:
#             if user.is_active:
#                 login(request, user)
#                 return HttpResponseRedirect(reverse('dem:index'))
#             else:
#                 return HttpResponse('Your Dem account is not active.')
#         else:
#             print('Invalid login details {0}, {1}'.format(username, password))
#             return HttpResponse("Invalid login details supplied")
#     else:
#         return render(request, 'dem/login.html', {})

def get_user_assignments(dem_user):
        return Assignment.objects.filter(assignee=dem_user)
