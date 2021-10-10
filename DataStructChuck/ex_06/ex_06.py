#Exercise 06_05 Convert extracted string into a floating point
text = "X-DSPAM-Confidence:    0.8475"
ipos = text.find(':')
print(ipos)
ypos = text[ipos+5:]
flpos = float(ypos)
print(ypos)
print(flpos)