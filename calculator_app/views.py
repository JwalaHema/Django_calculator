from django.shortcuts import render

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