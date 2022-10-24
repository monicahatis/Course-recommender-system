from django.contrib import admin
from .models import (
    ContactInfor,
    ContactFromUser,
    Subjects
)

# Register your models here.

admin.site.register(ContactInfor)
admin.site.register(ContactFromUser)
admin.site.register(Subjects)
