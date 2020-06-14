from django.urls import path
from . import views
urlpatterns = [
    path('',views.signup,name="signup"),
    path('employee/',views.employee,name="employee"),
    path('sale/',views.accounts,name="accounts" ),
    path('item/',views.item,name="item"),
    path('notes/',views.notes,name="notes"),
    path('myaccount/',views.myaccount,name="myaccount"),
    path('employee/delete/<int:id>',views.delete_employee,name="employee_delete"),
    path('employee/update/<int:id>',views.update_employee,name="employee_update"),
    path('employee/full_info/<int:id>',views.full_info,name="full_info"),
    path('notes/update/<int:id>',views.update_notes,name="update_notes"),
    path('notes/delete/<int:id>',views.delete_notes,name="delete_notes"),
]