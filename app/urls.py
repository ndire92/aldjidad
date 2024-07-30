from django.urls import path
from . import views

urlpatterns = [

    path('login/', views.user_login, name='login'),
    path('register/', views.register, name='register'),
    path('logout/', views.logout_view, name='logout'),

    path('permission_denied/', views.permission_denied_view, name='permission_denied'),
    path('liste_membres/', views.liste_membres, name='liste_membres'),
    path('ajouter_membre/', views.ajouter_membre, name='ajouter_membres'),
    path('update_membre/<int:pk>/', views.update_membre, name='update_membre'),
    path('delete_membre/<int:pk>/', views.delete_membre, name='delete_membre'),
    path('coordination/', views.coordination_form, name='coordinations'),
    
    path('liste_coord/', views.coordi, name='liste_structure'),
    
    path('section/', views.section_form, name='sections'),
    path('liste_section/', views.section_list, name='liste_sections'),
    path('secteur/', views.secteur_form, name='secteurs'),
    path('liste_secteur/', views.secteur_list, name='liste_secteurs'),
    path('combined-list/', views.combined_list, name='combined_list'),
    

    path('bureau/', views.bureau_form, name='bureau_form'),
    path('bureaux/', views.list_bureau_national, name='list_bureau_national'),
    path('bureau/update/<int:pk>/', views.update_bureau_national, name='update_bureau_national'),
    path('bureau/delete/<int:pk>/', views.delete_bureau_national, name='delete_bureau_national'),

   
    path('commissions/', views.commission_list, name='commission_list'),
    path('commissions/new/', views.commission_create, name='commission_create'),
    path('commissi/<int:pk>/edit/', views.commission_update, name='commission_update'),
    path('commissi/<int:pk>/delete/', views.commission_delete, name='commission_delete'),


    
    path('create/commission/org/', views.create_commission_org, name='create_commission_org'),
    path('list/commission/org/', views.list_commission_org, name='list_commission_org'),
    path('commissions/edit/<int:pk>/', views.update_commission_org, name='update_commission_org'),
    path('commissions/delete/<int:pk>/', views.delete_commission_org, name='delete_commission_org'),

    path('create/commission/fem/', views.create_commission_fem, name='create_commission_fem'),
    path('list/commission/fem/', views.list_commission_fem, name='list_commission_fem'),
    path('update/commission/fem/<int:pk>/', views.update_commission_fem, name='update_commission_fem'),
    path('delete/commission/fem/<int:pk>/', views.delete_commission_fem, name='delete_commission_fem'),


    path('create/commission/commu/', views.create_commission_commu, name='create_commission_commu'),
    path('list/commission/commu/', views.list_commission_commu, name='list_commission_commu'),
    path('update/commission/commu/<int:pk>/', views.update_commission_commu, name='update_commission_commu'),
    path('delete/commission/commu/<int:pk>/', views.delete_commission_commu, name='delete_commission_commu'),

    path('create/commission/cul/', views.create_commission_cul, name='create_commission_cul'),
    path('list/commission/cul/', views.list_commission_cul, name='list_commission_cul'),
    path('update/commission/cul/<int:pk>/', views.update_commission_cul, name='update_commission_cul'),
    path('delete/commission/cul/<int:pk>/', views.delete_commission_cul, name='delete_commission_cul'),

    
    path('create/commission/social/', views.create_commission_social, name='create_commission_social'),
    path('list/commission/social/', views.list_commission_social, name='list_commission_social'),
    path('commission/edit/<int:pk>/', views.update_commission_social, name='update_commission_social'),
    path('commission/delete/<int:pk>/', views.delete_commission_social, name='delete_commission_social'),

    
    
    path('create/commission/decen/', views.create_commission_decen, name='create_commission_decen'),
    path('list/commission/decen/', views.list_commission_decen, name='list_commission_decen'),
    path('commissiond/edit/<int:pk>/', views.update_commission_decen, name='update_commission_decen'),
    path('commissiond/delete/<int:pk>/', views.delete_commission_decen, name='delete_commission_decen'),


    path('membre_stats', views.membre_stats, name='membre_stats'),
    path('administratreur/', views.admin, name='administration'),
    
    # urls.py
 


]