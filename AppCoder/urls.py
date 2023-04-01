from django.urls import path
from django.contrib.auth.views import LogoutView
from AppCoder import views


app_name = "AppCoder"
urlpatterns = [

    path('inicio', views.inicio, name='Inicio'),
    path('cursos', views.cursos, name='Cursos'),
    path('profesores', views.profesores, name='Profesores'),
    path('estudiantes', views.estudiantes, name='Estudiantes'),
    path('entregables', views.entregables, name='Entregables'),
    path('buscar/', views.buscar),
    path('leerProfesores', views.leerProfesores, name='LeerProfesores'),
    path('eliminarProfesor/<profesor_nombre>/',views.eliminarProfesor, name="EliminarProfesor"),
    path('editaProfesor/<profesor_nombre>', views.editarProfesor, name = 'EditarProfesor'),
    path('curso/list', views.CursoList.as_view(), name='List'),
    path('<int:pk>', views.CursoDetalle.as_view(), name='Detail'),
    path('nuevo', views.CursoCreacion.as_view(), name='New'),
    path('editar/<int:pk>', views.CursoUpdate.as_view(), name='Edit'),
    path('borrar/<int:pk>', views.CursoDelete.as_view(), name='Delete'),
    path('', views.login_request, name='Login' ),
    path('register', views.register, name= 'Register'),
    path('logout', LogoutView.as_view(template_name='logout.html'), name='Logout'),
    path('editarPerfil', views.editarPerfil, name='EditarPerfil'),
    path('agregarAvatar', views.agregarAvatar, name='AgregarAvatar'),
    path('custom_404', views.custom_404, name='Custom_404'),
    path('proximamente', views.proximamente, name='Proximamente'),
    path('login_invitado/', views.login_invitado, name='Login_invitado'),
    path('aboutus', views.aboutus, name='About_Us'),

]