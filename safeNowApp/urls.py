from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),  # Home page with login/register
    path('createuserform', views.create_user_form, name='createuserform'),  # Registration POST
    path('loginuserform', views.login_user_form, name='loginuserform'),  # Login POST
    path('dashboard', views.display_dashboard, name='dashboard'),  # User dashboard
    path('logoutform', views.logout_form, name='logoutform'),
    path('about', views.about, name='about'),
    path('create_case', views.create_case_page, name='create_case'),
    path('services', views.show_services, name='services'),
    path('volunteer', views.volunteer),
    path('report_case', views.report_case, name='report_case'),
    path('success', views.success_description, name='success'),
    path("chat_ai", views.chat_ai, name="chat_ai"),
    path("volunteer_service_submit", views.volunteer_service_submit, name="volunteer_service_submit"),
    path("become_a_volunteer", views.become_a_volunteer, name="Become_a_volunteer"),
    path("cancel_service", views.cancel_service, name="cancel_service"),
    path('set-language', views.set_language, name='set_language'),
    path('rate_a_service/<service_id>', views.rate_a_service, name='rate_a_service'),
    path('my_cases', views.my_cases, name='my_cases'),
    path("filter_cases/", views.filter_cases, name="filter_cases"),
    path("change_status/<case_id>", views.change_status, name="change_status"),
    path('request_service/<service_id>', views.request_service, name='request_service'),
    path('filter_services/', views.filter_services, name='filter_services'),
    path('my_services', views.my_services, name='my_services'),
    path('delete_service/<service_id>', views.delete_service, name='delete_service'),

]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
