#!/usr/bin/env python3

class MyString:
  
  def __init__(self, value=None):
    self._value = value


  def get_value(self):
    return self._value

  
  def set_value(self, string):
    if type(string) == str:
      self._value = string
    else:
      print("The value must be a string.")


  value = property(get_value, set_value)


  def is_sentence(self):
    if self._value.endswith("."):
      return True
    else:
      return False