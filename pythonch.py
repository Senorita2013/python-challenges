#operator presedence,expression

a=12
b=3
c=4
d=9
answer= b**c + d/ b*c + a
print (answer)

#n1/n2

n1=int(input("Enter numerator:"))
n2=int(input("Enter denominator:"))

if n1%n2==0:
    print("n1 is divisible by n2")
else:
    print("n1 is not divisible by n2")

#activity 3 corrected mean
mean1=38
wrong_number=36
correct_number=56
total_number=40

sum=mean1*total_number
print("The wrong sum",sum)

corrected_sum=sum-wrong_number+correct_number
mean2=corrected_sum/total_number
print("The corrected mean is",mean2)

#find average speed
s1=int(input("Enter first cyclist speed:"))
s2=int(input("Enter second cyclist speed:"))
s3=int(input("Enter third cyclist speed:"))

average= (s1+s2+s3)/3
print("The average speed is",average)

if s1<average:
    print("Cyclist1 is slower than average",average-s1)

if s2<average:
    print("Cyclist2 is slower than average",average-s2)

if s3<average:
    print("Cyclist3 is slower than average",average-s3)