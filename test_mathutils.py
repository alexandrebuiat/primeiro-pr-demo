from mathutils import is_prime, fibonacci


def test_is_prime_true_for_primes():
    assert is_prime(2)
    assert is_prime(3)
    assert is_prime(7)
    assert is_prime(13)


def test_is_prime_false_for_non_primes():
    assert not is_prime(0)
    assert not is_prime(1)
    assert not is_prime(4)
    assert not is_prime(9)


def test_is_prime_false_for_negative_numbers():
    assert not is_prime(-5)


def test_fibonacci_sequence():
    assert fibonacci(0) == []
    assert fibonacci(1) == [0]
    assert fibonacci(5) == [0, 1, 1, 2, 3]
    assert fibonacci(8) == [0, 1, 1, 2, 3, 5, 8, 13]
