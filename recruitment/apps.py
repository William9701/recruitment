from django.contrib import admin
from django.apps import apps, AppConfig


class AdminClass(admin.ModelAdmin):
    def __init__(self, model, admin_site):
        # Automatically display all fields in the list page:
        self.list_display = [field.name for field in model._meta.fields]
        super(AdminClass, self).__init__(model, admin_site)

# automatically register all models
class UniversalManagerApp(AppConfig):
    """
    Application configuration executes after all Admin interfaces are loaded
    """
    # the name of the AppConfig must be the same as current application
    name = 'recruitment'

    def ready(self):
        models = apps.get_app_config('running').get_models() 
        for model in models:
            try:
                admin.site.register(model, AdminClass)
            except admin.sites.AlreadyRegistered:
                pass
