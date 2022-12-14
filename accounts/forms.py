from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.contrib.auth import get_user_model
from django import forms
from django.contrib.auth.hashers import check_password
from .models import Note


class DateInput(forms.DateInput):
    input_type = "date"


class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = get_user_model()
        fields = (
            "username",
            "password1",
            "password2",
            "career",
        )
        error_messages = {
            "username": {
                "unique": "입력한 계정으로 가입이 불가능 합니다.",
            },
        }
        labels = {
            "career": "입사 일자",
        }
        help_texts = {
            "career": "선택 사항입니다.",
        }
        widgets = {"career": DateInput()}


class CustomUserChangeForm(UserChangeForm):
    password = None

    class Meta:
        model = get_user_model()
        fields = ("username", "profile", "career", "email", "githuburl")
        labels = {
            "profile": "프로필 사진",
            "career": "경력(년차)",
            "githuburl": "Github 주소",
        }
        widgets = {"career": DateInput()}


class CheckPasswordForm(forms.Form):
    password = forms.CharField(
        label="비밀번호",
        widget=forms.PasswordInput(
            attrs={
                "class": "form-control",
            }
        ),
    )

    def __init__(self, user, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.user = user

    def clean(self):
        cleaned_data = super().clean()
        password = cleaned_data.get("password")
        confirm_password = self.user.password

        if password:
            if not check_password(password, confirm_password):
                self.add_error("password", "비밀번호가 일치하지 않습니다.")


class NoteForm(forms.ModelForm):
    class Meta:
        model = Note
        fields = (
            "receive_user",
            "title",
            "content",
        )
        labels = {
            "receive_user": "받는 사람",
            "title": "글 제목",
            "content": "글 내용",
        }
