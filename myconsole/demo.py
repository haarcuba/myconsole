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
