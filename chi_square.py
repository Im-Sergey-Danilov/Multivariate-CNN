import get_yTrue_yPred
import scipy.stats as stats
import numpy as np


def convert_strings_to_ints(str_list):
    return [int(x) for x in str_list]

expected, observed = get_yTrue_yPred.get_yTrue_yPred()
expected = np.array([convert_strings_to_ints(str_list=expected)])
observed = np.array([convert_strings_to_ints(str_list=observed)])

# print(type(expected[0]))
# print(type(observed[1]))
# print(type(expected))
# print(type(observed))
# observed = np.array([22, 23, 24, 25])
# expected = np.array([21, 22, 23, 24])
# (t, p) = stats.chisquare(observed, expected, ddof=12)
# print(t, p)
# print('Test t=%f p-value = %f' % (t, p))
# print(expected, observed)
