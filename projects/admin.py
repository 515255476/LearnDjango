from django.contrib import admin

# Register your models here.


from projects.models import Projects, Person


class ProjectAdmin(admin.ModelAdmin):
    fields = ("project_name", "leader", "tester")
    list_display = ["id", "project_name", "leader", "tester"]


class PersonAdmin(admin.ModelAdmin):
    list_display = ["id", "name", 'project_id']


admin.site.register(Projects, ProjectAdmin)
admin.site.register(Person, PersonAdmin)
