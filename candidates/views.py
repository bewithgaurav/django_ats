from rest_framework import viewsets
from rest_framework import filters
from .models import Candidate
from .serializers import CandidateSerializer
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import Candidate
from .serializers import CandidateSerializer

class CandidateViewSet(viewsets.ModelViewSet):
    queryset = Candidate.objects.all()
    serializer_class = CandidateSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['name', 'phone_number', 'email']

@api_view(['GET'])
def name_search(request, query):
    candidates = Candidate.objects.filter(name__icontains=query)
    sorted_candidates = sorted(candidates, key=lambda x: x.name.lower().split(), reverse=True)
    serializer = CandidateSerializer(sorted_candidates, many=True)
    return Response(serializer.data)