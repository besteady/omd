# Setup
```
pip install -r requirements.txt
cd pizza_resolver
```

# Run
Variants of usage:
```
python cli.py order pepperoni --delivery
```
```
python cli.py menu
```

# Test
```
python -m unittest -v
```

# Coverage
```
coverage run -m unittest discover
coverage report -m
```
