from django.contrib import admin
from diary.models import ProjectStatus, Unit, Project, DailyLog, Material, MaterialUsage, MaterialPurchase


admin.site.register(ProjectStatus)
admin.site.register(Unit)
admin.site.register(Project)
admin.site.register(DailyLog)
admin.site.register(Material)
admin.site.register(MaterialUsage)
admin.site.register(MaterialPurchase)
