import frappe
import erpnext
from erpnext.payroll.doctype.salary_slip.salary_slip import SalarySlip


class ERPNextSalarySlip(SalarySlip):
	def calculate_tax_by_tax_slab(self, annual_taxable_earning, tax_slab):
		data = self.get_data_for_eval()
		data.update({"annual_taxable_earning": annual_taxable_earning})
		tax_amount = 0
		for slab in tax_slab.slabs:
			if annual_taxable_earning > slab.from_amount and not slab.to_amount:
				tax_amount += abs(annual_taxable_earning - slab.from_amount) * slab.percent_deduction *.01
				continue
			if annual_taxable_earning > slab.from_amount:
				tax_amount += abs(slab.to_amount - slab.from_amount) * slab.percent_deduction *.01
		# other taxes and charges on income tax
		for d in tax_slab.other_taxes_and_charges:
			if flt(d.min_taxable_income) and flt(d.min_taxable_income) > annual_taxable_earning:
				continue

			if flt(d.max_taxable_income) and flt(d.max_taxable_income) < annual_taxable_earning:
				continue

			tax_amount += tax_amount * flt(d.percent) / 100

		return tax_amount