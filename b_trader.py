from __future__ import (absolute_import, division, print_function,
                        unicode_literals)

import backtrader as bt

if __name__ == '__main__':
    cerebro = bt.Cerebro()
    cerebro.broker.setcash(100000.0)
    
    print(f'Starting Portfolio Value: {cerebro.broker.getvalue()}')

    cerebro.run()

    print(f'Ending Portfolio Value: {cerebro.broker.getvalue()}')