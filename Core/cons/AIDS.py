from django.utils.translation import gettext_lazy as _
from django.utils.datastructures import MultiValueDict

class list_of_aid_categories():
    
    START = 'START'
    CATEGORY = 'CATEGORY'
    TYPE = 'TYPE'
    AID = 'AID'

    @property
    def list(self):
        return {
            self.START: _('START'),
            self.CATEGORY: _('CATEGORY'),
            self.TYPE: _('TYPE'),
            self.AID: _('AID'),
            }

    @property
    def iteratable(self):
        return self.list.items()

class list_of_aid_types():
    
    FINANCIAL_AIDS = 'FINANCIAL_AIDS'
    MATERIAL_AIDS = 'MATERIAL_AIDS'

    @property
    def list(self):
        return {
            self.FINANCIAL_AIDS: _('FINANCIAL_AIDS'),
            self.MATERIAL_AIDS: _('MATERIAL_AIDS'),
            }

    @property
    def iteratable(self):
        return self.list.items()

class list_of_filters_categories():
    
    START = 'START'
    CATEGORY = 'CATEGORY'
    FILTER = 'FILTER'
    INDIVIDUAL_FILTER = 'INDIVIDUAL_FILTER'
    FAMILY_FILTER = 'FAMILY_FILTER'

    @property
    def list(self):
        return {
            self.INDIVIDUAL_FILTER: _('INDIVIDUAL_FILTER'),
            self.FAMILY_FILTER: _('FAMILY_FILTER'),
            }

    @property
    def iteratable(self):
        return self.list.items()

class list_of_filters_types():
    
    INDIVIDUAL_FILTER = 'INDIVIDUAL_FILTER'
    FAMILY_FILTER = 'FAMILY_FILTER'

    @property
    def list(self):
        return {
            self.INDIVIDUAL_FILTER: _('INDIVIDUAL_FILTER'),
            self.FAMILY_FILTER: _('FAMILY_FILTER'),
            }

    @property
    def iteratable(self):
        return self.list.items()

class list_of_relative_relation_types():

    GRANDFATHER = 'GRANDFATHER'
    GRANDMOTHER = 'GRANDMOTHER'
    FATHER = 'FATHER'
    MOTHER = 'MOTHER'
    # HUSBAND = 'HUSBAND'
    # WIFE = 'WIFE'
    SON = 'SON'
    DAUGHTER = 'DAUGHTER'
    BROTHER = 'BROTHER'
    SISTER = 'SISTER'
    FATHER_UNCLE = 'FATHER_UNCLE'
    FATHER_AUNT = 'FATHER_AUNT'
    MOTHER_UNCLE = 'MOTHER_UNCLE'
    MOTHER_AUNT = 'MOTHER_AUNT'
    RELATIVE_MAN = 'RELATIVE_MAN'
    RELATIVE_WOMEN = 'RELATIVE_WOMEN'

    @property
    def list(self):
        return {
            self.GRANDFATHER: _('GRANDFATHER'),
            self.GRANDMOTHER: _('GRANDMOTHER'),
            self.FATHER: _('FATHER'),
            self.MOTHER: _('MOTHER'),
            # self.HUSBAND: _('HUSBAND'),
            # self.WIFE: _('WIFE'),
            self.SON: _('SON'),
            self.DAUGHTER: _('DAUGHTER'),
            self.BROTHER: _('BROTHER'),
            self.SISTER: _('SISTER'),
            self.FATHER_UNCLE: _('FATHER_UNCLE'),
            self.FATHER_AUNT: _('FATHER_AUNT'),
            self.MOTHER_UNCLE: _('MOTHER_UNCLE'),
            self.MOTHER_AUNT: _('MOTHER_AUNT'),
            self.RELATIVE_MAN: _('RELATIVE_MAN'),
            self.RELATIVE_WOMEN: _('RELATIVE_WOMEN'),
        }

    @property
    def iteratable(self):
        return self.list.items()

class list_of_criteria_types():

    INDIVIDUAL_FILTER_SEX = 'INDIVIDUAL_FILTER_SEX'
    INDIVIDUAL_FILTER_NATIONALITY = 'INDIVIDUAL_FILTER_NATIONALITY'
    INDIVIDUAL_FILTER_AGE = 'INDIVIDUAL_FILTER_AGE'
    INDIVIDUAL_FILTER_MARTIAL = 'INDIVIDUAL_FILTER_MARTIAL'
    INDIVIDUAL_FILTER_HEALTH = 'INDIVIDUAL_FILTER_HEALTH'
    INDIVIDUAL_FILTER_EDUCATION = 'INDIVIDUAL_FILTER_EDUCATION'
    INDIVIDUAL_FILTER_WORK = 'INDIVIDUAL_FILTER_WORK'
    INDIVIDUAL_FILTER_INCOME = 'INDIVIDUAL_FILTER_INCOME'    
    INDIVIDUAL_FILTER_SPONSORSHIP = 'INDIVIDUAL_FILTER_SPONSORSHIP'

    FAMILY_FILTER_HOUSING_TYPE = 'FAMILY_FILTER_HOUSING_TYPE'
    FAMILY_FILTER_HOUSING_PLACE = 'FAMILY_FILTER_HOUSING_PLACE'
    FAMILY_FILTER_HOUSING_RENT = 'FAMILY_FILTER_HOUSING_RENT'
    FAMILY_FILTER_MEMBER_NUMBER = 'FAMILY_FILTER_MEMBER_NUMBER'
    FAMILY_FILTER_INCOME_AVERAGE = 'FAMILY_FILTER_INCOME_AVERAGE'
    FAMILY_FILTER_HEALTH_STATUS = 'FAMILY_FILTER_HEALTH_STATUS'
    FAMILY_FILTER_SPONSORSHIP = 'FAMILY_FILTER_SPONSORSHIP'

    @property
    def list(self):
        return {
            self.INDIVIDUAL_FILTER_SEX: _('INDIVIDUAL_FILTER_SEX'),
            self.INDIVIDUAL_FILTER_NATIONALITY: _('INDIVIDUAL_FILTER_NATIONALITY'),
            self.INDIVIDUAL_FILTER_AGE: _('INDIVIDUAL_FILTER_AGE'),
            self.INDIVIDUAL_FILTER_MARTIAL: _('INDIVIDUAL_FILTER_MARTIAL'),
            self.INDIVIDUAL_FILTER_HEALTH: _('INDIVIDUAL_FILTER_HEALTH'),
            self.INDIVIDUAL_FILTER_EDUCATION: _('INDIVIDUAL_FILTER_EDUCATION'),
            self.INDIVIDUAL_FILTER_WORK: _('INDIVIDUAL_FILTER_WORK'),
            self.INDIVIDUAL_FILTER_INCOME: _('INDIVIDUAL_FILTER_INCOME'),
            self.INDIVIDUAL_FILTER_SPONSORSHIP: _('INDIVIDUAL_FILTER_SPONSORSHIP'),

            self.FAMILY_FILTER_HOUSING_TYPE: _('FAMILY_FILTER_HOUSING_TYPE'),
            self.FAMILY_FILTER_HOUSING_PLACE: _('FAMILY_FILTER_HOUSING_PLACE'),
            self.FAMILY_FILTER_HOUSING_RENT: _('FAMILY_FILTER_HOUSING_RENT'),
            self.FAMILY_FILTER_MEMBER_NUMBER: _('FAMILY_FILTER_MEMBER_NUMBER'),
            self.FAMILY_FILTER_INCOME_AVERAGE: _('FAMILY_FILTER_INCOME_AVERAGE'),
            self.FAMILY_FILTER_HEALTH_STATUS: _('FAMILY_FILTER_HEALTH_STATUS'),
            self.FAMILY_FILTER_SPONSORSHIP: _('FAMILY_FILTER_SPONSORSHIP')
            }

    @property
    def iteratable(self):
        return self.list.items()

    @property
    def individual_filters(self):
        return {
            self.INDIVIDUAL_FILTER_SEX: _('INDIVIDUAL_FILTER_SEX'),
            self.INDIVIDUAL_FILTER_NATIONALITY: _('INDIVIDUAL_FILTER_NATIONALITY'),
            self.INDIVIDUAL_FILTER_AGE: _('INDIVIDUAL_FILTER_AGE'),
            self.INDIVIDUAL_FILTER_MARTIAL: _('INDIVIDUAL_FILTER_MARTIAL'),
            self.INDIVIDUAL_FILTER_HEALTH: _('INDIVIDUAL_FILTER_HEALTH'),
            self.INDIVIDUAL_FILTER_EDUCATION: _('INDIVIDUAL_FILTER_EDUCATION'),
            self.INDIVIDUAL_FILTER_WORK: _('INDIVIDUAL_FILTER_WORK'),
            self.INDIVIDUAL_FILTER_INCOME: _('INDIVIDUAL_FILTER_INCOME'),
            self.INDIVIDUAL_FILTER_SPONSORSHIP: _('INDIVIDUAL_FILTER_SPONSORSHIP'),
            }

    @property
    def individual_filters_iteratable(self):
        return self.individual_filters.items()

    @property
    def family_filters(self):
        return {
            self.FAMILY_FILTER_HOUSING_TYPE: _('FAMILY_FILTER_HOUSING_TYPE'),
            self.FAMILY_FILTER_HOUSING_PLACE: _('FAMILY_FILTER_HOUSING_PLACE'),
            self.FAMILY_FILTER_HOUSING_RENT: _('FAMILY_FILTER_HOUSING_RENT'),
            self.FAMILY_FILTER_MEMBER_NUMBER: _('FAMILY_FILTER_MEMBER_NUMBER'),
            self.FAMILY_FILTER_INCOME_AVERAGE: _('FAMILY_FILTER_INCOME_AVERAGE'),
            self.FAMILY_FILTER_HEALTH_STATUS: _('FAMILY_FILTER_HEALTH_STATUS'),
            self.FAMILY_FILTER_SPONSORSHIP: _('FAMILY_FILTER_SPONSORSHIP')
            }

    @property
    def family_filters_iteratable(self):
        return self.family_filters.items()

    # **********************************

    @property
    def form_type_1(self):
        return {
            self.INDIVIDUAL_FILTER_AGE: _('INDIVIDUAL_FILTER_AGE'),
            self.INDIVIDUAL_FILTER_INCOME: _('INDIVIDUAL_FILTER_INCOME'),
            self.FAMILY_FILTER_HOUSING_RENT: _('FAMILY_FILTER_HOUSING_RENT'),
            self.FAMILY_FILTER_MEMBER_NUMBER: _('FAMILY_FILTER_MEMBER_NUMBER'),
            self.FAMILY_FILTER_INCOME_AVERAGE: _('FAMILY_FILTER_INCOME_AVERAGE'),
            }

    @property
    def form_type_2(self):
        return {
            self.INDIVIDUAL_FILTER_SEX: _('INDIVIDUAL_FILTER_SEX'),
            self.INDIVIDUAL_FILTER_NATIONALITY: _('INDIVIDUAL_FILTER_NATIONALITY'),
            self.INDIVIDUAL_FILTER_MARTIAL: _('INDIVIDUAL_FILTER_MARTIAL'),
            self.INDIVIDUAL_FILTER_HEALTH: _('INDIVIDUAL_FILTER_HEALTH'),
            self.INDIVIDUAL_FILTER_EDUCATION: _('INDIVIDUAL_FILTER_EDUCATION'),
            self.INDIVIDUAL_FILTER_WORK: _('INDIVIDUAL_FILTER_WORK'),
            self.INDIVIDUAL_FILTER_SPONSORSHIP: _('INDIVIDUAL_FILTER_SPONSORSHIP'),
            self.FAMILY_FILTER_HOUSING_TYPE: _('FAMILY_FILTER_HOUSING_TYPE'),
            self.FAMILY_FILTER_HOUSING_PLACE: _('FAMILY_FILTER_HOUSING_PLACE'),
            self.FAMILY_FILTER_HEALTH_STATUS: _('FAMILY_FILTER_HEALTH_STATUS'),
            self.FAMILY_FILTER_SPONSORSHIP: _('FAMILY_FILTER_SPONSORSHIP')
            }

class list_of_operand_types():
    
    IN = 'IN'
    EQUAL = 'EQUAL'
    GREATER_THAN = 'GREATER_THAN'
    SMALLER_THAN = 'SMALLER_THAN'

    @property
    def list(self):
        return {
            self.IN: _('IN'),
            self.EQUAL: _('EQUAL'),
            self.GREATER_THAN: _('GREATER_THAN'),
            self.SMALLER_THAN: _('SMALLER_THAN'),
            }

    @property
    def iteratable(self):
        return self.list.items()

class list_of_family_health_status():

    NORMAL = 'NORMAL'
    TEMPORARY_ILLNESS_ONE = 'TEMPORARY_ILLNESS_ONE'
    TEMPORARY_ILLNESS_MULTIPLE = 'TEMPORARY_ILLNESS_MULTIPLE'
    PERMANENT_ILLNESS_ONE = 'PERMANENT_ILLNESS_ONE'
    PERMANENT_ILLNESS_MULTIPLE = 'PERMANENT_ILLNESS_MULTIPLE'

    @property
    def list(self):
        return {
            self.NORMAL: _('NORMAL'),
            self.TEMPORARY_ILLNESS_ONE: _('TEMPORARY_ILLNESS_ONE'),
            self.TEMPORARY_ILLNESS_MULTIPLE: _('TEMPORARY_ILLNESS_MULTIPLE'),
            self.PERMANENT_ILLNESS_ONE: _('PERMANENT_ILLNESS_ONE'),
            self.PERMANENT_ILLNESS_MULTIPLE: _('PERMANENT_ILLNESS_MULTIPLE'),
            }

    @property
    def iteratable(self):
        return self.list.items()

class list_of_accommodation_type():

    PROPERTY = 'PROPERTY'
    RENT = 'RENT'

    @property
    def list(self):
        return {
            self.PROPERTY: _('PROPERTY'),
            self.RENT: _('RENT'),
            }

    @property
    def iteratable(self):
        return self.list.items()