from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import *

router = DefaultRouter()
router.register(r'companies', CompanyViewSet)
router.register(r'esg-data', ESGDataViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('fetch-esg-data/<int:company_id>/', ESGDataFetchView.as_view({'get': 'retrieve'})),
    path('nlp-query/', NLPQueryView.as_view(), name='nlp-query'),
    path('llm-insights/', LLMInsightsView.as_view(), name='llm-insights'),
    path('import-esg-data/', import_esg_data, name='import-esg-data'),
]