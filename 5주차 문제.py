import math

naver_closing_price=["474,500","461,500","501,000","500,500","488,500"] #1

print("목요일:",naver_closing_price[3]) #5

a=max(naver_closing_price) 
print("최대값:",a) #2

b=min(naver_closing_price)
print("최소값:",b) #3

naver_closing_price2_dict=dict()

naver_closing_price2_dict["09/07"]="474,500"
naver_closing_price2_dict["09/08"]="461,500"
naver_closing_price2_dict["09/09"]="501,000"
naver_closing_price2_dict["09/10"]="500,500"
naver_closing_price2_dict["09/11"]="488,500" #6

inp=input("날짜를 입력하시오:")
print(naver_closing_price2_dict[inp]) #7

print(max(naver_closing_price),"-",min(naver_closing_price),"=",max(naver_closing_price)-min(naver_closing_price)) #4
