from backtesting import Strategy
import pandas as pd
import numpy as np

def moving_average(x, n):
    return pd.Series(x).rolling(window=n).mean()

def find_cross(short, long):
    diff = np.where(pd.Series(short) - pd.Series(long)>0, 1, 0)
    return pd.Series(diff).diff()

def trend(x):
    return np.where(pd.Series(x).diff()>0, 1, 0)


class MyStratedy01(Strategy):
    n1 = 10
    n2 = 20
    n3 = 100
    sl = 0.92
    tp = 1.15

    # Indicator などを指定するメソッド
    def init(self):
        close = self.data.Close
        self.sma1 = self.I(moving_average, close, self.n1)
        self.sma2 = self.I(moving_average, close, self.n2)
        self.sma3 = self.I(moving_average, close, self.n3)
        self.cross = self.I(find_cross, self.sma1, self.sma2)
        self.trend = self.I(trend, self.sma3)

    # 売買条件を指定するメソッド
    def next(self):
      price = self.data.Close[-1]
      limit = self.data.High[-1]

      if self.cross == 1 \
        and self.trend == 1 \
        and self.sma1 > self.sma3 \
        and self.sma2 > self.sma3:
          self.buy(limit=limit, sl=price*self.sl, tp=price*self.tp, size=100)
      elif self.cross == -1:
          self.position.close()

