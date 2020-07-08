import views
from django.urls import path

app_name = 'app'
urlpatterns = [
    # Routes to a page where users can fill in their medical information with relevant questions
    path("users/", views.UserInformationView.as_view(), name="user_information"),

    # An endpoint that recieves the user's response to questions that request for medical information
    path("users/question/<int:pk>", views.UserResponseSubmitView.as_view(), name="submit_user_response")

    # Routes to a page that contains a table which displays all users and their relevant medical records
    path("records/", views.UserRecordsView.as_view(), name="user_records"),

    # Routes to a page that displays the statistical details of the medical records gotten from the users
    path("statistics/", views.UserRecordStatisticsView.as_view(), name="user_record_statistics"),
]
