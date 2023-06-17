from django.contrib.auth.backends import ModelBackend
from django.contrib.auth import get_user_model
from django.db.models import Q


User = get_user_model()


class EmailBackend(ModelBackend):
    """
    Allows users to login in with either a username or a password
    """
    def authenticate(self, request, username=None, password=None, **kwargs):
        """
        Authenticates the user by checking if the username or email matches the user model
        """
        try:
            user = User.objects.get(Q(username__iexact=username) | Q(email__iexact=username))
        except User.DoesNotExist:
            # Creates a new user if a user does not exist with this username or email
            User().set_password(password)
            return
        except User.MultipleObjectsReturned:
            user = User.objects.filter(Q(username__iexact=username) | Q(email__iexact=username)).order_by('id').first()
        
        if user.check_password(password) and self.user_can_authenticate(user):
            return user
        
