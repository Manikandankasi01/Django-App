from django.urls import path
from desg_t18 import views
app_name='desg_t18'

urlpatterns=[
    #test
    path('test/',views.test, name='test'),
    #validate user
    path('login/', views.login, name='login'),
    path('register/', views.register, name='register'),
    path('reset_password/', views.reset_pass, name='change_pass'),
    #hda home
    path('home/', views.hda_home, name='hda_home'),
    path('team_view/', views.team_view, name='team_view'),
    #desg home
    path('desg_home/',views.desg_home, name='desg_home'),
    path('desg_team/',views.desg_team, name='desg_team'),
    #pc
    path('perform_check/',views.perform_check, name='pc'),
    path('pc_update/',views.pc_update, name='pc_update'),
    path('pc_update/<id>/edit/',views.edit_pc_update, name='edit_pc_update'),
    path('pc_update/<id>/delete/', views.delete_pc_update,name='delete_pc_update'),
    #gml
    path('gml_creation/',views.gml_creation, name='gml'),
    path('gml_update/',views.gml_update, name='gml_update'),
    path('gml_update/<id>/edit/',views.edit_gml_update, name='edit_gml_update'),
    path('gml_update/<id>/delete/', views.delete_gml_update,name='delete_gml_update'),
    #triage updates
    path('triage_update/',views.triage_update, name='triage_update'),
    path('triage_update/<id>/edit/',views.edit_triage_content, name='edit_triage_content'),
    path('triage_update/<id>/delete/', views.delete_triage_content,name='delete_triage_content'),
    #meeting update
    path('meeting_update/',views.meeting_update, name='meeting_update'),
    path('meeting_update/<id>/edit/', views.edit_meeting_content,name='edit_meeting_content'),
    path('meeting_update/<id>/delete/', views.delete_meeting_content,name='delete_meeting_content'),
    #forum updates
    path('forum/',views.forum, name='forum'),
    path('forum/<id>/edit/', views.edit_forum_content,name='edit_forum_content'),
    path('forum/<id>/delete/', views.delete_forum_content,name='delete_forum_content'),
    #dashboard
    path('desg_dashboard/', views.desg_dashboard,name='desg_dashboard'),
    path('hda_dashboard/',views.hda_dashboard, name='hda_dashboard'),
    
    
]
