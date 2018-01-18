name = input("Enter name: ")
hours = int(input("Enter number of hours worked weekly: "))
payrate = float(input("Enter hourly pay rate: "))
cpf = int(input("Enter CPF contribution rate (%): "))

grosspay = hours * payrate
cpfdeduction = grosspay / 100 * cpf
netpay = grosspay - cpfdeduction

print("Payroll statement for", name)
print("Number of hours worked in week:", hours)
print("Hourly pay rate: ${0:.2f}".format(payrate))
print("Gross pay = ${0:.2f}".format(grosspay))
print("CPF contribution at {0}% = ${1:.2f}".format(cpf, cpfdeduction))
print("Net pay = ${0:.2f}".format(netpay))