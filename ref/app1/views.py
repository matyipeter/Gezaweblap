from django.shortcuts import render, redirect
from django.views.generic import TemplateView, ListView
from django.views import View
from .models import Service, Reference, Customer

# Create your views here.

class IndexView(TemplateView):
    
    template_name = "app1/index.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["ref"] = Reference.objects.get(pk=1)
        return context
    
class Bemutakozas(TemplateView):
    template_name = "app1/bemutatkozas.html"


class ServicesView(ListView):
    template_name = "app1/services.html"
    queryset = Service.objects.all()


class ReferenceView(ListView):
    template_name = "app1/reference.html"
    queryset = Reference.objects.all()


class Thanks(TemplateView):
    template_name = "app1/thanks.html"

class ContactView(View):

    def get(self, request):
        return render(request, "app1/contact.html")
    
    def post(self, request):
        fname = request.POST["fname"]
        lname = request.POST["lname"]
        email = request.POST["email"]
        message = request.POST["message"]
        new_customer = Customer(first_name=fname,last_name=lname,email=email,message=message)
        new_customer.save()
        return redirect("app1:thanks")