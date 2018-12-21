from django.http import HttpResponseRedirect
from django.shortcuts import reverse

def anonymous_required(meat):
    """
    Redirects the user to domain overview if already logged in.
    """
    def wrap(request, *args, **kwargs):
        if not request.user.is_authenticated:
            return meat(request, *args, **kwargs)
        return HttpResponseRedirect('/')
    wrap.__doc__ = meat.__doc__
    wrap.__name__ = meat.__name__
    return wrap