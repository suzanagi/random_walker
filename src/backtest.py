from .strategy import SmaCross

def main():
    bt = Backtest(GOOG, SmaCross,\
                cash=1000000, commission=.002,
                exclusive_orders=False)

    output = bt.run()
    bt.plot()

if __name__=="__main__":
    main()
