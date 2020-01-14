str_data = 'X-DSPAM-Confidence: 0.8475 '

colon_pos = str_data.find(':')
raw_result = str_data[colon_pos+1:]

print(raw_result.strip())
