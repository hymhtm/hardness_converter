import numpy as np
from scipy.interpolate import interp1d

"""
Hardness Conversion Scale

HRC: Rorkwell
HV: Vickers
HBW: Brinells
HS: Shore

Hardness Conversion Array
"""

nan = np.nan
hardness_scales = ['HRC', 'HV', 'HBW', 'HS']
hardness_array = np.array([
  [ 68., 940.,  nan,  97.],
  [ 67., 900.,  nan,  95.],
  [ 66., 865.,  nan,  92.],
  [ 65., 832.,  nan,  91.],
  [ 64., 800.,  nan,  88.],
  [ 63., 772.,  nan,  87.],
  [ 62., 746.,  nan,  85.],
  [ 61., 720.,  nan,  83.],
  [ 60., 697.,  nan,  81.],
  [ 59., 674.,  nan,  80.],
  [ 58., 653.,  nan,  78.],
  [ 57., 633.,  nan,  76.],
  [ 56., 613.,  nan,  75.],
  [ 55., 595.,  nan,  74.],
  [ 54., 577.,  nan,  72.],
  [ 53., 560.,  nan,  71.],
  [ 52., 544., 500.,  69.],
  [ 51., 528., 487.,  68.],
  [ 50., 513., 475.,  67.],
  [ 49., 498., 464.,  66.],
  [ 48., 484., 451.,  64.],
  [ 47., 471., 442.,  63.],
  [ 46., 458., 432.,  62.],
  [ 45., 446., 421.,  60.],
  [ 44., 434., 409.,  58.],
  [ 43., 423., 400.,  57.],
  [ 42., 412., 390.,  56.],
  [ 41., 402., 381.,  55.],
  [ 40., 392., 371.,  54.],
  [ 39., 382., 362.,  52.],
  [ 38., 372., 353.,  51.],
  [ 37., 363., 344.,  50.],
  [ 36., 354., 336.,  49.],
  [ 35., 345., 327.,  48.],
  [ 34., 336., 319.,  47.],
  [ 33., 327., 311.,  46.],
  [ 32., 318., 301.,  44.],
  [ 31., 310., 294.,  43.],
  [ 30., 302., 286.,  42.],
  [ 29., 294., 279.,  41.],
  [ 28., 286., 271.,  41.],
  [ 27., 279., 264.,  40.],
  [ 26., 272., 258.,  38.],
  [ 25., 266., 253.,  38.],
  [ 24., 260., 247.,  37.],
  [ 23., 254., 243.,  36.],
  [ 22., 248., 237.,  35.],
  [ 21., 243., 231.,  35.],
  [ 20., 238., 226.,  34.],
  [ 18., 230., 219.,  33.],
  [ 16., 222., 212.,  32.],
  [ 14., 213., 203.,  31.],
  [ 12., 204., 194.,  29.],
  [ 10., 196., 187.,  28.],
  [  8., 188., 179.,  27.],
  [  6., 180., 171.,  26.],
  [  4., 173., 165.,  25.],
  [  2., 166., 158.,  24.],
  [  0., 160., 152.,  24.]
])

def convert_hardness_scale(hardness_value, source_index):
  """
  Convert Hardness scales mutually.

  Args:
    hardness_value(float): the value to convert
    source_index(int): the index of the input value
    target_index(int): the index to convert to

  Returns:
    float:the converted value

  Raises:
    OutOfRangeError: if the input value is out of range
    KeyError: if the unit is not in the data
    ValueError: if the input value is not a number

  """

  if not isinstance(hardness_value, (int, float)):
    raise ValueError("硬度は数値で入れて下さい")

  source_values = hardness_array[:, source_index]

  converted_values = {}

  for target_unit in hardness_scales:
    if target_unit == hardness_scales[source_index]:
      min_value = np.nanmin(source_values)
      max_value = np.nanmax(source_values)
      if hardness_value < min_value or hardness_value > max_value:
        converted_values[target_unit] = np.nan
      else:
        converted_values[target_unit] = hardness_value
      continue

    target_index = hardness_scales.index(target_unit)
    target_values = hardness_array[:, target_index]

    mask = ~np.isnan(source_values) & ~np.isnan(target_values)
    source_values_filtered = source_values[mask]
    target_values_filtered = target_values[mask]

    sorted_indices = np.argsort(source_values_filtered)
    source_values_filtered = source_values_filtered[sorted_indices]
    target_values_filtered = target_values_filtered[sorted_indices]

    func = interp1d(source_values_filtered, target_values_filtered, kind='linear', bounds_error=False, fill_value=np.nan)
    converted_value = func(hardness_value)
    
    if np.isnan(converted_value):
      converted_values[target_unit] = np.nan
    else:
      converted_values[target_unit] = np.round(converted_value, 2)

  return converted_values