from django.urls import path, include
from .views import *
from django.contrib.auth.views import LogoutView

app_name = 'miapp'

urlpatterns = [
    path('', index, name="inicio"),

    path('clientes/', ClientesList.as_view(), name="clientes"),

    path('desarrolladores/', DesarrolladoresList.as_view(), name="desarrolladores"),


    path('propuestas_form', propuestasForm, name="propuestas_form"),

    path('desarrolladores_form', desarrolladoresForm, name="desarrolladores_form"),

    path('clientes_form', clientesForm, name="clientes_form"),

    path('buscar_propuesta/', buscarPropuesta, name="buscar_propuesta"),
    path('resultadosPropuesta/', resultadosPropuesta, name="resultadosPropuesta"),

    path('posteos/', PosteosList.as_view(), name="posteos"),
    path('create_posteos/', PosteosCreate.as_view(), name="create_posteos"),
    path('detail_posteos/<int:pk>/', PosteosDetail.as_view(), name="detail_posteos"),
    path('update_posteos/<int:pk>/', PosteosUpdate.as_view(), name="update_posteos"),
    path('delete_posteos/<int:pk>/', PosteosDelete.as_view(), name="delete_posteos"),


    path('propuestas/', PropuestasList.as_view(), name="propuestas"),
    path('create_propuestas/', PropuestasCreate.as_view(), name="create_propuestas"),
    path('detail_propuestas/<int:pk>/', PropuestasDetail.as_view(), name="detail_propuestas"),
    path('update_propuestas/<int:pk>/', PropuestasUpdate.as_view(), name="update_propuestas"),
    path('delete_propuestas/<int:pk>/', PropuestasDelete.as_view(), name="delete_propuestas"),



    
    path('login/', login_request, name="login"),
    path('logout/', LogoutView.as_view(template_name="miapp/logout.html"), name="logout"),
    path('register/', register, name="register"),

    path('editar_perfil/', editarPerfil, name="editar_perfil"),
    path('agregar_avatar/', agregarAvatar, name="agregar_avatar"),

]