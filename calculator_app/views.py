from django.shortcuts import render
from .models import Contact

# def calculator(request):
#     result=None

#     if request.method=="POST":  
        
#         num1=int(request.POST.get("num1"))
#         num2=int(request.POST.get("num2"))
#         operation=request.POST.get("operation")
    
#         if operation == "+":
#             result=num1+num2
#         elif operation == "-":
#             result=num1-num2
#         elif operation == "*":
#             result=num1*num2
#         elif operation =="%":
#             result=num1%num2
#         elif operation =="/":
#             result=num1/num2

#     return render(request, "calculator.html", {"result":result})


def calculator(request):
    display=request.session.get("display","")

    if request.method=="GET":
        if "clear" in request.GET:
            display=""

        elif "delete" in request.GET:
            display=display[:-1]
    
        elif "num" in request.GET:
            display+=request.GET.get("num")
        
        elif "operation" in request.GET:
            op=request.GET.get("operation")

            if op=="=":

                try:
                    # display=str(eval(display))

                    if "+" in display:
                         num1,num2=display.split("+")
                         display=str(int(num1)+int(num2))

                    elif "-" in display:
                        num1,num2=display.split("-")
                        display=str(int(num1)-int(num2))

                    elif "*" in display:
                        num1,num2=display.split("*")
                        display=str(int(num1)*int(num2))

                    elif "/" in display:
                        num1,num2=display.split("/")
                        display=str(int(num1)/int(num2))

                    elif "%" in display:
                        num1,num2=display.split("%")
                        display=str(int(num1)%int(num2))
            
                except Exception as e:
                    display=type(e).__name__

            else:
                display+=op
        
        request.session["display"]=display
    
    else:
        display=""
        request.session["display"]=display
    
    return render(request, "calculator.html", {"display": display})


def contact_form(request):
    success_message=""
    errors={}
    if request.method=="POST":
        firstName=request.POST.get("firstName")
        lastName=request.POST.get("lastName")
        email=request.POST.get("email")
        number=request.POST.get("number")
        message=request.POST.get("message")

        if not firstName:
            errors['firstName']="First Name Is Required"
        elif not firstName.replace(" ","").isalpha():
            errors['firstName']="only accepts alphabets ans spaces"
        
        if not lastName:
            errors['lastName']="Last Name Is Required"
        elif not lastName.replace(" ","").isalpha():
            errors['lastName']="only accepts alphabets ans spaces"

        if not email:
            errors['email']="Email Is Requird"
        elif "@" not in email:
            errors['email']="Invaild email format"

        if not number:
            errors['number']="Phone Number Is Required"
        elif len(number)<10:
            errors['number']="Should be 10 digits"

        if not message:
            errors['message']="Message Is Required "
        elif len(message)>300:
            errors['message']="should not exceed 300 characters"

        if not errors:
            Contact.objects.create(
                firstName=firstName,
                lastName=lastName,
                email=email,
                number=number,
                message=message,
            )

        if not errors:
            success_message="Form Submitted"

    return render(request,'form.html',{"success_message":success_message, "errors":errors})