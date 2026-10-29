morning = int(input("Enter morning patient: "))
afternoon = int(input("Enter afternoon patient: "))
evening = int(input("Enter evening patient: "))

total = morning + afternoon + evening

if morning < 0 or afternoon < 0 or evening < 0:
  print("Patient count cannot be negative")
else:
  print("Total patient seen today:", total)
