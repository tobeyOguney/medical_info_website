from django.views.generic.edit import CreateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.list import ListView
from django.shortcuts import render
from django.views import View
from .models import User, UserFieldQuestion


class UserInformationView(LoginRequiredMixin, View):
    template_name = 'app/user_records.html'

    def get_context_data(self, *args, **kwargs):
        context = super(UserRecordsStatisticsView, self).get_context_data(*args, **kwargs)
        
        #TODO

        return context    

class UserResponseSubmitView(LoginRequiredMixin, View):
    
    def post(self, request, pk):
        field_question = UserFieldQuestion.objects.get(pk=pk)

        if field_question.user_field == UserFieldQuestion.FIELD_CHOICES[0][0]:
            request.user.age = request.data.get(UserFieldQuestion.FIELD_CHOICES[0][0])

        elif field_question.user_field == UserFieldQuestion.FIELD_CHOICES[1][0]:
            request.user.sex = request.data.get(UserFieldQuestion.FIELD_CHOICES[1][0])

        elif field_question.user_field == UserFieldQuestion.FIELD_CHOICES[2][0]:
            request.user.blood_type = request.data.get(UserFieldQuestion.FIELD_CHOICES[2][0])

        elif field_question.user_field == UserFieldQuestion.FIELD_CHOICES[3][0]:
            request.user.genotype = request.data.get(UserFieldQuestion.FIELD_CHOICES[3][0])

        elif field_question.user_field == UserFieldQuestion.FIELD_CHOICES[4][0]:
            request.user.AIDS_status = request.data.get(UserFieldQuestion.FIELD_CHOICES[4][0])

        elif field_question.user_field == UserFieldQuestion.FIELD_CHOICES[5][0]:
            request.user.malaria_status = request.data.get(UserFieldQuestion.FIELD_CHOICES[5][0])

        elif field_question.user_field == UserFieldQuestion.FIELD_CHOICES[6][0]:
            request.user.ebola_status = request.data.get(UserFieldQuestion.FIELD_CHOICES[6][0])

        elif field_question.user_field == UserFieldQuestion.FIELD_CHOICES[7][0]:
            request.user.COVID19_status = request.data.get(UserFieldQuestion.FIELD_CHOICES[7][0])
        
        request.user.save()


class UserRecordsView(LoginRequiredMixin, ListView):
    model = User
    template_name = 'app/user_records.html'


class UserRecordsStatisticsView(LoginRequiredMixin, View):
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
    form_class = UserSignupForm
    template_name = 'app/user_signup.html'
    success_url = reverse_lazy('app:user_information')
