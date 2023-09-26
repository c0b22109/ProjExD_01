import sys
import pygame as pg


def main():
    pg.display.set_caption("はばたけ！こうかとん")
    screen = pg.display.set_mode((800, 600))
    clock  = pg.time.Clock()
    bg_img = pg.image.load("ex01/fig/pg_bg.jpg")
    bg_img_rev = pg.transform.flip(bg_img, True, False)
    bg_img_rev_flag = True
    charactor_img = pg.image.load("ex01/fig/3.png")
    charactor_img = pg.transform.flip(charactor_img, True, False)
#    rotated_charactor_img = pg.transform.rotozoom(charactor_img, 10, 1.0)
#    img_list = [charactor_img, rotated_charactor_img]
    img_list = [pg.transform.rotozoom(charactor_img, i, 1.0) for i in range(10)]
    display_width, display_size_h = pg.display.get_surface().get_size()
    bgimg_width = bg_img.get_width()

    tmr = 0
    while True:
        for event in pg.event.get():
            if event.type == pg.QUIT: return

        x = tmr % bgimg_width
        if x == 0:
            if bg_img_rev_flag:
                bg_img_rev_flag = False
            else:
                bg_img_rev_flag = True

        if bg_img_rev_flag:
            screen.blit(bg_img_rev, [-x, 0])
            if x >= bgimg_width - display_width:
                screen.blit(bg_img, [bgimg_width - x, 0])
        else:
            screen.blit(bg_img, [-x, 0])
            if x >= bgimg_width - display_width:
                screen.blit(bg_img_rev, [bgimg_width - x, 0])

        img_list_index = tmr % (len(img_list) * 2)
        if img_list_index >= len(img_list):
            img_list_index = len(img_list) * 2 - 1 - img_list_index
        screen.blit(img_list[img_list_index], [300, 200])
        pg.display.update()
        tmr += 1        
        clock.tick(100)


if __name__ == "__main__":
    pg.init()
    main()
    pg.quit()
    sys.exit()