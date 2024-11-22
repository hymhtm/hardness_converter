class OutOfRangeError(Exception):
  """
  Exception raised for errors in the input.

  """
  def __init__(self, message='数値が範囲外です'):
    self.message = message
    super().__init__(self.message)

class NoUnitError(Exception):
  """
  Exception raised for errors in the input.

  """
  def __init__(self, message='単位がありません'):
    self.message = message
    super().__init__(self.message)