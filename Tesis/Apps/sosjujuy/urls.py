from django.urls import path, include
from django.contrib.auth import views as auth_views
from django.contrib.auth.decorators import login_required

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('reportes/', views.reports, name='reports'),
    path('login/', auth_views.LoginView.as_view(), name='login'),
    path('signup/', views.signup, name='signup'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('domicilios/', login_required(views.DomicilioListView.as_view()), name='domicilio_changelist'),
    path('domicilio/', login_required(views.DomicilioCreateView.as_view()), name='domicilio_add'),
    path('domicilio/<int:pk>/', login_required(views.DomicilioUpdateView.as_view()), name='domicilio_change'),
    path('domiciliodelete/<domicilio_id>', login_required(views.deleteDomicilio), name='domicilio_delete'),
    path('beneficiarios/', login_required(views.BeneficiarioListView.as_view()), name='beneficiario_changelist'),
    path('beneficiario/', login_required(views.BeneficiarioCreateView.as_view()), name='beneficiario_add'),
    path('beneficiario/<int:pk>/', login_required(views.BeneficiarioUpdateView.as_view()), name='beneficiario_change'),
    path('beneficiariodelete/<beneficiario_id>', login_required(views.deleteBeneficiario), name='beneficiario_delete'),
    path('prestadores/', login_required(views.PrestadorListView.as_view()), name='prestador_changelist'),
    path('prestador/', login_required(views.PrestadorCreateView.as_view()), name='prestador_add'),
    path('prestador/<int:pk>/', login_required(views.PrestadorUpdateView.as_view()), name='prestador_change'),
    path('prestaciones/', login_required(views.PrestacionListView.as_view()), name='prestacion_changelist'),
    path('prestacion/', login_required(views.PrestacionCreateView.as_view()), name='prestacion_add'),
    path('prestacion/<int:pk>/', login_required(views.PrestacionUpdateView.as_view()), name='prestacion_change'),
    path('prestacion/eliminar/<int:pk>/', login_required(views.PrestacionDeleteView.as_view()), name='prestacion_delete'),
    path('derivaciones/', login_required(views.DerivacionListView.as_view()), name='derivacion_changelist'),
    path('derivacion/', login_required(views.DerivacionCreateView.as_view()), name='derivacion_add'),
    path('derivacion/<int:pk>/', login_required(views.DerivacionUpdateView.as_view()), name='derivacion_change'),
    path('derivacion/eliminar/<int:pk>/', login_required(views.DerivacionDeleteView.as_view()), name='derivacion_delete'),
    path('derivacion_pdf/<int:pk>/', login_required(views.DerivacionPDFView.as_view()), name='derivacion_pdf'),
    path('actividades_extension/', login_required(views.ActividadExtensionListView.as_view()), name='actividad_extension_changelist'),
    path('actividad_extension/', login_required(views.ActividadExtensionCreateView.as_view()), name='actividad_extension_add'),
    path('actividad_extension/<int:pk>/', login_required(views.ActividadExtensionUpdateView.as_view()), name='actividad_extension_change'),
    path('actividad_extensiondelete/<actividad_extension_id>', login_required(views.deleteActividadExtension), name='actividad_extension_delete'),
    path('encuesta_beneficiario/<int:pk_beneficiario>_<int:pk_derivacion>', views.EncuestaAtencionBeneficiarioCreateView.as_view(), name='encuesta_beneficiario_add'),
    path(r'report_builder/', include('report_builder.urls')),
]


