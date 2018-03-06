from django.shortcuts import render
from . import models
from django.urls import reverse_lazy
from . import forms
from django.views.generic import CreateView, UpdateView
# Create your views here.


class isUserMixin(object):
    """
    Mixin providing a dispatch overload that checks object ownership. is_staff and is_supervisor
    are considered object owners as well. This mixin must be loaded before any class based views
    are loaded for example class SomeView(OwnershipMixin, ListView)
    """
    def dispatch(self, request, *args, **kwargs):
        self.request = request
        self.args = args
        self.kwargs = kwargs
        # we need to manually "wake up" self.request.user which is still a SimpleLazyObject at this point
        # and manually obtain this object's owner information.
        current_user = request.user
        object_owner = getattr(self.get_object(), 'user')
        print(object_owner)
        print(self.get_object())
        if current_user.username != object_owner.username:
            raise PermissionDenied
        return super(isUserMixin, self).dispatch(request, *args, **kwargs)


class SignUp(CreateView):
    form_class = forms.UserCreateForm
    template_name = 'accounts/signup.html'
    success_url = reverse_lazy('accounts:login')


class EditInfo(isUserMixin, UpdateView):
    template_name='accounts/editInfo.html'
    model = models.UserAccount
    fields = ('profilePic', 'aboutMe')
