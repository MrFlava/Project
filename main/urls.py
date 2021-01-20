from django.urls import path

from . import views

urlpatterns = [
    path("portfolios", views.PortfolioListView.as_view(), name="my-portfolios"),
    path("portfolios/create", views.PortfolioCreateView.as_view(), name="create-portfolio"),
    path("portfolios/<int:pk>/update", views.PortfolioUpdateView.as_view(), name="update-portfolio"),
    path("portfolios/<int:pk>/delete", views.PortfolioDeleteView.as_view(), name="delete-portfolio"),
    path("portfolios/<str:portfolio_name>/images", views.ImageGetPortfolioNameView.as_view(), name="get-images-by-portfolio-name"),

    path("images", views.ImageListView.as_view(), name="image-feed"),
    path("images/create", views.ImageCreateView.as_view(), name="create-image"),
    path("images/<int:pk>/update", views.ImageUpdateView.as_view(), name="update-image"),
    path("images/<int:pk>/delete", views.ImageDeleteView.as_view(), name="delete-image"),
    path("images/name/<str:name>", views.ImageGetNameView.as_view(), name="get-image-by-name"),
    path("images/desc/<str:desc>", views.ImageGetDescriptionView.as_view(), name="get-image-by-desc"),
    path("images/<int:image_id>/comments/create", views.ImageCreateCommentView.as_view(), name="image-create-comment"),

]
