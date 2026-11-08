# RayID for Python

Generate short, readable IDs for logs, events, requests, and traces.

RayID is a tiny helper around a character set and a length. You pick the alphabet (`digit`, `lower`, `upper`, or `all`), then call `gen(length)`.

```python
from rayid import RayID

ray = RayID("digit")
print(ray.gen(16))  # e.g. 4829103756120483
```

|                  |                                                                                                     |
| ---------------- | --------------------------------------------------------------------------------------------------- |
| PyPI             | [pypi.org/project/rayid](https://pypi.org/project/rayid/)                                           |
| Source           | [GitLab](https://gitlab.com/blackiq-packages/pypi/rayid)                                            |
| **RayID for Js** | [npm `rayid`](https://www.npmjs.com/package/rayid) · [docs](https://rayid-js.docs.amirhossein.info) |

## Next

- [Install](learn/install.md)
- [Usage](learn/usage.md)
