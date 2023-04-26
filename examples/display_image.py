# Example of display image
import EnkPi_4in2 as epd
import time
import pics

e_paper = epd.E_paper()
e_paper.imageblack.fill(0xff)
e_paper.imagered.fill(0x00)
    
e_paper.imagered.blit(pics.sb_logo , 100,50) # print sb components logo
e_paper.display(e_paper.buffer_black,e_paper.buffer_red)

e_paper.clear_screen()
print("sleep")
e_paper.sleep()


