from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404, redirect, render

from users.decorators import members_required
from accounts.models import Member

@login_required
@members_required
def profile(request, slug):
    template_name = 'members/home.html'
    context = {}
    member = Member.objects.get(slug=slug)
    return render(request, template_name, context)
