import sys
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QVBoxLayout, QLabel, QFileDialog, QGridLayout
from PyQt5.QtGui import QIcon, QPixmap
from PyQt5.QtCore import pyqtSlot
import babel.numbers


def on_click():
    print('I\'ve been clicked')


def window():
    app = QApplication(sys.argv)
    widget = QWidget()
    layout = QVBoxLayout()
    widget.setLayout(layout)
    widget.setMinimumSize(600, 400)
    widget.setWindowTitle('Hello World')
    grid = QGridLayout()
    layout.addLayout(grid)

    # row 0
    profit_margin_label = QLabel('Profit Margin:')
    grid.addWidget(profit_margin_label, 0, 0)
    corporate_tax_rate_label = QLabel('Corporate Tax Rate:')
    grid.addWidget(corporate_tax_rate_label, 0, 1)

    # row 1
    engineer_payment_rate_label = QLabel('Engineer Payment Rate:')
    grid.addWidget(engineer_payment_rate_label, 1, 0)
    sales_payment_rate_label = QLabel('Sales Payment Rate:')
    grid.addWidget(sales_payment_rate_label, 1, 1)

    # row 2
    savings_rate_label = QLabel('Savings Rate:')
    grid.addWidget(savings_rate_label, 2, 0)
    engineer_yearly_salary_label = QLabel('New Hire Engineer Yearly Salary:')
    grid.addWidget(engineer_yearly_salary_label, 2, 1)

    # row 3
    initial_monthly_expenses_label = QLabel('Initial Monthly Expenses:')
    grid.addWidget(initial_monthly_expenses_label, 3, 0)
    tier_price_label = QLabel('Tier Price:')
    grid.addWidget(tier_price_label, 3, 1)

    # button = QPushButton('Click Me')
    # button.clicked.connect(on_click)
    # grid.addWidget(button, 1, 1)

    widget.show()
    sys.exit(app.exec_())


if __name__ == '__main__':
    window()
    # assumptions
    profit_margin = 0.5
    corporate_tax_rate = 0.3
    engineer_payment_rate = profit_margin * 0.5
    sales_payment_rate = profit_margin * 0.05
    savings_rate = profit_margin * 0.45
    engineer_yearly_salary = 65000.00
    engineer_monthly_salary = engineer_yearly_salary / 12
    engineer_yearly_cost = engineer_yearly_salary * 1.25
    engineer_monthly_cost = engineer_yearly_cost / 12
    initial_monthly_expenses = 100.00
    teams_tier_price = 10.00

    # inputs
    number_of_users = 100
    gross_monthly_revenue = number_of_users * teams_tier_price
    total_monthly_expenses = initial_monthly_expenses + (gross_monthly_revenue * corporate_tax_rate) + (
                gross_monthly_revenue * engineer_payment_rate) + (gross_monthly_revenue * sales_payment_rate) + (
                                         gross_monthly_revenue * savings_rate)
    net_monthly_profit = gross_monthly_revenue - total_monthly_expenses

    print('Gross monthly revenue: ' + babel.numbers.format_currency(gross_monthly_revenue, "USD", locale='en_US'))
    print('Total monthly expenses: ' + babel.numbers.format_currency(total_monthly_expenses, "USD", locale='en_US'))
    print('Net monthly profit: ' + babel.numbers.format_currency(net_monthly_profit, "USD", locale='en_US'))
    print('Breakdown of expenses...')
    print('Initial monthly expenses: ' + babel.numbers.format_currency(initial_monthly_expenses, "USD", locale='en_US'))
    print('Corporate monthly taxes: ' + babel.numbers.format_currency(gross_monthly_revenue * corporate_tax_rate, "USD", locale='en_US'))
    print('Engineer monthly payment: ' + babel.numbers.format_currency(gross_monthly_revenue * engineer_payment_rate, "USD", locale='en_US'))
    print('Sales monthly payment: ' + babel.numbers.format_currency(gross_monthly_revenue * sales_payment_rate, "USD", locale='en_US'))
    print('Monthly savings (+ profit): ' + babel.numbers.format_currency((gross_monthly_revenue * savings_rate) + net_monthly_profit, "USD", locale='en_US'))
    '''
    Is
    profitable
    calculation

    Extract
    taxes = total(monthly)
    revenue * 0.3

    Check if remainder is greater
    than $100
    for cloud costs

    Individual
    tier is free or very
    cheap( < $5 / user / month)

    B2B
    Pro
    tier is paid; $25 / user
    month
    '''
