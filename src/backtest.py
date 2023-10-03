from backtesting import Backtest
from backtesting.test import GOOG
from all_strategy.SmaCross import MyStratedy01

def main():
    bt = Backtest(GOOG, MyStratedy01,\
                cash=1000000, commission=.002,
                exclusive_orders=True)

    output = bt.run()
    bt.plot()

if __name__=="__main__":
    main()
