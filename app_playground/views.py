from django.utils.translation import gettext_lazy
from iommi import Page

from .forms import ProfileInfoForm


class ProfileInfoPage(Page):
    profile_info_form = ProfileInfoForm

    class Meta:
        h_tag__include = False
        title = gettext_lazy("Profile Information")