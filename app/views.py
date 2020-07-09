from django.views.generic.edit import CreateView, UpdateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.list import ListView
from django.shortcuts import render
from django.views.generic.base import TemplateView, RedirectView
from django.views import View
from django.urls import reverse_lazy
from django.shortcuts import redirect
from django.http import JsonResponse
from rest_framework.generics import ListAPIView
from .serializers import UserSerializer
from .pagination import StandardResultsSetPagination
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


class UserListing(ListAPIView):
    # set the pagination and serializer class

    pagination_class = StandardResultsSetPagination
    serializer_class = UserSerializer

    def get_queryset(self):
        # filter the queryset based on the filters applied
        queryList = User.objects.filter(is_practitioner=False).all()
        AIDS_status = self.request.query_params.get('AIDS_status', None)
        malaria_status = self.request.query_params.get('malaria_status', None)
        ebola_status = self.request.query_params.get('ebola_status', None)
        COVID19_status = self.request.query_params.get('COVID19_status', None)
        sort_by = self.request.query_params.get('sort_by', None)

        if AIDS_status:
            queryList = queryList.filter(AIDS_status = AIDS_status)  
        if malaria_status:
            queryList = queryList.filter(malaria_status = malaria_status)  
        if ebola_status:
            queryList = queryList.filter(ebola_status = ebola_status)  
        if COVID19_status:
            queryList = queryList.filter(COVID19_status = COVID19_status)    

        # sort it if applied on based on age

        if sort_by == "age":
            queryList = queryList.order_by("age")
        if sort_by == "blood_type":
            queryList = queryList.order_by("blood_type")
        if sort_by == "genotype":
            queryList = queryList.order_by("genotype")
        if sort_by == "sex":
            queryList = queryList.order_by("sex")
            
        return queryList


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
                "positive_count": User.objects.filter(COVID19_status=User.TEST_STATUS_CHOICES[0][0]).count(),
                "not_tested_count": User.objects.filter(COVID19_status=User.TEST_STATUS_CHOICES[2][0]).count(),
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


def get_test_status(request):
    if request.method == "GET" and request.is_ajax():
        test_status = [i[0] for i in User.TEST_STATUS_CHOICES]
        data = {
            "test_status": test_status, 
        }
        return JsonResponse(data, status = 200)
