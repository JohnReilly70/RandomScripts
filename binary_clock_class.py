from datetime import datetime
import unicornhat as UH
import time


class binary_clock():
    """
    Binary Clock class provides all the functions required to create a 6 bit binary clock on a UnicornHat
    """


    @staticmethod
    def dec_to_bin_nbit(decimal_num, nbits):
        """
        A method to convert any decimal number to a binary number with the desired number of bits

        :param decimal_num: number which you wish to convert to binary
        :param nbits: number of bits you wish to represent your number
        """
        try:
            if decimal_num > 2**nbits:
                raise ValueError
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
        except ValueError:
            print("ERROR OCCURRED: {} bits cannot represent the number {}, number of required bits is {}".format(nbits,decimal_num,decimal_num.bit_length()))

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

    def time_to_binary(self):
        """
        Method which uses the datetime method to get the current time and break it into hours,minutes,seconds converted to binary value.

        clock_time is a tuple with all the time info
        """

        time_now = datetime.now().time()
        hours = self.dec_to_bin_nbit(time_now.hour, 6)
        mins = self.dec_to_bin_nbit(time_now.minute, 6)
        secs = self.dec_to_bin_nbit(time_now.second, 6)
        self.clock_time = hours, mins, secs

    def clock_mapping(self):
        """
        clock_mapping takes the clock_time and breaks it into 3 separate lines one for each item (hours,minutes,seconds)

        pixels are offset by one on the X-axis to allow a key to the left to allow uses to recognise what each line is
        """

        self.time_to_binary()
        for y in range(3):
            for x in range(0, 6):
                if int(self.clock_time[y][x]) == 1:
                    UH.set_pixel(x + 1, y, 255, 255, 255)
                else:
                    UH.set_pixel(x + 1, y, 0, 0, 0)
        UH.show()

    def start_clock(self):
        """
        start_clock method does what it says on the time, sets up the clock key first and then continually updates the time
        every 1 seconds.

        To stop programming running simple press Ctrl+C.

        NOTE: Worst case this clock will be one second out of sync, as datetime is run every second
        """

        print("6 Bit Binary Clock for UnicornHat")
        print("Red: Hour, Green: Minute, Blue: Second ")
        print("Ctrl+C to stop the program")
        UH.brightness(0.75)
        UH.set_pixel(0, 0, 255, 0, 0)
        UH.set_pixel(0, 1, 0, 255, 0)
        UH.set_pixel(0, 2, 0, 0, 255)
        while True:
            try:
                self.clock_mapping()
                time.sleep(1)
            except KeyboardInterrupt:
                print("\nProgram Stopped")
                UH.clear()
                break


clock = binary_clock()
clock.start_clock()