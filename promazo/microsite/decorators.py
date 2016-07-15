from functools import wraps

from django.http import HttpResponseRedirect


def redirect_if_logged_in(redirect_url):
    """
    Decorator for views that checks that the user is logged in, redirecting
    to another page if loggued in
    """
    def decorator(func):
        def inner_decorator(request, *args, **kwargs):
            # If there is a user and it is authenticated
            if request.user and request.user.is_authenticated():
                return HttpResponseRedirect(redirect_url)
            else:
                return func(request, *args, **kwargs)
        return wraps(func)(inner_decorator)
    return decorator