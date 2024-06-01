import streamlit as st
from faker import Faker
import random
import pandas as pd

fake = Faker()

# Function to generate synthetic data
def generate_synthetic_data(num_rows):
    user_ids = list(range(1, num_rows + 1))  # Generate ascending user IDs
    data = {
        'UserID': user_ids,
        'Name 👤': [fake.name() for _ in range(num_rows)],
        'Address 🏠': [fake.address() for _ in range(num_rows)],
        'Email 📧': [fake.email() for _ in range(num_rows)],
        'Phone Number 📞': [fake.phone_number() for _ in range(num_rows)],
        'Company 🏢': [fake.company() for _ in range(num_rows)],
        'Job Title 💼': [fake.job() for _ in range(num_rows)],
        'Birth Date 🎉': [fake.date_of_birth(minimum_age=18, maximum_age=70) for _ in range(num_rows)],
        'Salary 💰': [round(random.uniform(30000, 150000), 2) for _ in range(num_rows)],
        'Age 🎂': [random.randint(18, 70) for _ in range(num_rows)],
        'Gender ⚧️': [random.choice(['Male', 'Female', 'Other']) for _ in range(num_rows)],
        'Country 🌍': [fake.country() for _ in range(num_rows)],
        'Credit Card Number 💳': [fake.credit_card_number() for _ in range(num_rows)],
        'Credit Card Expiry 📅': [fake.credit_card_expire() for _ in range(num_rows)],
        'Credit Card Provider 🏦': [fake.credit_card_provider() for _ in range(num_rows)],
        'License Plate 🚗': [fake.license_plate() for _ in range(num_rows)],
        'Website 🌐': [fake.url() for _ in range(num_rows)],
       
    }
    return pd.DataFrame(data)

# Function to generate an inspiring message
def generate_inspiration():
    inspirations = [
        "This data holds the key to unlocking valuable insights about your target audience.",
        "By analyzing this data, you can make data-driven decisions that drive your business forward.",
        "Harness the power of this data to gain a deeper understanding of market trends and customer behavior.",
        "Don't let this data go to waste! Use it to optimize your strategies and maximize your ROI.",
        "With this data at your fingertips, you have the opportunity to gain a competitive edge in your industry.",
        "The possibilities are endless with this data. Let your imagination run wild and discover new opportunities.",
        "By leveraging this data effectively, you can uncover hidden patterns and uncover untapped potential.",
        "Take advantage of this data to gain actionable insights that drive meaningful change in your organization."
    ]
    return random.choice(inspirations)

# App title with emojis
st.title('🌟 Synthetic Data Creator 🛠️')

# Number input for rows
num_rows = st.number_input('Number of Rows 📊', min_value=1, value=10)

# Generate button
if st.button('🚀 Create and Download'):
    synthetic_data = generate_synthetic_data(num_rows)
    st.dataframe(synthetic_data)
    csv = synthetic_data.to_csv(index=False)
    st.download_button(
        label="Download CSV 📥",
        data=csv,
        file_name='synthetic_data.csv',
        mime='text/csv'
    )
    inspiration = generate_inspiration()
    st.write(f"🚀 **Inspiration:** {inspiration}")
