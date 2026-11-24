
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

class Config:
    strict = True