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

