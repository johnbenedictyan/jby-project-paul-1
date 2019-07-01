from django.shortcuts import render,redirect
from fault_submission.models import fault
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, authenticate
from .forms import RegisterUserForm,LoginForm

def sign_up(request):
    if request.method == 'GET':
        sign_up_form = RegisterUserForm()
        return render(request,
                      'signup.html', 
                      {
                          'sign_up_form': sign_up_form
                      }
                     )
    else:
        dirty_sign_up_form = UserCreationForm(request.POST)
        if dirty_sign_up_form.is_valid():
            dirty_sign_up_form.save()
            username = dirty_sign_up_form.cleaned_data.get('username')
            raw_password = dirty_sign_up_form.cleaned_data.get('password1')
            user = authenticate(
                username=username, 
                password=raw_password
            )
            login(
                request, 
                user
            )
            return redirect('/')
        else:
            messages.error(
                request,
                "We are unable to create your account!"
            )
            return(request,
                  'signup.html',
                  {
                      'sign_up_form':dirty_sign_up_form
                  })

def sign_in(request):
    if request.method == "GET":
        sign_in_form = LoginForm()
        return render(request,
                     'signin.html',
                     {
                         'sign_in_form':sign_in_form
                     }
                     )
    else:
        input_username = request.POST.get('username')
        input_password = request.POST.get('password')
        user = auth.authenticate(
            username=input_username, 
            password=input_password
        )
        if user is not None:
            auth.login(
                user=user, 
                request=request
            )
            messages.success(
                request, 
                "Welcome back"
            )
            return redirect("/")
        else:
            messages.error(
                request, 
                "Invalid Login"
            )
            return redirect("/sign_in/")
        return

@login_required
def sign_out(request):
    auth.logout(request)
    messages.success(request, "You have successfully logged out")
    return redirect("/")

@login_required
def admin_panel(request):
    all_faults = fault.objects.all()
    return render(
        request,
        "index.html",
        {
            "all_faults":all_faults
        }
    )

def follow_up(request,fault_id):
    requested_fault = fault.objects.get(pk=fault_id)
    if requested_fault.followed_up is True:
        requested_fault.followed_up = False
        requested_fault.save()
    else:
        requested_fault.followed_up = True
        requested_fault.save()
    return redirect("/")