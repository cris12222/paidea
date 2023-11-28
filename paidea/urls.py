
from django.contrib import admin
from django.urls import path
from paideacrud import views
from django.contrib.auth.views import LoginView,LogoutView



urlpatterns = [
    #path('admin/', admin.site.urls),
    path('',views.home_view,name=''),
    path('Metas',views.CreateMeta,name='Metas'),
    path('EditMeta/<int:pk>', views.EditMeta,name='EditMeta'),
    path('DeleteMeta/<int:pk>', views.DeleteMeta,name='DeleteMeta'),

    path('Temas',views.CreateTema,name='Temas'),
    path('EditTema/<int:pk>', views.EditTema,name='EditTema'),
    path('DeleteTema/<int:pk>', views.DeleteTema,name='DeleteTema'),

    path('Eventos',views.CreateEvento,name='Eventos'),
    path('EditEvento/<int:pk>', views.EditEvento,name='EditEvento'),
    path('DeleteEventos/<int:pk>', views.DeleteEvento,name='DeleteEvento'),

    path('Reportes', views.GenerateReport,name='Reportes'),
]
