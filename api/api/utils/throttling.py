from functools import wraps

from rest_framework.throttling import AnonRateThrottle, UserRateThrottle
from rest_framework.exceptions import Throttled

from ninja.errors import HttpError


def throttle_request(request, view):
    """
    Checks if a request should be throttled based on predefined rates.

    This function uses Django REST Framework's AnonRateThrottle and
    UserRateThrottle to check if a request exceeds the allowed rate
    limits. If the request is throttled, it raises a Throttled exception.

    :param request: The HTTP request object.
    :param view: The view function that the request is targeting.
    :raises Throttled: If the request exceeds the allowed rate.
    """

    throttle_classes = [AnonRateThrottle(), UserRateThrottle()]
    for throttle in throttle_classes:
        if not throttle.allow_request(request, view):
            raise Throttled(throttle.wait())


def throttle_view(view_func):
    """
    Decorator that applies throttling to a view function.

    This decorator integrates Django REST Framework's throttling
    functionality into Django Ninja views. It checks the request
    rate and raises an HttpError with a 429 status code if the
    request is throttled.

    Usage:
        @throttle_view
        def my_view(request):
            ...

    :param view_func: The view function to be decorated.
    :return: The wrapped view function with throttling applied.
    """

    @wraps(view_func)
    def _wrapped_view(request, *args, **kwargs):
        try:
            throttle_request(request, view_func)
        except Throttled as e:
            wait_time = e.wait if e.wait is not None else 0
            raise HttpError(
                429, f"Request was throttled. Try again in {int(wait_time)} seconds."
            )
        return view_func(request, *args, **kwargs)

    return _wrapped_view
