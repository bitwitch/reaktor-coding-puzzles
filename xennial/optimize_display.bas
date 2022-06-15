
600 REM move player and draw
601 REM only draw maze if first execution
602 IF maze_drawn = 1 THEN GOTO 620
610 GOSUB 820
620 REM draw player row
621 LET p_row$ = ""
630 LET row = PEEK(1)
640 LET col = PEEK(2)
650 FOR c = 0 TO width-1
651   IF c = col THEN
652     p_row$ = p_row$ + "@"
653   ELSE
660     LET cell = PEEK(16 + row * width + c)
670     IF cell = 0 THEN p_row$ = p_row$ + " "
680     IF cell = 1 THEN p_row$ = p_row$ + "X"
681   END IF
690 NEXT c
691 LOCATE row+2, 1: PRINT p_row$

700 REM draw rows above and below player
701 LET dir = PEEK(0)
702 IF dir = 1 AND row > 1 THEN
703   LET row = row-1
704   GOSUB 1000
710 END IF
720 IF dir = 3 AND row < height-1 THEN
722   LET row = row+1
723   GOSUB 1000
724 END IF


780 REM print some statistics on top
790 LOCATE 1, 10 : PRINT "steps: "; steps
800 steps = steps + 1
810 RETURN




820 REM print maze
822 maze_drawn = 1
830 CLS
840 LOCATE 2,1 : REM top left corner of the maze
850 FOR row = 0 TO height-1
860   GOSUB 1000
970 NEXT row
980 RETURN

1000 REM draw row
1010 LET r$ = ""
1020 FOR col = 0 TO width-1
1030   LET cell = PEEK(16 + row * width + col)
1040   LET c$ = " "
1050   IF cell = 1 THEN c$ = "X"
1060   r$ = r$ + c$
1070 NEXT col
1080 LOCATE row+2, 1: PRINT r$
1090 RETURN
