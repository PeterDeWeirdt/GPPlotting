# GPPlotting

Plotting functions for the Genetic Perturbation Platform's 
[R&D group](https://sites.google.com/broadinstitute.org/doench/home) at the Broad institute. 

## Notes for development

* Include all reusable functions in gpplotting/__init__.py
* To use functions from the gpplotting in a notebook in notebooks/:
```python
import os
import sys
module_path = os.path.abspath(os.path.join('..'))
if module_path not in sys.path:
    sys.path.append(module_path)
```

and then 

```python
import gpplotting
```

* If you use an outside package in gpplotting, include it in setup.py, under ```install_requires``` along with an import 
statement in gpplotting/__init__.py