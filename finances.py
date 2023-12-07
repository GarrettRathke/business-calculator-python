class FinanceVariables:
    def __init__(self, number_of_users: int, teams_tier_price: float, initial_monthly_expenses: float,
                 primary_engineer_pay_rate: float,
                 primary_sales_pay_rate: float, savings_rate: float, corporate_tax_rate: float = 0.3):
        self.number_of_users = number_of_users
        self.teams_tier_price = teams_tier_price
        self.initial_monthly_expenses = initial_monthly_expenses
        self.primary_engineer_pay_rate = primary_engineer_pay_rate
        self.primary_sales_pay_rate = primary_sales_pay_rate
        self.savings_rate = savings_rate
        self.corporate_tax_rate = corporate_tax_rate

    def get_number_of_users(self):
        return self.number_of_users

    def get_teams_tier_price(self):
        return self.teams_tier_price

    def get_initial_monthly_expenses(self):
        return self.initial_monthly_expenses

    def get_primary_engineer_pay_rate(self):
        return self.primary_engineer_pay_rate

    def get_primary_sales_pay_rate(self):
        return self.primary_sales_pay_rate

    def get_savings_rate(self):
        return self.savings_rate

    def get_corporate_tax_rate(self):
        return self.corporate_tax_rate

    def __str__(self):
        return self.number_of_users + " " + self.teams_tier_price + " " + self.initial_monthly_expenses + " " + self.primary_engineer_pay_rate + " " + self.savings_rate + " " + self.primary_sales_pay_rate + " " + self.corporate_tax_rate


class FinanceTotals:
    def __init__(self, gross_monthly_revenue: float, total_monthly_expenses: float, net_monthly_profit: float):
        self.gross_monthly_revenue = gross_monthly_revenue
        self.total_monthly_expenses = total_monthly_expenses
        self.net_monthly_profit = net_monthly_profit

    def get_gross_monthly_revenue(self):
        return self.gross_monthly_revenue

    def get_total_monthly_expenses(self):
        return self.total_monthly_expenses

    def get_net_monthly_profit(self):
        return self.net_monthly_profit

    def __str__(self):
        return self.gross_monthly_revenue + " " + self.total_monthly_expenses + " " + self.net_monthly_profit
