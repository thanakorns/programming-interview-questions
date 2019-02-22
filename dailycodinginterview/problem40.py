def find_unique(arr):
    bit_arr = [0] * 32
    for num in range(arr):
        for i in range(32):
            bit = num >> i & 1
            bit_arr[i] = (bit_arr[i] + bit) % 3

    result = 0
    for i, bit in enumerate(bit_arr):
        if bit:
            result += 2 ** i

    return result
