from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .forms import EmployeeChangeForm, EmployeeCreationForm
from .models import Employee, TradingPoint, Visit

class EmplyeeAdmin(UserAdmin):
    add_form = EmployeeCreationForm
    form = EmployeeChangeForm
    model = Employee
    save_on_top = True
    list_display = ('name', 'phone', 'is_staff', 'is_active',)
    list_filter = ('is_staff', 'is_active',)
    fieldsets = (
        (None, {'fields': ('name', 'phone', 'password')}),
        ('Permissions', {'fields': ('is_staff', 'is_active')}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('name', 'phone', 'password1', 'password2', 'is_staff', 'is_active')}
        ),
    )
    search_fields = ('phone', 'name')
    ordering = ('phone',)

class TradingPointAdmin(admin.ModelAdmin):
    save_on_top = True

class VisitAdmin(admin.ModelAdmin):

    def has_add_permission(self, request):
        return False
    
    def has_change_permission(self, request):
        return False

    def has_delete_permission(self, request):
        return False

admin.site.register(Employee, EmplyeeAdmin)
admin.site.register(TradingPoint, TradingPointAdmin)
admin.site.register(Visit, VisitAdmin)