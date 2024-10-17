import requests
from rest_framework import viewsets
from .models import Company, ESGData
from .serializers import CompanySerializer, ESGDataSerializer
from rest_framework.response import Response
from rest_framework.views import APIView
from .nlp_service import NLPService
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
import pandas as pd
from .models import ESGData

class CompanyViewSet(viewsets.ModelViewSet):
    queryset = Company.objects.all()
    serializer_class = CompanySerializer

class ESGDataViewSet(viewsets.ModelViewSet):
    queryset = ESGData.objects.all()
    serializer_class = ESGDataSerializer

def fetch_esg_data_from_api(company_name):
    # Replace with your actual ESG data API endpoint
    api_url = f"http://127.0.0.1:8000/api/company={company_name}"
    response = requests.get(api_url)
    if response.status_code == 200:
        return response.json()
    return None

class ESGDataFetchView(viewsets.ViewSet):
    def retrieve(self, request, company_id=None):
        try:
            company = Company.objects.get(id=company_id)
            esg_data = ESGData.objects.filter(company=company).first()  # Retrieve ESG data for the company

            if esg_data:
                serializer = ESGDataSerializer(esg_data)
                return Response(serializer.data)
            return Response({"error": "ESG data not found for this company"}, status=404)
        except Company.DoesNotExist:
            return Response({"error": "Company not found"}, status=404)

    
class NLPQueryView(APIView):
    def post(self, request):
        nlp_service = NLPService()
        query = request.data.get('query', '')
        processed_query = nlp_service.process_query(query)
        # You can add logic here to use processed_query for fetching data
        return Response({'processed_query': processed_query})

class LLMInsightsView(APIView):
    def post(self, request):
        query = request.data.get('query', '')
        if not query:
            return Response({"error": "Query is required"}, status=status.HTTP_400_BAD_REQUEST)

        nlp_service = NLPService()
        insights = nlp_service.process_query(query)

        return Response(insights, status=status.HTTP_200_OK)

@api_view(['POST'])
def import_esg_data(request):
    file = request.FILES.get('file')
    if not file:
        return Response({"error": "No file provided"}, status=400)

    df = pd.read_csv(file)
    for index, row in df.iterrows():
        # Assuming the DataFrame has columns that match your model
        esg_data = ESGData(
            company=row['company'],
            environmental=row['environmental'],
            social=row['social'],
            governance=row['governance']
        )
        esg_data.save()

    return Response({"message": "Data imported successfully"})