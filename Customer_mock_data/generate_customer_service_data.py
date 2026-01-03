from faker import Faker
import uuid
import pandas as pd
import random
from datetime import datetime, timedelta

fake = Faker()
data = []

resolutionStatus = ["Backlog", "Blocked", "Resolved", "In-Progress", "In-progress_Urgent"]
fake_countries = Faker(["de_DE", "fr_FR"])
current_time = datetime.now()
minutes_of_calls = random.randint(1, 40)

def customer_care(entries=5):
    
    
    for i in range(entries):
        data_entry = {
            "call_id": uuid.uuid4(), #122 bit
            "customer_id": uuid.uuid1(), #128 bits
            "first_name": fake_countries.first_name(),
            "last_name" : fake_countries.last_name(),
            "job": fake.job(),
            "age": fake.random_int(min=20, max=85),
            "Email": fake.email(),
            "phone_number": fake_countries.phone_number(),
            "country_code": fake_countries.current_country_code(),
            "address": fake_countries.address(),
            "agent_id": random.randint(1,10_000),
            "resolution_status": random.choice(resolutionStatus),
            "current_time": current_time,
            "end_call" : current_time + timedelta(minutes=minutes_of_calls)
        
            

            
        }
        
        data.append(data_entry)
    return pd.DataFrame(data)

generic_df = customer_care(5)
print(generic_df)