from django.shortcuts import render,redirect,render_to_response
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .models import fault
from .forms import fault_form
from condo_fault_project import settings

def csrf_failure(request, reason=""):
    messages.error(
                request,
                "Login form has expired. Please try again."
            )
    return redirect("/")
    
def fault_submission(request):
    if request.method=="GET":
        new_fault_form = fault_form()
        return render(
            request,
            "fault_form.html",
            {
                "fault_form":new_fault_form
            }
        )
    else:
        dirty_fault_form = fault_form(request.POST,request.FILES)
        if dirty_fault_form.is_valid():
            dirty_fault_form.save()
            messages.success(
                request,
                "The report has been successfully created!"
            )
            return redirect("/")
        else:
            messages.error(
                request,
                "We are unable to create your report!"
            )
            return render(
                request,
                "fault_form.html",
                {
                    "fault_form":dirty_fault_form
                }
            )
            
