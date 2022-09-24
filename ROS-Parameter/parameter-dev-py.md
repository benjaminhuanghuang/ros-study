
## declare parameter
```
self.declare_parameter("write_timer_period",5)
```


## read parameter
```
timer_period = self.get_parameter('write_timer_period').get_parameter_value().integer_value
```