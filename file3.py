ls=["hello","world","python","awesome"]
ln=[]
lp=[]
# for x in ls:
#     s=x.capitalize()
    
#     lp.append(s)
    
# print(lp)
    
for x in ls:
    # this line will make first and last letter of the word to be capitalized
    w=x[0:1].capitalize()+x[1:-1].lower()+x[-1:].capitalize()
    ln.append(w)
    # this line will make 2nd first and 2nd last letter of the word to be capitalized 
    s=x[0:1].lower()+x[1:2].capitalize()+x[2:-2].lower()+x[-2:-1].capitalize()+x[-1:].lower()
    lp.append(s)
print(ln)
print(lp)


# # home work 
# ls=["hello","world","python","awesome"]
# ln=[]
# lp=[]

# for x in ls:
#     ln.insert(0,x)
# print(ln)
# for x in ln:
#     a=x[0:1].capitalize()+x[1:-1].lower()+x[-1].capitalize()
#     lp.append(a)
# print(lp)

    

