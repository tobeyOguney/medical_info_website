from .views import (
    UserInformationView, UserRecordsStatisticsView, UserRecordsView, UserRedirectView, UserListing,
    get_test_status,
)
from django.urls import path

app_name = 'app'
urlpatterns = [
    # Routes to root page depending on if user is a medical practitioner or not
    path("redirect/", UserRedirectView.as_view(), name="user_redirect"),

    # Routes to a page where users can fill in their medical information
    path("user/", UserInformationView.as_view(), name="user_information"),

    # Routes to a page that contains a table which displays all users and their relevant medical records
    path("records/", UserRecordsView.as_view(), name="user_records"),

    # Routes to a page that displays the statistical details of the medical records gotten from the users
    path("statistics/", UserRecordsStatisticsView.as_view(), name="user_record_statistics"),

    path("user_listing/", UserListing.as_view(), name = 'user_listing'),
    path("ajax/test_status/", get_test_status, name = 'get_test_status'),
]
