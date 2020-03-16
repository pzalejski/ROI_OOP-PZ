

class Roi():
    """ simple class used to calculate the ROI on rental properties """

    def __init__(self, property_value, downpayment):
        self.income = 0
        self.expenses = 0.0
        self.mortgage = 0.0
        self.property_value = property_value
        self.downpayment = downpayment
        self.cashflow = 0

    def monthly_income(self, sources_of_inc):
        """
         method for total monthly income
         sources of income could be: rent, parking, laundry, storage, etc....
         provide total fo all sources
        """
        self.income = sources_of_inc
        return self.income

    def monthly_expenses(self, sources_of_exp):
        """
        method used to calculate
        mortgage calculated in its own methd and used when calculating total for monthly expenses
        total monthly expenses
        expense examples : tax, insurance, utilities, HOA, lawn/snow, etc
        """
        self.expenses = sources_of_exp + self.mortgage
        print(f'\nTotal monthly expenses are: {self.expenses} ')
        return self.expenses

    def mortgage_payment(self):
        """
        used to calculate total monthly mortgage pay
        """
        loan_amount = self.property_value - self.downpayment
        years = float(
            input('\nWhat will the mortgage length be in years?: '))*12
        rate = float(input('What is the yearly interest rate? : ')) / 100 / 12
        self.mortgage = round(loan_amount *
                              (rate * ((1 + rate) ** years) / (((1 + rate) ** years) - 1)), 2)
        print(f"The mortgage payment will be : {self.mortgage}")
        return self.mortgage

    def total_cash_flow(self):
        """
        used to calculate your income minus your expenses
        """
        self.cashflow = round(((self.income - self.expenses)*12), 2)
        # self.cash_flow = self.income - self.expenses
        print(f"The anual cash flow is {self.cashflow}")
        return self.cashflow

    def cash_on_cash_roi(self, initial_investment):
        total_investment = self.downpayment + initial_investment
        # print(self.downpayment)
        # print(self.cashflow)
        # print(total_investment)
        cash_roi = round(float(self.cashflow / total_investment)*100, 2)
        print(f'\nYour Cash-on-Cash-ROI is: {cash_roi}')
