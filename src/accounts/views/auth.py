from django.contrib.auth import logout, login
from django.shortcuts import redirect
from django.views.generic.edit import CreateView

from accounts.forms import MemberSignUpForm
from users.models import User


class UserSignUpView(CreateView):
    model = User
    form_class = MemberSignUpForm
    template_name = 'registration/signup_form.html'

    def get_context_data(self, **kwargs):
        kwargs['user_type'] = 'User'
        return super().get_context_data(**kwargs)

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return redirect('home')


def logout_view(request):
    logout(request)
    return redirect('home')



