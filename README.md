# MYCONSOLE

MYCONSOLE simplifies [IPython](ipython.org) configuration so that you can easily create a customized console. Just do this:

```python
import myconsole.console

BANNER =\
"""
***********************************************
*                                             *
*       Welcome to the MYCONSOLE DEMO         *
*                                             *
***********************************************
"""

def main():
    myconsole.console.go( BANNER, 'MyConsole', exitMessage = 'enjoy your shiny new console!' )
```

The result:

