from faker import Faker
import uuid
import pandas as pd
import random
from datetime import datetime, timedelta
import awswrangler as wr

fake = Faker()
data = []
bucket_name = "demo-03-bucket"

resolutionStatus = ["Backlog", "Blocked", "Resolved", "In-Progress", "In-Progress-Urgent"]
fake_countries = Faker(["de_DE", "fr_FR"])


def customer_care(entries=5):

    for i in range(entries):
        current_time = datetime.now()
        minutes_of_calls = random.randint(1, 30)

        data_entry = {
            "call_id": str(uuid.uuid4()),
            "customer_id": str(uuid.uuid1()),
            "first_name": fake_countries.first_name(),
            "last_name": fake_countries.last_name(),
            "age": fake.random_int(min=20, max=80),
            "job": fake.job(),
            "Email": fake.email(),
            "phone_number": fake_countries.phone_number(),
            "country_code": fake_countries.current_country_code(),
            "address": fake_countries.address(),
            "agent_id": random.randint(1,10_000),
            "resolution_status": random.choice(resolutionStatus),
            "start_time": current_time,
            "end_call": current_time + timedelta(minutes=minutes_of_calls)
        }

        data.append(data_entry)

        today = datetime.now().strftime('%Y-%m-%d')
        s3_path = f"s3://{bucket_name}/raw_data/test/{"customer_care"}_{today}.parquet"

    df=pd.DataFrame(data)
    wr.s3.to_parquet(
        df=df,
        path=s3_path,
        )

    print(f"Uploaded to {s3_path}")
    return "Loaded Successfully"
