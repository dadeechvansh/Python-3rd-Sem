# attendance = []   

# print("Enter attendance for 30 days (P/A):")

# for i in range(30):
#     val = input(f"Day {i+1}: ").upper()
#     if val == "P" or val == "A":
#         attendance.append(val)
#     else:
#         print("Invalid! Marking A")
#         attendance.append("A")
# totalp = attendance.count("P")
# totala = attendance.count("A")
# streak = 0
# maxstreak = 0

# for day in attendance:
#     if day == "P":
#         streak += 1
#         if streak > maxstreak:
#             maxstreak = streak
#     else:
#         streak = 0
# attendancetuple = tuple(attendance)
# uniquevalues = set(attendance)
# if totalp == 25:
#     status = "Excellent"
# elif 20 <= totalp < 25:
#     status = "Good"
# else:
#     status = "Needs Improvement"
# print("\n----- Monthly Attendance Summary -----")
# print("Attendance List:", attendance)
# print("Total Present:", totalp)
# print("Total Absent:", totala)
# print("Longest Present Streak:", maxstreak)
# print("Attendance Tuple:", attendancetuple)
# print("Unique Values:", uniquevalues)
# print("Performance:", status)


def predict(balance, deposit):
    balances = []

    for m in range(12):

        balance += deposit               
        interest = balance * 0.02        
        balance += interest              

        balances.append(balance)

    return balances
start = float(input("Enter starting balance: "))
deposit = float(input("Enter monthly deposit: "))
balances = predict(start, deposit)
highest = max(balances)
lowest = min(balances)
average = sum(balances) / len(balances)
growthpercent = ((balances[-1] - start) / start) * 100
print("\n----- Savings Summary -----")
print("Month-wise Balances:", balances)
print("Highest Balance:", highest)
print("Lowest Balance:", lowest)
print("Average Balance:", average)
print("Growth Percentage:", growthpercent, "%")
