from django.urls import path
from ldm import views
app_name='ldm'

urlpatterns=[
    #pdc home
    path('ldm_home/',views.ldm_home, name='ldm_home'),
    path('ldm_team/',views.ldm_team, name='ldm_team'),
    path('ldm_workflow/',views.ldm_workflow, name='ldm_workflow'),
    #meeting update
    path('ldm_meeting_update/',views.ldm_meeting_update, name='ldm_meeting_update'),
    path('meeting_update/<id>/edit/', views.edit_meeting_content,name='edit_meeting_content'),
    path('meeting_update/<id>/delete/', views.delete_meeting_content,name='delete_meeting_content'),
    #forum updates
    path('ldm_forum/',views.ldm_forum, name='ldm_forum'),
    path('ldm_forum/<id>/edit/', views.edit_forum_content,name='edit_forum_content'),
    path('ldm_forum/<id>/delete/', views.delete_forum_content,name='delete_forum_content'),
    #dashboard
    path('ldm_dashboard/', views.ldm_dashboard,name='ldm_dashboard'),
    
    
]
