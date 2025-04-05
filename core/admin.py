from django.contrib import admin
from .models import CleanupEvent, Participation, YearlyImpact

admin.site.register(CleanupEvent)
admin.site.register(Participation)
admin.site.register(YearlyImpact)

