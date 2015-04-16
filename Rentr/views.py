from django.template import RequestContext
from django.shortcuts import render_to_response
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect, HttpResponse

@login_required
def index(request):
    return render_to_response('rentr/index.html')

def user_login(request):
    context = RequestContext(request)
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(username=username, password=password)

        if user:
            if user.is_active:
                login(request, user)
                return HttpResponseRedirect('/')
            else:
                error = {'error': "Your account is disabled."}
                return render_to_response('registration/login.html', error, context)
        else:
            error = {'error': "Invalid username and/or password"}
            return render_to_response('registration/login.html', error, context)

    else:
        return render_to_response('registration/login.html', {}, context)


@login_required
def user_logout(request):
        logout(request)
        return HttpResponseRedirect('/')
