def gcd(a,b):

    if b==0:
        return a
    else:
        return gcd(b,a%b)

def extended_gcd(a,b):
    if b==0:
        st=[[1,0],[0,1]]
        for i in range(len(q)):
            st.append([st[i][0]-st[i+1][0]*q[i], st[i][1]-st[i+1][1]*q[i]] )
        return st[-2][0],st[-2][1]
    else:
        q.append(a//b)
        return extended_gcd(b,a%b)

g=[[45,75],[666,1414],[102,222],[2**101+16,2**202+8]]
for i in g:
    print("gcd(%d,%d)= %d "%(i[0],i[1],gcd(i[0],i[1])))


q=[]
a_e=[[45,75],[1414,666],[102,222],[2**101+16,2**202+8]]
for i in a_e:
    s,t=extended_gcd(i[0],i[1])
    print("extended_gcd(%d,%d)= %d s= %d t= %d"%(i[0],i[1],s*i[0]+i[1]*t,s,t))
    q=[]

print(gcd(1444,666),extended_gcd(1444, 666))