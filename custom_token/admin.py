from django.contrib import admin
from .models import AdminCustomToken, ProfessorCustomToken, StudentCustomToken
admin.site.register(AdminCustomToken)
admin.site.register(ProfessorCustomToken)
admin.site.register(StudentCustomToken)