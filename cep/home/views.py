from django.shortcuts import render, HttpResponse
from home.models import Customer, Payment
# Create your views here.

def home(request):
    return render(request, 'home.html')

def about(request):
    return HttpResponse('This is about page.')

def vehicles(request):
    return render(request, 'vehicles.html')

def form(request):
    if request.method == 'POST':
        CustID = request.POST.get('custid')
        CustName = request.POST.get('custname')
        CustContact = request.POST.get('custcontact')
        CustCity = request.POST.get('custcity')
        CustEmail = request.POST.get('custemail')
        CustDOB = request.POST.get('custdob')
        CustGender = request.POST.get('custgender')
        CustHouse = request.POST.get('custaddress')
        cust = Customer(custid=CustID, custname=CustName, custcontact=CustContact, custcity=CustCity, custemail=CustEmail, custdob=CustDOB, custgender=CustGender, custhouse=CustHouse)
        cust.save()

    return render(request, 'form.html')

def payment(request):
    if request.method == 'POST':
        PayID = request.POST.get('payid')
        DateOfPayment = request.POST.get('dateofpayment')
        PaymentMethod = request.POST.get('paymentmethod')
        PaymentStatus = request.POST.get('paymentstatus')
        CustID = request.POST.get('custid')

        customer = Customer.objects.get(custid=CustID)  # Retrieve the Customer instance
        payment = Payment(payid=PayID, dateofpayment=DateOfPayment, paymentmethod=PaymentMethod, paymentstatus=PaymentStatus, custid=customer)
        payment.save()

    return render(request, 'payment.html')