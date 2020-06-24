from django.shortcuts import render, HttpResponse, HttpResponseRedirect
from django.views.generic import TemplateView
from accounts.models import newLead
from accounts.forms import HomeForm

# Create your views here.
class HomeView(TemplateView):
    template_name = 'accounts/home.html'

    def get(self, request):
        form = HomeForm()
        return render(request, self.template_name, {'form': form})

    def post( self, request):
    # if this is a POST request we need to process the form data
        # create a form instance and populate it with data from the request:
        form = HomeForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            # process the data in form.cleaned_data as required
            first_name = form.cleaned_data['first_name']
            last_name = form.cleaned_data['last_name']
            email = form.cleaned_data['email']
            phone_number = form.cleaned_data['phone_number']
            address_of_property = form.cleaned_data['address_of_property']

            # insert data into database
            newLead.objects.create(
                first_name=first_name,
                last_name=last_name,
                email=email,
                phone_number=phone_number,
                address_of_property=address_of_property
            )

            # redirect to a new URL:
            # create a "thank you" page
            return HttpResponseRedirect('/account')
