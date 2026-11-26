import pandas as pd
import pandera.pandas as pa
from pandera.typing import DataFrame
from pydantic.alias_generators import to_snake

from kaggle_experiments.schemas import CleanAppointmentsSchema, RawAppointmentsSchema


@pa.check_types
def prepare_appointments(
    raw_df: DataFrame[RawAppointmentsSchema],
) -> DataFrame[CleanAppointmentsSchema]:
    df = raw_df.rename(columns=lambda c: to_snake(c).replace("-", "_")).copy()

    #removing anomaly age
    df = df[df["age"] >= 0].copy()

    df["target"] = (df["no_show"] == "Yes").astype(int)

    scheduled_dt = pd.to_datetime(df["scheduled_day"]).dt.tz_localize(None)
    appointment_dt = pd.to_datetime(df["appointment_day"]).dt.tz_localize(None)

    df["scheduled_day"] = scheduled_dt
    df["appointment_day"] = appointment_dt.dt.normalize()
    df["scheduled_hour"] = scheduled_dt.dt.hour
    df["appointment_dow"] = df["appointment_day"].dt.day_of_week
    df["lead_time_days"] = (
        df["appointment_day"] - scheduled_dt.dt.normalize()
    ).dt.days

    df = df[df["lead_time_days"] >= 0].copy()

    df = df.sort_values(
        ["patient_id", "scheduled_day", "appointment_id"]
    ).reset_index(drop=True)
    df["prev_appointments"] = df.groupby("patient_id").cumcount()
    df["prev_noshows"] = (
        df.groupby("patient_id")["target"].cumsum() - df["target"]
    )
    df["prev_noshow_rate"] = (
        df["prev_noshows"] / df["prev_appointments"]
    ).fillna(0.0)

    output_cols = list(CleanAppointmentsSchema.to_schema().columns.keys())
    return df[output_cols]

