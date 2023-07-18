def solveTimeConversion(twelve_hour_format_time):
	if "PM" in twelve_hour_format_time:
		if twelve_hour_format_time[0:2] == "12":
			return twelve_hour_format_time[0:len(twelve_hour_format_time)  - 2]
		else:
			hour = str((24/2) + int(twelve_hour_format_time[0:2]))
			return hour + twelve_hour_format_time[2:len(twelve_hour_format_time)  - 2]
	else:
		if twelve_hour_format_time[0:2] == "12":
			return "00" + twelve_hour_format_time[2:len(twelve_hour_format_time)  - 2]
		else:
			return twelve_hour_format_time[0:len(twelve_hour_format_time)  - 2]
print(solveTimeConversion("11:05:37PM"))