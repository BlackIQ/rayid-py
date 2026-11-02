# Usage

## Create a generator

```python
from rayid import RayID

ray = RayID("digit")   # type is required
```

### Types

| Type    | Characters             |
| ------- | ---------------------- |
| `digit` | `0-9`                  |
| `lower` | `a-z`                  |
| `upper` | `A-Z`                  |
| `all`   | digits + lower + upper |

Invalid type raises `ValueError`.

## Generate an ID

```python
ray.gen(12)
```

- `length` must be a positive integer.
- For `digit` (and any set that includes `0`), the **first character is never `0`**, so IDs are safer to treat as numeric-looking strings.

```python
from rayid import RayID

digits = RayID("digit")
print(digits.gen(10))

lower = RayID("lower")
print(lower.gen(10))

mixed = RayID("all")
print(mixed.gen(16))
```

## API

### `RayID(type)`

| Argument | Description                             |
| -------- | --------------------------------------- |
| `type`   | One of `digit`, `lower`, `upper`, `all` |

### `gen(length) -> str`

| Argument | Description                       |
| -------- | --------------------------------- |
| `length` | Positive `int` — length of the ID |

Raises `TypeError` / `ValueError` on invalid length.

### `characters() -> str`

Returns the alphabet for the current type (useful for debugging or custom use).
