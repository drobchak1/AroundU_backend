from django.contrib.auth import get_user_model
from django.contrib.contenttypes.models import ContentType

from .models import Visitors

User = get_user_model()

def add_visit(obj, user):
    """Visit event.
    """
    obj_type = ContentType.objects.get_for_model(obj)
    visit, is_created = Visitors.objects.get_or_create(
        content_type=obj_type, object_id=obj.id, user=user)
    return visit

def remove_visit(obj, user):
    """Unvisit event.
    """
    obj_type = ContentType.objects.get_for_model(obj)
    Visitors.objects.filter(
        content_type=obj_type, object_id=obj.id, user=user
    ).delete()

def is_fan(obj, user) -> bool:
    """Check if user visit event
    """
    if not user.is_authenticated:
        return False
    obj_type = ContentType.objects.get_for_model(obj)
    visitors = Visitors.objects.filter(
        content_type=obj_type, object_id=obj.id, user=user)
    return visitors.exists()

def get_visitors(obj):
    """Get all users, who visited event
    """
    obj_type = ContentType.objects.get_for_model(obj)
    return User.objects.filter(
        visitors__content_type=obj_type, visitors__object_id=obj.id)
