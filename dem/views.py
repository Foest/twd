from django.shortcuts import render
from dem.models import DemUser
from dem.forms import DemUserForm, UserForm

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
