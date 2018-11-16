from decimal import Decimal
import matplotlib.pyplot as plt

# w1 = weight 1
# w2 = weight 2
# b = bias
# lr = learning rate (between 0 and 1)

def adjust(w1, w2, b, x, y, rateX, rateY, rateB, interations = 0):
    result = (w1 * x) + (w2 * y) + b

    if result >= 0:
        dicts = {}
        dicts['result'] = result
        dicts['w1'] = w1
        dicts['w2'] = w2
        dicts['b'] = b
        dicts['interations'] = interations

        return dicts
    else:
        interations = interations + 1
        w1 = w1 + rateX
        w2 = w2 + rateY
        b = b + rateB

        # print([w1, w2, b, rateX, rateY,rateB])
        return adjust(w1, w2, b, x, y, rateX, rateY, rateB, interations)
    
w1 = (3)
w2 = (4)
b = (-10)
lr = Decimal.from_float(0.1)

x = 1
y = 1

rateX = x * lr
rateY = y * lr
rateB = lr

plt.plot([3,0], [0, 3])
plt.axis([0, 3, 0, 3])
plt.plot(1, 1, 'ro')

result = adjust(w1, w2, b, x, y, rateX, rateY, lr)

whenY0 = (result['b'] * -1) / result['w1']
whenX0 = ((result['w1'] * -1) / result['w2']) + ((result['b'] * -1) / result['w2'])

plt.plot([whenY0,0], [0, whenX0])

plt.show()