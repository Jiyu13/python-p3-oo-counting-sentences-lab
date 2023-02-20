#!/usr/bin/env python3

class MyString:
  
  def __init__(self, value=""):
    self._value = value


  def get_value(self):
    return self._value

  
  def set_value(self, string):
    if type(string) == str:
      self._value = string
    else:
      print("The value must be a string.")


  value = property(get_value, set_value)


  # define instance method
  def is_sentence(self):
    return self._value.endswith(".")


  # define instance method
  def is_question(self):
    return  self._value.endswith("?")


  # define instance method
  def is_exclamation(self):
    return self._value.endswith("!")


  # define instance method
  def count_sentences(self):
    value = self.value
    for mark in ["?", "!"]:
      value = value.replace(mark, ".")
    
    sentences = [sentence for sentence in value.split(".") if sentence]

    return len(sentences)
