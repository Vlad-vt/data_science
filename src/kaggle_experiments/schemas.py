
import pandera.pandas as pa
from pandera.typing import Series


class RawAppointmentsSchema(pa.DataFrameModel):
    patient_id: Series[float] = pa.Field(alias="PatientId")
    appointment_id: Series[int] = pa.Field(alias="AppointmentID")
    gender: Series[str] = pa.Field(alias="Gender")
    scheduled_day: Series[str] = pa.Field(alias="ScheduledDay")
    appointment_day: Series[str] = pa.Field(alias="AppointmentDay")
    age: Series[int] = pa.Field(alias="Age")
    neighbourhood: Series[str] = pa.Field(alias="Neighbourhood")
    scholarship: Series[int] = pa.Field(alias="Scholarship")
    hipertension: Series[int] = pa.Field(alias="Hipertension")
    diabetes: Series[int] = pa.Field(alias="Diabetes")
    alcoholism: Series[int] = pa.Field(alias="Alcoholism")
    handcap: Series[int] = pa.Field(alias="Handcap")
    sms_received: Series[int] = pa.Field(alias="SMS_received")
    no_show: Series[str] = pa.Field(alias="No-show")

class CleanAppointmentsSchema(pa.DataFrameModel):
    patient_id: Series[float] = pa.Field(gt=0)
    appointment_id: Series[int] = pa.Field(unique=True, gt=0)
    gender: Series[str] = pa.Field(isin=["M", "F"])
    appointment_day: Series[pa.Timestamp]
    age: Series[int] = pa.Field(ge=0, le=120)
    neighbourhood: Series[str]
    scholarship: Series[int] = pa.Field(isin=[0, 1])
    hipertension: Series[int] = pa.Field(isin=[0, 1])
    diabetes: Series[int] = pa.Field(isin=[0, 1])
    alcoholism: Series[int] = pa.Field(isin=[0, 1])
    handcap: Series[int] = pa.Field(isin=[0, 1, 2, 3, 4])
    sms_received: Series[int] = pa.Field(isin=[0, 1])
    scheduled_hour: Series[int] = pa.Field(ge=0, le=23)
    appointment_dow: Series[int] = pa.Field(ge=0, le=6)
    lead_time_days: Series[int] = pa.Field(ge=0)
    prev_appointments: Series[int] = pa.Field(ge=0)
    prev_noshows: Series[int] = pa.Field(ge=0)
    prev_noshow_rate: Series[float] = pa.Field(ge=0.0, le=1.0)
    target: Series[int] = pa.Field(isin=[0, 1])

    class Config:
        strict = True
        coerce = True