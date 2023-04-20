def compute_tax_rate(status, taxincome):
    """
    Calculate the tax rate based on the filing status and taxable income
    """
    if taxincome < 0:
        return 0

    status = status.upper()

    if status == "S":
        if taxincome < 15000:
            rate = 14
        elif 15000 <= taxincome <= 30000:
            rate = 20
        else:
            rate = 31
    elif status == "M":
        if taxincome < 20000:
            rate = 15
        elif 20000 <= taxincome <= 65000:
            rate = 20
        else:
            rate = 27
    elif status == "H":
        if taxincome < 30000:
            rate = 13
        elif 30000 <= taxincome <= 85000:
            rate = 21
        else:
            rate = 30
    else:
        print("Invalid Status")
        rate = None

    return rate


def compute_tax_income(gross, exemptions):
    taxincome = gross - 1500 * exemptions - 4000
    return taxincome


def status_description(status):
    status = status.upper()

    if status == "S":
        text = "Single"
    elif status == "M":
        text = "Married filing Jointly"
    elif status == "H":
        text = "Head of household"
    else:
        text = None

    return text


file_name = "p5set1.txt"
with open(file_name, "r") as fp:
    data = fp.readlines()

    data = [d.strip() for d in data]
print(data)

n = int(data[0])

highest_tax = 0
highest_tid = None
total_tax = 0

for i in range(1, n * 4, 4):

    tid = data[i]
    status = data[i + 1]
    gross = float(data[i + 2])
    exemptions = int(data[i + 3])

    tax_income = compute_tax_income(gross, exemptions)
    tax_rate = compute_tax_rate(status, tax_income)
    if tax_rate > 0:
        tax = tax_income * tax_rate / 100
    else:
        tax = 0

    status = status_description(status)
    print(f"Taxpayer ID: {tid}")
    print(f"Filing Status: {status}")
    print(f"Taxable Income: ${tax_income:.2f}")
    print(f"Tax Rate: {tax_rate}%")
    print(f"Tax Owed: ${tax:.2f}")
    print()

    total_tax = total_tax + tax

    if tax > highest_tax:
        highest_tax = tax
        highest_tid = tid

    if n > 0:
        avgtax = total_tax / n

    else:
        avgtax = 0

print("Final Summary\n")
print(f"Number of Taxpayers: {n}")
print(f"Highest Tax Amount: ${highest_tax:.2f}")
print(f"Taxpayer ID of Highest Tax Amount: {highest_tid}")
print(f"Total Taxes Paid: ${total_tax:.2f}")
print(f"Average Tax Paid per Taxpayer: ${avgtax:.2f}")
