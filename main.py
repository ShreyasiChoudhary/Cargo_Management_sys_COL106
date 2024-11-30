
from gcms import GCMS
from object import Color
from exceptions import NoBinFoundException
if __name__=="__main__":

    gcms = GCMS()

    gcms.add_bin(1111, 10)
    gcms.add_bin(6666, 20)
    gcms.add_bin(5555,13)
    gcms.add_bin(4444, 10)
    gcms.add_bin(3500, 15)
    gcms.add_bin(1000, 20)
    gcms.add_bin(3333, 15)
    gcms.add_bin(2222, 10)

    gcms.add_object(4839, 9, Color.YELLOW)
    gcms.add_object(8989, 6, Color.BLUE)
    gcms.add_object(2892, 14, Color.GREEN)
    gcms.add_object(7777, 9, Color.RED)
    gcms.add_object(3283, 2, Color.YELLOW)
    gcms.add_object(8983, 8, Color.GREEN)
    #gcms.delete_object(8989)
    gcms.add_object(8984, 10, Color.BLUE)
    gcms.add_object(8982, 2, Color.RED)
    #gcms.delete_object(3283)
    gcms.add_object(8666, 5, Color.RED)
    gcms.add_object(8982, 7, Color.BLUE)

    print(gcms.bin_info(1000))
    print(gcms.bin_info(1111))
    print(gcms.bin_info(2222))
    print(gcms.bin_info(3333))
    print(gcms.bin_info(3500))
    print(gcms.bin_info(4444))
    print(gcms.bin_info(5555))
    print(gcms.bin_info(6666))
    #print(gcms.object_info(2892))
    #print(gcms.object_info(8983))
