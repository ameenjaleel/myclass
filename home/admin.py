from django.contrib import admin
from .models import Classroom,Student

class StudentModelAdmin(admin.ModelAdmin):
    list_display = ["classroom","student_name","mark"]
    class Meta:
        model = Student


admin.site.register(Classroom)
admin.site.register(Student,StudentModelAdmin)
# Register your models here.
