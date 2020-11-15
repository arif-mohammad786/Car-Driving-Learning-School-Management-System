from django.urls import path
from . import views
urlpatterns = [
    path('packages/',views.available_packages,name="packages"),
    path('aboutus/',views.about_us,name="aboutus"),
    path('contactus/',views.contact_us,name="contactus"),
    path('applynow/',views.apply_now,name="applynow"),
]