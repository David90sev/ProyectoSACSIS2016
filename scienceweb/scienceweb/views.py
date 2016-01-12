from django.shortcuts import render
from django.views.generic.base import TemplateView
from users.models import YoungInvestigator, PrincipalInvestigator
from django.contrib.auth import authenticate, login, logout

# Create your views here.

def login(request):
    username = request.POST['username']
    password = request.POST['password']
    user = authenticate(username=username, password=password)
    if user is not None:
        if user.is_active:
            login(request, user)
            # Redirect to a success page.
        else:
            # Return a 'disabled account' error message
#             ...


def logout_view(request):
    logout(request)
    # Redirect to a success page.


    