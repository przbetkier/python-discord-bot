import csv
import datetime


async def remind(client):
    lines = list()
    rows_to_remove = []

    with open('reminders.csv', 'r') as file:
        reader = csv.DictReader(file)
        now = datetime.datetime.now()
        for row_number, row in enumerate(reader, start=1):
            remind_at = datetime.datetime.fromtimestamp(int(row['time']))
            if now > remind_at:
                channel_id = int(row['channel'])
                channel = client.get_channel(channel_id)
                await channel.send('Hey, {0}! Friendly reminder: _{1}_ 📅 '.format(row['user'], row['reminder']))
                rows_to_remove.append(row_number)
            else:
                lines.append(row)

    # override rows from reminders file - skip reminders sent
    if len(rows_to_remove) > 0:
        print("Sent {0} reminders, deleting from csv.".format(len(rows_to_remove)))
        with open('reminders.csv', 'w') as file:
            writer = csv.DictWriter(file, fieldnames=['user', 'reminder', 'channel', 'time'])
            writer.writeheader()
            writer.writerows(lines)
