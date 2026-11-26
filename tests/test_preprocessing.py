import pandas as pd

from kaggle_experiments.preprocessing import prepare_appointments


def test_prepare_appointments_filters_anomalies_and_prevents_leakage() -> None:
    raw = pd.DataFrame(
        {
            "PatientId": [101.0, 101.0, 202.0, 303.0],
            "AppointmentID": [1, 2, 3, 4],
            "Gender": ["F", "F", "M", "M"],
            "ScheduledDay": [
                "2016-05-01T08:30:00Z",
                "2016-05-02T10:00:00Z",
                "2016-05-01T09:00:00Z",
                "2016-05-10T09:00:00Z",
            ],
            "AppointmentDay": [
                "2016-05-01T00:00:00Z",  # день в день -> lead_time_days = 0
                "2016-05-05T00:00:00Z",  # через 3 дня -> lead_time_days = 3
                "2016-05-02T00:00:00Z",  # отфильтруется из-за Age = -1
                "2016-05-05T00:00:00Z",  # отфильтруется из-за записи позже приёма
            ],
            "Age": [30, 30, -1, 45],
            "Neighbourhood": ["JARDIM CAMBURI"] * 4,
            "Scholarship": [0, 0, 0, 1],
            "Hipertension": [0, 0, 1, 0],
            "Diabetes": [0, 0, 0, 0],
            "Alcoholism": [0, 0, 0, 0],
            "Handcap": [0, 0, 0, 0],
            "SMS_received": [0, 1, 0, 1],
            "No-show": ["Yes", "No", "No", "Yes"],
        }
    )

    result = prepare_appointments(raw)

    assert len(result) == 2
    assert list(result["lead_time_days"]) == [0, 3]
    assert list(result["prev_appointments"]) == [0, 1]
    assert list(result["prev_noshows"]) == [0, 1]
    assert list(result["prev_noshow_rate"]) == [0.0, 1.0]