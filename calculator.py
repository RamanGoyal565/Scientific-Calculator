import math

a=int(input("enter your number: "))
print("For performing factorial use:'!',sine use:'sin',cosine use:'cos',tangent use:'tan',secant:'sec',cosecant:'cosec,"
      "cotangent:'cot',sininverse:'asine',cosinverse:'acos',taninverse:'atan',cotinverse:'acot',cosecinverse:'acosec,secinverse:'asec'")
b=" "
ans=0
while b!="":
    print("To get answer press enter")
    b=str(input("operation: "))     
    if b == "*":
        c = int(input("enter second number: "))
        ans= a*c
    elif b =="/":
        c = int(input("enter second number: "))
        ans= a/c
    elif b == "+":
        c = int(input("enter second number: "))
        ans=a+c
    elif b == "-":
        c = int(input("enter second number: "))
        ans=a-c
    elif b == "%":
        c = int(input("enter second number: "))
        ans=a%c
    elif b == "//":
        c = int(input("enter second number: "))
        ans=a//c
    elif b == "pow":
        c = int(input("enter second number: "))
        ans=math.pow(a,c)
    elif b == "sin":
        ans=round(math.sin(a),2)
    elif b == "cos":
        ans = round(math.cos(a),2)
    elif b == "tan":
        ans = round(math.tan(a),2)
    elif b == "cosec":
        try:
            ans = round(1/math.sin(a),2)
        except ZeroDivisionError:
            print("cosec of",ans,"is not defined")
    elif b == "sec":
        try:
            ans = round(1/math.cos(a),2)
        except ZeroDivisionError:
            print("sec of",ans,"is not defined")
        
    elif b == "cot":
        try:
            ans = round(1/math.tan(a),2)
        except ZeroDivisionError:
            print("cot of",ans,"is not defined")
    elif b == "square":
        ans = math.pow(a,2)
    elif b == "sqrt":
        ans = math.sqrt(a)
    elif b == "cube":
        ans = math.pow(a,3)
    elif b == "cbrt":
        ans = math.pow(a,1/3)
    elif b == "log":
        c = int(input("enter second number: "))
        ans = math.log(a,c)
    elif b == "expo":
        ans = math.exp(a)
    elif b == "asin":
        ans = round(math.asin(a),2)
    elif b == "acos":
        ans = round(math.acos(a),2)
    elif b == "atan":
        ans = round(math.atan(a),2)
    elif b == "acosec":
        ans = 1/math.asin(a)
    elif b == "asec":
        ans = 1/math.acos(a)
    elif b == "acot":
        ans = 1/math.atan(a)
    elif b == "per":
        ans= a/100
    elif b == "abs":
        ans = abs(a)
    elif b == "!":
        ans = math.factorial(a)
    a=ans
print(ans)
