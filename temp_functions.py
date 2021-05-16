def fahr_to_celsius(temp_fahrenheit):
  """
  The input temperature in Fahrenheit is converted to Celsius.

  Parameters
 
  temp_fahrenheit:
  Temperature in Celsius.

  Returns

  Changed to fahr_to_celsius.
  """
  
  converted_temp=(temp_fahrenheit - 32)/1.8 

  return converted_temp
  
def temp_classifier(temp_celsius):
   if temp_celsius<-2:
    return 0
   elif temp_celsius<2:
      return 1
   elif temp_celsius<15:
      return 2
   else:
      return 3