print()
print("{:^100}".format("WELCOME TO EX+RA FAST CALCULATOR"))
print()

import time
time_1 = int(time.strftime('%H'))
if 5 <= time_1 <= 10:
    print('GOOD MORNING!')
elif 11 <= time_1 <= 14:
    print('GOOD AFTER NOON!')
elif 15 <= time_1 <= 18:
    print('GOOD EVENING!')
elif 19 <= time_1 <= 23:
    print('GOOD NIGHT!')
else:
    print("How is your MIDNIGHT!")
print("Dear user.")

name = input("What is your name?   ")
print()
print(
    "So Mr.{}, Let me introduce you with us.\n\t"
    "This is an income tax calculator, as per the income tax act, 1961.\n\t"
    "And, the rules and slab rates of old tax regime of the indian government.".format(name.title())
)

print()
consent = input("\nAre you here for the same purpose?   ")

if consent.lower() in ['yes', 'yeah', 'ofcourse']:
    print()
    print("GOOD {}!\n\tThen fill the following required details below:\n"
          "Remember one thing, the details should belong to the current year.".format(name.title()))
    print()
    print('-' * 90)
    print("First of all, let me know your all sources of income:")
    print('-' * 90)
    Income_from_salary = float(input(
        "{:<80}|    ".format(
            'Your monthly salary i.e,Sum of your Basic salary, HRA, LTA, DA allowances etc.')
    )) * 12
    basic_salary = float(input("{:>20}{:<23}|  ".format('', 'Basic salary'))) * 12
    HRA = float(input("{:>20}{:<23}|  ".format('', 'House Rent Allowance'))) * 12
    LTA = float(input("{:>20}{:<23}|  ".format('', 'Leave travel allowance'))) * 12
    DA = float(input("{:>20}{:<23}|  ".format('', 'Dearness allowance'))) * 12
    CA = float(input("{:>20}{:<23}|  ".format('', 'Conveyance allowance'))) * 12
    other_allowance = float(input("{:>20}{:<23}|  ".format('', 'Other allowance'))) * 12
    if (basic_salary + HRA + LTA + DA + CA + other_allowance) != Income_from_salary:
        print("Dear user, You are providing the wrong info about your salary component.\n"
              "Your total salary does not match with the total of your salary component.\n"
              "Check the details and try again.")
    else:
        print('-' * 90)
        Income_from_house_rent = float(input(
            "{:<80}|    ".format('Monthly Income from house property (if any). like, rental income etc.'))
        ) * 12
        print('-' * 90)
        Income_form_personal_business = float(input(
            "{:<80}|    ".format(
                'Total annual Income from own business and profession (if any), i.e, Net income.'))
        )
        print('-' * 90)
        capital_gain_or_loss = float(input(
            "{:<80}|\n{:<80}|    ".format(
                'Total Profit or loss from sale of capital assets (if any).like, profit or loss',
                'from sale of shares, property, other short or long term asset, in current year.')
        ))
        print('-' * 90)
        Income_form_other_source = float(input(
            "{:<80}|    ".format(
                'Monthly Income from other source (if any).like, interest income, dividends etc.'))
        ) * 12
        print('-' * 90)

        GTI = (Income_from_salary + Income_form_personal_business + Income_form_other_source
               + Income_from_house_rent + capital_gain_or_loss)

        print('\n{:^80}'.format('USER INFORMATION REGARDING EXEMPTIONS'))
        print("Now Mr.{}, let me inform you, As per section 10 of the income tax act, 1961\n"
              "Some specific portion of your salary income (i.e, income from HRA, DA, TA allowances etc.)\n"
              "is exempted from tax calculation, that is determined according to the specified rules.\n"
              "So, You can claim these exemptions, by supplying the following details accurately, and\n"
              "minimize your taxable income.".format(name.title()))
        print()
        print('-' * 90)
        rent_paid = float(input("{:<80}|   ".format('The amount of rent paid (Monthly), to the household'))) * 12
        print('-' * 90)
        city_type = input("{:<80}|    ".format('Type of city, where you currently live. (Metro or Non-metro)'))
        print('-' * 90)
        no_of_children = int(input('{:<80}|    '.format('The number of children you have.')))
        print('-' * 90)
        gratuity_received = float(input(
            "{:<80}|\n{:<80}|\n{:<80}|    ".format(
                'The amount of gratuity received in current year (if any).',
                'Note: Do not provide this detail, if the amount of gratuity received in current',
                'year, is not included in you salary income.')
        ))

        HRA_exemption = min(
            HRA,
            0.5 * (basic_salary + DA) if city_type.lower() == 'metro' else 0.4 * (basic_salary + DA),
            rent_paid - (0.1 * (basic_salary + DA))
        )
        print('-' * 90)
        LTA_exemption = LTA
        CA_exemption = min(CA, (1600 * 12))
        children_education_exemption = (min(no_of_children, 2) * 100 * 12)
        gratuity_exemption = min(gratuity_received, 2000000)

        Total_exemption = (HRA_exemption + LTA_exemption + CA_exemption +
                           children_education_exemption + gratuity_exemption)
        Net_salary = (GTI - Total_exemption)

        print()
        print("{:^80}".format("USER INFORMATION ABOUT DEDUCTION"))
        print("Now Mr.{}, let me inform you about the deduction. According to the income tax act, 1961\n"
              "Some specific type of expenditure are excluded form income for tax-calculation. if you have\n"
              "incur such type of expenditures then you can minimize your taxable income and get the tax-relief.\n"
              "So, kindly supply the following information, so that, we can determine the eligible deduction.".format(name.title()))
        print()
        print('-' * 90)
        investment_80c = float(input(
            "{:<80}|\n{:<80}|\n{}\n{}|    ".format(
                'Amount of investment in the funds specified under section 80C. (if any)',
                'The section 80C includes:',
                '\t\t investment like PPF, ELSS, NSC, life insurance premium, 5-year FD,',
                '\t\t tuition fees for children, principal repayment of home loan.'
            )
        ))
        deduction_under_80c = min(investment_80c, 150000)
        print('-' * 90)
        section_80d = float(input(
            "{:<80}|    ".format(
                'Amount of health insurance premium for self, spouse, and dependent-children.')))
        print('-' * 90)
        insurnce_for_parents = float(input(
            "{:<80}|    ".format('Amount of health insurance for your parents. (if any)')))
        print('-' * 90)
        parents_age = int(input(
            "{:<80}|    ".format('Age of your parent (for whom you have bought the insurnce policy.)')))
        print('-' * 90)
        deduction_under_80d = min(section_80d, 25000) + min(insurnce_for_parents, 50000 if parents_age >= 80 else 25000)
        deduction_under_80e = float(input(
            "{:<80}|    ".format('Amount of monthly interest for any educational loan. (if any)'))) * 12
        print('-' * 90)
        deduction_under_80g = float(input(
            "{:<80}|    ".format('Amount of donation to any charitable organisation. (if any)')))
        print('-' * 90)
        section_80tta = float(input(
            "{:<80}|    ".format('Total amount of saving account interest for the current year.')))
        print('-' * 90)
        deduction_under_80tta = min(section_80tta, 10000)
        deduction_under_80gg = 0
        section_24 = float(input(
            "{:<80}|    ".format('Amount of monthly interest on home loan. (if any)'))) * 12
        print('-' * 90)
        possession = input("{:<80}|    ".format('The possession above home is rented or self_occupied.'))
        print('-' * 90)
        deduction_under_24 = section_24 if possession.lower() == 'rented' else min(section_24, 200000)
        print("\nDeclaration:")
        declaration = input(
            "\tI Mr.{}, hereby declare that the information i have provided\n"
            "above is true and correct in the best of my knowledge. (True or false)  ".format(name.title())
        )
        if declaration.lower() == 'false':
            print("If the information you provide is wrong in your belief, then it may cause\n"
                  "wrong calculation of income tax.")
            input("Got it?  ")

        total_deduction = (deduction_under_80c + deduction_under_80d + deduction_under_80e +
                           deduction_under_80g + deduction_under_80tta + deduction_under_80gg + deduction_under_24)
        total_taxable_income = (Net_salary - total_deduction)

        print()
        print("\nOK {}, according to the details provided by you, your taxable income is as follows:".format(name.title()))
        print()
        print("{:^105}".format("Taxable Income Calculation Chart"))
        print("-" * 105)
        print("|{:^6}|{:^80}|{:^15}|".format("S.no.", "Particular", "Amount"))
        print("-" * 105)
        print("|{:^6}|{:<80}|{:^15}|".format("I.", "Total income from different sources", GTI))
        print("|{:^6}|{:<80}|{:->15}|".format("II.", "Less: Exemptions", ""))
        print("|{:^6}|{:>5}{:<75}|{:^15}|".format("--", "", "Exemption for Home rent allowance (HRA)", HRA_exemption))
        print("|{:^6}|{:>5}{:<75}|{:^15}|".format("--", "", "Exemption for Leave travel allowance (LTA)", LTA_exemption))
        print("|{:^6}|{:>5}{:<75}|{:^15}|".format("--", "", "Exemption for Conveyance allowance (CA)", CA_exemption))
        print("|{:^6}|{:>5}{:<75}|{:^15}|".format("--", "", "Exemption for Children education allowance", children_education_exemption))
        print("|{:^6}|{:>5}{:<75}|{:^15}|".format("--", "", "Exemption for Gratuity exemption (GE)", gratuity_exemption))
        print("-" * 105)
        print("|{:^6}|{:<80}|{:^15}|".format("III.", "Net income", Net_salary))
        print("|{:^6}|{:<80}|{:->15}|".format("IV.", "Less: Deductions", ""))
        print("|{:^6}|{:>5}{:<75}|{:^15}|".format("--", "", "Deduction under section 80C", deduction_under_80c))
        print("|{:^6}|{:>5}{:<75}|{:^15}|".format("--", "", "Deduction under section 80D", deduction_under_80d))
        print("|{:^6}|{:>5}{:<75}|{:^15}|".format("--", "", "Deduction under section 80E", deduction_under_80e))
        print("|{:^6}|{:>5}{:<75}|{:^15}|".format("--", "", "Deduction under section 80G", deduction_under_80g))
        print("|{:^6}|{:>5}{:<75}|{:^15}|".format("--", "", "Deduction under section 80TTA", deduction_under_80tta))
        print("|{:^6}|{:>5}{:<75}|{:^15}|".format("--", "", "Deduction under section 80GG", deduction_under_80gg))
        print("|{:^6}|{:>5}{:<75}|{:^15}|".format("--", "", "Deduction under section 24", deduction_under_24))
        print("-" * 105)
        print("|{:^6}|{:^80}|{:^15}|".format("V.", "Total taxable income", total_taxable_income))
        print("-" * 105)

        print()
        print("\nNow mr.{}, we will calculate the amount of your income tax, as per the age-rules\n"
              "and applicable slab rate of income tax act.".format(name.title()))
        print()
        age = int(input("So please {}, Enter your age.   ".format(name.title())))
        if age <= 60:
            age_category = "Below 60 year age group"
        elif 60 < age <= 80:
            age_category = 'Senior citizen group'
        else:
            age_category = 'Super senior citizen group'
        print('\nSo, Mr.{} You are under the {}. So the calculation of income tax,\n'
              'as per the applicable slab rate to you, is as follows:'.format(name.title(), age_category))

        print()
        print("{:^105}".format("Income Tax Calculation Chart"))
        S_no = ('I.', 'II.', 'III.', 'IV.', 'V.')

        def perc(income, t_rate):
            if income == 0:
                return 0
            return (income * t_rate)/100

        # Tax calculation for each age group
        result = 0
        surcharge = 0

        if age_category == "Below 60 year age group":
            Category = ('0 - 250,000', '250,001 - 500,000', '500,001 - 10,00,000', 'Above 10,00,000')
            rate = ('0%', '5%', '20%', '30%')
            calculation = ('250000 x 0% = 0', '250000 x 5% = 12500', '500000 x 20% = 100000')
            a = "|{:^6}|{:^30}|{:^25}|{:^35}|".format(S_no[0], Category[0], rate[0], calculation[0])
            b = "|{:^6}|{:^30}|{:^25}|{:^35}|".format(S_no[1], Category[1], rate[1], calculation[1])
            c = "|{:^6}|{:^30}|{:^25}|{:^35}|".format(S_no[2], Category[2], rate[2], calculation[2])
            e = perc(250000, 0)
            f = perc(250000, 5)
            g = perc(500000, 20)

            if total_taxable_income <= 250000:
                print('-' * 100)
                print("|{:^6}|{:^30}|{:^25}|{:^35}|".format("S_no.", "Income category", "Slab rate", "Tax_calculation"))
                print('-' * 100)
                print(a)
                print('-' * 100)
                print("|{:^6}|{:^56}={:^35}|".format("II.", "Total income tax", "{:.2f}".format(e)))
                print('-' * 100)
                print()
                print("Mr.{}, your annual income do not fall into any taxable category.\n"
                      "As per the slab rate for {} of the old tax regime,\n"
                      "the income upto 250,000 rupees is exempted for tax.".format(name.title(), age_category))
                print("\n\t So, your tax payable liability for this year is: 0")
                result = 0
            else:
                print('-' * 100)
                print("|{:^6}|{:^30}|{:^25}|{:^35}|".format("S_no.", "Income category", "Slab rate", "Tax_calculation"))
                print('-' * 100)
                print(a)
                print('-' * 100)
                if 250000 < total_taxable_income <= 500000:
                    step_1 = (total_taxable_income - 250000)
                    step_2 = perc(total_taxable_income - 250000, 5)
                    result = (e + step_2)
                    print("|{:^6}|{:^30}|{:^25}|{:^35}|".format(S_no[1], Category[1], rate[1], '{} x 5% = {}'.format(step_1, step_2)))
                elif 500000 < total_taxable_income <= 1000000:
                    step_1 = (total_taxable_income - 500000)
                    step_2 = perc(total_taxable_income - 500000, 20)
                    result = (e + f + step_2)
                    print(b)
                    print('-' * 100)
                    print("|{:^6}|{:^30}|{:^25}|{:^35}|".format(S_no[2], Category[2], rate[2], '{} x 20% = {}'.format(step_1, step_2)))
                elif total_taxable_income > 1000000:
                    step_1 = (total_taxable_income - 1000000)
                    step_2 = perc(total_taxable_income - 1000000, 30)
                    result = (e + f + g + step_2)
                    print(b)
                    print('-' * 100)
                    print(c)
                    print('-' * 100)
                    print("|{:^6}|{:^30}|{:^25}|{:^35}|".format(S_no[3], Category[3], rate[3], '{} x 30% = {}'.format(step_1, step_2)))
                print('-' * 100)
                print("|{:^6}|{:^56}={:^35}|".format(S_no[4], "Total income tax", "{:.2f}".format(result)))
                print('-' * 100)

        elif age_category == "Senior citizen group":
            Category = ('0 - 300,000', '300,001 - 500,000', '500,001 - 10,00,000', 'Above 10,00,000')
            rate = ('0%', '5%', '20%', '30%')
            calculation = ('300000 x 0% = 0', '200000 x 5% = 10000', '500000 x 20% = 100000')
            a = "|{:^6}|{:^30}|{:^25}|{:^35}|".format(S_no[0], Category[0], rate[0], calculation[0])
            b = "|{:^6}|{:^30}|{:^25}|{:^35}|".format(S_no[1], Category[1], rate[1], calculation[1])
            c = "|{:^6}|{:^30}|{:^25}|{:^35}|".format(S_no[2], Category[2], rate[2], calculation[2])
            e = perc(300000, 0)
            f = perc(200000, 5)
            g = perc(500000, 20)
            if total_taxable_income <= 300000:
                print('-' * 100)
                print("|{:^6}|{:^30}|{:^25}|{:^35}|".format("S_no.", "Income category", "Slab rate", "Tax_calculation"))
                print('-' * 100)
                print(a)
                print('-' * 100)
                print("|{:^6}|{:^56}={:^35}|".format("II.", "Total income tax", "{:.2f}".format(e)))
                print('-' * 100)
                print()
                print("Mr.{}, your annual income do not fall into any taxable category.\n"
                      "As per the slab rate for {} of the old tax regime,\n"
                      "the income upto 300,000 rupees is exempted for tax.".format(name.title(), age_category))
                print("\n\t So, your tax payable liability for this year is: 0")
                result = 0
            else:
                print('-' * 100)
                print("|{:^6}|{:^30}|{:^25}|{:^35}|".format("S_no.", "Income category", "Slab rate", "Tax_calculation"))
                print('-' * 100)
                print(a)
                print('-' * 100)
                if 300000 < total_taxable_income <= 500000:
                    step_1 = (total_taxable_income - 300000)
                    step_2 = perc(total_taxable_income - 300000, 5)
                    result = (e + step_2)
                    print("|{:^6}|{:^30}|{:^25}|{:^35}|".format(S_no[1], Category[1], rate[1], '{} x 5% = {}'.format(step_1, step_2)))
                elif 500000 < total_taxable_income <= 1000000:
                    step_1 = (total_taxable_income - 500000)
                    step_2 = perc(total_taxable_income - 500000, 20)
                    result = (e + f + step_2)
                    print(b)
                    print('-' * 100)
                    print("|{:^6}|{:^30}|{:^25}|{:^35}|".format(S_no[2], Category[2], rate[2], '{} x 20% = {}'.format(step_1, step_2)))
                elif total_taxable_income > 1000000:
                    step_1 = (total_taxable_income - 1000000)
                    step_2 = perc(total_taxable_income - 1000000, 30)
                    result = (e + f + g + step_2)
                    print(b)
                    print('-' * 100)
                    print(c)
                    print('-' * 100)
                    print("|{:^6}|{:^30}|{:^25}|{:^35}|".format(S_no[3], Category[3], rate[3], '{} x 30% = {}'.format(step_1, step_2)))
                print('-' * 100)
                print("|{:^6}|{:^56}={:^35}|".format(S_no[4], "Total income tax", "{:.2f}".format(result)))
                print('-' * 100)

        else:
            Category = ('0 - 500,000', '500,001 - 10,00,000', 'Above 10,00,000')
            rate = ('0%', '20%', '30%')
            calculation = ('500000 x 0% = 0', '500000 x 20% = 100000')
            a = "|{:^6}|{:^30}|{:^25}|{:^35}|".format(S_no[0], Category[0], rate[0], calculation[0])
            b = "|{:^6}|{:^30}|{:^25}|{:^35}|".format(S_no[1], Category[1], rate[1], calculation[1])
            c = "|{:^6}|{:^30}|{:^25}|".format(S_no[2], Category[2], rate[2])
            d = perc(500000, 0)
            e = perc(500000, 20)
            if total_taxable_income <= 500000:
                print('-' * 100)
                print("|{:^6}|{:^30}|{:^25}|{:^35}|".format("S_no.", "Income category", "Slab rate", "Tax_calculation"))
                print('-' * 100)
                print(a)
                print('-' * 100)
                print("|{:^6}|{:^56}={:^35}|".format("II.", "Total income tax", "{:.2f}".format(d)))
                print('-' * 100)
                print()
                print("Mr.{}, your annual income do not fall into any taxable category.\n"
                      "As per the slab rate for {} of the old tax regime,\n"
                      "the income upto 500,000 rupees is exempted for tax.".format(name.title(), age_category))
                print("\n\t So, your tax payable liability for this year is: 0")
                result = 0
            else:
                print('-' * 100)
                print("|{:^6}|{:^30}|{:^25}|{:^35}|".format("S_no.", "Income category", "Slab rate", "Tax_calculation"))
                print('-' * 100)
                print(a)
                print('-' * 100)
                if 500000 < total_taxable_income <= 1000000:
                    step_1 = (total_taxable_income - 500000)
                    step_2 = perc(total_taxable_income - 500000, 20)
                    result = (d + step_2)
                    print("|{:^6}|{:^30}|{:^25}|{:^35}|".format(S_no[1], Category[1], rate[1], '{} x 20% = {}'.format(step_1, step_2)))
                elif total_taxable_income > 1000000:
                    step_1 = (total_taxable_income - 1000000)
                    step_2 = perc(total_taxable_income - 1000000, 30)
                    result = (d + e + step_2)
                    print(b)
                    print('-' * 100)
                    print("|{:^6}|{:^30}|{:^25}|{:^35}|".format(S_no[2], Category[2], rate[2], '{} x 30% = {}'.format(step_1, step_2)))
                print('-' * 100)
                print("|{:^6}|{:^56}={:^35}|".format(S_no[3], "Total income tax", "{:.2f}".format(result)))
                print('-' * 100)

        total_tax = result

        if total_taxable_income <= 500000:
            print("|{:<63}={:^35}|".format('Less: Rebate under section 87A (for income upto 5 lakh)', "{:.2f}".format(result)))
            print("|{:<63}|{:>36}".format('It means, no tax will be charged to individual with an income', '|'))
            print("|{:<63}|{:>36}".format('of upto rupees 5 lakh, does\'nt matter the individual belong', '|'))
            print("|{:<63}|{:>36}".format('to which age category, slab rate and so on.', '|'))
            print("|{:>64}{:->35}|".format('', '-'))
            print("|{:^63}={:^35}|".format('Tax after rebate under section 87A', '0.00'))
            print('-' * 100)
            total_tax = 0

        elif total_taxable_income > 500000:
            if 5000000 <= total_taxable_income < 10000000:
                print("|{:<63}|{:>35}|".format('Add: Surcharge (an extra charge, other than tax) at the rate,', ''))
                print("|{:<63}|{:^35}|".format(
                    'of 10% of basic tax for income "50 lakh <= income < 1 crore"',
                    '{} x 10% = {:.2f}'.format(result, perc(result, 10))))
                surcharge = perc(result, 10)
            elif 10000000 <= total_taxable_income < 20000000:
                print("|{:<63}|{:>35}|".format('Add: Surcharge (an extra charge, other than tax) at the rate', ''))
                print("|{:<63}|{:^35}|".format(
                    'of 15% of basic tax for income "1 crore <= income < 2 crore"',
                    '{} x 15% = {:.2f}'.format(result, perc(result, 15))))
                surcharge = perc(result, 15)
            elif 20000000 <= total_taxable_income < 50000000:
                print("|{:<63}|{:>35}|".format('Add: Surcharge (an extra charge, other than tax) at the rate', ''))
                print("|{:<63}|{:^35}|".format(
                    'of 25% of basic tax for income "2 crore <= income < 5 crore"',
                    '{} x 25% = {:.2f}'.format(result, perc(result, 25))))
                surcharge = perc(result, 25)
            elif total_taxable_income >= 50000000:
                print("|{:<63}|{:>35}|".format('Add: Surcharge (an extra charge, other than tax) at the rate', ''))
                print("|{:<63}|{:^35}|".format(
                    'of 37% of basic tax for income greater than equal to 5 crore',
                    '{} x 37% = {:.2f}'.format(result, perc(result, 37))))
                surcharge = perc(result, 37)
            print("|{:>64}{:->35}|".format('', '-'))
            print("|{:^63}={:^35}|".format('Income tax plus surcharge', result + surcharge))
            print('-' * 100)
            total_tax = result + surcharge
        else:
            total_tax = result

        print("|{:<63}|{:^35}|".format('Add: Health and education cess (at the rate of 4%)',
                                        '{} x 4% = {:.2f}'.format(total_tax, perc(total_tax, 4))))
        tax_payable = total_tax + perc(total_tax, 4)
        print("|{:>64}{:->35}|".format('', '-'))
        print("|{:^63}={:^35}|".format('Total income tax payable.', tax_payable))
        print('-' * 100)
        print()
        print("So Mr.{}, as you can see, according to the details provided by you,\n"
              "your income tax liability for this year is: INR {:.2f}.".format(name.title(), tax_payable))
        print()
        print("Thanks to interact with us, Mr.{}.\nHave a good time.".format(name.title()))

else:
    print('Then why are you here idiot.\n'
          'yaha jhunjhuna bajane ke liye aaye ho ka!😂😂😂😂')
input("Got it")
