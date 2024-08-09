from iommi import Style, register_style, Asset
from iommi.style_base import select2_enhanced_forms
from iommi.style_bootstrap5 import bootstrap5_base
from iommi.style_bootstrap_icons import bootstrap_icons

custom_style = Style(
    bootstrap5_base,
    bootstrap_icons,
    select2_enhanced_forms,
    root__assets=dict(
        # css__include=True,
        # popper_js__include=True,
        # js__include=True,
        # jquery__include=True
    ),
    base_template='iommi_base.html',
    Container__attrs={
        "class":
            {
                'contents': True,
                'mt-5': False,
                'pt-5': False,
                'container': False
            }
    },
    **{
        "Field__attrs__class": {
            "col": False,
            "mb-3": False,
            "form-group": True,
            "mb-25": True,
            "required": lambda field, **_: field.required
        },
        "Actions__attrs__class": {
            "links": False,
            "button-group d-flex pt-sm-25 justify-content-md-end justify-content-start": True,
            "btn-secondary": False
        }
    })