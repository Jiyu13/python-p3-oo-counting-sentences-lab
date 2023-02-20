class MyString:
    def __init__(self, value=""):
        self._value = value
        self._favorite_letter = "d"

    def get_value(self):
        return self._value

    def set_value(self, stringVal):
        if type(stringVal) == str:
            self._value = stringVal
        else:
            print("The value must be a string.")

    value = property(get_value, set_value)

    def is_sentence(self):
        return self._value.endswith(".")

    def is_question(self):
        return self._value.endswith("?")

    def is_exclamation(self):
        return self._value.endswith("!")

    def count_sentences(self):

        value = self.value
        print(value)
        # value = self.property(get_value, set_value), so it will run the getter and setter again, value: "call value"
        # value is public attribute
        # _value is protected attribute - with single underscore no matter is class attr or instance attr

        for punc in ['!', '?']:
            value = value.replace(punc, '.')

        sentences = [s for s in value.split('.') if s]

        return len(sentences)

    def get_favorite_letter(self):
        return self._favorite_letter

    def set_favorite_letter(self, letter):
        if type(letter) == str and len(letter) == 1:
            self._favorite_letter = letter.upper()
        else:
            print('Not a valid single letter')

    favorite_letter = property(get_favorite_letter, set_favorite_letter)


# 1. ============================ Initialising instance ============================
my_string = MyString("Test. Test! Test?")
# # will run __init__() first
# # => my_string = self, value = "Test. Test! Test?"
# # => self._value = (value = "Test. Test! Test?")
#
# # get value => triggers get_value() which will return self._value
print(my_string.value)     # bz it's the first time getting the value, so it will only trigger get_value()

# my_string.value          # Property value of count_sentences.MyString, def get_value(self) -> str, Accessor kind: Getter
# my_string._value         # Instance attribute _value of count_sentences.MyString, _value: str = value. protected member
# my_string.get_value()    # trigger get_value()


# 2. ============================ Setting value =======================================
my_string.value = "Change test. Change test! Change test?"
# set value => triggers set_value(), saves stringVal = "Change test. Change test! Change test?" to self._value
# value here means value = property(get_value, set_value)
# Property value of count_sentences.MyString, def set_value(self, stringVal: Any) -> None, Accessor kind: Setter

print("line 73: ", my_string.value)
# get value after setting, => triggers get_value() which will return self._value which is stringVal
# Property value of count_sentences.MyString, def get_value(self) -> str, Accessor kind: Getter


# ===========================================================================
# my_string.set_value("call setter")  # call setter
# my_string.value                     # call getter

# my_string.value = "call value"      # call setter
# my_string.value                     # call getter

# These two are the same
# ==========================================================================


# ====================================================================================
my_string.value = "Call count_sentence(). What will be returned? I don't know!"
# now value = "Call count_sentence(). What will be returned? I don't know!"
my_string.count_sentences()

print("line 94: ", my_string.value)
print("line 95: ", my_string._value)

# self.value => value = property(get_value, set_value) => main variable
# self._value is where you save the result of self.set_value => hidden variable
# self.value returns self._value
# work with hidden variable _value inside the class

# when call instance.value = "......", it would run set_value again
# the hidden value _value is where you save the result,
# users use value, but self.value has nothing in it, self._value is where the real value is
# if it's getting the value, it runs get_value (which returns whatever's in self._value)
# if it's setting the value, it performs some logic then saves the result to self._value
#  ========================================================================================

# print(my_string.favorite_letter)        # default value => "d"
# my_string.set_favorite_letter(2)        # Not a valid single letter
#
# my_string.favorite_letter = "p"
# print(my_string.favorite_letter)        # set value to "p"
#
# print(my_string.get_favorite_letter)
# <bound method MyString.get_favorite_letter of <__main__.MyString object at 0x000002156EC90EB0>>
