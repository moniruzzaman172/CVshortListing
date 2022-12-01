from django.contrib import admin
from Candidate.models import Candidate, Resume, Personal

admin.site.register(Resume)
admin.site.register(Candidate)
admin.site.register(Personal)
