def sprints():
    integrs =input("enter int nums: ").split()
    int1= map(int , integrs)
    m = list(int1)
    float_=input("enter float nums: ").split()
    float1=map(float,float_)
    z= list(set(float1))
    total=0
    counter=0
    try:
        for x in m :
            if x%2==0:
                counter += 1
                total += x
        try:
            print(total/counter,z[-1])
        except:
            try:
                print(z[-1])
            except:
                print(total/counter)
    except:
        print(0)
