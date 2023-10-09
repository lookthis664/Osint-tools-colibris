from datetime import datetime, timedelta

def get_remaining_days():
    start_date = datetime(2023, 9, 29)  # Remplacez par la date de début réelle
    trial_duration = timedelta(days=30)  # Remplacez par la durée réelle de l'essai
    end_date = start_date + trial_duration
    remaining_days = (end_date - datetime.now()).days
    return remaining_days