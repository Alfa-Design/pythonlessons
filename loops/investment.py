# Enter Investment and expected Intrest
# increase = investment + (investment * intrest rate)
# Print the earnings after 10 years

invst = input("Enter what you wish to invest: ")
intrst = input("Enter your interest rate: ")

invst = float(invst)
intrst = float(intrst) * .01
increase = 0

for i in range(10):
    increase = invst * (invst * intrst)

print("Your eaxpected Money amount at the end of ten years is : {:.2f}" .format(
    increase))
