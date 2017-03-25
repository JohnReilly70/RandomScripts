from datetime import datetime
import unicornhat as UH
import time


def dec_to_bin_nbit(decimal_num, nbits):
    binary = []
    for bit in range(0, nbits):
        temp_value = decimal_num % 2
        binary.append(int(temp_value))
        if temp_value == 1:
            decimal_num = (decimal_num - 1) / 2
        else:
            decimal_num = decimal_num / 2

    binary = "".join(str(bit) for bit in binary[::-1])
    return binary


def time_to_binary():
    time_now = datetime.now().time()
    hours = dec_to_bin_nbit(time_now.hour, 6)
    mins = dec_to_bin_nbit(time_now.minute, 6)
    secs = dec_to_bin_nbit(time_now.second, 6)
    return hours, mins, secs


def main():
    binary_time = time_to_binary()
    for y in range(3):
        for x in range(0,6):
            if int(binary_time[y][x]) == 1:
                UH.set_pixel(x+1, y, 255, 255, 255)
            else:
                UH.set_pixel(x+1, y, 0, 0, 0)
    UH.show()


if __name__ == "__main__":
    print("6 Bit Binary Clock for UnicornHat")
    print("Red: Hour, Green: Minute, Blue: Second ")
    print("Ctrl+C to stop the program")
    UH.brightness(0.75)
    UH.set_pixel(0, 0, 255, 0, 0)
    UH.set_pixel(0, 1, 0, 255, 0)
    UH.set_pixel(0, 2, 0, 0, 255)
    while True:
        try:
            main()
            time.sleep(1)
        except KeyboardInterrupt:
            print("\nProgram Stopped")
            UH.clear()
            break