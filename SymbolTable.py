class TypeValue:
    def __init__(self, var_type, value=None):
        self.var_type = var_type
        self.value = value


class SymbolTable:
    def __init__(self):
        self.table = {}
        self._types = {"int": int, "string": str, "bool": bool}

    def _insert(self, symbol, var_type, value=None):
        self.table[symbol] = TypeValue(var_type, value)

    def lookup(self, symbol):
        if symbol in self.table.keys():
            print(f"Variable:[{symbol}], Type:[{self.table[symbol].var_type}], Value:[{self.table[symbol].value}]")
        else:
            print(f"Variable [{symbol}] does not exist")

    def _remove(self, symbol):
        if symbol in self.table:
            del self.table[symbol]

    def initialize(self, symbol, var_type, value=None):
        if symbol not in self.table.keys() and var_type in self._types.keys():
            if (value is not None and type(value) == self._types[var_type]) or value is None:
                self._insert(symbol, var_type, value)
        elif symbol in self.table.keys():
            print(f"Variable [{symbol}] already Initialized")
        else:
            print("Not a valid Type")

    def declare(self, symbol, value):
        if symbol in self.table.keys() and type(value) == self._types[self.table[symbol].var_type]:
            self.table[symbol] = TypeValue(self.table[symbol].var_type, value)

        else:
            print("incorrect type")

    def display(self):
        for symbol, tv in self.table.items():
            print(f"{symbol} - {tv.var_type}: {tv.value}")
