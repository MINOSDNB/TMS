lambda_func = lambda **kwargs: {key*2: value for key, value in kwargs.items()}
print(lambda_func(abc=5, oiu=6))
