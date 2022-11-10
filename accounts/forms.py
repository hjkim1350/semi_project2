from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import get_user_model


class CustumUserCreationForm(UserCreationForm):
    class Meta:
        model = get_user_model()
        fields = (
            "username",
            "profile",
        )
