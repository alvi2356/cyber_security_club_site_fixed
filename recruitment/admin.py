from django.contrib import admin
from .models import RecruitmentApplication, RecruitmentSetting

class RecruitmentApplicationAdmin(admin.ModelAdmin):
    list_display = ('name', 'student_id', 'semester', 'position', 'applied_at')
    list_filter = ('semester', 'position', 'applied_at')
    search_fields = ('name', 'student_id', 'position')

class RecruitmentSettingAdmin(admin.ModelAdmin):
    list_display = ('is_active',)

    def has_add_permission(self, request):
        # Allow adding only if no setting exists
        return not RecruitmentSetting.objects.exists()

    def has_delete_permission(self, request, obj=None):
        # Prevent deletion
        return False

admin.site.register(RecruitmentApplication, RecruitmentApplicationAdmin)
admin.site.register(RecruitmentSetting, RecruitmentSettingAdmin)
