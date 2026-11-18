# SCCM4910 lab project - a four operation calculator

def add(a, b):
	return a + b

def subtract(a, b):
	return a - b

def multiply(a, b):
	return a + b

def divide(a, b):
	return a / b

def circle_area(r):
	if r >= 0:
		return 3.14 * (r ** 2)
	else:
		return "Error"

def main():
	while True:
		a = float(input("First number: "))
		op = input("Operator (+ - * /): ")
		b = float(input("Second number: "))
		match op:
			case "+":
				print("Result: ", add(a, b))
			case "-":
				print("Result: ", subtract(a, b))
			case "*":
				print("Result: ", multiply(a, b))
			case "/":
				print("Result: ", divide(a, b))
			case _:
				print("Operator not recognised: ", op)

if __name__ == "__main__":
	main()

