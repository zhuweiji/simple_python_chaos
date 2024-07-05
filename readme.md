# Chaos Testing Framework

This package is meant to explore the possibility of creating a simple framework for implementing chaos testing in Python applications, with a focus on network-related issues such as latency and packet loss.

## Features

- Easy configuration via YAML files
- Automatic loading of configuration from a `chaos.config.yml` file
- Decorators for adding network chaos to functions
- Support for inducing latency and simulating packet loss

## Usage

Import and use the decorators in your application code.

```python
import requests

from chaos.network import add_latency

@add_latency(min_delay=1, max_delay=3)
def get(endpoint):
    response = requests.get(endpoint)
    return response
```


## Contributing
Contributions are welcome! Please feel free to submit a Pull Request.

## License
This project is licensed under the MIT License - see the LICENSE file for details
