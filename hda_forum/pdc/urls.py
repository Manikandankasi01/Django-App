from django.urls import path
from pdc import views
app_name='pdc'

urlpatterns=[
    #pdc home
    path('pdc_home/',views.pdc_home, name='pdc_home'),
    path('pdc_team/',views.pdc_team, name='pdc_team'),
    path('pdc_workflow/',views.pdc_workflow, name='pdc_workflow'),

   
    #meeting update
    path('pdc_meeting_update/',views.meeting_update, name='pdc_meeting_update'),
    path('meeting_update/<id>/edit/', views.edit_meeting_content,name='edit_meeting_content'),
    path('meeting_update/<id>/delete/', views.delete_meeting_content,name='delete_meeting_content'),
    #forum updates
    path('pdc_forum/',views.pdc_forum, name='pdc_forum'),
    path('pdc_forum/<id>/edit/', views.edit_forum_content,name='edit_forum_content'),
    path('pdc_forum/<id>/delete/', views.delete_forum_content,name='delete_forum_content'),
    #dashboard
    path('pdc_dashboard/', views.pdc_dashboard,name='pdc_dashboard'),
    
    
]
