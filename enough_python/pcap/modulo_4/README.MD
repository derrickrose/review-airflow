# miscelaneo (divers)

## generadores, iteradores, cierres

## sistema de archivos, arbol de directorios y archivos

## modulos seleccionados de la biblioteca estandar de Python (os, datetime, time y calendar)

# 📅 Datetime Format Directives Cheat Sheet

This document lists common `strftime` (`%`) directives for formatting and parsing dates and times.

---

## 📆 Weekday

| Directive | Meaning                                   | Example (en_US)   | Example (de_DE)    |
|-----------|-------------------------------------------|-------------------|--------------------|
| **%a**    | Abbreviated weekday name                  | Sun, Mon, …, Sat  | So, Mo, …, Sa      |
| **%A**    | Full weekday name                         | Sunday, Monday, … | Sonntag, Montag, … |
| **%w**    | Weekday as decimal (0=Sunday, 6=Saturday) | 0–6               | 0–6                |

---

## 📅 Day, Month, Year

| Directive | Meaning                            | Example (en_US)   | Example (de_DE)  |
|-----------|------------------------------------|-------------------|------------------|
| **%d**    | Day of month (zero-padded)         | 01–31             | 01–31            |
| **%b**    | Abbreviated month name             | Jan, Feb, …       | Jan, Feb, …, Dez |
| **%B**    | Full month name                    | January, February | Januar, Februar  |
| **%m**    | Month as zero-padded number        | 01–12             | 01–12            |
| **%y**    | Year without century (zero-padded) | 00–99             | 00–99            |
| **%Y**    | Year with century                  | 0001–9999         | 0001–9999        |

---

## ⏰ Time

| Directive | Meaning                     | Example                        |
|-----------|-----------------------------|--------------------------------|
| **%H**    | Hour (24-hour, zero-padded) | 00–23                          |
| **%I**    | Hour (12-hour, zero-padded) | 01–12                          |
| **%p**    | AM/PM                       | AM, PM (en_US); am, pm (de_DE) |
| **%M**    | Minute (zero-padded)        | 00–59                          |
| **%S**    | Second (zero-padded)        | 00–59                          |
| **%f**    | Microsecond (zero-padded)   | 000000–999999                  |

---

## 🌍 Timezones

| Directive | Meaning                           | Example             |
|-----------|-----------------------------------|---------------------|
| **%z**    | UTC offset ±HHMM\[SS\[.ffffff\]\] | +0000, -0400, +1030 |
| **%:z**   | UTC offset ±HH:MM[:SS[.ffffff]]   | +00:00, -04:00      |
| **%Z**    | Time zone name                    | UTC, GMT, CET       |

---

## 📖 Day of Year & Week Numbers

| Directive | Meaning                                           | Example   |
|-----------|---------------------------------------------------|-----------|
| **%j**    | Day of year (zero-padded)                         | 001–366   |
| **%U**    | Week number (Sunday first)                        | 00–53     |
| **%W**    | Week number (Monday first)                        | 00–53     |
| **%u**    | ISO weekday (1=Monday, 7=Sunday)                  | 1–7       |
| **%V**    | ISO week number (Monday first, week 01 has Jan 4) | 01–53     |
| **%G**    | ISO year (with century)                           | 0001–9999 |

---

## 📑 Locale-Specific Representations

| Directive | Meaning       | Example (en_US)          | Example (de_DE)         |
|-----------|---------------|--------------------------|-------------------------|
| **%c**    | Date and time | Tue Aug 16 21:30:00 1988 | Di 16 Aug 21:30:00 1988 |
| **%x**    | Date          | 08/16/1988               | 16.08.1988              |
| **%X**    | Time          | 21:30:00                 | 21:30:00                |

---

## 🔣 Special

| Directive | Meaning     | Example |
|-----------|-------------|---------|
| **%%**    | Literal `%` | %       |

---

## 🐍 Python Example

```python
from datetime import datetime

now = datetime.now()

print(now.strftime("%A, %d %B %Y"))   # Monday, 03 October 2025
print(now.strftime("%c"))             # Locale date and time
print(now.strftime("%I:%M %p"))       # 09:15 PM style
print(now.strftime("ISO Week: %G-W%V-%u"))
```

# library standard for calendar

https://docs.python.org/3/library/calendar.html)