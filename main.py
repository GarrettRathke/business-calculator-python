import sys
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QVBoxLayout, QLabel, QGridLayout, QLineEdit, QMessageBox
import babel.numbers


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

    button = QPushButton('Calculate')
    button.clicked.connect(calculate)
    button.setStyleSheet('background-color: #4CAF50; color: white; font-size: 20px; font-weight: bold; border-radius: '
                         '10px; margin-top:'
                         '20px; margin-bottom: 10px;')
    grid.addWidget(button, 6, 0, 1, 4)

    widget.show()
    sys.exit(app.exec_())


def calculate():
    print('calculating')
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
    gross_monthly_revenue = number_of_users * teams_tier_price
    total_monthly_expenses = initial_monthly_expenses + (gross_monthly_revenue * corporate_tax_rate) + (
            gross_monthly_revenue * primary_engineer_pay_rate) + (gross_monthly_revenue * primary_sales_pay_rate) + (
                                     gross_monthly_revenue * savings_rate)
    net_monthly_profit = gross_monthly_revenue - total_monthly_expenses

    # formatting
    formatted_gross_monthly_revenue = babel.numbers.format_currency(gross_monthly_revenue, "USD", locale='en_US')
    formatted_total_monthly_expenses = babel.numbers.format_currency(total_monthly_expenses, "USD", locale='en_US')
    formatted_net_monthly_profit = babel.numbers.format_currency(net_monthly_profit, "USD", locale='en_US')
    formatted_corporate_monthly_taxes = babel.numbers.format_currency(gross_monthly_revenue * corporate_tax_rate, "USD",
                                                                      locale='en_US')
    formatted_primary_engineer_monthly_pay = babel.numbers.format_currency(gross_monthly_revenue * primary_engineer_pay_rate,
                                                                     "USD", locale='en_US')
    formatted_primary_sales_monthly_pay = babel.numbers.format_currency(gross_monthly_revenue * primary_sales_pay_rate, "USD",
                                                                  locale='en_US')
    formatted_monthly_savings = babel.numbers.format_currency(
        (gross_monthly_revenue * savings_rate) + net_monthly_profit, "USD", locale='en_US')
    formatted_new_hire_engineer_monthly_salary = babel.numbers.format_currency(new_hire_engineer_monthly_salary, "USD", locale='en_US')
    formatted_new_hire_engineer_yearly_cost = babel.numbers.format_currency(new_hire_engineer_yearly_cost, "USD", locale='en_US')
    formatted_new_hire_engineer_monthly_cost = babel.numbers.format_currency(new_hire_engineer_monthly_cost, "USD", locale='en_US')

    display_calculation_results(formatted_gross_monthly_revenue, formatted_total_monthly_expenses, formatted_net_monthly_profit, formatted_corporate_monthly_taxes, formatted_monthly_savings, formatted_primary_engineer_monthly_pay, formatted_primary_sales_monthly_pay, formatted_new_hire_engineer_monthly_salary,
                                formatted_new_hire_engineer_monthly_cost, formatted_new_hire_engineer_yearly_cost)


def display_calculation_results(gross_monthly_revenue, total_monthly_expenses, net_monthly_profit, corporate_monthly_taxes, monthly_savings, primary_engineer_monthly_pay, primary_sales_monthly_pay, new_hire_engineer_monthly_salary,
                                new_hire_engineer_monthly_cost, new_hire_engineer_yearly_cost):
    msg = QMessageBox()
    msg.setMinimumSize(400, 200)
    msg.setIcon(QMessageBox.Information)
    msg_content = "Gross Monthly Revenue: %s \nTotal Monthly Expenses: %s \nNet Monthly Profit: %s \nMonthly " \
                  "Corporate Taxes: %s \nTotal Monthly Savings (savings + profit): %s \nPrimary Engineer Monthly Pay: " \
                  "%s \nPrimary Sales Monthly Pay: %s \nNew Hire Engineer Monthly Pay: %s \nNew Hire Engineer Total " \
                  "Monthly Corporate Cost: %s \nNew Hire Engineer Total Yearly Cost: %s \n" % (gross_monthly_revenue,
                                                                                               total_monthly_expenses,
                                                                    net_monthly_profit, corporate_monthly_taxes,
                                                                    monthly_savings, primary_engineer_monthly_pay, primary_sales_monthly_pay, new_hire_engineer_monthly_salary, new_hire_engineer_monthly_cost, new_hire_engineer_yearly_cost)
    msg.setText(msg_content)
    msg.setWindowTitle("Calculation Results")
    msg.setStandardButtons(QMessageBox.Ok)
    msg.exec()


if __name__ == '__main__':
    window()
