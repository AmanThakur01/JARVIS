is_english = 0
is_hindi = 0
if is_english and is_hindi:
    print("Can speak english , hindi or both.")
elif is_english and not( is_hindi):
    print("Can speak english only")
elif not(is_english) and is_hindi:
    print("Can only speak hindi.")
else:
    print("cannot able to speak both.")


