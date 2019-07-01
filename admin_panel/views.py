from django.shortcuts import render,redirect
from fault_submission.models import fault

# Create your views here.
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