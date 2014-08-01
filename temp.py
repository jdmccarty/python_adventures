##converts celsius temperature to fahrenheit or vice versa

system = raw_input('Are you are STARTING with fahrenheit or celsius: ')
s = system[0]
if s.lower() == 'f':
   f = int(raw_input('Enter your starting fahrenheit integer '))
   c = (f - 32) * 5/9
   print str(c) + ' degrees celsius'
elif s.lower() == 'c':
   c = int(raw_input('Enter your starting celsius integer '))
   f = (c * 9/5) +32
   print str(f) + ' degrees fahrenheit'
else:
   print 'There was a problem, please try again!'
