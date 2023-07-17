from django.urls import path
from . import views


urlpatterns = [
    path('', views.home),
    path('registrarCurso/', views.registrarCurso),
    path('editarCurso/<codigo>', views.editarCurso),
    path('edicaoCurso/', views.edicaoCurso),
    path('excluirCurso/<codigo>', views.excluirCurso),
    path('cadastro/', views.cadastro, name='cadastro'),
    path('login/', views.login, name='login'),
    
    
] 