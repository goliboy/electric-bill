import sys

if len(sys.argv) == 2:
    script_name = sys.argv[0]
    units = float(sys.argv[1])
    print("User provided input value:")
else:
    script_name = sys.argv[0]
    units = 100.0     
    print("No input given — using default value:")


rate = 5


bill_amount = units * rate


print("\n--- Electricity Bill Calculation ---")
print("Script Name:", script_name)
print("Units Consumed:", units)
print("Rate per Unit: rs", rate)
print("Total Bill Amount: rs", bill_amount)
