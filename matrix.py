class Matrix:
  val = [[]]
  width = None
  height = None

  # Private Methods:
  def __scalar_mult(self, s): # Functionality for Multiplying a Scalar and a Matrix
    return_val = [[0 for _ in range(self.width)] for _ in range(self.height)]
    for i in range(self.height):
      for j in range(self.width):
        return_val[i][j] = s*self.val[i][j]
    return Matrix(return_val)
  
  def __matrix_mult(self, m): # Functionality for Multiplying Matrices
    if(self.width != m.height):
      raise Exception("The width of the source matrix must equal the height of the multiplicative matrix")
    return_val = [[0 for _ in range(m.width)] for _ in range(self.height)]
    for i in range(len(return_val)):
      for j in range(len(return_val[i])):
        temp = 0
        for k in range(self.width):
          temp += self.val[i][k]*m.val[k][j]
        return_val[i][j] = temp
    return Matrix(return_val)
  
  # Public Methods
  def transpose(self): # Transpose the Matrix
    return_val = [[0 for _ in range(self.height)] for _ in range(self.width)]
    for i in range(self.height):
      for j in range(self.width):
        return_val[j][i] = self.val[i][j]
    return Matrix(return_val)
  
  def inverse(self): # Inverse a Matrix; In Progress
    if(self.width != self.height):
      raise Exception("The matrix must be square")
    
  def del_row(self, row): # Delete a Row
    return_val = [[0 for _ in range(self.width)] for _ in range(self.height)]
    for i in range(self.height):
      for j in range(self.width):
        return_val[i][j] = self.val[i][j]
    return_val.pop(row)
    return Matrix(return_val)
  
  def del_col(self, col): # Delete a Column
    return_val = [[0 for _ in range(self.width)] for _ in range(self.height)]
    for i in range(self.height):
      for j in range(self.width):
        return_val[i][j] = self.val[i][j]
    for i in range(self.height):
      return_val[i].pop(col)
    return Matrix(return_val)
  
  def del_cr_index(self, row, col): # Delete a Column and Row Given an Intersection Coordinate
    return_val = [[0 for _ in range(self.width)] for _ in range(self.height)]
    for i in range(self.height):
      for j in range(self.width):
        return_val[i][j] = self.val[i][j]
    for i in range(self.height):
      return_val[i].pop(col)
    return_val.pop(row)
    return Matrix(return_val)
  
  # Magic Methods
  def __init__(self, val): # Initiate the Matrix Object: Matrix([[]])
    self.height = len(val)
    self.width = len(val[0])
    for i in range(self.height):
      if(len(val[i]) != self.width):
        raise Exception("All rows must be of the same width")
    self.val = val

  def __add__(self, m): # Add Two Matrices Together: M1 + M2
    if(self.width != m.width or self.height != m.height):
      raise Exception("Can not add two matrices of different dimensions")
    return_val = [[0 for _ in range(self.width)] for _ in range(self.height)]
    for i in range(self.height):
      for j in range(self.width):
        return_val[i][j] = self.val[i][j] + m.val[i][j]
    return Matrix(return_val)
  
  def __mul__(self, o): # Perform Standard Matrix Multiplication: M1 * M2, s * M
    if(type(o) == type(self)):
      return self.__matrix_mult(o)
    return self.__scalar_mult(o)
  
  def __rmul__(self, s): # Add Scalar Multiplication Functionality for the Right Side: M * s
    return self.__scalar_mult(s)
  
  def __lshift__(self, m): # Perform the Hadamard Product (Naive Matrix Multiplication): M1 << M2
    if(self.height != m.height or self.width != m.width):
      raise Exception("Can not perform the Hadamard Product on matrices of inequal dimensions")
    return_val = [[0 for _ in range(self.width)] for _ in range(self.height)]
    for i in range(self.height):
      for j in range(self.width):
        return_val[i][j] = self.val[i][j]*m.val[i][j]
    return Matrix(return_val)
