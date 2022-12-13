from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from django.views.generic import FormView
from .models import Proyecto
from .forms import ProyectoForm


# Create your views here.

@login_required
def home(request):
    proyectos=Proyecto.objects.all()
    context={
        "proyectos":proyectos
    }
    return render(request,'session/index.html',context)

class CreateProject(FormView):
    model = Proyecto
    form_class = ProyectoForm
    template_name = "session/form.html"
    # para guardar la informacion existe lo que es una funcion llamada
    def form_valid(self, form):
        Proyecto.objects.create(**form.cleaned_data)
        return redirect('session-home')

    def form_invalid(self, form):
        print("errors", form.errors)
        return redirect('session-home')
