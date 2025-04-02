import numpy as np

if __name__ == '__main__':

    # variant
    k = 31
    a = np.array([
        [2 + k, -3, 1],
        [4, -5 + k, 2],
        [5, -7, 3 + k]
    ])
    b = np.array([
        [4 - k, -1, -2],
        [2, 1 - k, 3],
        [-3, -2, 0 - k]
    ])

    # -A + 2 * B
    minus_a_plus_2_b = -a + 2 * b
    print('-A + 2 * B:\n', minus_a_plus_2_b)

    # AA
    a_squared = a ** 2
    print('\nAA:\n', a_squared)

    # A * B
    a_multiply_b = np.dot(a, b)
    print('\nA * B:\n', a_multiply_b)

    # (exp(A) – exp(-A)) / (exp(A) + exp(-A))
    manual_tanh_a = (np.exp(a) - np.exp(-a)) / (np.exp(a) + np.exp(-a))
    tanh_a = np.tanh(a)
    print('\n(exp(A) – exp(-A)) / (exp(A) + exp(-A)):\n', manual_tanh_a)
    print('\nHyperbolic tangent:\n', tanh_a)

    # Sum of Abs of A
    sum_abs_a = np.sum(np.abs(a))
    print('\nSum of Abs of A:\n', sum_abs_a)

    # Sum of Abs of B
    sum_abs_b = np.sum(np.abs(b))
    print('\nSum of Abs of B:\n', sum_abs_b)