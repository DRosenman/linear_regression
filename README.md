
# linear_regression Version 0.1
- <a href = "#installing">Installing The Package</a>
- <a href = "#purpose">Purpose of Package</a>
- <a href="#comparison">Comparison with scipy.stats.linregress</a> 
- <a href="#using">Using The Package</a>
- <a href="#equations">Linear Regression Mathematical Equations</a>
- <a href="#v.2">Plans for Version 0.2</a>

    




## Installing the Package <a name="installing"></a>
From the command line:
```cmd
pip install linear_regression
```

Also available at <a href="https://pypi.python.org/pypi?name=linear-regression&version=0.1&:action=display">https://pypi.python.org/pypi?name=linear-regression&version=0.1&:action=display</a>

## <a name="purpose"></a> Purpose of Package 
The purpose of this package is to make it simple to perform simple least squares regression analysis on two sets of measurements. The scipy.stats module contains a function 'linregress' that can quickly perform regression analysis on two sets of measurements, but it does not have the option to force the best fit line to intercept the origin (i.e. to have a y intercept of 0). It also lacks other options, as demonstrated in the comparison below.

<a name="comparison"></a>
## Comparison Between scipy.stats.linregress and the linear_regression package: 
| Best Fit Line (BFL) Attributes and Options      | linear_regression v0.1| scipy.stat.linregress  |
| ------------- |:-------------:| -----:|
| slope     | Yes | Yes |
| std. error of slope|Yes|Yes|
| y-intercept | Yes|Yes |
|r (correlation coefficient)|Yes|Yes|
|r-squared|Yes|No|
|p-value|No|Yes|
|std. error of y-intercept|Yes|No|
|slope of BFL through origin|Yes|No|
|std. error of slope of BFL through origin|Yes|No|
|r for BFL through origin|Yes|No|
|r-squared for BFL through origin|Yes|No|
|Returns Regression Results As|Pandas DataFrame or String|Tuple|
|Option To Return Results For BFL, BFL through origin, or both simultaneously|Yes|No|



## Using  The Package <a name="using"></a> 

Version 0.1 of this package only contains a single module, <a href ="https://github.com/DRosenman/linear_regression/blob/master/v0.1/lr.py">lr.py</a>,  which contains a simple class named lr.

### **Load The lr class**


```python
from linear_regression.lr import lr
```

### Store the x and y coordinates from you dataset into seperate array-like object (arrays, np arrays, lists, tuples...)

Example: My dataset contains the following (x,y) data points:

(1.0,2.2), (1.8,3.8),(4.5,6.3), (5.2, 9.3)

I then create a list for the x coordinates and a list for the y coordinates below:


```python
x = [1.0,1.8,4.5,4.7,5.0]
y = [2.2,3.8,6.4,7.2,9.3]
```

### Create an instance object of the lr class using the x and y variables are instance arguments. 

I'll name my object data. I will use this object throughout the tutorial.



```python
data = lr(x,y)
```

### lr Object Methods 
**results** 

*parameters*: 

 - zero_intercept: (default value is False) if set to True, returns DataFrame for the best fit line through the origin.
 
 - both: (default value is False) if set to True, returns DataFrame  both the best fit line and the best fit line through the origin (both overrides zero_intercept if both is set to True).
 
*returns*:
 - DataFrame contaning slope, y-intercept, std.error of slope, std. error of y intercept, r, and r-squared for either the regular best fit line, the best fit line through the origin, or both the regular best fit line + the best fit line through the origin.
 
*__Examples__*:


```python
regression_results = data.results() #No parameters specified, so by default returns 
                                    #DataFrame with values for the regular best fit line 
print(regression_results)
```

            Slope  Intercept  Std. Error, Slope  Std. Error, Intercept         r  \
    BFL  1.445573   0.865051           0.257081               0.972703  0.955689   
    
         r-squared  
    BFL   0.913341  
    


```python
print(data.results(zero_intercept = True)) #Retuns DataFrame with results for the best fit line through the origin
```

                         Slope  Intercept  Std. Error, Slope         r  r-squared
    BFL Through (0,0)  1.65102        0.0           0.109809  0.991269   0.982613
    


```python
print(data.results(both = True)) #Returns DataFrame with values for both the regular best 
                          # fit line and the best fit line through the origin
```

                          Slope  Intercept  Std. Error, Slope  \
    BFL                1.445573   0.865051           0.257081   
    BFL Through (0,0)  1.651020   0.000000           0.109809   
    
                       Std. Error, Intercept         r  r-squared  
    BFL                             0.972703  0.955689   0.913341  
    BFL Through (0,0)                    NaN  0.991269   0.982613  
    

**Printing the object**

If you print your lr object, it will return a string with the regression results for both the best fit line and the best fit line through the origin.

*__Example using the data lr object:__*


```python
print(data)
```

    LINEAR LEAST-SQUARES REGRESSION ANALYSIS
    
    BEST FIT LINE:
    slope = 1.44557329463
    intercept = 0.865050798258
    std. error, slope = 0.257080665506
    std. error, intercept = 0.972703011277
    r = 0.955688839522
    r-squared = 0.913341157987
    number of data points = 5
    
    BEST FIT LINE THROUGH THE ORIGIN, (0,0):
    slope = 1.65101983794
    intercept = 0.0
    std. error, slope = 0.109809386014
    r = 0.991268534449
    r-squared = 0.982613307389
    number of data points = 5
    

### lr Object Attributes

**slope** - returns the slope of the best fit line.


```python
print(data.slope)
```

    1.44557329463
    

**slope00** - returns the slope of the best fit line through the origin


```python
print(data.slope00)
```

    1.65101983794
    

**intercept** - returns the y-intercept of the best fit line


```python
print(data.intercept)
```

    0.865050798258
    

**slope_std_error** - returns the std. error of the slope of the best fit line


```python
print(data.slope_std_error)
```

    0.257080665506
    

**slope_std_error00** - returns the std. error of the slope of the best fit line through the origin


```python
print(data.slope_std_error00)
```

    0.109809386014
    

**intercept_std_error** - returns the std. error of the intercept of the best fit line


```python
print(data.intercept_std_error)
```

    0.972703011277
    

**r** - returns the correlation coefficient


```python
print(data.r)
```

    0.955688839522
    

**r00** - returns the correlation coefficient for the BFL through the origin


```python
print(data.r00)
```

    0.991268534449
 
<a id='equations'></a> 

## Linear Regression Mathematical Equations <a id='equations'></a>
The least squares regression mathematical equations that I used can be found at <a href = "https://github.com/DRosenman/linear_regression/blob/master/leastsquaresmath.pdf">https://github.com/DRosenman/linear_regression/blob/master/leastsquaresmath.pdf</a>



## Plans for Version 0.2 <a name='v.2'></a>
- Add module for creating various regression plots.

- Add p-value for BFL and BFL through origin

