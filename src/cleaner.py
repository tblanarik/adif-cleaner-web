from datetime import datetime
import re

def filter_adi_data(data, start_datetime, end_datetime=None, dedup=False):
    filtered_data = []
    seen_callsigns = set()
    for line in data:
        if '<CALL:' in line:
            try:
                qso_date = re.search(r'<QSO_DATE:\d+>(\d+)', line).group(1)
                time_on = re.search(r'<TIME_ON:\d+>(\d+)', line).group(1)
                qso_datetime = datetime.strptime(qso_date + time_on, '%Y%m%d%H%M%S')
                callsign = re.search(r'<CALL:\d+>(\w+)', line).group(1)
                if qso_datetime >= start_datetime and (end_datetime is None or qso_datetime <= end_datetime):
                    if dedup:
                        if callsign not in seen_callsigns:
                            filtered_data.append(line)
                            seen_callsigns.add(callsign)
                    else:
                        filtered_data.append(line)
            except (IndexError, ValueError, AttributeError) as e:
                print(f"Error parsing line: {line}\nError: {e}")
    return filtered_data

def write_cleaned_adi_file(data, original_file_path):
    cleaned_file_path = original_file_path + '.clean'
    with open(cleaned_file_path, 'w') as file:
        file.writelines(data)