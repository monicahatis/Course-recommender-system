from django.contrib import admin

# Register your models here.

from .models import (
    Course,
    ClusterClasses,
  
    AdvertUserLinks,CourseRattingAndComment,
    MinimumRequirement,
    UserMinimumRequirement
)


admin.site.register(Course)

admin.site.register(ClusterClasses)

admin.site.register(AdvertUserLinks)
admin.site.register(CourseRattingAndComment)
admin.site.register(MinimumRequirement)
admin.site.register(UserMinimumRequirement)