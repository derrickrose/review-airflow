from airflow.plugins_manager import AirflowPlugin

from .daily import DailyTimetable


class MiketrikyDailyTimetablePlugin(AirflowPlugin):
    name = "miketriky_daily_timetable"
    timetables = [DailyTimetable]

