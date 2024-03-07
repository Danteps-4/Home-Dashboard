from django.shortcuts import render, get_object_or_404
from django.contrib.auth.models import User
from user_auth.models import Person, Family

# Create your views here.
def member(request):
    person = get_object_or_404(Person, user=request.user)
    family_persons = Family.list_members(person)
    return render(request, "member/member.html", {"members": family_persons})

def add_member(request):
    return render(request, "member/add.html")