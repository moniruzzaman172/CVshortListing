from django.contrib import admin
from Authority.models import Skill, TopCandidates, Authority, authority_account

admin.site.register(Skill)
admin.site.register(TopCandidates)
admin.site.register(Authority)
admin.site.register(authority_account)

