#!/usr/bin/python3
import struct


def u64(x):
    return struct.unpack("<Q", x)[0]


def read_bit(b, n):
    return 1 if (b[n // 8] & (1 << (n % 8))) != 0 else 0


def write_bit(b, n, i):
    b[n // 8] |= (b[n // 8] | ((1 if i != 0 else 0) << (n % 8)))


def decode(src, dst):
    src_curr = 0
    src_end = len(src) * 8

    dst_curr = 0
    run_length_log = 0
    run_length = 0

    while src_curr < src_end:
        run_length_log = 0
        while True:
            if src_curr >= src_end:
                return
            bit = read_bit(src, src_curr)
            src_curr += 1
            run_length_log += 1
            if not bit:
                break
        run_length = 0
        for i in range(run_length_log - 1):
            run_length |= (read_bit(src, src_curr) << i)
            src_curr += 1
        run_length |= (read_bit(src, src_curr) << (run_length_log - 1))
        src_curr += 1
        for _ in range(run_length):
            write_bit(dst, dst_curr, 0)
            dst_curr += 1
        write_bit(dst, dst_curr, 1)
        dst_curr += 1


if __name__ == "__main__":
    with open("flag.enc", "rb") as f:
        data = f.read()

    file_size = u64(data[:8]) // 8
    src = list(data[8:])

    res = [0 for _ in range(file_size)]

    decode(src, res)

    with open("flag", "wb") as f:
        f.write(bytes(res))
