from rest_framework import viewsets
from rest_framework import filters
from .models import Candidate
from .serializers import CandidateSerializer
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import Candidate
from .serializers import CandidateSerializer
from rest_framework import generics
from .models import Candidate
from .serializers import CandidateSerializer
from rest_framework import status

class CandidateViewSet(viewsets.ModelViewSet):
    queryset = Candidate.objects.all()
    serializer_class = CandidateSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['name', 'phone_number', 'email', 'status', 'current_salary', 'expected_salary', 'years_of_exp', 'age']

from rest_framework import generics
from .models import Candidate
from .serializers import CandidateSerializer
from rest_framework.response import Response
from rest_framework import status


class CandidateAPIView(generics.ListCreateAPIView):
    queryset = Candidate.objects.all()
    serializer_class = CandidateSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)

class CandidateSearchAPIView(generics.ListAPIView):
    serializer_class = CandidateSerializer

    def get_queryset(self):
        queryset = Candidate.objects.all()

        # Apply filters based on query parameters
        expected_salary_min = self.request.query_params.get('expected_salary_min')
        expected_salary_max = self.request.query_params.get('expected_salary_max')
        age_min = self.request.query_params.get('age_min')
        age_max = self.request.query_params.get('age_max')
        years_of_exp_min = self.request.query_params.get('years_of_exp_min')
        phone_number = self.request.query_params.get('phone_number')
        email = self.request.query_params.get('email')
        name = self.request.query_params.get('name')
        print("HIIII")
        if expected_salary_min:
            queryset = queryset.filter(expected_salary__gte=expected_salary_min)
        if expected_salary_max:
            queryset = queryset.filter(expected_salary__lte=expected_salary_max)
        if age_min:
            queryset = queryset.filter(age__gte=age_min)
        if age_max:
            queryset = queryset.filter(age__lte=age_max)
        if years_of_exp_min:
            queryset = queryset.filter(years_of_exp__gte=years_of_exp_min)
        if phone_number:
            queryset = queryset.filter(phone_number=phone_number)
        if email:
            queryset = queryset.filter(email=email)
        if name:
            queryset = queryset.filter(name__icontains=name)

        # Debugging: Print the queryset
        print("Filtered queryset:", queryset)

        return queryset

    def list(self, request, *args, **kwargs):
        queryset = self.get_queryset()
        serializer = self.serializer_class(queryset, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)