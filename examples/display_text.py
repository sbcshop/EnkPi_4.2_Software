# Example of display text
import EnkPi_4in2 as epd
import time

e_paper = epd.E_paper()
e_paper.imageblack.fill(0xff)
e_paper.imagered.fill(0x00)
    
e_paper.imageblack.text("SB COMPONENTS", 5, 10, 0x00)
e_paper.imagered.text("EnkPi 4.2 inch", 5, 40, 0xff)
e_paper.display(e_paper.buffer_black,e_paper.buffer_red)

e_paper.clear_screen()
print("sleep")
e_paper.sleep()


