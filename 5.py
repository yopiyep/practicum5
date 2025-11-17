weight = int(input())
height = int(input())
weight2 = weight / 2.20462
height2 = height * 0.0254
total = round(weight2 / (height2 ** 2), 2)
if total < 16:
    print('Выраженный дефецит массы тела')
elif 16 <= total <= 18.49:
    print('Недостаточная масса тела')
elif 18.5 <= total < 25:
    print('Норма')
elif 25 <= total < 30:
    print('Избыточная масса тела')
elif 30 <= total < 35:
    print('Ожирение первой степени')
elif 35 <= total < 40:
    print('Ожирение второй степени')
else:
    print('Ожирение третьей степени')