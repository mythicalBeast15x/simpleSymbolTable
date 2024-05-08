from SymbolTable import SymbolTable
#Defining Symbol Table
symbol_table = SymbolTable()

# Tests
# initialize + declare
symbol_table.initialize("x","int")
symbol_table.declare("x",10)

# initialize with value
symbol_table.initialize("y","int", 5)

# initializing variable types with values
symbol_table.initialize("z","string", "This is a string")

# Demonstrating variable name checking
symbol_table.initialize("z","bool", True)
symbol_table.initialize("a","bool", True)

# Demonstrating Type Checking
symbol_table.initialize("b","bool", "True")

# Demonstrating lookup
symbol_table.lookup("x")
symbol_table.initialize("c","string")
symbol_table.lookup("c")
symbol_table.lookup("kraken")
print()
# Demonstrating Display
symbol_table.display()

symbol_table.declare("z", "Is this an int?")
symbol_table.declare("a", False)
symbol_table.declare("x", 3)

print("\nAfter Changes:")
symbol_table.display()
