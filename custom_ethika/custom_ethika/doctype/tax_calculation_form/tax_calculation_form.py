# Copyright (c) 2021, Vivek and contributors
# For license information, please see license.txt

# import frappe
from frappe.model.document import Document

class TaxCalculationForm(Document):
	def validate(self):
		self.get_total()

	def get_total(self):
		self.total = 0
		self.total_amount_of_any_other_exemption_under_section_10 = 0
		self.total_amount_of_exemption = 0
		self.total_amount_of_salary_received_from_current_employer = 0
		self.total_amount_of_deductions_under_section_16 = 0
		self.income_chargeable_under_the_head = 0
		# self.total_amount_of_other_income_reported_by_the_employee = 0
		self.total_deduction_under_section = 0
		self.aggregate_of_deductible = 0
		self.total = self.salary_as_per_provisions_contained_in_section + self.value_of_perquisites_under_section + self.profits_in_lieu_of_salary_under_section
		# self.total_amount_of_any_other_exemption_under_section_10 = (self.uniform_allowance * 12) + (self.travel_allowance * 12) + (self.self_development_allowance * 12)
		self.total_amount_of_exemption = self.travel_concession_or_assistance + self.death_cum_retirement_gratuity + self.commuted_value_of_pension + self.cash_equivalent_of_leave_salary_encashment + self.house_rent_allowance + self.total_amount_of_any_other_exemption_under_section_10
		self.total_amount_of_deductions_under_section_16 = self.standard_deduction_under_section + self.entertainment_allowance_under_section + self.entertainment_allowance_under_section
		self.total_amount_of_salary_received_from_current_employer = self.total + self.total_amount_of_any_other_exemption_under_section_10
		self.income_chargeable_under_the_head = self.total_amount_of_salary_received_from_current_employer + self.reported_total_amount_of_salary_received_from_other_employer - self.total_amount_of_deductions_under_section_16
		self.total_amount_of_other_income_reported_by_the_employee = self.income_from_house_property + self.income_under_the_head_other_sources_offered_for_tds
		self.total_deduction_under_section = self.total_80c + self.taxpayer_to_pension
		self.aggregate_of_deductible = self.deductible_amount + self.deductible_amount_1 + self.deductible_amount_1 + self.deductible_amount_2 + self.deductible_amount_3 + self.deductible_amount_4 + self.deductible_amount_5 + self.other_provision