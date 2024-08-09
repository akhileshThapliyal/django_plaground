from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy
from iommi import Form, Action
from iommi.form import Field
from iommi.table import LAST

from .models import ProfileInfo

from django import forms
from django.contrib.auth.forms import AuthenticationForm, UsernameField


class LoginForm(AuthenticationForm):
    username = UsernameField(label='Enter Username', widget=forms.TextInput(attrs={'class': 'form-control'}))
    password = forms.CharField(label='Enter Password', widget=forms.PasswordInput(attrs={'class': 'form-control'}))

    def confirm_login_allowed(self, user):
        if user.is_staff and not user.is_superuser:
            raise ValidationError(
                ("This account is not allowed here."),
                code='not_allowed',
            )

ProfileInfoForm = Form.create_or_edit(
    auto__model=ProfileInfo,
    instance=lambda request, **_: ProfileInfo.objects.filter(user=request.user).first(),
    fields__user=Field.hardcoded(
        parsed_data=lambda form, user, **_: form.instance.user if form.instance else user,
    ),
    fields__profile_image=Field.image(
        required=lambda form, **_: form.instance is None,
        template='image_row.html'
        # img__attrs={
        #     "width": "24px",
        #     "height": "24px"
        # },
    ),
    fields__first_name__initial=lambda form, user,
                                       **_: user.first_name if form.instance is None else form.instance.first_name,
    fields__last_name__initial=lambda form, user,
                                      **_: user.last_name if form.instance is None else form.instance.last_name,
    fields__email__initial=lambda form, user, **_: user.email if form.instance is None else form.instance.email,
    title=None,
    attrs__id="profile_info_form",
    actions__submit=dict(
        display_name=gettext_lazy('Save & Next'),
        attrs={
            "class": {
                "btn btn-primary btn-default btn-squared text-capitalize radius-md shadow2 "
                "btn-sm": True,
                "btn-secondary": False
            },
            "type": "submit"
        },
        after=LAST
    ),
    extra__redirect_to='./profile_info',
    extra__name="personal-info",
)
