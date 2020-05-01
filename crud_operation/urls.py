from django.urls import path
from . import views as crud_views


urlpatterns = [
    path('grupo-economico-list/', crud_views.GrupoEconomicoAPIView.as_view()),
    path('add-grupo-economico/', crud_views.GrupoEconomicoCreateView.as_view(),
        name="add_grupo_economico" ),
    path('update-grupo-economico/<int:id_grupo_economico>/', crud_views.GrupoEconomicoUpdateView.as_view(),
        name="update_grupo_economico" ),
    path('delete-grupo-economico/<int:id_grupo_economico>/', crud_views.GrupoEconomicoDeleteView.as_view(),
        name="delete_grupo_economico" ),
    path('detail-grupo-economico/<int:id_grupo_economico>/', crud_views.GrupoEconomicoDetailView.as_view(),
        name="detail_grupo_economico" ),

    path('cedente/', crud_views.CedenteView.as_view(), name="cedente"),
    path('cedente-list/', crud_views.CedenteAPIView.as_view()),
    path('add-cedente/', crud_views.CedenteCreateView.as_view(),
        name="add_cedente" ),
    path('update-cedente/<int:id_cedente>/', crud_views.CedenteUpdateView.as_view(),
        name="update_cedente" ),
    path('delete-cedente/<int:id_cedente>/', crud_views.CedenteDeleteView.as_view(),
        name="delete_cedente" ),
    path('detail-cedente/<int:id_cedente>/', crud_views.CedenteDetailView.as_view(),
        name="detail_cedente" ),

    path('limite-credito-cedente-list/', crud_views.LimiteCreditoCedenteAPIView.as_view()),
    path('limite-credito-cedente/', crud_views.LimiteCreditoCedenteView.as_view(),
        name="limite_credito_cedente"),
    path('add-limite-credito-cedente/', crud_views.LimiteCreditoCedenteCreateView.as_view(),
        name="add_limite_credito_cedente" ),
    path('update-limite-credito-cedente/<int:id_limite_credito_cedente>/', crud_views.LimiteCreditoCedenteUpdateView.as_view(),
        name="update_limite_credito_cedente" ),
    path('delete-limite-credito-cedente/<int:id_limite_credito_cedente>/', crud_views.LimiteCreditoCedenteDeleteView.as_view(),
        name="delete_limite_credito_cedente" ),
    path('detail-limite-credito-cedente/<int:id_limite_credito_cedente>/', crud_views.LimiteCreditoCedenteDetailView.as_view(),
        name="detail_limite_credito_cedente" ),
]
