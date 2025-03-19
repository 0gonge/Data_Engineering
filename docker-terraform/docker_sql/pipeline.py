#여기가 데이터 파이프라인이 될 것! 
import sys
import pandas as pd

print(sys.argv)

day = sys.argv[1]
# 판다스 했다고 치고

print(f'job finished successfully for the day = {day}')