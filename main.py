# Built-in imports
def reverse(text):
  """
  text: string
  return: boolean

  function reverse string
  
  
  """
  
  if len(text)>0:
    return reverse(text[1:]) + text[0]
  else: 
    return ''


def is_palindrome(whatever):
  """
  
  whatever: string
  return: boolean

  True if palindrome
  """
  if len(whatever) <= 1:
    return True
    
  if len(whatever) > 0:
    if whatever[0].lower == whatever[-1].lower:
      return is_palindrome(whatever[1:-1]) 
    else:
      return False
  