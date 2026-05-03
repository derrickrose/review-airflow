# MWAA Plugins

## How to Create plugins.zip

To create a properly structured `plugins.zip` file for AWS MWAA:

```bash
cd ~/Documents/reviews/review-airflow/plugins
zip -r ../plugins.zip miketriky_daily_timetable/
```

This will create `plugins.zip` in the parent directory with the correct structure.

## Verify ZIP Structure

To verify the ZIP file is structured correctly:

```bash
unzip -l ../plugins.zip
```

Expected output:
```
Archive:  plugins.zip
  Length      Date    Time    Name
---------  ---------- -----   ----
        0  YYYY-MM-DD HH:MM   miketriky_daily_timetable/
      XXX  YYYY-MM-DD HH:MM   miketriky_daily_timetable/__init__.py
      XXX  YYYY-MM-DD HH:MM   miketriky_daily_timetable/daily.py
---------                     -------
     XXXX                     3 files
```

## Upload to S3

After creating the ZIP file, upload it to your MWAA S3 bucket:

```bash
aws s3 cp ../plugins.zip s3://your-mwaa-bucket/plugins.zip
```

MWAA will automatically detect and load the plugin within 5-10 minutes.
