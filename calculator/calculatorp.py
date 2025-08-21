import addition as ad
import subtraction as sb
import multiplication as mp
import division as dv
import module as md
operations={
    "1.Addition \n" 
    "2.Subtraction \n"
    "3.Multiplication \n"
    "4.Division \n"
    "5.Module \n"

}

if __name__ == "__main__":
    print(operations)
    choice =int(input("Please select your opreation : "))
    if choice ==1:
        a= list(map(int,input().split()))
        res= ad.add(a)
        print("sum of two number:",res)
    elif choice ==2:
        a,b= map(int,input().split())
        res= sb.sub(a,b)
        print("difference of two number:",res)
    elif choice ==3:
        a= list(map(int,input().split()))
        res= mp.mup(a)
        print("Multiplication of two number:",res)
    elif choice ==4:
        a,b= map(int,input().split())
        res= dv.div(a,b)
        print("Division of two number:",res)
    elif choice ==5:
        a,b= map(int,input().split())
        res= md.mod(a,b)
        print("Module of two number:",res)
    else:
        print("This operations is not present")
    