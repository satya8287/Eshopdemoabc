from django.shortcuts import render, redirect
from django.contrib.auth.hashers import make_password
from store.models.customer import Customer
from django.views import View


class Signup(View):
    def get(self, request):
        return render(request, 'signup.html')

    def post(self, request):
        postData = request.POST
        first_name = postData.get('firstname')
        last_name = postData.get('lastname')
        phone = postData.get('mobile')
        email = postData.get('email')
        password = postData.get('password')

        # retaining the previously filled value in dictionary

        value = {
            'first_name': first_name,
            'last_name': last_name,
            'phone': phone,
            'email': email
        }

        customer = Customer(first_name=first_name,
                            last_name=last_name,
                            phone=phone,
                            email=email,
                            password=password)
        error_msg = self.validateCustomer(customer)

        # saving
        if not error_msg:
            customer.password = make_password(customer.password)
            customer.register()

            return redirect('homepage')
        else:

            data = {
                'error': error_msg,
                'values': value
            }
            return render(request, 'signup.html', data)
            ##

    def validateCustomer(self, customer):
        # validation
        error_msg = None

        if not customer.first_name:
            error_msg = "Naam btta tu bye/first name required file views.py mai edit kar lena phele deploy kare ne " \
                        "phele "
        elif len(customer.first_name) < 4:
            error_msg = "too short aname "
        elif not customer.last_name:
            error_msg = "last name required"
        elif len(customer.last_name) < 4:
            error_msg = "too short last name"
        elif not customer.phone:
            error_msg = "phone number required"
        elif len(customer.phone) <= 10:
            error_msg = "phone number must be 10 digit"
        elif not customer.email:
            error_msg = "email nhi daal bhe "
        elif not customer.password:
            error_msg = "paassoed not match"
        elif customer.isExists():
            error_msg = "email exist enter other email"

        return error_msg
    ##classs end
