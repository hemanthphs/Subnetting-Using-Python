print("-----------------------------------SUBNET CALCULATOR--------------------------------------")
print("""Instructions:\n""")
print("You are prompted to choose type of Subnet (or) valid Host ranges (or) No.of Subnets and Hosts.")
print("1 (or) 2. Displays all the IP ranges in the given Network ID.")
print("   Additionally it displays new Subnet mask, it's binary form ,Prefix length ,N/W's and Hosts")
print(" 3. It displays Network and Broadcast addresses, Host range for the given Network.")
print(" 4. It displays number of Hosts and Subnets, number of Valid Hosts in a given Subnet.")
while 1:
    print("--------------------\n")
    print("CALCULATIONS:")
    a=int(input("Enter the choice of subnet:\n1.FLSM \n2.VLSM \n3.Valid Host ranges on the Subnetwork\n4.No.of Subnets and Hosts\n"))
    if a==1:
        print("Your choice is FLSM")
        while 1:
            b=input("Enter the required number of ip address: \n")
            if b.isdigit():
                b=int(b)
                break
            else:
                print("You enter number is invaild.So re-check and ",end="")
                continue
    elif a==2:
        print("Your choice is VLSM")
        list1=list(map(str,input("Enter the required number of ip address with spaces:(In decreasing order) \n").split()))
        for k in range(len(list1)):
            if list1[k].isdigit():
                list1[k]=int(list1[k])
            else:
                while 1:
                    print("You entered {}. This number is invaild.So re-check and Enter the number again:\n".format(list1[k]))
                    list1[k]=input()
                    if list1[k].isdigit():
                        list1[k]=int(list1[k])
                        break
                    else:
                        continue
        #print(list1)
        b=sum(list1)
    if a==1 or a==2:
        i=1
        d=0
        while(i<b):
            if 2**i>=b+2:
                break
            i=i+1
        d=i
        y_n=input("Do you have any preferred network id :(Y or N)\n")
        if y_n=='Y' or y_n=='y':
                if i<=8:
                    print("Enter the IP ID in the range(192-223) ,eg:-192.168.10.0")
                    ip=list(map(int,input().split(".")))
                elif i<=16:
                    print("Enter the IP ID in the range(128-191) ,eg:-128.141.10.0")
                    ip=list(map(int,input().split(".")))
                elif i<=24:
                    print("Enter the IP ID in the range(0-126) ,eg:-10.0.1.0")
                    ip=list(map(int,input().split(".")))
        else:
            if i<=8:
                ip=[192,168,10,0]
            elif i<=16:
                ip=[128,10,0,0]
            elif i<=24:
                ip=[10,0,0,0]

    if a==1:
        nearest_value=2**d
        #print("Nearest Value is ",nearest_value)
        slash_value=32-d
        c=d%8
        i=0
        l=0
        while(i<8):
            if i>=c:
                l+=2**i
            i+=1
        n_w=2**(8-c)
        print("Number of N/W  are:",2**(8-c))
        print("Number of Host are:",2**d)
        print("Prefix length is:",(32-d))
        #ip_r=input("Do you want to print all the IP ranges:(Y or N)")
        #print(l)
        if d<=8:
            #print("It is class C")
            #print("Identify n/w is 255.255.255."+str(l)+" /",slash_value)
            print("Identified new subnet mask is 255.255.255."+str(l))
            print("Binary form of subnet mask is 11111111 11111111 11111111 "+str(bin(l)).replace("0b",""))
            #ip=[192,168,10,0]
            ip_r=input("Do you want to print all the IP ranges:(Y or N)")
            if ip_r=='Y' or ip_r=='y':
                n_w_p=n_w
            else:
                n_w_p=int(input("Enter how many IP ranges do you print to show:\n"))    
            j=0
            while(ip[-1]<=255 and j<n_w_p):
                print(".".join(str(x) for x in ip),end=" - ")
                ip[-1]+=2**d-1
                print(".".join(str(x) for x in ip))
                ip[-1]+=1
                j+=1
        elif d<=16:
            #print("It is class B")
            #print("Identify n/w is 255.255."+str(l)+".0"+" /",slash_value)
            print("Identified new subnet mask is 255.255."+str(l)+".0")
            print("Binary form of subnet mask is 11111111 11111111 "+str(bin(l)).replace("0b","")+" 00000000")
            #ip=[128,10,0,0]
            ip_r=input("Do you want to print all the IP ranges:(Y or N)")
            if ip_r=='Y' or ip_r=='y':
                n_w_p=n_w
            else:
                n_w_p=int(input("Enter how many IP ranges do you print to show:\n"))
            t=0
            j=0
            while((ip[-2]*254+ip[-1])<=255*255 and j<n_w_p):
                if t==0 and ip[-2]<=255:
                    print(".".join(str(x) for x in ip),end=" - ")
                ip[-1]+=255
                t+=256
                if t>=2**d:
                    print(".".join(str(x) for x in ip))
                    t=0
                    j+=1
                #print(".".join(str(x) for x in ip))
                ip[-2]+=1
                ip[-1]=0
        elif d<=24:
            #print("It is class A")
            #print("Identify n/w is 255."+str(l)+".0.0"+" /",slash_value)
            print("Identified new subnet mask is 255."+str(l)+".0.0")
            print("Binary form of subnet mask is 11111111 "+str(bin(l)).replace("0b","")+" 00000000 00000000")
            #ip=[10,0,0,0]
            ip_r=input("Do you want to print all the IP ranges:(Y or N)")
            if ip_r=='Y' or ip_r=='y':
                n_w_p=n_w
            else:
                n_w_p=int(input("Enter how many IP ranges do you print to show:\n"))
            t=0
            j=0
            while((ip[-3]*254*254+ip[-2]*254+ip[-1])<=255*255*255 and j<n_w_p):
                if t==0 and ip[-3]<=255:
                    print(".".join(str(x) for x in ip),end=" - ")
                ip[-1]+=255
                ip[-2]+=255
                t+=255*255
                if t>=2**d and ip[-3]<=256:
                    ip[-3]-=1
                    print(".".join(str(x) for x in ip))
                    t=0
                    j+=1
                ip[-3]+=1
                ip[-1],ip[-2]=0,0
                
        
    elif a==2:
        s=sum(list1)
        for b in list1:
            i=1
            d=0
            while(i<b):
                if 2**i>=b+2:
                    break
                i=i+1
            d=i
            nearest_value=2**d
            #print("Nearest Value is ",nearest_value)
            #slash_value=32-d
            c=d%8
            i=0
            l=0
            while(i<8):
                if i>=c:
                    l+=2**i
                i+=1
            print("Number of N/W are:",2**(8-c))
            print("Number of host are:",2**d)
            print("Prefix length is : ",32-d)
            #print(l)
            if d<=8:
                #print("It is class C")
                #print("Identify n/w is 255.255.255."+str(l)+" /",slash_value)
                print("Identified new subnet mask is 255.255.255."+str(l))
                print("Binary form of subnet mask is 11111111 11111111 11111111 "+str(bin(l)).replace("0b",""))
                print(".".join(str(x) for x in ip),end=" - ")
                ip[-1]+=2**d-1
                print(".".join(str(x) for x in ip))
                ip[-1]+=1
            elif d<=16:
                #print("It is class B")
                print("Identified new subnet mask is 255.255."+str(l)+".0")
                print("Binary form of subnet mask is 11111111 11111111 "+str(bin(l)).replace("0b","")+" 00000000")
                #print(".".join(str(x) for x in ip),end=" - ")
                t=0
                while(1):
                    if t==0 and ip[-2]<=255:
                        print(".".join(str(x) for x in ip),end=" - ")
                    ip[-1]+=255
                    t+=256
                    if t>=2**d:
                        print(".".join(str(x) for x in ip))
                        ip[-2]+=1
                        ip[-1]=0
                        break
                    #print(".".join(str(x) for x in ip))
                    ip[-2]+=1
                    ip[-1]=0
            elif d<=24:
                #print("It is class A")
                print("Identified new subnet mask is 255."+str(l)+".0.0")
                print("Binary form of subnet mask is 11111111 "+str(bin(l)).replace("0b","")+" 00000000 00000000")
                #print(".".join(str(x) for x in ip),end=" - ")
                t=0
                while(1):
                    if t==0:
                        print(".".join(str(x) for x in ip),end=" - ")
                    ip[-1]+=255
                    ip[-2]+=255
                    t+=255*255
                    if t>=2**d:
                        ip[-3]-=1
                        print(".".join(str(x) for x in ip))
                        #print("done1")
                        ip[-3]+=1
                        ip[-1],ip[-2]=0,0
                        break
                    #print("done")
                    ip[-3]+=1
                    ip[-1],ip[-2]=0,0
            print()
            print()
    elif a==3 or a==4:
        print("Enter the network in the given example format. eg:-172.23.0.0/22 (or) 172.20.106.0 255.255.254.0")
        n=input()
        while 1:
            if "/" in n and n.count(".")==3:
                ip,e=n.split("/")
                ip=[int(x) for x in ip.split(".")]
                #print(n,e)
                b="".join("1" for x in range(int(e)))+"".join("0" for x in range(32-int(e)))
                b=[b[i:i+8] for i in range(0,32,8)]
                break
            elif " " in n and n.count(".")==6:
                ip,d=n.split(" ")
                #print(n,d)
                ip=[int(x) for x in ip.split(".")]
                b=list(d.split("."))
                b=[str(bin(int(x)).replace("0b","")) for x in b]
                e="".join(x for x in b)
                print(e)
                e=e.count("1")
                #print(e)
                break
            else:
                n=input("You entered is incorrect format. Once re-check and Enter the network in the given example format. eg:-172.23.0.0/22 (or) 172.20.106.0 255.255.254.0\n")
                continue
        d=32-int(e)
        if d<=8:
            s=b[-1].count("1")
        elif d<=16:
            s=b[-2].count("1")+b[-1].count("1")
        elif d<=24:
            s=b[-3].count("1")+b[-3].count("1")+b[-1].count("1")

        s_b_t=2**s
        if a==4:
            print("Number of host are:",2**d)
            print("No.of Valid Hosts per subnet are :",2**d-2)
            print("Number of subnets  are:",2**s)
        else:
            if d<=8:
                ip=ip[:3]
                ip.append(0)
                l1=[]
                while(ip[-1]<=255):
                    print("Network Address :"+".".join(str(x) for x in ip))
                    #l1.append([x for x in ip])
                    #print(l1)
                    ip[-1]+=1
                    print("Host Range :"+".".join(str(x) for x in ip),end="-")
                    ip[-1]+=2**d-2
                    print(".".join(str(x) for x in ip))
                    ip[-1]+=1
                    print("Broadcast Address :"+".".join(str(x) for x in ip))
                    ip[-1]+=1
                    print()
                    print()
            elif d<=16:
                t=0
                j=0
                ip=[ip[0],ip[1],0,0]
                while((ip[-2]*254+ip[-1])<=255*255):
                    if t==0 and ip[-2]<=255:
                        print("Network Address :"+".".join(str(x) for x in ip))
                        ip[-1]+=1
                        print("Host Range :"+".".join(str(x) for x in ip),end=" - ")
                    ip[-1]+=255
                    t+=256
                    if t>=2**d:
                        ip[-1]-=1
                        print(".".join(str(x) for x in ip))
                        ip[-1]+=1
                        print("Broadcast Address :"+".".join(str(x) for x in ip))
                        print()
                        t=0
                        j+=1
                    ip[-2]+=1
                    ip[-1]=0
            elif d<=24:
                t=0
                j=0
                ip=[ip[0],0,0,0]
                while((ip[-3]*254*254+ip[-2]*254+ip[-1])<=255*255*255):
                    if t==0 and ip[-3]<=255:
                        print("Network Address :"+".".join(str(x) for x in ip))
                        ip[-1]+=1
                        print("Host Range :"+".".join(str(x) for x in ip),end=" - ")
                    ip[-1]+=255
                    ip[-2]+=255
                    t+=255*255+1
                    if t>=2**d and ip[-3]<=256:
                        ip[-3]-=1
                        ip[-1]-=1
                        print(".".join(str(x) for x in ip))
                        ip[-1]+=1
                        print("Broadcast Address :"+".".join(str(x) for x in ip))
                        print()
                        t=0
                        j+=1
                    ip[-3]+=1
                    ip[-1],ip[-2]=0,0
                    #print(ip[-3])
                #print(ip)
    print()
    k=input("Do you want to check any other Network ....(Y or N)\n")
    if k=='n' or k=='N':
        break
    else:
        print()
        continue
                    
                

