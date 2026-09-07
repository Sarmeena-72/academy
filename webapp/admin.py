from django.contrib import admin
from .models import Enrollment


@admin.register(Enrollment)
class EnrollmentAdmin(admin.ModelAdmin):

    # Columns shown in the enrollment list
    list_display = (
        'full_name',
        'email',
        'phone',
        'education',
        'course',
        'created_at',
    )

    # Search students
    search_fields = (
        'full_name',
        'email',
        'phone',
        'course',
    )

    # Filters on the right side
    list_filter = (
        'course',
        'education',
        'created_at',
    )

    # Latest enrollments will appear first
    ordering = ('-created_at',)

    # Number of records per page
    list_per_page = 20