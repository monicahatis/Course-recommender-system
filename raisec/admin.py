from django.contrib import admin

# Register your models here.
from accounts.models import RaisecAnswer

from .models import (
    RaisecGroup,
    RaisecQuestions
)


admin.site.register(RaisecGroup)
admin.site.register(RaisecQuestions)
admin.site.register(RaisecAnswer)
