import pandas as pd

# Load the dataset
file_path = '/mnt/data/hotel_bookings.csv'
hotel_data = pd.read_csv(file_path)

# Display the first few rows of the dataset and its general information to understand its structure
hotel_data.head(), hotel_data.info(), hotel_data.describe(include='all')
