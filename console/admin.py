from django.contrib import admin
from .models import Semester, Subject, Internal, Grade, SubjectAssign, SemAssign

admin.site.register(Semester)
admin.site.register(Subject)
admin.site.register(Internal)
admin.site.register(Grade)
admin.site.register(SubjectAssign)
admin.site.register(SemAssign)



