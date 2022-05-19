from airflow.plugins_manager import AirflowPlugin

from izybe_timetable_plugin.daily import DailyTimetable


class IzybeTimetablePlugin(AirflowPlugin):
    name = "izybe_timetable_plugin"
    timetables = [DailyTimetable]

