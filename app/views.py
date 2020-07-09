from django.views.generic.edit import CreateView, UpdateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.list import ListView
from django.shortcuts import render
from django.views.generic.base import TemplateView, RedirectView
from django.views import View
from django.urls import reverse_lazy
from django.shortcuts import redirect
from .models import User
from .forms import (
    UserSignupForm, AgeForm, SexForm, BloodTypeForm, GenotypeForm, AIDSForm,
    MalariaForm, EbolaForm, COVID19Form
)


class UserRedirectView(LoginRequiredMixin, RedirectView):
    """
    Depending on if user is a medical practitioner or not, redirects to corresponding
    root page after login
    """

    def get_redirect_url(self, *args, **kwargs):
        if self.request.user.is_practitioner:
            return reverse_lazy("app:user_records")

        return reverse_lazy("app:user_information")


class UserInformationView(LoginRequiredMixin, TemplateView):
    """
    Serves a page where users can fill in their medical information
    """
    model = User
    template_name = 'app/user_information.html'
    
    def post(self, request, *args, **kwargs):
        print(request.POST)
        if "age" in request.POST:
            request.user.age = request.POST.get('age')
        elif "sex" in request.POST:
            request.user.sex = request.POST.get('sex')
        elif "blood_type" in request.POST:
            request.user.blood_type = request.POST.get('blood_type')
        elif "genotype" in request.POST:
            request.user.genotype = request.POST.get('genotype')
        elif "AIDS_status" in request.POST:
            request.user.AIDS_status = request.POST.get('AIDS_status')
        elif "malaria_status" in request.POST:
            request.user.malaria_status = request.POST.get('malaria_status')
        elif "ebola_status" in request.POST:
            request.user.ebola_status = request.POST.get('ebola_status')
        elif "COVID19_status" in request.POST:
            request.user.COVID19_status = request.POST.get('COVID19_status')
        
        request.user.save()

        return redirect("app:user_information")

    def get_context_data(self, *args, **kwargs):
        context = super(UserInformationView, self).get_context_data(*args, **kwargs)
        context.update({
            "object_list": [
                {
                    "question": "What is your age?",
                    "form": AgeForm(instance=self.request.user),
                },
                {
                    "question": "What is your sex?",
                    "form": SexForm,
                },
                {
                    "question": "What is your blood type?",
                    "form": BloodTypeForm,
                },
                {
                    "question": "What is your genotype?",
                    "form": GenotypeForm,
                },
                {
                    "question": "What is your AIDS status?",
                    "form": AIDSForm,
                },
                {
                    "question": "What is your Malaria status?",
                    "form": MalariaForm,
                },
                {
                    "question": "What is your Ebola status?",
                    "form": EbolaForm,
                },
                {
                    "question": "What is your COVID-19 status?",
                    "form": COVID19Form,
                },
            ]
        })
        return context


class UserRecordsView(LoginRequiredMixin, ListView):
    """
    Serves a page that contains a table which displays all users and their relevant medical records
    """

    model = User
    template_name = 'app/user_records.html'


class UserRecordsStatisticsView(LoginRequiredMixin, TemplateView):
    """
    Serves a page that displays the statistical details of the medical records gotten from the users
    """

    template_name = 'app/user_records_statistics.html'

    def get_context_data(self, *args, **kwargs):
        context = super(UserRecordsStatisticsView, self).get_context_data(*args, **kwargs)
        context.update({
            'aids': {
                "positive_count": User.objects.filter(AIDS_status=User.TEST_STATUS_CHOICES[0][0]).count(),
                "not_tested_count": User.objects.filter(AIDS_status=User.TEST_STATUS_CHOICES[2][0]).count(),
            },
            'malaria': {
                "positive_count": User.objects.filter(malaria_status=User.TEST_STATUS_CHOICES[0][0]).count(),
                "not_tested_count": User.objects.filter(malaria_status=User.TEST_STATUS_CHOICES[2][0]).count(),
            },
            'ebola': {
                "positive_count": User.objects.filter(ebola_status=User.TEST_STATUS_CHOICES[0][0]).count(),
                "not_tested_count": User.objects.filter(ebola_status=User.TEST_STATUS_CHOICES[2][0]).count(),
            },
            'covid19': {
                "positive_count": User.objects.filter(COVID19_status=User.TEST_RESULT_CHOICES[0][0]).count(),
                "not_tested_count": User.objects.filter(COVID19_status=User.TEST_RESULT_CHOICES[2][0]).count(),
            },
        })
        return context


class UserSignupView(CreateView):
    """
    Mediates the creation of new users
    """

    form_class = UserSignupForm
    template_name = 'registration/user_signup.html'
    success_url = reverse_lazy('app:user_information')
