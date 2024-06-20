from functools import wraps

from rest_framework.throttling import AnonRateThrottle, UserRateThrottle
from rest_framework.exceptions import Throttled

from ninja.errors import HttpError


def throttle_request(request, view):
    throttle_classes = [AnonRateThrottle(), UserRateThrottle()]
    for throttle in throttle_classes:
        if not throttle.allow_request(request, view):
            raise Throttled(throttle.wait())


def throttle_view(view_func):
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
