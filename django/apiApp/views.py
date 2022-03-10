from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt 
#csrf_exempt je tu kako bi dozvolili drugim domenama da mogu dobiti access nasim modelima

from rest_framework.parsers import JSONParser # to parse(devide) incoming data into data model
from  django.http.response import JsonResponse
#When a page is requested, Django creates an HttpRequest object that contains metadata about the request. Then Django loads the appropriate view, passing the HttpRequest as the first argument to the view function. Each view is responsible for returning an HttpResponse object.

from .models import JobOffer,Company
from .serializers import CompanySerializer,JobOfferSerializer



from django.core.files.storage import default_storage #default storage module to save the file




@csrf_exempt # decorator ( @ ) is used to add another function (csrf_exempt) in this function
def companyApi(request,id=0): #the method will recieve an optional id which we will need to use in the delete method
    if request.method == 'GET': # in get method we will return all the records in json format
        company = Company.objects.all()
        company_serializer = CompanySerializer(company,many=True) #we are making use of serializer class to convert it into json format
        return JsonResponse(company_serializer.data,safe=False) #the parameter safe=false is basivally used to inform django that while we are trying to convert to json is actuallty valid format and we are fine is there are still any issue in it
    elif request.method =='POST': #used to insert new records into departments table
        company_data = JSONParser().parse(request) #parsing request
        company_serializer = CompanySerializer(data=company_data) #using serializer to convert it inot model
        if company_serializer.is_valid(): #if model valid, save in database
            company_serializer.save()
            return JsonResponse("Added Sucessfully", safe=False) #and return success message
        return JsonResponse("Failed to Add", safe=False)
    elif request.method =='PUT': #used to update a given record
        company_data = JSONParser().parse(request)
        company = Company.objects.get(CompanyID=company_data['CompanyID']) #first we are capturing the existing record using department id
        company_serializer = CompanySerializer(company,data=company_data) #maping with new value using serializer class
        if company_serializer.is_valid():
            company_serializer.save()
            return JsonResponse("Update Sucessfully", safe=False)
        return JsonResponse("Failed to Update")
    elif request.method == 'DELETE':
        company = Company.objects.get(CompanyID=id)
        company.delete()
        return JsonResponse("Deleted Successfully",safe=False)


@csrf_exempt # decorator ( @ ) is used to add another function (csrf_exempt) in this function
def jobOfferApi(request,id=0): #the method will recieve an optional id which we will need to use in the delete method
    if request.method == 'GET': # in get method we will return all the records in json format
        jobOffer = JobOffer.objects.all()
        jobOffer_serializer = JobOfferSerializer(jobOffer,many=True) #we are making use of serializer class to convert it into json format
        return JsonResponse(jobOffer_serializer.data,safe=False) #the parameter safe=false is basivally used to inform django that while we are trying to convert to json is actuallty valid format and we are fine is there are still any issue in it
    elif request.method =='POST': #used to insert new records into employees table
        jobOffer_data = JSONParser().parse(request) #parsing request
        jobOffer_serializer = JobOfferSerializer(data=jobOffer_data) #using serializer to convert it inot model
        if jobOffer_serializer.is_valid(): #if model valid, save in database
            jobOffer_serializer.save()
            return JsonResponse("Added Sucessfully", safe=False) #and return success message
        return JsonResponse("Failed to Add", safe=False)
    elif request.method =='PUT': #used to update a given record
        jobOffer_data = JSONParser().parse(request)
        jobOffer = JobOffer.objects.get(JobOfferID=jobOffer_data['JobOfferID']) #first we are capturing the existing record using employee id
        jobOffer_serializer = JobOfferSerializer(jobOffer,data=jobOffer_data) #maping with new value using serializer class
        if jobOffer_serializer.is_valid():
            jobOffer_serializer.save()
            return JsonResponse("Update Sucessfully", safe=False)
        return JsonResponse("Failed to Update")
    elif request.method == 'DELETE':
        jobOffer = JobOffer.objects.get(JobOfferID=id)
        jobOffer.delete()
        return JsonResponse("Deleted Successfully",safe=False)

@csrf_exempt
def SaveFile(request):
    file=request.FILES['file']
    file_name=default_storage.save(file.name,file)
    return JsonResponse(file_name,safe=False)
