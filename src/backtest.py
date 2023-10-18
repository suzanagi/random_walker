from backtesting import Backtest
from backtesting.test import GOOG
from all_strategy.common.SmaCross import SmaCross

def main():
    bt = Backtest(GOOG, SmaCross,\
                cash=1000000, commission=.002,
                exclusive_orders=True)

    output = bt.run()
    bt.plot()
    print(output)

if __name__=="__main__":
    main()
