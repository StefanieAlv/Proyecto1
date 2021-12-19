#Variables categoricas con NA
CATEGORICAL_VARS_WITH_NA_FREQUENT = []

#Variable categoricas con NA pero indicador de Missing
CATEGORICAL_VARS_WITH_NA_MISSING = []


#Variables numéricas con NA
NUMERICAL_VARS_WITH_NA = ['children']

#Variables que vamos a tirar
DROP_FEATURES = []

#Variables para binarización por sesgo fuerte
BINARIZE_VARS = []

#Variables categoricas a codificar
ART = ['assigned_room_type']
ADM = ['arrival_date_month']
MS = ['market_segment']
DC = ['distribution_channel']
Meal = ['meal']
CT = ['customer_type']
RS = ['reservation_status']
Hotel = ['hotel']
DT = ['deposit_type']
RRT = ['reserved_room_type']

#Mapeos de variables categoricas
Diccio_ART = {'A':1, 'B':2, 'C':3, 'D':4, 'E':5, 'F':6, 'G':7, 'H':8, 'I':9,'K':10, 'L':11, 'P':12, 'Missing':0, 'NA':0, 'NaN':0}
Diccio_ADM = {'April':1, 'August':2, 'December':3, 'February':4, 'January':5, 'July':6, 'June':7, 'March':8, 'May':9,'November':10, 'September':11, 'October':12, 'Missing':0, 'NA':0, 'NaN':0}
Diccio_MS = {'Aviation':1, 'Complementary':2, 'Corporate':3, 'Direct':4, 'Groups':5, 'Offline TA/TO':6, 'Online TA':7, 'Undefined':8, 'Missing':0, 'NA':0, 'NaN':0}
Diccio_DC = {'Corporate':1, 'Direct':2, 'GDS':3, 'TA/TO':4, 'Undefined':5, 'Missing':0, 'NA':0, 'NaN':0}
Diccio_Meal = {'BB':1, 'HB':2, 'Undefined':3, 'SC':4, 'FB':5, 'Missing':0, 'NA':0, 'NaN':0}
Diccio_CT = {'Contract':1, 'Group':2, 'Transient':3, 'Transient-Party':4, 'Missing':0, 'NA':0, 'NaN':0}
Diccio_RS = {'Canceled':1, 'Check-Out':2, 'No-Show':3, 'Missing':0, 'NA':0, 'NaN':0}
Diccio_Hotel = {'City Hotel':1, 'Resort Hotel':2, 'Missing':0, 'NA':0, 'NaN':0}
Diccio_DT = {'No Deposit':1, 'Non Refund':2, 'Refundable':3, 'Missing':0, 'NA':0, 'NaN':0}
Diccio_RRT = {'A':1, 'D':2, 'E':3, 'G':4, 'C':5, 'F':6, 'B':7, 'H':8, 'L':9, 'P':10, 'Missing':0, 'NA':0, 'NaN':0}

#Variables seleccionadas según análisis de Lasso
FEATURES = ['hotel', 'is_canceled', 'lead_time', 'arrival_date_month','stays_in_weekend_nights', 
            'stays_in_week_nights', 'adults', 'children', 'babies', 'meal', 
            'market_segment', 'distribution_channel', 'is_repeated_guest', 
            'previous_cancellations', 'previous_bookings_not_canceled', 
            'reserved_room_type', 'assigned_room_type', 'booking_changes', 'deposit_type',
            'days_in_waiting_list', 'customer_type', 'required_car_parking_spaces', 
            'total_of_special_requests', 'reservation_status']