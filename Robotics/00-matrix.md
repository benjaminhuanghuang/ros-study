## Matrix
```
np.random.rand(3,3)  # value 0 ... 1

np.asarray([1,2,3,4]]).reshape(2,2)
```


### Identity matrix 单位矩阵
```
np.identity(3)
```

### Zero matrix 0矩阵
```
np.zeros([3,3])
```

## Operation
### Add / Sub
```
    np.add(A, B)

    np.substract(A, B)
```
A + 0 = A
A + B = B + A
(A+B) + C = A + (B+C)

### Dot product
```
    np.dot(A, B)
```
A x I = A
A x 0 = 0
(AB)C=A(BC)

A x B != B x A

### Inverse 
```
    A_INV = np.linalg.inv(A)
```
A x A_INV = I

0 matrix dose not have inverse matrix

## Transpose 
```
    A_T = A.T
```






表示旋转的旋转矩阵、
坐标变换中的齐次矩阵、
关节速度映射雅可比矩阵
仿真中的惯性矩阵等等


## Reference 
矩阵乘法的本质是什么？
https://www.zhihu.com/question/21351965

