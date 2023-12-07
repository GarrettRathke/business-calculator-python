from finances import FinanceVariables, FinanceTotals
import csv


def calculate_finance_variables(finance_variables: FinanceVariables):
    gross_monthly_revenue = finance_variables.number_of_users * finance_variables.teams_tier_price
    total_monthly_expenses = finance_variables.initial_monthly_expenses + (gross_monthly_revenue * finance_variables.corporate_tax_rate) + (
            gross_monthly_revenue * finance_variables.primary_engineer_pay_rate) + (gross_monthly_revenue * finance_variables.primary_sales_pay_rate) + (
                                     gross_monthly_revenue * finance_variables.savings_rate)
    net_monthly_profit = gross_monthly_revenue - total_monthly_expenses
    return FinanceTotals(gross_monthly_revenue, total_monthly_expenses, net_monthly_profit)


def calculate_finances_bulk():
    print('calculating finances in bulk...')
    """
    users per month in multiples of 100
    teams_tier_price in multiples of $1
    monthly expenses in multiples of $100
    primary engineer pay rate in multiples of 1%
    primary sales pay rate in multiples of 1%
    savings rate in multiples of 10%

    :return: Writes a combinatorics of business finances to a csv file
    """
    profit_margin = 0.5
    corporate_tax_rate = 0.3

    with open('business-finances-combinatorics.csv', 'w', newline='') as file:
        writer = csv.writer(file)
        field = ["gross_monthly_revenue", "monthly_expenses", "net_monthly_profit", "number_of_users", "teams_tier_price", "primary_engineer_pay_percent", "primary_engineer_pay",
                 "primary_sales_pay_percent", "primary_sales_pay", "savings_percent", "savings"]

        writer.writerow(field)
        for number_of_users in range(100, 2000, 100):
            for teams_tier_price in range(10, 20, 1):
                for monthly_expenses in range(100, 1000, 100):
                    for primary_engineer_pay_rate in range(1, 50, 1):
                        for primary_sales_pay_rate in range(1, 10, 1):
                            for savings_rate in range(0, 80, 5):
                                calculation_totals = calculate_finance_variables(
                                    FinanceVariables(number_of_users, float(teams_tier_price), float(monthly_expenses),
                                                     (float(primary_engineer_pay_rate) / 100) * profit_margin,
                                                     (float(primary_sales_pay_rate) / 100) * profit_margin, (float(savings_rate) / 100) * profit_margin, corporate_tax_rate))
                                writer.writerow([calculation_totals.gross_monthly_revenue, calculation_totals.total_monthly_expenses, calculation_totals.net_monthly_profit, number_of_users, teams_tier_price,
                                                 primary_engineer_pay_rate, calculation_totals.gross_monthly_revenue * primary_engineer_pay_rate,
                                                 primary_sales_pay_rate, calculation_totals.gross_monthly_revenue * primary_sales_pay_rate, savings_rate, (calculation_totals.gross_monthly_revenue * savings_rate) + calculation_totals.net_monthly_profit])
    print('done calculating finances in bulk!')
