from return_on_investment import Roi


def main():
    main = Roi(float(input('What is the property value? : ')),
               float(input('What is your expected downpayment? : ')))
    main.monthly_income(float(input(
        '\nPlease provide total of all expected income.\nIe. Rental, Parking, Storage, etc : ')))

    main.mortgage_payment()
    main.monthly_expenses(float(input(
        '\nPlease provide total of all expected expenses aside from mortgage.\nIe. HOA, Snow, Insurance, Tax, etc. : ')))
    main.total_cash_flow()
    main.cash_on_cash_roi(float(input(
        '\nPlease provide total of all upfront investment costs aside from downpayment.\nIe. Rehab, Closing Costs, etc. : ')))


main()
