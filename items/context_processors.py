# items/context_processors.py

from items.utils import get_notifications


def notifications(request):
    return {"notifications": get_notifications(request.user)}
