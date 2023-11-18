from django import forms
from django.contrib import admin
from .models import Belongings, Box, Storage, User


class BelongingsAdminForm(forms.ModelForm):
    class Meta:
        model = Belongings
        fields = '__all__'
        widgets = {
            'owner': forms.Select(attrs={'class': 'admin-user-select'}),
        }


class BelongingsAdmin(admin.ModelAdmin):
    form = BelongingsAdminForm


admin.site.register(Belongings, BelongingsAdmin)

admin.site.register(User)
admin.site.register(Box)
admin.site.register(Storage)
