from django.contrib import admin
from curriculum import models
from curriculum.admin import modeladmins


class ResumeAdmin(modeladmins.ResumeAdmin):
    def get_queryset(self, request):
        if request.user.is_superuser:
            return models.Resume.objects.all()
        return models.Resume.objects.filter(userresumes__user=request.user)

    def has_module_permission(self, request):
        return True

    def has_change_permission(self, request, obj=None):
        return True


class ExperienceAdmin(modeladmins.ExperienceAdmin):
    def get_queryset(self, request):
        if request.user.is_superuser:
            return models.Experience.objects.all()
        return models.Experience.objects.filter(resume__userresumes__user=request.user)

    def get_form(self, request, obj=None, **kwargs):
        form = super(ExperienceAdmin, self).get_form(request, obj, **kwargs)
        form.base_fields['resume'].queryset = models.Resume.objects.filter(userresumes__user=request.user.id)
        form.base_fields['resume'].initial = models.Resume.objects.filter(userresumes__user=request.user.id)[0]
        return form

    def has_module_permission(self, request):
        return True

    def has_change_permission(self, request, obj=None):
        return True

    def has_add_permission(self, request):
        return True


class TrainingAdmin(modeladmins.TrainingAdmin):
    def get_queryset(self, request):
        if request.user.is_superuser:
            return models.Training.objects.all()
        return models.Training.objects.filter(resume__userresumes__user=request.user)

    def get_form(self, request, obj=None, **kwargs):
        form = super(TrainingAdmin, self).get_form(request, obj, **kwargs)
        form.base_fields['resume'].queryset = models.Resume.objects.filter(userresumes__user=request.user.id)
        form.base_fields['resume'].initial = models.Resume.objects.filter(userresumes__user=request.user.id)[0]
        return form

    def has_module_permission(self, request):
        return True

    def has_change_permission(self, request, obj=None):
        return True

    def has_add_permission(self, request):
        return True


class ProjectAdmin(modeladmins.ProjectAdmin):
    def has_add_permission(self, request):
        return True


class ProjectItemAdmin(modeladmins.ProjectItemAdmin):
    def get_queryset(self, request):
        if request.user.is_superuser:
            return models.ProjectItem.objects.all()
        return models.ProjectItem.objects.filter(resume__userresumes__user=request.user)

    def get_form(self, request, obj=None, **kwargs):
        form = super(ProjectItemAdmin, self).get_form(request, obj, **kwargs)
        form.base_fields['resume'].queryset = models.Resume.objects.filter(userresumes__user=request.user.id)
        form.base_fields['resume'].initial = models.Resume.objects.filter(userresumes__user=request.user.id)[0]
        return form

    def has_module_permission(self, request):
        return True

    def has_change_permission(self, request, obj=None):
        return True

    def has_add_permission(self, request):
        return True


class SkillAdmin(modeladmins.SkillAdmin):
    def has_add_permission(self, request):
        return True


class SkillItemAdmin(modeladmins.SkillItemAdmin):
    def get_queryset(self, request):
        if request.user.is_superuser:
            return models.SkillItem.objects.all()
        return models.SkillItem.objects.filter(resume__userresumes__user=request.user)

    def get_form(self, request, obj=None, **kwargs):
        form = super(SkillItemAdmin, self).get_form(request, obj, **kwargs)
        form.base_fields['resume'].queryset = models.Resume.objects.filter(userresumes__user=request.user.id)
        form.base_fields['resume'].initial = models.Resume.objects.filter(userresumes__user=request.user.id)[0]
        return form

    def has_module_permission(self, request):
        return True

    def has_change_permission(self, request, obj=None):
        return True

    def has_add_permission(self, request):
        return True


class CertificationAdmin(modeladmins.CertificationAdmin):
    def has_add_permission(self, request):
        return True


class CertificationItemAdmin(modeladmins.CertificationItemAdmin):
    def get_queryset(self, request):
        if request.user.is_superuser:
            return models.CertificationItem.objects.all()
        return models.CertificationItem.objects.filter(resume__userresumes__user=request.user)

    def get_form(self, request, obj=None, **kwargs):
        form = super(CertificationItemAdmin, self).get_form(request, obj, **kwargs)
        form.base_fields['resume'].queryset = models.Resume.objects.filter(userresumes__user=request.user.id)
        form.base_fields['resume'].initial = models.Resume.objects.filter(userresumes__user=request.user.id)[0]
        return form

    def has_module_permission(self, request):
        return True

    def has_change_permission(self, request, obj=None):
        return True

    def has_add_permission(self, request):
        return True


class LanguageAdmin(modeladmins.LanguageAdmin):
    def has_add_permission(self, request):
        return True


class LanguageItemAdmin(modeladmins.LanguageItemAdmin):
    def get_queryset(self, request):
        if request.user.is_superuser:
            return models.LanguageItem.objects.all()
        return models.LanguageItem.objects.filter(resume__userresumes__user=request.user)

    def get_form(self, request, obj=None, **kwargs):
        form = super(LanguageItemAdmin, self).get_form(request, obj, **kwargs)
        form.base_fields['resume'].queryset = models.Resume.objects.filter(userresumes__user=request.user.id)
        form.base_fields['resume'].initial = models.Resume.objects.filter(userresumes__user=request.user.id)[0]
        return form

    def has_module_permission(self, request):
        return True

    def has_change_permission(self, request, obj=None):
        return True

    def has_add_permission(self, request):
        return True


admin.site.unregister([
    models.Resume,
    models.Experience,
    models.Training,
    models.Project,
    models.ProjectItem,
    models.Skill,
    models.SkillItem,
    models.Certification,
    models.CertificationItem,
    models.Language,
    models.LanguageItem,
])
admin.site.register(models.Resume, ResumeAdmin)
admin.site.register(models.Experience, ExperienceAdmin)
admin.site.register(models.Training, TrainingAdmin)
admin.site.register(models.Project, ProjectAdmin)
admin.site.register(models.ProjectItem, ProjectItemAdmin)
admin.site.register(models.Skill, SkillAdmin)
admin.site.register(models.SkillItem, SkillItemAdmin)
admin.site.register(models.Certification, CertificationAdmin)
admin.site.register(models.CertificationItem, CertificationItemAdmin)
admin.site.register(models.Language, LanguageAdmin)
admin.site.register(models.LanguageItem, LanguageItemAdmin)
