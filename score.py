# -*- coding: utf-8 -*-
"""score.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1PEu-pxlskF9hoPvXpGMPSD48nFpLS_Ys
"""

score = input().split()
countF = 0
for i in score:
  if int(i) <60:
    countF += 1
print(countF)