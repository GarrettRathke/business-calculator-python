import sys
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QVBoxLayout, QLabel, QGridLayout, QLineEdit, QMessageBox
import babel.numbers
from calculate import calculate_finance_variables, calculate_finances_bulk
from finances import FinanceVariables

# TODO: field validation
# TODO: add unit tests

app = QApplication(sys.argv)
widgets = {
    1: {
        'profit_margin': {
            'label': QLabel('Profit Margin: %'),
            'input_box': QLineEdit('50')
        },
        'corporate_tax_rate': {
            'label': QLabel('Corporate Tax Rate: %'),
            'input_box': QLineEdit('30')
        },
    },
    2: {
        'primary_engineer_pay_rate': {
            'label': QLabel('Primary Engineer Pay Rate (percentage of profit): %'),
            'input_box': QLineEdit('50')
        },
        'primary_sales_pay_rate': {
            'label': QLabel('Primary Sales Pay Rate (percentage of profit): %'),
            'input_box': QLineEdit('5')
        },
    },
    3: {
        'savings_rate': {
            'label': QLabel('Company Savings Rate (percentage of profit): %'),
            'input_box': QLineEdit('45')
        },
        'new_hire_engineer_yearly_salary': {
            'label': QLabel('New Hire Engineer Yearly Salary (in dollars): $'),
            'input_box': QLineEdit('65000')
        },
    },
    4: {
        'initial_monthly_expenses': {
            'label': QLabel('Initial Monthly Expenses (in dollars): $'),
            'input_box': QLineEdit('100')
        },
        'tier_price': {
            'label': QLabel('Tier Price (in dollars): $'),
            'input_box': QLineEdit('10')
        },
    },
    5: {
        'number_of_users': {
            'label': QLabel('Number of Users:'),
            'input_box': QLineEdit('100')
        }
    }
}


def window():
    widget = QWidget()
    layout = QVBoxLayout()
    widget.setLayout(layout)
    widget.setMinimumSize(600, 300)
    widget.setWindowTitle('Business Calculator')
    grid = QGridLayout()
    layout.addLayout(grid)

    app_label = QLabel('Unless otherwise stated, all inputs are whole number percentages of total revenue. For '
                       'example, the number '
                       '5 is interpreted as %5 (0.05). But if you input 0.05, that\'s interpreted as %0.005. Be '
                       'careful! Only input whole numbers, unless you have a good reason for doing otherwise.')
    app_label.setWordWrap(True)
    grid.addWidget(app_label, 0, 0, 1, 4)

    for row in widgets:
        column = 0
        for group in widgets[row]:
            for key in widgets[row][group]:
                grid.addWidget(widgets[row][group][key], row, column)
                column += 1

    calculate_finance_variables_button = QPushButton('Calculate Finance Variables')
    calculate_finance_variables_button.clicked.connect(calculate)
    calculate_finance_variables_button.setStyleSheet('background-color: #4CAF50; color: white; font-size: 20px; '
                                                     'font-weight: bold; border-radius:'
                                                     '10px; margin-top:'
                                                     '20px; margin-bottom: 10px;')
    grid.addWidget(calculate_finance_variables_button, 6, 0, 1, 4)

    calculate_bulk_finances_button = QPushButton('Calculate Bulk Finances')
    calculate_bulk_finances_button.clicked.connect(calculate_finances_bulk)
    calculate_bulk_finances_button.setStyleSheet('background-color: #4CAF50; color: white; font-size: 20px; '
                                                 'font-weight: bold; border-radius:'
                                                 '10px; margin-top:'
                                                 '20px; margin-bottom: 10px;')
    grid.addWidget(calculate_bulk_finances_button, 7, 0, 1, 4)

    widget.show()
    sys.exit(app.exec_())


def calculate():
    profit_margin = float(widgets[1]['profit_margin']['input_box'].text()) / 100
    corporate_tax_rate = float(widgets[1]['corporate_tax_rate']['input_box'].text()) / 100
    primary_engineer_pay_rate = (float(
        widgets[2]['primary_engineer_pay_rate']['input_box'].text()) / 100) * profit_margin
    primary_sales_pay_rate = (float(widgets[2]['primary_sales_pay_rate']['input_box'].text()) / 100) * profit_margin
    savings_rate = (float(widgets[3]['savings_rate']['input_box'].text()) / 100) * profit_margin
    new_hire_engineer_yearly_salary = float(widgets[3]['new_hire_engineer_yearly_salary']['input_box'].text())
    new_hire_engineer_monthly_salary = new_hire_engineer_yearly_salary / 12
    new_hire_engineer_yearly_cost = new_hire_engineer_yearly_salary * 1.25
    new_hire_engineer_monthly_cost = new_hire_engineer_yearly_cost / 12
    initial_monthly_expenses = float(widgets[4]['initial_monthly_expenses']['input_box'].text())
    teams_tier_price = float(widgets[4]['tier_price']['input_box'].text())

    # calculation
    number_of_users = 100
    calculation_totals = calculate_finance_variables(
        FinanceVariables(number_of_users, teams_tier_price, initial_monthly_expenses, primary_engineer_pay_rate,
                         primary_sales_pay_rate, savings_rate, corporate_tax_rate))

    # formatting
    formatted_gross_monthly_revenue = money_string_format(calculation_totals.gross_monthly_revenue)
    formatted_total_monthly_expenses = money_string_format(calculation_totals.total_monthly_expenses)
    formatted_net_monthly_profit = money_string_format(calculation_totals.net_monthly_profit)
    formatted_corporate_monthly_taxes = money_string_format(
        calculation_totals.gross_monthly_revenue * corporate_tax_rate)
    formatted_primary_engineer_monthly_pay = money_string_format(
        calculation_totals.gross_monthly_revenue * primary_engineer_pay_rate)
    formatted_primary_sales_monthly_pay = money_string_format(
        calculation_totals.gross_monthly_revenue * primary_sales_pay_rate)
    formatted_monthly_savings = money_string_format(
        (calculation_totals.gross_monthly_revenue * savings_rate) + calculation_totals.net_monthly_profit)
    formatted_new_hire_engineer_monthly_salary = money_string_format(new_hire_engineer_monthly_salary)
    formatted_new_hire_engineer_yearly_cost = money_string_format(new_hire_engineer_yearly_cost)
    formatted_new_hire_engineer_monthly_cost = money_string_format(new_hire_engineer_monthly_cost)

    display_calculation_results(formatted_gross_monthly_revenue, formatted_total_monthly_expenses,
                                formatted_net_monthly_profit, formatted_corporate_monthly_taxes,
                                formatted_monthly_savings, formatted_primary_engineer_monthly_pay,
                                formatted_primary_sales_monthly_pay, formatted_new_hire_engineer_monthly_salary,
                                formatted_new_hire_engineer_monthly_cost, formatted_new_hire_engineer_yearly_cost)


def money_string_format(dollar_amount: float):
    return babel.numbers.format_currency(dollar_amount, "USD", locale='en_US')


def display_calculation_results(gross_monthly_revenue, total_monthly_expenses, net_monthly_profit,
                                corporate_monthly_taxes, monthly_savings, primary_engineer_monthly_pay,
                                primary_sales_monthly_pay, new_hire_engineer_monthly_salary,
                                new_hire_engineer_monthly_cost, new_hire_engineer_yearly_cost):
    msg = QMessageBox()
    msg.setMinimumSize(400, 200)
    msg.setIcon(QMessageBox.Information)
    msg_content = "Gross Monthly Revenue: %s \nTotal Monthly Expenses: %s \nNet Monthly Profit: %s \nMonthly " \
                  "Corporate Taxes: %s \nTotal Monthly Savings (savings + profit): %s \nPrimary Engineer Monthly Pay: " \
                  "%s \nPrimary Sales Monthly Pay: %s \nNew Hire Engineer Monthly Pay: %s \nNew Hire Engineer Total " \
                  "Monthly Corporate Cost: %s \nNew Hire Engineer Total Yearly Cost: %s \n" % (gross_monthly_revenue,
                                                                                               total_monthly_expenses,
                                                                                               net_monthly_profit,
                                                                                               corporate_monthly_taxes,
                                                                                               monthly_savings,
                                                                                               primary_engineer_monthly_pay,
                                                                                               primary_sales_monthly_pay,
                                                                                               new_hire_engineer_monthly_salary,
                                                                                               new_hire_engineer_monthly_cost,
                                                                                               new_hire_engineer_yearly_cost)
    msg.setText(msg_content)
    msg.setWindowTitle("Calculation Results")
    msg.setStandardButtons(QMessageBox.Ok)
    msg.exec()


if __name__ == '__main__':
    window()
