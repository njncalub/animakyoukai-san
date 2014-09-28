from django.core.urlresolvers import reverse
from django.contrib.auth.models import User
from django.contrib.auth.forms import AuthenticationForm
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.template import RequestContext
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.views import password_reset

from profiling.models import Person
from profiling.forms import PersonForm


def login_page(request):
    if request.user.is_authenticated():
        return HttpResponseRedirect(reverse('index_page'))

    context = {}
    context['title'] = "Log in"
    errors = []

    auth_form = AuthenticationForm()
    if request.method == "POST":
        auth_form = AuthenticationForm(request.POST)
        context['form'] = auth_form

        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(username=username, password=password)
        if user is not None:
            if user.is_active:
                login(request, user)
                return HttpResponseRedirect(reverse('index_page'))
            else:
                errors.append("Account is disabled.")
        else:
            errors.append("Invalid login credentials.")

    context['form'] = auth_form
    context['errors'] = errors

    return render(request,
                  "profiling/login.html",
                  context,
                  context_instance=RequestContext(request))

def registration_page(request):
    if request.user.is_authenticated():
        return HttpResponseRedirect(reverse('index_page'))

    context = {}
    context['title'] = "Register"

    errors = []

    if request.method == "POST":
        person_form = PersonForm(request.POST, request.FILES)

        if person_form.is_valid() and \
           person_form.cleaned_data['email_address'] != "" and \
           person_form.cleaned_data['last_name'] != "" and \
           person_form.cleaned_data['first_name'] != "":

            new_person = person_form.save(commit=False)
            new_person.save()

            username = ""
            for n in new_person.first_name.split():
                username += n[0]
            for n in new_person.middle_name.split():
                username += n[0]
            for n in new_person.last_name.split():
                username += n

            username = username.lower()

            try:
                user = User.objects.get(username=username)
                print "user already exists"
                username += "2"
            except User.DoesNotExist:
                print "does not exist"

            new_user = User.objects.create_user(username,
                                                new_person.email_address,
                                                new_person.email_address)
            new_user.last_name = new_person.last_name
            new_user.first_name = new_person.first_name
            new_user.save()

            return HttpResponseRedirect(reverse('index_page'))
        else:
            context['person_form'] = person_form

            if person_form.cleaned_data['last_name'] == "":
                errors.append("Last name must not be empty")
            if person_form.cleaned_data['first_name'] == "":
                errors.append("First name must not be empty")
            if person_form.cleaned_data['email_address'] == "":
                errors.append("Please enter a valid email address")

            context['errors'] = errors

            return render(request,
                          "profiling/join.html",
                          context,
                          context_instance=RequestContext(request))

    context['person_form'] = PersonForm()

    return render(request,
                  "profiling/join.html",
                  context,
                  context_instance=RequestContext(request))


def logout_page(request):
    logout(request)

    return HttpResponseRedirect(reverse('index_page'))

def reset_password_page(request):
    if request.method == 'POST':
        return password_reset(request,
            from_email=request.POST.get('email'))
    else:
        context = {}
        context['title'] = "Forgot password"

        return render(request,
                      'profiling/forgot.html',
                      context,
                        context_instance=RequestContext(request))

def index_page(request):
    if not request.user.is_authenticated():
        return HttpResponseRedirect(reverse('login_page'))

    context = {}
    context['title'] = "Update"

    if request.method == "POST":

        if Person.objects.filter(email_address=request.user.email).count():
            print "has person"
            person = Person.objects.get(email_address=request.user.email)
            person_form = PersonForm(request.POST or None, request.FILES or None, instance=person)
        else:
            print "has no person"
            person_form = PersonForm()

        if person_form.is_valid() and \
           person_form.cleaned_data['email_address'] != "" and \
           person_form.cleaned_data['last_name'] != "" and \
           person_form.cleaned_data['first_name'] != "":

            person_form.save()

            request.user.last_name = person_form.cleaned_data['last_name']
            request.user.first_name = person_form.cleaned_data['first_name']

            print "went here 1"

            context['person_form'] = person_form
            return render(request,
                "profiling/update.html",
                context,
                context_instance=RequestContext(request))
        else:
            if person_form.cleaned_data['last_name'] == "":
                errors.append("Last name must not be empty")
            if person_form.cleaned_data['first_name'] == "":
                errors.append("First name must not be empty")
            if person_form.cleaned_data['email_address'] == "":
                errors.append("Please enter a valid email address")

            context['errors'] = errors

            print "went here 2"

            context['person_form'] = person_form
            return render(request,
                "profiling/update.html",
                context,
                context_instance=RequestContext(request))

        context['person_form'] = person_form

    if Person.objects.filter(email_address=request.user.email).count():
        person = Person.objects.get(email_address=request.user.email)
        person_form = PersonForm(request.POST or None, instance=person)
    else:
        person_form = PersonForm()

    context['person_form'] = person_form

    return render(request,
                  "profiling/update.html",
                  context,
                  context_instance=RequestContext(request))
