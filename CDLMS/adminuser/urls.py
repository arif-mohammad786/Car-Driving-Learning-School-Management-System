from django.urls import path
from . import views
urlpatterns = [
    path('adminlogin/',views.admin_login,name="adminlogin"),
    path('dashboard/',views.dashboard,name="dashboard"),
    path('logout/',views.logout_admin,name="logout"),
    path('addnewpackage/',views.add_new_package,name="addnewpackage"),
    path('manage-packages/',views.manage_packages,name="manage-packages"),
    path('update-package/<int:id>/',views.update_package,name="update-package"),
    path('delete-package/<int:id>/',views.delete_package,name="delete-package"),
    path('new-application/',views.new_applications,name="new-application"),
    path('applicant-detail/<int:id>/',views.view_applicant_detail,name="applicant-detail"),
    path('take-action/<int:id>/',views.take_action,name="take-action"),
    path('available-user/',views.available_users,name="available-user"),
    path('available-user-detail/<int:id>/',views.available_user_detail,name="available-user-detail"),


]