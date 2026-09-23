# test-gen-it cases

## Pure function

Input:
```python
def discount(price, pct):
    return price * (1 - pct / 100)
```

Output (pytest):
```python
def test_discount_normal():
    assert discount(100, 20) == 80

def test_discount_edges():
    assert discount(100, 0) == 100
    assert discount(100, 100) == 0

def test_discount_error():
    import pytest
    with pytest.raises(TypeError):
        discount(None, 10)
```

Run with: `pytest -q`
