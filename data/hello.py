# result=10/0
# print(result)
try:
    result = 10 / 0
    print(result)
except ZeroDivisionError:
    print("Error: Cannot divide by zero!")
else:
    print("Division successful,result:",result)
finally:
    print("This block always executes, cleaning up resources if needed.")

    