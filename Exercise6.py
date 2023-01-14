# Take the following Python code stores a string
# str = 'X-DSPAM-Confidence: 0.8475'
str = 'X-DSPAM-Confidence: 0.8475'
starPos = str.find(':')
value = str[starPos+1:]
value = value.lstrip
value = float(value)
print(value)