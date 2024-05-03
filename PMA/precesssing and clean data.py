import pandas as pd

# load the data set (hotel_bookings.csv)
file_path = './hotel_bookings.csv'
hotel_data = pd.read_csv(file_path)


# Processing missing value
# After checking the data, we found that the "children" column has 4 missing values, "country" column has 488 missing values.

# replace missing values in "children" column with 0
hotel_data['children'] = hotel_data['children'].fillna(0)
# replace missing values in "country" column with "not known"
hotel_data['country'] = hotel_data['country'].fillna('not known')  

# After checking the data, we found that the "agent" column has 16340 missing values, "company" column has 112593 missing values.
# Too many missing values in the "agent" and "company" columns, so we decided to delete these two columns.
hotel_data.drop(columns=['agent', 'company'], inplace=True)  



# convert data type
hotel_data['reservation_status_date'] = pd.to_datetime(hotel_data['reservation_status_date'])  # convert reservation_status_date to datetime type
# combine year, month, and day columns to create a new column "arrival_date_full"
hotel_data['arrival_date_full'] = pd.to_datetime(hotel_data['arrival_date_year'].astype(str) + '-' +
                                                 hotel_data['arrival_date_month'] + '-' +
                                                 hotel_data['arrival_date_day_of_month'].astype(str))



# circumstance value processing
# 1 negative adr value, convert it to positive.
hotel_data['adr'] = hotel_data['adr'].apply(abs)  

# Delete the records with 0 guests (adults, children, and babies). We regard these records as invalid or not existing booking information.
valid_guests = (hotel_data['adults'] != 0) | (hotel_data['children'] != 0) | (hotel_data['babies'] != 0)
hotel_data = hotel_data[valid_guests]

# Delete duplicate records
hotel_data = hotel_data.drop_duplicates()


hotel_data.drop(columns=['arrival_date_year', 'arrival_date_month', 'arrival_date_day_of_month'], inplace=True)

# save the cleaned data to a new csv file
cleaned_file_path = './cleaned_hotel_bookings.csv'
hotel_data.to_csv(cleaned_file_path, index=False)
