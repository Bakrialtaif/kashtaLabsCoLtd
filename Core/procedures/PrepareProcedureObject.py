from Core.procedures.ProcedureImports import *

from Core.cons.PROCEDURES import list_of_procedure_names

class PrepareProcedureObject():
    
    def __init__(self, procedure_code: str, connected_object):
        self.procedure_code = procedure_code
        self.connected_object = connected_object

    def instantiate_object(self):
        if self.procedure_code == list_of_procedure_names().user_creation_procedure:
            return user_creation_procedure(connected_object=self.connected_object)

        if self.procedure_code == list_of_procedure_names().dummy_test_procedure:
            return dummy_test_procedure(connected_object=self.connected_object)

        if self.procedure_code == list_of_procedure_names().workflow_build_procedure:
            return workflow_build_procedure(connected_object=self.connected_object)

        if self.procedure_code == list_of_procedure_names().unit_card_build_procedure:
            return unit_card_build_procedure(connected_object=self.connected_object)

        if self.procedure_code == list_of_procedure_names().job_card_build_procedure:
            return job_card_build_procedure(connected_object=self.connected_object)

        if self.procedure_code == list_of_procedure_names().employee_dismissal_procedure:
            return employee_dismissal_procedure(connected_object=self.connected_object)

        if self.procedure_code == list_of_procedure_names().employee_recruitment_procedure:
            return employee_recruitment_procedure(connected_object=self.connected_object)

        if self.procedure_code == list_of_procedure_names().fiscal_year_open_procedure:
            return fiscal_year_open_procedure(connected_object=self.connected_object)

        if self.procedure_code == list_of_procedure_names().fiscal_year_close_procedure:
            return fiscal_year_close_procedure(connected_object=self.connected_object)

        if self.procedure_code == list_of_procedure_names().chart_of_accounts_procedure:
            return chart_of_accounts_procedure(connected_object=self.connected_object)

        if self.procedure_code == list_of_procedure_names().chart_of_cost_centers_procedure:
            return chart_of_cost_centers_procedure(connected_object=self.connected_object)

        if self.procedure_code == list_of_procedure_names().entry_procedure:
            return entry_procedure(connected_object=self.connected_object)

        if self.procedure_code == list_of_procedure_names().stocktaking_procedure:
            return stocktaking_procedure(connected_object=self.connected_object)

        if self.procedure_code == list_of_procedure_names().purchase_requisitions_procedure:
            return purchase_requisitions_procedure(connected_object=self.connected_object)

        if self.procedure_code == list_of_procedure_names().purchase_order_procedure:
            return purchase_order_procedure(connected_object=self.connected_object)

        if self.procedure_code == list_of_procedure_names().purchase_order_financial_processing:
            return purchase_order_financial_processing(connected_object=self.connected_object)

        if self.procedure_code == list_of_procedure_names().purchase_check_in_procedure:
            return purchase_check_in_procedure(connected_object=self.connected_object)

        if self.procedure_code == list_of_procedure_names().sales_order_procedure:
            return sales_order_procedure(connected_object=self.connected_object)

        if self.procedure_code == list_of_procedure_names().delivery_sales_procedure:
            return delivery_sales_procedure(connected_object=self.connected_object)

        if self.procedure_code == list_of_procedure_names().quotation_request_procedure:
            return quotation_request_procedure(connected_object=self.connected_object)

        if self.procedure_code == list_of_procedure_names().operational_project_procedure:
            return operational_project_procedure(connected_object=self.connected_object)

        if self.procedure_code == list_of_procedure_names().business_model_procedure:
            return business_model_procedure(connected_object=self.connected_object)

        if self.procedure_code == list_of_procedure_names().operational_plan_procedure:
            return operational_plan_procedure(connected_object=self.connected_object)

        if self.procedure_code == list_of_procedure_names().provider_account_creation_procedure:
            return provider_account_creation_procedure(connected_object=self.connected_object)

        if self.procedure_code == list_of_procedure_names().customer_account_creation_procedure:
            return customer_account_creation_procedure(connected_object=self.connected_object)

        if self.procedure_code == list_of_procedure_names().permission_request_procedure:
            return permission_request_procedure(connected_object=self.connected_object)