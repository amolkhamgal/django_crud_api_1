from django.shortcuts import render
from .models import Employee
from .serializers import EmpSerializer
from rest_framework import viewsets
from rest_framework.decorators import api_view
from rest_framework import status
from rest_framework.response import Response
from rest_framework.authentication import BasicAuthentication,SessionAuthentication,TokenAuthentication
from rest_framework.permissions import AllowAny,IsAdminUser,IsAuthenticated,IsAuthenticatedOrReadOnly,DjangoModelPermissions,DjangoModelPermissionsOrAnonReadOnly
from rest_framework_simplejwt.authentication import JWTAuthentication
# Create your views here.


# Class Based Operatons:

class EmployeeData(viewsets.ModelViewSet):
    queryset=Employee.objects.all()
    serializer_class=EmpSerializer
    authentication_classes=[BasicAuthentication,SessionAuthentication,JWTAuthentication]
    permission_classes=[IsAuthenticated]
    


# Function Based Opearions:    
@api_view(["GET","POST"])
def get_post_emp(request):
    if request.method=="GET":
        all_emp=Employee.objects.all()
        empSer=EmpSerializer(all_emp,many=True)
        return Response(empSer.data,status=status.HTTP_200_OK)
    elif request.method=="POST":
        data_post=EmpSerializer(data=request.data)
        if data_post.is_valid():
            data_post.save()
            return Response(data_post.data,status=status.HTTP_201_CREATED)
        return Response(data_post.errors,status=status.HTTP_400_BAD_REQUEST)
    
@api_view(["GET","PUT","DELETE"])
def update_delete_emp(request,pk):
    try:
        emp_data=Employee.objects.get(pk=pk)
        
    except Employee.DoesNotExist:
        return  Response(status=status.HTTP_404_NOT_FOUND)
    
    if request.method=="GET":
        empSer=EmpSerializer(emp_data)
        return Response(empSer.data,status=status.HTTP_200_OK)
    elif request.method=="PUT":
        update_data=EmpSerializer(emp_data,data=request.data)
        if update_data.is_valid():
            update_data.save()
            return Response(update_data.data,status=status.HTTP_202_ACCEPTED)
        return Response(update_data.errors,status=status.HTTP_400_BAD_REQUEST)
    elif request.method=="DELETE":
        emp_data.delete()
        return Response(f"Data Deleted succeessfully")       
    
        

    
