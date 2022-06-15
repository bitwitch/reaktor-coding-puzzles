600 REM print maze
610 IF maze_drawn THEN GOTO 730
620 LET maze_drawn = 1
630 LET pr = PEEK(1) : LET pc = PEEK(2) : REM player row, column
640 CLS : REM the first time around we need to draw the maze
650 LOCATE 2,1
660 FOR row = 0 TO height-1
670     LET s$ = ""
680     FOR col = 0 TO width-1
690         LET cell = PEEK(16 + row * width + col)
700         s$ = s$ + MID$(" X", cell, 1)
710     NEXT col : PRINT s$
720 NEXT row
730 REM erase the previous player position and print the new one
740 LOCATE 2+pr, 1+pc : PRINT " ";
750 pr = PEEK(1) : pc = PEEK(2)
760 LOCATE 2+pr, 1+pc : PRINT "@";
770 REM print the number of steps so far
780 LOCATE 1,10 : PRINT "STEPS: "; steps;
790 LET steps = steps + 1
791 FOR x=0 TO 0
792   PAUSE 100
793 NEXT x
800 RETURN

1000 REM calculate player direction
1010 LET player_row = PEEK(1)
1020 LET player_col = PEEK(2)
1030 REM these variables tell whether there's a wall in that direction
1040 LET right = PEEK(16 + player_row * width + player_col + 1)
1050 LET down = PEEK(16 + (player_row+1) * width + player_col)
1060 LET left = PEEK(16 + player_row * width + player_col - 1)
1070 LET up = PEEK(16 + (player_row-1) * width + player_col)
1080 GOSUB 1300
1090 RETURN


1100 REM here's an interactive version
1110 GET key
1120 IF key = -2 THEN POKE 0, 1 : RETURN : REM no user present
1130 IF key = -1 THEN PAUSE 100: GOTO 1110 : REM wait for input
1140 IF key = 13 THEN STOP : REM user wants out
1150 IF key = 0 THEN
1160     IF right = 0 THEN GOTO 1250
1170 ELSE IF key = 1 THEN
1180     IF down = 0 THEN GOTO 1250
1190 ELSE IF key = 2 THEN
1200     IF left = 0 THEN GOTO 1250
1210 ELSE IF key = 3 THEN
1220     IF up = 0 THEN GOTO 1250
1230 END IF
1240 PAUSE 100 : GOTO 1110 : REM ignore key, wait for next one
1250 POKE 0, key : RETURN


1300 REM  write the next direction
1301 REM  0=right, 1=down, 2=left, 3=up
1306 LET dir = PEEK(0)
1307 LET new_dir = dir
1309 REM moving right
1310 IF dir = 0 THEN
1320   IF down = 0 THEN
1321     new_dir = 1
1330   ELSE IF right = 0 THEN
1331     new_dir = 0
1340   ELSE IF up = 0 THEN
1341     new_dir = 3
1350   ELSE
1351     new_dir = 2
1360   END IF
1361 REM moving down
1370 ELSE IF dir = 1 THEN
1380   IF left = 0 THEN
1381     new_dir = 2
1390   ELSE IF down = 0 THEN
1391     new_dir = 1
1400   ELSE IF right = 0 THEN
1401     new_dir = 0
1410   ELSE
1411     new_dir = 3
1420   END IF
1421 REM moving left
1430 ELSE IF dir = 2 THEN
1440   IF up = 0 THEN
1441     new_dir = 3
1450   ELSE IF left = 0 THEN
1451     new_dir = 2
1460   ELSE IF down = 0 THEN
1461     new_dir = 1
1470   ELSE
1471     new_dir = 0
1480   END IF
1490 ELSE
1491 REM moving up
1500   IF right = 0 THEN
1501     new_dir = 0
1510   ELSE IF up = 0 THEN
1511     new_dir = 3
1520   ELSE IF left = 0 THEN
1521     new_dir = 2
1530   ELSE
1531     new_dir = 1
1540   END IF
1550 END IF


1700 POKE 0, new_dir : RETURN

