from django.shortcuts import redirect, render
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import Domicilio, Beneficiario, Derivacion, Prestador, Prestacion, ActividadExtension, \
    EncuestaAtencionBeneficiario
from django.template import loader
from django.http import HttpResponse, HttpResponseRedirect
from .forms import DomicilioForm, BeneficiarioForm, DerivacionForm, PrestadorForm, PrestacionForm, \
    ActividadExtensionForm, EncuestaAtencionBeneficiarioForm
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from easy_pdf.views import PDFTemplateView
from django.core.mail import send_mail, send_mass_mail


def index(request):
    context = {}
    template = loader.get_template('sosjujuy/index.html')
    return HttpResponse(template.render(context, request))

def reports(request):
    context = {}
    template = loader.get_template('sosjujuy/reportes_form.html')
    return HttpResponse(template.render(context, request))

def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('home')
    else:
        form = UserCreationForm()
    return render(request, 'registration/signup.html', {'form': form})


class DomicilioListView(ListView):
    model = Domicilio
    context_object_name = 'domicilio'


class DomicilioCreateView(CreateView):
    model = Domicilio
    form_class = DomicilioForm
    success_url = reverse_lazy('domicilio_changelist')


class DomicilioUpdateView(UpdateView):
    model = Domicilio
    form_class = DomicilioForm
    success_url = reverse_lazy('domicilio_changelist')


def deleteDomicilio(request, domicilio_id):
    domicilio = Domicilio.objects.get(pk=domicilio_id)
    domicilio.delete()

    return redirect('domicilio_changelist')


class BeneficiarioListView(ListView):
    model = Beneficiario
    context_object_name = 'beneficiario'


class BeneficiarioCreateView(CreateView):
    model = Beneficiario
    template_name = 'sosjujuy/beneficiario_form.html'
    form_class = BeneficiarioForm
    second_form_class = DomicilioForm
    success_url = reverse_lazy('beneficiario_changelist')

    def get_context_data(self, **kwargs):
        context = super(BeneficiarioCreateView, self).get_context_data(**kwargs)
        if 'form' not in context:
            context['form'] = self.form_class(self.request.GET)
        if 'form2' not in context:
            context['form2'] = self.second_form_class(self.request.GET)
        return context

    def post(self, request, *args, **kwargs):
        self.object = self.get_object
        form = self.form_class(request.POST)
        print(" ")
        print(request.POST)
        form2 = self.second_form_class(request.POST)
        if form.is_valid() and form2.is_valid():
            beneficiario = form.save(commit=False)
            beneficiario.domicilio_legal = form2.save()
            beneficiario.save()
            return HttpResponseRedirect(self.get_success_url())
        else:
            return self.render_to_response(self.get_context_data(form=form, form2=form2))


class BeneficiarioUpdateView(UpdateView):
    model = Beneficiario
    second_model = Domicilio
    template_name = 'sosjujuy/beneficiario_form.html'
    form_class = BeneficiarioForm
    second_form_class = DomicilioForm
    success_url = reverse_lazy('beneficiario_changelist')

    def get_context_data(self, **kwargs):
        context = super(BeneficiarioUpdateView, self).get_context_data(**kwargs)
        pk = self.kwargs.get('pk', 0)
        beneficiario = self.model.objects.get(id=pk)
        domicilio = self.second_model.objects.get(id=beneficiario.domicilio_legal_id)
        if 'form' not in context:
            context['form'] = self.form_class()
        if 'form2' not in context:
            context['form2'] = self.second_form_class(instance=domicilio)
        context['id'] = pk
        return context

    def post(self, request, *args, **kwargs):
        self.object = self.get_object
        id_beneficiario = kwargs['pk']
        beneficiario = self.model.objects.get(id=id_beneficiario)
        domicilio = self.second_model.objects.get(id=beneficiario.domicilio_legal_id)
        form = self.form_class(request.POST, instance=beneficiario)
        form2 = self.second_form_class(request.POST, instance=domicilio)
        if form.is_valid() and form2.is_valid():
            form.save()
            form2.save()
            return HttpResponseRedirect(self.get_success_url())
        else:
            return self.render_to_response(self.get_context_data(form=form, form2=form2))


def deleteBeneficiario(request, beneficiario_id):
    beneficiario = Beneficiario.objects.get(pk=beneficiario_id)
    beneficiario.delete()

    return redirect('beneficiario_changelist')


class PrestadorListView(ListView):
    model = Prestador
    template_name = 'sosjujuy/prestador_list.html'
    context_object_name = 'prestador'


class PrestadorCreateView(CreateView):
    model = Prestador
    form_class = PrestadorForm
    template_name = 'sosjujuy/prestador_form.html'
    success_url = reverse_lazy('prestador_changelist')


class PrestadorUpdateView(UpdateView):
    model = Prestador
    form_class = PrestadorForm
    template_name = 'sosjujuy/prestador_form.html'
    success_url = reverse_lazy('prestador_changelist')


class PrestacionListView(ListView):
    model = Prestacion
    template_name = 'sosjujuy/prestacion_list.html'
    context_object_name = 'prestacion'


class PrestacionCreateView(CreateView):
    model = Prestacion
    template_name = 'sosjujuy/prestacion_form.html'
    form_class = PrestacionForm
    second_form_class = DomicilioForm
    success_url = reverse_lazy('prestacion_changelist')

    def get_context_data(self, **kwargs):
        context = super(PrestacionCreateView, self).get_context_data(**kwargs)
        if 'form' not in context:
            context['form'] = self.form_class(self.request.GET)
        if 'form2' not in context:
            context['form2'] = self.second_form_class(self.request.GET)
        return context

    def post(self, request, *args, **kwargs):
        self.object = self.get_object
        form = self.form_class(request.POST)
        form2 = self.second_form_class(request.POST)
        if form.is_valid() :
            prestacion = form.save(commit=False)
            #prestacion.domicilio = form2.save()
            #prestacion.save()
            return HttpResponseRedirect(self.get_success_url())
        else:
            return self.render_to_response(self.get_context_data(form=form, form2=form2))


class PrestacionUpdateView(UpdateView):
    model = Prestacion
    second_model = Domicilio
    template_name = 'sosjujuy/prestacion_form.html'
    form_class = PrestacionForm
    second_form_class = DomicilioForm
    success_url = reverse_lazy('prestacion_changelist')

    def get_context_data(self, **kwargs):
        context = super(PrestacionUpdateView, self).get_context_data(**kwargs)
        pk = self.kwargs.get('pk', 0)
        prestacion = self.model.objects.get(id=pk)
        domicilio = self.second_model.objects.get(id=prestacion.domicilio_id)
        if 'form' not in context:
            context['form'] = self.form_class()
        if 'form2' not in context:
            context['form2'] = self.second_form_class(instance=domicilio)
        context['id'] = pk
        return context

    def post(self, request, *args, **kwargs):
        self.object = self.get_object
        id_prestacion = kwargs['pk']
        prestacion = self.model.objects.get(id=id_prestacion)
        domicilio = self.second_model.objects.get(id=prestacion.domicilio_id)
        form = self.form_class(request.POST, instance=prestacion)
        form2 = self.second_form_class(request.POST, instance=domicilio)
        if form.is_valid() and form2.is_valid():
            form.save()
            form2.save()
            return HttpResponseRedirect(self.get_success_url())
        else:
            return HttpResponseRedirect(self.get_success_url())


class PrestacionDeleteView(DeleteView):
    model = Prestacion
    form_class = PrestacionForm
    template_name = 'sosjujuy/prestacion_delete.html'
    success_url = reverse_lazy('prestacion_changelist')


class DerivacionListView(ListView):
    model = Derivacion
    template_name = 'sosjujuy/derivacion_list.html'
    context_object_name = 'derivacion'


class DerivacionCreateView(CreateView):
    model = Derivacion
    form_class = DerivacionForm
    template_name = 'sosjujuy/derivacion_form.html'
    success_url = reverse_lazy('derivacion_changelist')

    def post(self, request, *args, **kwargs):
        self.object = self.get_object
        form = self.form_class(request.POST)
        if form.is_valid():
            derivacion = form.save(commit=False)
            derivacion.save()
            enviaremail(derivacion)
            return HttpResponseRedirect(self.get_success_url())
        else:
            return self.render_to_response(self.get_context_data(form=form))


def enviaremail(derivacion):
    send_mail(
        'Derivación SOSJujuy',
        mail_body(derivacion),
        'sos.jujuy2018@gmail.com',
        [derivacion.beneficiario.email],
        fail_silently=False,
    )


def mail_body(derivacion):
    cadena = "Hola {0}, " \
             "\nDesde SOSJujuy queremos saber cómo te fue con tu atención de {1}, atendida por {2} el día {3}." \
             "\nEncuesta de atención: sosjujuy.com:8000/encuesta_beneficiario/{4}_{5}" \
             "\nGracias por tu tiempo," \
             "\nSaludos," \
             "\nSOSJujuy"
    return cadena.format(derivacion.beneficiario, derivacion.prestacion.rubro, derivacion.prestacion.prestador,
                         derivacion.fecha_hora.strftime('%d-%m-%Y a las %H:%M'), derivacion.beneficiario.id, derivacion.id)


class DerivacionUpdateView(UpdateView):
    model = Derivacion
    form_class = DerivacionForm
    template_name = 'sosjujuy/derivacion_form.html'
    success_url = reverse_lazy('derivacion_changelist')


class DerivacionDeleteView(DeleteView):
    model = Derivacion
    form_class = DerivacionForm
    template_name = 'sosjujuy/derivacion_delete.html'
    success_url = reverse_lazy('derivacion_changelist')


class ActividadExtensionListView(ListView):
    model = ActividadExtension
    context_object_name = 'actividad_extension'


class ActividadExtensionCreateView(CreateView):
    model = ActividadExtension
    template_name = 'sosjujuy/actividadextension_form.html'
    form_class = ActividadExtensionForm
    success_url = reverse_lazy('actividad_extension_changelist')

    def get_context_data(self, **kwargs):
        context = super(ActividadExtensionCreateView, self).get_context_data(**kwargs)
        if 'form' not in context:
            context['form'] = self.form_class(self.request.GET)
        return context

    def post(self, request, *args, **kwargs):
        self.object = self.get_object
        form = self.form_class(request.POST)
        if form.is_valid():
            actividad_extension = form.save(commit=False)
            actividad_extension.save()
            enviaremailActividad(actividad_extension)
            return HttpResponseRedirect(self.get_success_url())
        else:
            return self.render_to_response(self.get_context_data(form=form))


def enviaremailActividad(actividad):
    obj = Beneficiario.objects.all()
    mails = ()

    for objeto in obj:
        mail = ('Actividades SOSJujuy', mail_bodyActividad(actividad, objeto.nombre), 'sos.jujuy2018@gmail.com', [objeto.email])
        mails = (*mails, mail)

    send_mass_mail(mails, fail_silently=False)


def mail_bodyActividad(actividad, nombre):
    cadena = "Hola " + nombre + ", " \
            "\nDesde SOSJujuy queremos invitarte a participar de la siguiente actividad a realizar: {0}" \
            "\nLa misma será guiada por {1}, y comenzará a partir del {2}." \
            "\nTe esperamos," \
            "\nSaludos," \
            "\nSOSJujuy"
    return cadena.format(actividad.titulo, actividad.disertante, actividad.fecha.strftime('%d-%m-%Y a las %H:%M'))


class ActividadExtensionUpdateView(UpdateView):
    model = ActividadExtension
    template_name = 'sosjujuy/actividadextension_form.html'
    form_class = ActividadExtensionForm
    success_url = reverse_lazy('actividad_extension_changelist')

    def get_context_data(self, **kwargs):
        context = super(ActividadExtensionUpdateView, self).get_context_data(**kwargs)
        pk = self.kwargs.get('pk', 0)
        actividad_extension = self.model.objects.get(id=pk)
        if 'form' not in context:
            context['form'] = self.form_class()
        context['id'] = pk
        return context

    def post(self, request, *args, **kwargs):
        self.object = self.get_object
        id_actividad_extension = kwargs['pk']
        actividad_extension = self.model.objects.get(id=id_actividad_extension)
        form = self.form_class(request.POST, instance=actividad_extension)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(self.get_success_url())
        else:
            return self.render_to_response(self.get_context_data(form=form))


def deleteActividadExtension(request, actividad_extension_id):
    actividad_extension = ActividadExtension.objects.get(pk=actividad_extension_id)
    actividad_extension.delete()

    return redirect('actividad_extension_changelist')


class EncuestaAtencionBeneficiarioCreateView(CreateView):
    model = EncuestaAtencionBeneficiario
    template_name = 'sosjujuy/encuestabeneficiario_form.html'
    form_class = EncuestaAtencionBeneficiarioForm
    success_url = reverse_lazy('index')

    def get_context_data(self, **kwargs):
        context = super(EncuestaAtencionBeneficiarioCreateView, self).get_context_data(**kwargs)
        if 'form' not in context:
            context['form'] = self.form_class(self.request.GET)
        if 'beneficiario' not in context:
            pk_beneficiario = self.kwargs.get('pk_beneficiario', 0)
            context['beneficiario'] = Beneficiario.objects.get(pk=pk_beneficiario)
        if 'derivacion' not in context:
            pk_derivacion = self.kwargs.get('pk_derivacion', 0)
            context['derivacion'] = Derivacion.objects.get(pk=pk_derivacion)
        return context

    def post(self, request, *args, **kwargs):
        self.object = self.get_object
        form = self.form_class(request.POST)
        if form.is_valid():
            encuesta_beneficiario = form.save(commit=False)
            pk_beneficiario = self.kwargs.get('pk_beneficiario', 0)
            encuesta_beneficiario.beneficiario = Beneficiario.objects.get(pk=pk_beneficiario)
            pk_derivacion = self.kwargs.get('pk_derivacion', 0)
            encuesta_beneficiario.derivacion = Derivacion.objects.get(pk=pk_derivacion)
            encuesta_beneficiario.save()
            return HttpResponseRedirect(self.get_success_url())
        else:
            return self.render_to_response(self.get_context_data(form=form))


class DerivacionPDFView(PDFTemplateView):
    model = Derivacion
    template_name = 'sosjujuy/derivacion_pdf.html'
    #form_class = DerivacionPDFForm
    success_url = reverse_lazy('derivacion_changelist')

    def get_context_data(self, **kwargs):
        context = super(DerivacionPDFView, self).get_context_data(**kwargs)
        pk = self.kwargs.get('pk', 0)
        derivacion = self.model.objects.get(id=pk)
        context['id'] = pk
        context['derivacion'] = derivacion
        return context


