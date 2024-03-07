from django.shortcuts import render, get_object_or_404
from user_auth.models import Person, Family

# Create your views here.
def dashboard(request):
    person = get_object_or_404(Person, user=request.user)
    family_persons = Family.list_members(person)[:4]
    return render(request, "dashboard/dashboard.html", {"members": family_persons})