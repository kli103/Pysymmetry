# Pysymmetry

## Representation of Two-Particle Wavefunction

Input is single particle wavefunction data calculated from the last step:

```
[[sigma 1, sigma 2, sigma 3, sigma N coefficent in MO] <- using sigma 1 derive
[sigma 1, sigma 2, sigma 3, sigma N coefficent in MO] <- using sigma 2 derive
[sigma 1, sigma 2, sigma 3, sigma N coefficent in MO] <- using sigma 3 derive
[sigma 1, sigma 2, sigma 3, sigma N coefficent in MO]] <- using sigma N derive

[[0.3333333333333333, 0.3333333333333333, 0.3333333333333333, 0.0], [0.3333333333333333, 0.3333333333333333, 0.3333333333333333, 0.0], [0.3333333333333333, 0.3333333333333333, 0.3333333333333333, 0.0], [0.0, 0.0, 0.0, 1.0]],

[[0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0]],

[[0.36602540378443865, 0.13397459621556135, -0.5, 0.0], [-0.36602540378443865, -0.13397459621556135, 0.5, 0.0], [-0.36602540378443865, -0.13397459621556135, 0.5, 0.0], [0.0, 0.0, 0.0, 
0.0]],

[[0.0, 0.0, 0.0, 0.0], [0.36602540378443865, 0.13397459621556138, -0.5, 0.0], [-0.36602540378443865, -0.13397459621556138, 0.5, 0.0], [0.0, 0.0, 0.0, 0.0]]
```

$$
\begin{aligned}
& e_x=\varphi^{e_x}=\mathcal{P}^{E_x} \sigma_1 \\
& =\frac{2}{6}\left[\begin{array}{c}
\left(E_{x x}(E) \sigma_1+E_{y x}(E) \sigma_1\right) \\
+\left(E_{x x}\left(C_3\right) \sigma_2+E_{y x}\left(C_3\right) \sigma_2\right) \\
+\left(E_{x x}\left(C_3^{-1}\right) \sigma_3+E_{y x}\left(C_3^{-1}\right) \sigma_3\right) \\
+\left(E_{x x}\left(\sigma_v\right) \sigma_1+E_{y x}\left(\sigma_v\right) \sigma_1\right) \\
+\left(E_{x x}\left(\sigma_v^{\prime}\right) \sigma_3+E_{y x}\left(\sigma_v^{\prime}\right) \sigma_3\right) \\
+\left(E_{x x}\left(\sigma_v^{\prime \prime}\right) \sigma_2+E_{y x}\left(\sigma_v^{\prime \prime}\right) \sigma_2\right)
\end{array}\right]
\end{aligned}
$$

$$
\begin{aligned}
& e_y=\varphi^{e_y}=\mathcal{P}^{E_y} \sigma_1 \\
& =\frac{2}{6}\left[\begin{array}{c}
\left(E_{x y}(E) \sigma_1+E_{y y}(E) \sigma_1\right) \\
+\left(E_{x y}\left(C_3\right) \sigma_2+E_{y y}\left(C_3\right) \sigma_2\right) \\
+\left(E_{x y}\left(C_3^{-1}\right) \sigma_3+E_{y y}\left(C_3^{-1}\right) \sigma_3\right) \\
+\left(E_{x y}\left(\sigma_v\right) \sigma_1+E_{y y}\left(\sigma_v\right) \sigma_1\right) \\
+\left(E_{x y}\left(\sigma_v^{\prime}\right) \sigma_3+E_{y y}\left(\sigma_v^{\prime}\right) \sigma_3\right) \\
+\left(E_{x y}\left(\sigma_v^{\prime \prime}\right) \sigma_2+E_{y y}\left(\sigma_v^{\prime \prime}\right) \sigma_2\right)
\end{array}\right]
\end{aligned}
$$

And we get

```
[[ 1.         0.25       0.25       1.         0.25       0.25     ]
 [ 0.        -0.4330127  0.4330127  0.         0.4330127 -0.4330127]
 [ 0.        -0.4330127  0.4330127  0.         0.4330127 -0.4330127]
 [ 0.         0.75       0.75       0.         0.75       0.75     ]]
 
[[ 0.         0.75       0.75       0.         0.75       0.75     ]
 [ 0.         0.4330127 -0.4330127 -0.        -0.4330127  0.4330127]
 [ 0.         0.4330127 -0.4330127 -0.        -0.4330127  0.4330127]
 [ 1.         0.25       0.25       1.         0.25       0.25     ]]
 
[[ 0.         0.4330127 -0.4330127  0.         0.4330127 -0.4330127]
 [ 1.         0.25       0.25      -1.        -0.25      -0.25     ]
 [ 0.        -0.75      -0.75       0.         0.75       0.75     ]
 [ 0.        -0.4330127  0.4330127 -0.        -0.4330127  0.4330127]]
 
[[ 0.         0.4330127 -0.4330127  0.         0.4330127 -0.4330127]
 [ 0.        -0.75      -0.75       0.         0.75       0.75     ]
 [ 1.         0.25       0.25      -1.        -0.25      -0.25     ]
 [ 0.        -0.4330127  0.4330127 -0.        -0.4330127  0.4330127]]
```

 ![](https://cdn.mathpix.com/snip/images/719p5GkJw-VUdr1LZSK_89X0YCavGdYaxWTFiSDgGpY.original.fullsize.png)

## Embed of Two-Particle Wavefunction

```
==================================================
[3. 0. 0. 3.]
[0. 0. 0. 0.]
[ 1.5  0.   0.  -1.5]
[ 0.  -1.5 -1.5  0. ]
==================================================
[3. 0. 0. 3.]
[0. 0. 0. 0.]
[-1.5  0.   0.   1.5]
[0.  1.5 1.5 0. ]
==================================================
[0. 0. 0. 0.]
[ 0.  3. -3.  0.]
[-1.5  0.   0.   1.5]
[0.  1.5 1.5 0. ]
==================================================
[0. 0. 0. 0.]
[ 0. -3.  3.  0.]
[-1.5  0.   0.   1.5]
[0.  1.5 1.5 0. ]
```

$$
\begin{aligned}
P_R\left[\left(\varphi^{e_x}, \varphi^{e_y}\right) \otimes\left(\phi^{e_x}, \phi^{e_y}\right)\right] & =\left(P_R \varphi^{e_x}, P_R \varphi^{e_y}\right) \otimes\left(P_R \phi^{e_x}, P_R \phi^{e_y}\right) \\
& =P_R \otimes P_R\left(\varphi^{e_x} \otimes \phi^{e_x}, \varphi^{e_x} \otimes \phi^{e_y}, \varphi^{e_y} \otimes \phi^{e_x}, \varphi^{e_y} \otimes \phi^{e_y}\right) \\
& =P_R \otimes P_R\left(\varphi^{e_x} \phi^{e_x}, \varphi^{e_x} \phi^{e_y}, \varphi^{e_y} \phi^{e_x}, \varphi^{e_y} \phi^{e_y}\right)
\end{aligned}
$$

![](https://cdn.mathpix.com/snip/images/m5VUKODwC8e9i-MuVN16JwI5rghQb4ceJg6kBNL20Io.original.fullsize.png)

![](https://cdn.mathpix.com/snip/images/j25mkgOW9WwBvAPcbbHor9xHbrbjmvKMDZ73twYiVwc.original.fullsize.png)
