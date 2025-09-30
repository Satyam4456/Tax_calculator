
from flask import Flask, render_template, request, flash, redirect, url_for
from datetime import datetime
import os

class TaxCalculator:
    """Professional Income Tax Calculator Class"""
    
    def __init__(self):
        self.tax_slabs = {
            'below_60': [
                (250000, 0),
                (500000, 5),
                (1000000, 20),
                (float('inf'), 30)
            ],
            'senior_citizen': [
                (300000, 0),
                (500000, 5),
                (1000000, 20),
                (float('inf'), 30)
            ],
            'super_senior': [
                (500000, 0),
                (1000000, 20),
                (float('inf'), 30)
            ]
        }
    
    def get_greeting(self):
        """Generate time-based greeting"""
        current_hour = datetime.now().hour
        greetings = {
            (5, 11): "Good Morning! ☀️",
            (11, 15): "Good Afternoon! 🌤️",
            (15, 19): "Good Evening! 🌅",
            (19, 24): "Good Night! 🌙",
            (0, 5): "Working Late? 🌃"
        }
        
        for (start, end), greeting in greetings.items():
            if start <= current_hour < end:
                return greeting
        return "Hello! 👋"
    
    def calculate_percentage(self, amount, rate):
        """Calculate percentage of amount"""
        return (amount * rate) / 100 if amount > 0 else 0
    
    def calculate_exemptions(self, form_data):
        """Calculate total exemptions"""
        basic_salary = float(form_data.get('basic_salary', 0)) * 12
        da = float(form_data.get('da', 0)) * 12
        hra = float(form_data.get('hra', 0)) * 12
        lta = float(form_data.get('lta', 0)) * 12
        ca = float(form_data.get('ca', 0)) * 12
        rent_paid = float(form_data.get('rent_paid', 0)) * 12
        city_type = form_data.get('city_type', 'non-metro')
        children = int(form_data.get('children', 0))
        gratuity = float(form_data.get('gratuity', 0))
        
        # HRA Exemption
        hra_rate = 0.5 if city_type.lower() == 'metro' else 0.4
        hra_exemption = min(
            hra,
            hra_rate * (basic_salary + da),
            max(0, rent_paid - (0.1 * (basic_salary + da)))
        )
        
        # Other exemptions
        lta_exemption = lta
        ca_exemption = min(ca, 19200)  # 1600 * 12
        children_exemption = min(children, 2) * 1200  # 100 * 12
        gratuity_exemption = min(gratuity, 2000000)
        
        return {
            'hra_exemption': hra_exemption,
            'lta_exemption': lta_exemption,
            'ca_exemption': ca_exemption,
            'children_exemption': children_exemption,
            'gratuity_exemption': gratuity_exemption,
            'total_exemption': hra_exemption + lta_exemption + ca_exemption + children_exemption + gratuity_exemption
        }
    
    def calculate_deductions(self, form_data):
        """Calculate total deductions"""
        investment_80c = min(float(form_data.get('investment_80c', 0)), 150000)
        health_insurance = min(float(form_data.get('health_insurance', 0)), 25000)
        parents_insurance = float(form_data.get('parents_insurance', 0))
        parents_age = int(form_data.get('parents_age', 0))
        
        # Parents insurance deduction based on age
        parents_insurance_limit = 50000 if parents_age >= 80 else 25000
        parents_insurance_deduction = min(parents_insurance, parents_insurance_limit)
        
        education_loan = float(form_data.get('education_loan', 0)) * 12
        donation = float(form_data.get('donation', 0))
        savings_interest = min(float(form_data.get('savings_interest', 0)), 10000)
        home_loan = float(form_data.get('home_loan', 0)) * 12
        possession = form_data.get('possession', 'self_occupied')
        
        # Home loan deduction
        home_loan_deduction = home_loan if possession == 'rented' else min(home_loan, 200000)
        
        total_80d = health_insurance + parents_insurance_deduction
        
        return {
            'section_80c': investment_80c,
            'section_80d': total_80d,
            'section_80e': education_loan,
            'section_80g': donation,
            'section_80tta': savings_interest,
            'section_24': home_loan_deduction,
            'total_deduction': investment_80c + total_80d + education_loan + donation + savings_interest + home_loan_deduction
        }
    
    def calculate_tax(self, taxable_income, age):
        """Calculate income tax based on age category"""
        if age <= 60:
            category = 'below_60'
        elif age <= 80:
            category = 'senior_citizen'
        else:
            category = 'super_senior'
        
        tax = 0
        remaining_income = taxable_income
        tax_breakdown = []
        
        slabs = self.tax_slabs[category]
        prev_limit = 0
        
        for limit, rate in slabs:
            if remaining_income <= 0:
                break
                
            taxable_in_slab = min(remaining_income, limit - prev_limit)
            tax_in_slab = self.calculate_percentage(taxable_in_slab, rate)
            tax += tax_in_slab
            
            if taxable_in_slab > 0:
                tax_breakdown.append({
                    'range': f"₹{prev_limit:,} - ₹{min(limit, prev_limit + taxable_in_slab):,}",
                    'rate': f"{rate}%",
                    'taxable_amount': taxable_in_slab,
                    'tax_amount': tax_in_slab
                })
            
            remaining_income -= taxable_in_slab
            prev_limit = limit
            
            if limit == float('inf'):
                break
        
        # Rebate under section 87A
        if taxable_income <= 500000:
            tax = 0
        
        return tax, tax_breakdown, category
    
    def calculate_surcharge(self, taxable_income, base_tax):
        """Calculate surcharge based on income"""
        if taxable_income <= 5000000:
            return 0
        elif taxable_income <= 10000000:
            return self.calculate_percentage(base_tax, 10)
        elif taxable_income <= 20000000:
            return self.calculate_percentage(base_tax, 15)
        elif taxable_income <= 50000000:
            return self.calculate_percentage(base_tax, 25)
        else:
            return self.calculate_percentage(base_tax, 37)

# Initialize Flask app
app = Flask(__name__)
app.secret_key = os.urandom(24)
calculator = TaxCalculator()

@app.route('/')
def home():
    """Render the main tax calculation form"""
    greeting = calculator.get_greeting()
    return render_template('tax_form.html', greeting=greeting)

@app.route('/calculate', methods=['POST'])
def calculate_tax():
    """Process tax calculation and display results"""
    try:
        # Extract form data
        name = request.form.get('name', '').strip()
        age = int(request.form.get('age', 0))
        
        if not name:
            flash('Please enter your name', 'error')
            return redirect(url_for('home'))
        
        if age <= 0 or age > 120:
            flash('Please enter a valid age', 'error')
            return redirect(url_for('home'))
        
        # Calculate income components
        monthly_salary = float(request.form.get('monthly_salary', 0))
        annual_salary = monthly_salary * 12
        
        other_income = (
            float(request.form.get('house_rent', 0)) * 12 +
            float(request.form.get('business_income', 0)) +
            float(request.form.get('capital_gain', 0)) +
            float(request.form.get('other_income', 0)) * 12
        )
        
        gross_total_income = annual_salary + other_income
        
        # Calculate exemptions and deductions
        exemptions = calculator.calculate_exemptions(request.form)
        net_income = gross_total_income - exemptions['total_exemption']
        
        deductions = calculator.calculate_deductions(request.form)
        taxable_income = max(0, net_income - deductions['total_deduction'])
        
        # Calculate tax
        base_tax, tax_breakdown, age_category = calculator.calculate_tax(taxable_income, age)
        surcharge = calculator.calculate_surcharge(taxable_income, base_tax)
        tax_before_cess = base_tax + surcharge
        cess = calculator.calculate_percentage(tax_before_cess, 4)
        final_tax = tax_before_cess + cess
        
        # Prepare result data
        result_data = {
            'name': name,
            'age': age,
            'age_category': age_category.replace('_', ' ').title(),
            'gross_total_income': gross_total_income,
            'exemptions': exemptions,
            'net_income': net_income,
            'deductions': deductions,
            'taxable_income': taxable_income,
            'tax_breakdown': tax_breakdown,
            'base_tax': base_tax,
            'surcharge': surcharge,
            'tax_before_cess': tax_before_cess,
            'cess': cess,
            'final_tax': final_tax
        }
        
        return render_template('tax_result.html', **result_data)
        
    except ValueError as e:
        flash('Please enter valid numeric values', 'error')
        return redirect(url_for('home'))
    except Exception as e:
        flash('An error occurred during calculation. Please try again.', 'error')
        return redirect(url_for('home'))

@app.errorhandler(404)
def page_not_found(e):
    """Handle 404 errors"""
    return render_template('404.html'), 404

@app.errorhandler(500)
def internal_server_error(e):
    """Handle 500 errors"""
    return render_template('500.html'), 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
