from django.urls import path
from automation import views
app_name='automation'


urlpatterns=[
	#Desg Automation url
	path('desg_automation/', views.desg_automation,name='desg_automation'),
	path('desg_automation_update/',views.desg_automation_update, name='desg_automation_update'),
	path('desg_automation/<id>/edit/', views.edit_desg_automation_content,name='edit_desg_automation_content'),
    path('desg_automation/<id>/delete/', views.delete_desg_automation_content,name='delete_desg_automation_content'),
	path('desg_automation_update/<id>/edit/', views.edit_desg_automation_update,name='edit_desg_automation_update'),
	path('desg_automation_update/<id>/delete/', views.delete_desg_automation_update,name='delete_desg_automation_update'),

	#Pdc Automation Url
	path('pdc_automation/', views.pdc_automation,name='pdc_automation'),
	path('pdc_automation_update/',views.pdc_automation_update, name='pdc_automation_update'),
	path('pdc_automation/<id>/edit/', views.edit_pdc_automation_content,name='edit_pdc_automation_content'),
    path('pdc_automation/<id>/delete/', views.delete_pdc_automation_content,name='delete_pdc_automation_content'),
	path('pdc_automation_update/<id>/edit/', views.edit_pdc_automation_update,name='edit_pdc_automation_update'),
	path('pdc_automation_update/<id>/delete/', views.delete_pdc_automation_update,name='delete_pdc_automation_update'),

	#Ldm Automation Url
	path('ldm_automation/', views.ldm_automation,name='ldm_automation'),
	path('ldm_automation_update/', views.ldm_automation_update, name='ldm_automation_update'),
	path('ldm_automation/<id>/edit/', views.edit_ldm_automation_content,name='edit_ldm_automation_content'),
    path('ldm_automation/<id>/delete/', views.delete_ldm_automation_content,name='delete_ldm_automation_content'),
	path('ldm_automation_update/<id>/edit/', views.edit_ldm_automation_update,name='edit_ldm_automation_update'),
	path('ldm_automation_update/<id>/delete/', views.delete_ldm_automation_update,name='delete_ldm_automation_update'),
]