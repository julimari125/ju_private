class FizzBuzz:
 def convert(self, input):
  if input % 15 == 0: 
    return 'FizzBuzz'
  elif input % 3 == 0: 
    return 'Fizz'
  elif input % 5 == 0: return 'Buzz'
  else:
    return input