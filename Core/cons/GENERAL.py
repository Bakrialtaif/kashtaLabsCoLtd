from django.utils.translation import gettext_lazy as _
from django.utils.datastructures import MultiValueDict

class list_of_app_labels():

    CORE = 'Core'
    P000 = 'P000'
    P001 = 'P001'
    P002 = 'P002'
    P003 = 'P003'
    P004 = 'P004'
    P005 = 'P005'
    P006 = 'P006'
    P007 = 'P007'
    P008 = 'P008'
    P009 = 'P009'
    P010 = 'P010'
    P011 = 'P011'
    P012 = 'P012'
    P013 = 'P013'
    P014 = 'P014'
    P015 = 'P015'
    P016 = 'P016'
    P017 = 'P017'
    P018 = 'P018'
    P019 = 'P019'
    P020 = 'P020'
    P021 = 'P021'
    P022 = 'P022'
    P023 = 'P023'
    P024 = 'P024'
    PRESENTATION = 'Presentation'


    @property
    def list(self):
        return {
            self.CORE: _('CORE'),
            self.P000: _('P000'),
            self.P001: _('P001'),
            self.P002: _('P002'),
            self.P003: _('P003'),
            self.P004: _('P004'),
            self.P005: _('P005'),
            self.P006: _('P006'),
            self.P007: _('P007'),
            self.P008: _('P008'),
            self.P009: _('P009'),
            self.P010: _('P010'),
            self.P011: _('P011'),
            self.P012: _('P012'),
            self.P013: _('P013'),
            self.P014: _('P014'),
            self.P015: _('P015'),
            self.P016: _('P016'),
            self.P017: _('P017'),
            self.P018: _('P018'),
            self.P019: _('P019'),
            self.P020: _('P020'),
            self.P021: _('P021'),
            self.P022: _('P022'),
            self.P023: _('P023'),
            self.P024: _('P024'),
            self.PRESENTATION: _('PRESENTATION'),
            }

    @property
    def iteratable(self):
        return self.list.items()

class list_of_model_names():
    PERMISSION = 'permission'
    WF_DUMP = 'wf_dump'
    PROFILE = 'profile'
    EDUCATION = 'education'
    WORK = 'work'
    TRAINING = 'training'
    ORGANIZATION = 'organization'
    WF_REQUEST = 'wf_request'
    OPERATIONAL_PLAN='operationalplan'
    PROJECT = 'project'
    TASK = 'task'
    TRANSACTION = 'transaction'
    FLEET = 'fleet'
    PARAGRAPH = 'paragraph'
    COMPONENT = 'component'
    FEATURE = 'feature'
    PARAMETER = 'parameter'
    PERMIT = 'permit'
    ELEMENT = 'element'
    FACT = 'fact'
    DATUM = 'datum'
    ANALYZE = 'analyze'
    UNIT = 'unit'
    CARD = 'card'
    PROCEDURE = 'procedure'
    BUSINESSMODEL = 'businessmodel'
    VOUCHER = 'voucher'
    DAYINWEEK = 'dayinweek'
    VERSION = 'version'
    REFINEMENT = 'refinement'
    QUOTE = 'quote'
    FAMILY = 'family'
    CURRICULUMS = 'curriculums'
    CALENDAR = 'calendar'
    Item = 'item'

    @property
    def list(self):
        return {
            self.PERMISSION: _('permission'),
            self.WF_DUMP: _('wf_dump'),
            self.PROFILE: _('profile'),
            self.EDUCATION: _('education'),
            self.WORK: _('work'),
            self.TRAINING: _('training'),
            self.ORGANIZATION: _('organization'),
            self.WF_REQUEST: _('wf_request'),
            self.OPERATIONAL_PLAN: _('operational_plan'),
            self.PROJECT: _('project'),
            self.TASK: _('task'),
            self.TRANSACTION: _('transaction'),
            self.PARAGRAPH: _('paragraph'),
            self.COMPONENT: _('component'),
            self.FLEET: _('fleet'),
            self.FEATURE: _('feature'),
            self.PARAMETER: _('parameter'),
            self.PERMIT: _('permit'),
            self.ELEMENT: _('element'),
            self.FACT: _('fact'),
            self.DATUM: _('datum'),
            self.ANALYZE: _('analyze'),
            self.UNIT: _('unit'),
            self.CARD: _('card'),
            self.PROCEDURE: _('procedure'),
            self.BUSINESSMODEL: _('businessmodel'),
            self.VOUCHER: _('voucher'),
            self.DAYINWEEK: _('dayinweek'),
            self.VERSION: _('version'),
            self.REFINEMENT: _('refinement'),
            self.FAMILY: _('family'),
            self.CURRICULUMS: _('curriculums'),
            self.CALENDAR: _('CALENDAR'),
            self.ITEM: _('item'),
            self.QUOTE: _('quote'),
            }

    @property
    def iteratable(self):
        return self.list.items()

    @property
    def core_models(self):
        return {
            self.COMPONENT,
            self.FEATURE,
            self.PARAMETER,
            self.PERMIT,
        }

class list_of_component_names():

    profile = 'profile'
    education_data = 'education-data'
    work_data = 'work-data'
    training_data = 'training-data'
    housing_data = 'housing-data'
    permission_request = 'permission-request'
    leave_request = 'leave-request'
    leave_credit_request = 'leave-credit-request'
    leave_cancel_request = 'leave-cancel-request'
    assignment_request = 'assignment-request'
    out_work_request = 'out-work-request'
    out_work_payment_request = 'out-work-payment-request'
    mandate_request = 'mandate-request'
    mandate_payment_request = 'mandate-payment-request'
    advance_payment_request = 'advance-payment-request'
    exchange_request = 'exchange-request'
    user_documents = 'user-documents'
    tasks = 'tasks'
    user_mail_box = 'user-mail-box'
    user_preferences = 'user-preferences'
    user_regulations = 'user-regulations'
    users = 'users'
    quotes = 'quotes'
    dump_requests = 'dump-requests'
    workflow = 'workflow'
    organization = 'organization'
    documents_configuration = 'documents-configuration'
    states = 'states'
    it_regulations = 'it-regulations'
    buildings = 'buildings'
    units = 'units'
    committees = 'committees'
    employees = 'employees'
    recruitment = 'recruitment'
    dismissal = 'dismissal'
    reports_dismissal = 'reports-dismissal'
    units_manager = 'units-manager'
    hr_regulations = 'hr-regulations'
    entries = 'entries'
    chart_of_accounts = 'chart-of-accounts'
    charts_of_cost_centers = 'charts-of-cost-centers'
    fiscal_years = 'fiscal-years'
    accountants = 'accountants'
    currencies = 'currencies'
    assets = 'assets'
    reports_data = 'reports-data'
    reports_charts = 'reports-charts'
    asset_types = 'asset-types'
    inventory_categories_and_items = 'inventory-categories-and-items'
    warehouses = 'warehouses'
    purchases = 'purchases'
    payment_requests = 'payment-requests'
    business_models = 'business-models'
    operational_plans = 'operational-plans'
    archives_transactions = 'archives-transactions'
    folders = 'folders'
    tags = 'tags'
    customers = 'customers'
    suppliers = 'suppliers'
    customer_requests = 'customer-requests'
    customer_items = 'customer-items'
    customer_inventory = 'customer-inventory'
    customer_users = 'customer-users'
    customer_data = 'customer-data'
    vouchers = 'vouchers'
    families = 'families'
    curriculums = 'curriculums'

    @property
    def list(self):
        return {
            self.profile: _('profile'),
            self.education_data: _('education-data'),
            self.work_data: _('work-data'),
            self.training_data: _('training-data'),
            self.housing_data: _('housing-data'),
            self.permission_request: _('permission-request'),
            self.leave_request: _('leave-request'),
            self.leave_credit_request: _('leave-credit-request'),
            self.leave_cancel_request: _('leave-cancel-request'),
            self.assignment_request: _('assignment-request'),
            self.out_work_request: _('out-work-request'),
            self.out_work_payment_request: _('out-work-payment-request'),
            self.mandate_request: _('mandate-request'),
            self.mandate_payment_request: _('mandate-payment-request'),
            self.advance_payment_request: _('advance-payment-request'),
            self.exchange_request: _('exchange-request'),
            self.user_documents: _('user-documents'),
            self.user_tasks: _('user-tasks'),
            self.user_mail_box: _('user-mail-box'),
            self.user_preferences: _('user-preferences'),
            self.user_regulations: _('user-regulations'),
            self.users: _('users'),
            self.quotes: _('quotes'),
            self.dump_requests: _('dump-requests'),
            self.workflow: _('workflow'),
            self.organization: _('organization'),
            self.documents_configuration: _('documents-configuration'),
            self.states: _('states'),
            self.it_regulations: _('it-regulations'),
            self.buildings: _('buildings'),
            self.units: _('units'),
            self.committees: _('committees'),
            self.employees: _('employees'),
            self.recruitment: _('recruitment'),
            self.dismissal: _('dismissal'),
            self.reports_dismissal: _('reports-dismissal'),
            self.units_manager: _('units-manager'),
            self.hr_regulations: _('hr-regulations'),
            self.entries: _('entries'),
            self.chart_of_accounts: _('chart-of-accounts'),
            self.charts_of_cost_centers: _('charts-of-cost-centers'),
            self.fiscal_years: _('fiscal-years'),
            self.accountants: _('accountants'),
            self.currencies: _('currencies'),
            self.assets: _('assets'),
            self.reports_data: _('reports-data'),
            self.reports_charts: _('reports-charts'),
            self.asset_types: _('asset-types'),
            self.inventory_categories_and_items: _('inventory-categories-and-items'),
            self.warehouses: _('warehouses'),
            self.purchases: _('purchases'),
            self.payment_requests: _('payment-requests'),
            self.business_models: _('business-models'),
            self.operational_plans: _('operational-plans'),
            self.archives_transactions: _('archives-transactions'),
            self.folders: _('folders'),
            self.tags: _('tags'),
            self.customers: _('customers'),
            self.suppliers: _('suppliers'),
            self.customer_requests: _('customer-requests'),
            self.customer_items: _('customer-items'),
            self.customer_inventory: _('customer-inventory'),
            self.customer_users: _('customer-users'),
            self.customer_data: _('customer-data'),
            self.vouchers: _('vouchers'),
            self.families: _('families'),
            self.curriculums: _('curriculums'),
        }

    @property
    def iteratable(self):
        return self.list.items()

    @property
    def user_data_components(self):
        return {
            self.education_data: _('education-data'),
            self.work_data: _('work-data'),
            self.training_data: _('training-data'),
        }
    
    @property
    def user_data_components_iteratable(self):
        return self.user_data_components.items()


class list_of_procedures_names():
    
    BUSINESS_MODEL_PROCEDURE = 'business_model_procedure'
    OPERATIONAL_PLAN_PROCEDURE = 'operational_plan_procedure'

    @property
    def list(self):
        return {
            self.BUSINESS_MODEL_PROCEDURE: _('business model procedure'),
            self.OPERATIONAL_PLAN_PROCEDURE: _('operational plan procedure'),
            }

    @property
    def iteratable(self):
        return self.list.items()

class list_of_week_days():
    
    Monday = 'Monday'
    Tuesday = 'Tuesday'
    Wednesday = 'Wednesday'
    Thursday = 'Thursday'
    Friday = 'Friday'
    Saturday = 'Saturday'
    Sunday = 'Sunday'

    @property
    def list(self):
        return {
                self.Monday: _('Monday'),
                self.Tuesday: _('Tuesday'),
                self.Wednesday: _('Wednesday'),
                self.Thursday: _('Thursday'),
                self.Friday: _('Friday'),
                self.Saturday: _('Saturday'),
                self.Sunday: _('Sunday'),
            }

    @property
    def iteratable(self):
        return self.list.items()


class list_of_ownership_types():
    
    ORGANIZATION = 'ORGANIZATION'
    USER = 'USER'

    @property
    def list(self):
        return {
            self.ORGANIZATION: _('organization'),
            self.USER: _('user'),
            }

    @property
    def iteratable(self):
        return self.list.items()

class list_of_colors_types():
    
    COLOR_001f3f = '#001f3f'
    COLOR_0074d9 = '#0074d9'
    COLOR_39cccc = '#39cccc'
    COLOR_3d9970 = '#3d9970'
    COLOR_ff851b = '#ff851b'
    COLOR_ff4136 = '#ff4136'
    COLOR_ff4136 = '#ff4136'
    COLOR_85144b = '#85144b'
    COLOR_b10dc9 = '#b10dc9'
    COLOR_aaaaaa = '#aaaaaa'
    COLOR_dddddd = '#dddddd'
    COLOR_00afb9 = '#00afb9'
    COLOR_f07167 = '#f07167'
    COLOR_ad6a6c = '#ad6a6c'
    COLOR_708d81 = '#708d81'
    COLOR_01497c = '#01497c'
    COLOR_3b6064 = '#3b6064'
    COLOR_3c7a89 = '#3c7a89'
    COLOR_4f5d75 = '#4f5d75'
    COLOR_9db4c0 = '#9db4c0'

    @property
    def list(self):
        return {
            self.COLOR_001f3f: '#001f3f',
            self.COLOR_0074d9: '#0074d9',
            self.COLOR_39cccc: '#39cccc',
            self.COLOR_3d9970: '#3d9970',
            self.COLOR_ff851b: '#ff851b',
            self.COLOR_ff4136: '#ff4136',
            self.COLOR_ff4136: '#ff4136',
            self.COLOR_85144b: '#85144b',
            self.COLOR_b10dc9: '#b10dc9',
            self.COLOR_aaaaaa: '#aaaaaa',
            self.COLOR_dddddd: '#dddddd',
            self.COLOR_00afb9: '#00afb9',
            self.COLOR_f07167: '#f07167',
            self.COLOR_ad6a6c: '#ad6a6c',
            self.COLOR_708d81: '#708d81',
            self.COLOR_01497c: '#01497c',
            self.COLOR_3b6064: '#3b6064',
            self.COLOR_3c7a89: '#3c7a89',
            self.COLOR_4f5d75: '#4f5d75',
            self.COLOR_9db4c0: '#9db4c0',
        }

    @property
    def iteratable(self):
        return self.list.items()

class list_of_notification_status():
    SENT = 'sent'
    VISITED = 'visited'

    @property
    def list(self):
        return {
            self.SENT: _('sent'),
            self.VISITED: _('visited'),
            }

    @property
    def iteratable(self):
        return self.list.items()        

class list_of_business_model_item_types():
    KEY_PARTNERS = 'KEY_PARTNERS'
    KEY_ACTIVITIES = 'KEY_ACTIVITIES'
    VALUE_PROPOSITION = 'VALUE_PROPOSITION'
    CUSTOMER_RELATIONSHIP = 'CUSTOMER_RELATIONSHIP'
    CUSTOMER_SEGMENTS = 'CUSTOMER_SEGMENTS'
    KEY_RESOURCES = 'KEY_RESOURCES'
    CHANNELS = 'CHANNELS'
    COST_STRUCTURE = 'COST_STRUCTURE'
    REVENUE_STREAMS = 'REVENUE_STREAMS'

    @property
    def list(self):
        return {
            self.KEY_PARTNERS: _('KEY_PARTNERS'),
            self.KEY_ACTIVITIES: _('KEY_ACTIVITIES'),
            self.VALUE_PROPOSITION: _('VALUE_PROPOSITION'),
            self.CUSTOMER_RELATIONSHIP: _('CUSTOMER_RELATIONSHIP'),
            self.CUSTOMER_SEGMENTS: _('CUSTOMER_SEGMENTS'),
            self.KEY_RESOURCES: _('KEY_RESOURCES'),
            self.CHANNELS: _('CHANNELS'),
            self.COST_STRUCTURE: _('COST_STRUCTURE'),
            self.REVENUE_STREAMS: _('REVENUE_STREAMS'),
        }

    @property
    def iteratable(self):
        return self.list.items()

class list_of_goals_types():
    
    START = 'START'
    GENERAL_GOAL = 'GENERAL_GOAL'
    DETAILED_GOAL = 'DETAILED_GOAL'
    PROJECT = 'PROJECT'

    @property
    def list(self):
        return {
            self.START: _('START'),
            self.GENERAL_GOAL: _('GENERAL_GOAL'),
            self.DETAILED_GOAL: _('DETAILED_GOAL'),
            self.PROJECT: _('PROJECT'),
        }

    @property
    def iteratable(self):
        return self.list.items()

class list_of_place_types():
    
    COUNTRY = 'COUNTRY'
    STATE = 'STATE'
    PROVINCE = 'PROVINCE'
    TOWN = 'TOWN'
    DISTRICT = 'DISTRICT'
    LOCATION = 'LOCATION'

    @property
    def list(self):
        return {
            self.COUNTRY: _('COUNTRY'),
            self.STATE: _('STATE'),
            self.PROVINCE: _('PROVINCE'),
            self.TOWN: _('TOWN'),
            self.DISTRICT: _('DISTRICT'),
            self.LOCATION: _('LOCATION'),
        }

    @property
    def iteratable(self):
        return self.list.items()

# Reference 
# https://www.nationsonline.org/oneworld/countrynames_arabic.htm
class list_of_countries_names():
    ABW = 'ABW'
    AFG = 'AFG'
    AGO = 'AGO'
    AIA = 'AIA'
    ALA = 'ALA'
    ALB = 'ALB'
    AND = 'AND'
    ANT = 'ANT'
    ARE = 'ARE'
    ARG = 'ARG'
    ARM = 'ARM'
    ASM = 'ASM'
    ATA = 'ATA'
    ATF = 'ATF'
    ATG = 'ATG'
    AUS = 'AUS'
    AUT = 'AUT'
    AZE = 'AZE'
    BDI = 'BDI'
    BEL = 'BEL'
    BEN = 'BEN'
    BFA = 'BFA'
    BGD = 'BGD'
    BGR = 'BGR'
    BHR = 'BHR'
    BHS = 'BHS'
    BIH = 'BIH'
    BLM = 'BLM'
    BLR = 'BLR'
    BLZ = 'BLZ'
    BMU = 'BMU'
    BOL = 'BOL'
    BRA = 'BRA'
    BRB = 'BRB'
    BRN = 'BRN'
    BTN = 'BTN'
    BVT = 'BVT'
    BWA = 'BWA'
    CAF = 'CAF'
    CAN = 'CAN'
    CCK = 'CCK'
    CHE = 'CHE'
    CHL = 'CHL'
    CHN = 'CHN'
    CIV = 'CIV'
    CMR = 'CMR'
    COD = 'COD'
    COG = 'COG'
    COK = 'COK'
    COL = 'COL'
    COM = 'COM'
    CPV = 'CPV'
    CRI = 'CRI'
    CUB = 'CUB'
    CXR = 'CXR'
    CYM = 'CYM'
    CYP = 'CYP'
    CZE = 'CZE'
    DEU = 'DEU'
    DJI = 'DJI'
    DMA = 'DMA'
    DNK = 'DNK'
    DOM = 'DOM'
    DZA = 'DZA'
    ECU = 'ECU'
    EGY = 'EGY'
    ERI = 'ERI'
    ESH = 'ESH'
    ESP = 'ESP'
    EST = 'EST'
    ETH = 'ETH'
    FIN = 'FIN'
    FJI = 'FJI'
    FLK = 'FLK'
    FRA = 'FRA'
    FRO = 'FRO'
    FSM = 'FSM'
    GAB = 'GAB'
    GBR = 'GBR'
    GEO = 'GEO'
    GGY = 'GGY'
    GHA = 'GHA'
    GIB = 'GIB'
    GIN = 'GIN'
    GLP = 'GLP'
    GMB = 'GMB'
    GNB = 'GNB'
    GNQ = 'GNQ'
    GRC = 'GRC'
    GRD = 'GRD'
    GRL = 'GRL'
    GTM = 'GTM'
    GUF = 'GUF'
    GUM = 'GUM'
    GUY = 'GUY'
    HKG = 'HKG'
    HMD = 'HMD'
    HND = 'HND'
    HRV = 'HRV'
    HTI = 'HTI'
    HUN = 'HUN'
    IDN = 'IDN'
    IMN = 'IMN'
    IND = 'IND'
    IOT = 'IOT'
    IRL = 'IRL'
    IRN = 'IRN'
    IRQ = 'IRQ'
    ISL = 'ISL'
    ISR = 'ISR'
    ITA = 'ITA'
    JAM = 'JAM'
    JEY = 'JEY'
    JOR = 'JOR'
    JPN = 'JPN'
    KAZ = 'KAZ'
    KEN = 'KEN'
    KGZ = 'KGZ'
    KHM = 'KHM'
    KIR = 'KIR'
    KNA = 'KNA'
    KOR = 'KOR'
    KWT = 'KWT'
    LAO = 'LAO'
    LBN = 'LBN'
    LBR = 'LBR'
    LBY = 'LBY'
    LCA = 'LCA'
    LIE = 'LIE'
    LKA = 'LKA'
    LSO = 'LSO'
    LTU = 'LTU'
    LUX = 'LUX'
    LVA = 'LVA'
    MAC = 'MAC'
    MAF = 'MAF'
    MAR = 'MAR'
    MCO = 'MCO'
    MDA = 'MDA'
    MDG = 'MDG'
    MDV = 'MDV'
    MEX = 'MEX'
    MHL = 'MHL'
    MKD = 'MKD'
    MLI = 'MLI'
    MLT = 'MLT'
    MMR = 'MMR'
    MNE = 'MNE'
    MNG = 'MNG'
    MNP = 'MNP'
    MOZ = 'MOZ'
    MRT = 'MRT'
    MSR = 'MSR'
    MTQ = 'MTQ'
    MUS = 'MUS'
    MWI = 'MWI'
    MYS = 'MYS'
    MYT = 'MYT'
    NAM = 'NAM'
    NCL = 'NCL'
    NER = 'NER'
    NFK = 'NFK'
    NGA = 'NGA'
    NIC = 'NIC'
    NIU = 'NIU'
    NLD = 'NLD'
    NOR = 'NOR'
    NPL = 'NPL'
    NRU = 'NRU'
    NZL = 'NZL'
    OMN = 'OMN'
    PAK = 'PAK'
    PAN = 'PAN'
    PCN = 'PCN'
    PER = 'PER'
    PHL = 'PHL'
    PLW = 'PLW'
    PNG = 'PNG'
    POL = 'POL'
    PRI = 'PRI'
    PRK = 'PRK'
    PRT = 'PRT'
    PRY = 'PRY'
    PSE = 'PSE'
    PYF = 'PYF'
    QAT = 'QAT'
    REU = 'REU'
    ROU = 'ROU'
    RUS = 'RUS'
    RWA = 'RWA'
    SAU = 'SAU'
    SDN = 'SDN'
    SEN = 'SEN'
    SGP = 'SGP'
    SGS = 'SGS'
    SHN = 'SHN'
    SJM = 'SJM'
    SLB = 'SLB'
    SLE = 'SLE'
    SLV = 'SLV'
    SMR = 'SMR'
    SOM = 'SOM'
    SPM = 'SPM'
    SRB = 'SRB'
    STP = 'STP'
    SUR = 'SUR'
    SVK = 'SVK'
    SVN = 'SVN'
    SWE = 'SWE'
    SWZ = 'SWZ'
    SYC = 'SYC'
    SYR = 'SYR'
    TCA = 'TCA'
    TCD = 'TCD'
    TGO = 'TGO'
    THA = 'THA'
    TJK = 'TJK'
    TKL = 'TKL'
    TKM = 'TKM'
    TLS = 'TLS'
    TON = 'TON'
    TTO = 'TTO'
    TUN = 'TUN'
    TUR = 'TUR'
    TUV = 'TUV'
    TWN = 'TWN'
    TZA = 'TZA'
    UGA = 'UGA'
    UKR = 'UKR'
    UMI = 'UMI'
    URY = 'URY'
    USA = 'USA'
    UZB = 'UZB'
    VAT = 'VAT'
    VCT = 'VCT'
    VEN = 'VEN'
    VGB = 'VGB'
    VIR = 'VIR'
    VNM = 'VNM'
    VUT = 'VUT'
    WLF = 'WLF'
    WSM = 'WSM'
    YEM = 'YEM'
    ZAF = 'ZAF'
    ZMB = 'ZMB'
    ZWE = 'ZWE'

    @property
    def list(self):
        return {
            self.ABW: _('ABW'),
            self.AFG: _('AFG'),
            self.AGO: _('AGO'),
            self.AIA: _('AIA'),
            self.ALA: _('ALA'),
            self.ALB: _('ALB'),
            self.AND: _('AND'),
            self.ANT: _('ANT'),
            self.ARE: _('ARE'),
            self.ARG: _('ARG'),
            self.ARM: _('ARM'),
            self.ASM: _('ASM'),
            self.ATA: _('ATA'),
            self.ATF: _('ATF'),
            self.ATG: _('ATG'),
            self.AUS: _('AUS'),
            self.AUT: _('AUT'),
            self.AZE: _('AZE'),
            self.BDI: _('BDI'),
            self.BEL: _('BEL'),
            self.BEN: _('BEN'),
            self.BFA: _('BFA'),
            self.BGD: _('BGD'),
            self.BGR: _('BGR'),
            self.BHR: _('BHR'),
            self.BHS: _('BHS'),
            self.BIH: _('BIH'),
            self.BLM: _('BLM'),
            self.BLR: _('BLR'),
            self.BLZ: _('BLZ'),
            self.BMU: _('BMU'),
            self.BOL: _('BOL'),
            self.BRA: _('BRA'),
            self.BRB: _('BRB'),
            self.BRN: _('BRN'),
            self.BTN: _('BTN'),
            self.BVT: _('BVT'),
            self.BWA: _('BWA'),
            self.CAF: _('CAF'),
            self.CAN: _('CAN'),
            self.CCK: _('CCK'),
            self.CHE: _('CHE'),
            self.CHL: _('CHL'),
            self.CHN: _('CHN'),
            self.CIV: _('CIV'),
            self.CMR: _('CMR'),
            self.COD: _('COD'),
            self.COG: _('COG'),
            self.COK: _('COK'),
            self.COL: _('COL'),
            self.COM: _('COM'),
            self.CPV: _('CPV'),
            self.CRI: _('CRI'),
            self.CUB: _('CUB'),
            self.CXR: _('CXR'),
            self.CYM: _('CYM'),
            self.CYP: _('CYP'),
            self.CZE: _('CZE'),
            self.DEU: _('DEU'),
            self.DJI: _('DJI'),
            self.DMA: _('DMA'),
            self.DNK: _('DNK'),
            self.DOM: _('DOM'),
            self.DZA: _('DZA'),
            self.ECU: _('ECU'),
            self.EGY: _('EGY'),
            self.ERI: _('ERI'),
            self.ESH: _('ESH'),
            self.ESP: _('ESP'),
            self.EST: _('EST'),
            self.ETH: _('ETH'),
            self.FIN: _('FIN'),
            self.FJI: _('FJI'),
            self.FLK: _('FLK'),
            self.FRA: _('FRA'),
            self.FRO: _('FRO'),
            self.FSM: _('FSM'),
            self.GAB: _('GAB'),
            self.GBR: _('GBR'),
            self.GEO: _('GEO'),
            self.GGY: _('GGY'),
            self.GHA: _('GHA'),
            self.GIB: _('GIB'),
            self.GIN: _('GIN'),
            self.GLP: _('GLP'),
            self.GMB: _('GMB'),
            self.GNB: _('GNB'),
            self.GNQ: _('GNQ'),
            self.GRC: _('GRC'),
            self.GRD: _('GRD'),
            self.GRL: _('GRL'),
            self.GTM: _('GTM'),
            self.GUF: _('GUF'),
            self.GUM: _('GUM'),
            self.GUY: _('GUY'),
            self.HKG: _('HKG'),
            self.HMD: _('HMD'),
            self.HND: _('HND'),
            self.HRV: _('HRV'),
            self.HTI: _('HTI'),
            self.HUN: _('HUN'),
            self.IDN: _('IDN'),
            self.IMN: _('IMN'),
            self.IND: _('IND'),
            self.IOT: _('IOT'),
            self.IRL: _('IRL'),
            self.IRN: _('IRN'),
            self.IRQ: _('IRQ'),
            self.ISL: _('ISL'),
            self.ISR: _('ISR'),
            self.ITA: _('ITA'),
            self.JAM: _('JAM'),
            self.JEY: _('JEY'),
            self.JOR: _('JOR'),
            self.JPN: _('JPN'),
            self.KAZ: _('KAZ'),
            self.KEN: _('KEN'),
            self.KGZ: _('KGZ'),
            self.KHM: _('KHM'),
            self.KIR: _('KIR'),
            self.KNA: _('KNA'),
            self.KOR: _('KOR'),
            self.KWT: _('KWT'),
            self.LAO: _('LAO'),
            self.LBN: _('LBN'),
            self.LBR: _('LBR'),
            self.LBY: _('LBY'),
            self.LCA: _('LCA'),
            self.LIE: _('LIE'),
            self.LKA: _('LKA'),
            self.LSO: _('LSO'),
            self.LTU: _('LTU'),
            self.LUX: _('LUX'),
            self.LVA: _('LVA'),
            self.MAC: _('MAC'),
            self.MAF: _('MAF'),
            self.MAR: _('MAR'),
            self.MCO: _('MCO'),
            self.MDA: _('MDA'),
            self.MDG: _('MDG'),
            self.MDV: _('MDV'),
            self.MEX: _('MEX'),
            self.MHL: _('MHL'),
            self.MKD: _('MKD'),
            self.MLI: _('MLI'),
            self.MLT: _('MLT'),
            self.MMR: _('MMR'),
            self.MNE: _('MNE'),
            self.MNG: _('MNG'),
            self.MNP: _('MNP'),
            self.MOZ: _('MOZ'),
            self.MRT: _('MRT'),
            self.MSR: _('MSR'),
            self.MTQ: _('MTQ'),
            self.MUS: _('MUS'),
            self.MWI: _('MWI'),
            self.MYS: _('MYS'),
            self.MYT: _('MYT'),
            self.NAM: _('NAM'),
            self.NCL: _('NCL'),
            self.NER: _('NER'),
            self.NFK: _('NFK'),
            self.NGA: _('NGA'),
            self.NIC: _('NIC'),
            self.NIU: _('NIU'),
            self.NLD: _('NLD'),
            self.NOR: _('NOR'),
            self.NPL: _('NPL'),
            self.NRU: _('NRU'),
            self.NZL: _('NZL'),
            self.OMN: _('OMN'),
            self.PAK: _('PAK'),
            self.PAN: _('PAN'),
            self.PCN: _('PCN'),
            self.PER: _('PER'),
            self.PHL: _('PHL'),
            self.PLW: _('PLW'),
            self.PNG: _('PNG'),
            self.POL: _('POL'),
            self.PRI: _('PRI'),
            self.PRK: _('PRK'),
            self.PRT: _('PRT'),
            self.PRY: _('PRY'),
            self.PSE: _('PSE'),
            self.PYF: _('PYF'),
            self.QAT: _('QAT'),
            self.REU: _('REU'),
            self.ROU: _('ROU'),
            self.RUS: _('RUS'),
            self.RWA: _('RWA'),
            self.SAU: _('SAU'),
            self.SDN: _('SDN'),
            self.SEN: _('SEN'),
            self.SGP: _('SGP'),
            self.SGS: _('SGS'),
            self.SHN: _('SHN'),
            self.SJM: _('SJM'),
            self.SLB: _('SLB'),
            self.SLE: _('SLE'),
            self.SLV: _('SLV'),
            self.SMR: _('SMR'),
            self.SOM: _('SOM'),
            self.SPM: _('SPM'),
            self.SRB: _('SRB'),
            self.STP: _('STP'),
            self.SUR: _('SUR'),
            self.SVK: _('SVK'),
            self.SVN: _('SVN'),
            self.SWE: _('SWE'),
            self.SWZ: _('SWZ'),
            self.SYC: _('SYC'),
            self.SYR: _('SYR'),
            self.TCA: _('TCA'),
            self.TCD: _('TCD'),
            self.TGO: _('TGO'),
            self.THA: _('THA'),
            self.TJK: _('TJK'),
            self.TKL: _('TKL'),
            self.TKM: _('TKM'),
            self.TLS: _('TLS'),
            self.TON: _('TON'),
            self.TTO: _('TTO'),
            self.TUN: _('TUN'),
            self.TUR: _('TUR'),
            self.TUV: _('TUV'),
            self.TWN: _('TWN'),
            self.TZA: _('TZA'),
            self.UGA: _('UGA'),
            self.UKR: _('UKR'),
            self.UMI: _('UMI'),
            self.URY: _('URY'),
            self.USA: _('USA'),
            self.UZB: _('UZB'),
            self.VAT: _('VAT'),
            self.VCT: _('VCT'),
            self.VEN: _('VEN'),
            self.VGB: _('VGB'),
            self.VIR: _('VIR'),
            self.VNM: _('VNM'),
            self.VUT: _('VUT'),
            self.WLF: _('WLF'),
            self.WSM: _('WSM'),
            self.YEM: _('YEM'),
            self.ZAF: _('ZAF'),
            self.ZMB: _('ZMB'),
            self.ZWE: _('ZWE'),
        }

    @property
    def iteratable(self):
        return self.list.items()