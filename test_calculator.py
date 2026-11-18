from calculator import add, subtract, multiply, divide, circle_area

def test_add():
	assert add(2,3) == 5

def test_divide():
	assert divide(6,2) == 3

def test_subtract():
        assert subtract(5,3) == 2

def test_multiply():
        assert multiply(4,3) == 12

def test_division_decimal():
	#Arrange
	a, b = 5, 2
	#Act
	result = divide(a, b)
	#Assert
	assert result == 2.5

def test_circle_area():
	#Arrange
	a = -4
	#Act
	result = circle_area(a)
	#Assert
	assert result == "Error"
