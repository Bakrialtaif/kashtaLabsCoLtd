from django.utils.translation import gettext_lazy as _
from django.utils.datastructures import MultiValueDict

class list_of_procedure_names():
    
    user_creation_procedure = 'user_creation_procedure'
    dummy_test_procedure = 'dummy_test_procedure'
    workflow_build_procedure = 'workflow_build_procedure'
    unit_card_build_procedure = 'unit_card_build_procedure'
    job_card_build_procedure = 'job_card_build_procedure'
    employee_dismissal_procedure = 'employee_dismissal_procedure'
    employee_recruitment_procedure = 'employee_recruitment_procedure'
    fiscal_year_open_procedure = 'fiscal_year_open_procedure'
    fiscal_year_close_procedure = 'fiscal_year_close_procedure'
    chart_of_accounts_procedure = 'chart_of_accounts_procedure'
    chart_of_cost_centers_procedure = 'chart_of_cost_centers_procedure'
    entry_procedure = 'entry_procedure'
    stocktaking_procedure = 'stocktaking_procedure'
    purchase_requisitions_procedure = 'purchase_requisitions_procedure'
    purchase_order_procedure = 'purchase_order_procedure'
    purchase_order_financial_processing = 'purchase_order_financial_processing'
    purchase_check_in_procedure = 'purchase_check_in_procedure'
    sales_order_procedure = 'sales_order_procedure'
    delivery_sales_procedure = 'delivery_sales_procedure'
    quotation_request_procedure = 'quotation_request_procedure'
    operational_project_procedure = 'operational_project_procedure'
    business_model_procedure = 'business_model_procedure'
    operational_plan_procedure = 'operational_plan_procedure'
    provider_account_creation_procedure = 'provider_account_creation_procedure'
    customer_account_creation_procedure = 'customer_account_creation_procedure'    
    permission_request_procedure = 'permission_request_procedure'    
    lession_calendar_building_procedure = 'lession_calendar_building_procedure'    
    student_procedure = 'student_procedure'    
    curriculum_procedure = 'curriculum_procedure'    

    @property
    def list(self):
        return {
            self.user_creation_procedure: _('user_creation_procedure'),
            self.dummy_test_procedure: _('dummy_test_procedure'),
            self.workflow_build_procedure: _('workflow_build_procedure'),
            self.unit_card_build_procedure: _('unit_card_build_procedure'),
            self.job_card_build_procedure: _('job_card_build_procedure'),
            self.employee_dismissal_procedure: _('employee_dismissal_procedure'),
            self.employee_recruitment_procedure: _('employee_recruitment_procedure'),
            self.fiscal_year_open_procedure: _('fiscal_year_open_procedure'),
            self.fiscal_year_close_procedure: _('fiscal_year_close_procedure'),
            self.chart_of_accounts_procedure: _('chart_of_accounts_procedure'),
            self.chart_of_cost_centers_procedure: _('chart_of_cost_centers_procedure'),
            self.entry_procedure: _('entry_procedure'),
            self.stocktaking_procedure: _('stocktaking_procedure'),
            self.purchase_requisitions_procedure: _('purchase_requisitions_procedure'),
            self.purchase_order_procedure: _('purchase_order_procedure'),
            self.purchase_order_financial_processing: _('purchase_order_financial_processing'),
            self.purchase_check_in_procedure: _('purchase_check_in_procedure'),
            self.sales_order_procedure: _('sales_order_procedure'),
            self.delivery_sales_procedure: _('delivery_sales_procedure'),
            self.quotation_request_procedure: _('quotation_request_procedure'),
            self.operational_project_procedure: _('operational_project_procedure'),
            self.business_model_procedure: _('business_model_procedure'),
            self.operational_plan_procedure: _('operational_plan_procedure'),
            self.provider_account_creation_procedure: _('provider_account_creation_procedure'),
            self.customer_account_creation_procedure: _('customer_account_creation_procedure'),
            self.permission_request_procedure: _('permission_request_procedure'),
            self.lession_calendar_building_procedure: _('lession_calendar_building_procedure'),
            self.student_procedure: _('student_procedure'),
            self.curriculum_procedure: _('curriculum_procedure'),
        }

    @property
    def iteratable(self):
        return self.list.items()
        