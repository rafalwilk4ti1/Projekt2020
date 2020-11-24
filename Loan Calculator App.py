from matplotlib import pyplot



def get_loan_info():
    loan = {

    }
    loan["Principal"] = float(input("Enter the loan amount: "))
    loan["Rate"] = float(input("Enter the interest rate: "))
    loan["Rate"] = round((loan["Rate"]/100),4)
    loan["Monthly payment"] = float(input("Enter the desired monthly payment amount: "))
    loan["Money paid"] = 0
    return loan
#Checked - everything is correct ^

def show_loan_info(current_loan, number_of_months):
    print("----Loan information after "+str(number_of_months)+" months----")
    for x,y in current_loan.items():
        print(x + ": "+str(y))

def collect_interest(current_loan):
    current_loan["Principal"] = current_loan["Principal"]+((current_loan["Principal"]*current_loan["Rate"])/12)

def make_monthly_payment(current_loan):
    current_loan["Principal"] -= current_loan["Monthly payment"]
    if current_loan["Principal"] > 0:
        current_loan["Money paid"] += current_loan["Monthly payment"]

    if current_loan["Principal"] < 0:
        current_loan["Money paid"] += (current_loan["Monthly payment"] - current_loan["Principal"])
        current_loan["Principal"] = 0

def summarize_loan(current_loan, number_of_months, principal_of_a_loan):
    print("\nCongratulations! You paid off your loan in "+str(number_of_months)+" months!")
    print("Your initial loan was $"+str(principal_of_a_loan)+ " at a rate of "+str(current_loan["Rate"]*100)+"%.")
    print("Your monthly payment was $"+str(current_loan["Monthly payment"]) +".")
    total_rates = (current_loan["Monthly payment"] * number_of_months)
    print("You spent $"+ str(round(current_loan["Money paid"],2)) +" total.")
    print("You spent $"+ str(round(total_rates,2)) +" on interest.")

def create_graph(data_set,current_loan):
    x_values = []
    y_values = []

    for point in data_set:
        x_values.append(point[0])
        y_values.append(point[1])


    pyplot.plot(x_values,y_values)
    pyplot.title(str(100*current_loan["Rate"]) + "% Interest With $" + str(current_loan["Monthly payment"])+" Monthly Payment")
    pyplot.xlabel("Month Number")
    pyplot.ylabel("Principal of Loan")
    pyplot.show()




print("Welcome to the Loan Calculator App")
number_of_months = 0

get_loan = get_loan_info()
starting_principal = get_loan["Principal"]
data_to_plot = []

show_loan_info(get_loan, number_of_months)

input("Press 'enter' to begin paying off your loan.")

while get_loan["Principal"] > 0:
    if get_loan["Principal"] > starting_principal:
        print("You will never pay off the loan")
        break
    number_of_months +=1
    collect_interest(get_loan)
    make_monthly_payment(get_loan)
    data_to_plot.append((number_of_months,get_loan["Principal"]))
    show_loan_info(get_loan, number_of_months)

if get_loan["Principal"] == 0:
    summarize_loan(get_loan,number_of_months,starting_principal)
    create_graph(data_to_plot,get_loan)
else:
    print("You will never be paid off")
    print("You cannot get ahead of the interest! :-( ")




