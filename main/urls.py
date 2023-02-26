from django.urls import path
from .views import HomeView, RegisterView, LoginView, LogoutView, CreateView, AssignView, DashboardView, CompleteView

app_name = "main"

urlpatterns = [
    path("", HomeView.as_view(), name="home"),
    path("dashboard", DashboardView.as_view(), name="dashboard"),
    path("register", RegisterView.as_view(), name="register"),
    path("login", LoginView.as_view(), name="login"),
    path("create", CreateView.as_view(), name="create"),
    path("assign", AssignView.as_view(), name="assign"),
    path("complete", CompleteView.as_view(), name="complete"),
    path("logout", LogoutView.as_view(), name="logout"),
]
