#BMI.py
height,weight=eval(input('请输入身高（米）和体重（千克）[逗号隔开]：'))
bmi = weight/pow(height,2)
print('BMI 数值为：{:.2f}'.format(bmi))
who,nat= '',''
if bmi<18.5:
    who,nat = '偏瘦','偏瘦'
elif bmi<24:
    who,nat = '正常','正常'
elif bmi<25:
    who,nat = '正常','偏胖'
elif bmi<28:
    who,nat = '偏胖','偏胖'
elif bmi<30:
    who,nat = '偏胖','肥胖'
else:
    who,nat = '肥胖','肥胖'
print('BMI 指标为：国际"{0}"，国内"{1}"'.format(who,nat))