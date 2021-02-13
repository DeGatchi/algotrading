import unittest
from cryptoalgotrading.aux import get_data_from_file
from cryptoalgotrading.cryptoalgotrading import backtest, backtest_market,\
                                                is_time_to_buy, is_time_to_exit,\
                                                tick_by_tick

import cryptoalgotrading.entry as entry
import cryptoalgotrading.exit as exit_

class TestCryptoalgotrading(unittest.TestCase):


    def test_is_time_to_buy(self):

        q = get_data_from_file("BTC-XRP", interval='10m')

        self.assertEqual(is_time_to_buy(q[4416:4416+50],
                                        [entry.cross_smas],
                                        [4,8,12], [4,8,12]),
                                         False)
        self.assertEqual(is_time_to_buy(q[4417:4417+50],
                                        [entry.cross_smas],
                                        [4,8,12], [4,8,12]),
                                         True)
        self.assertEqual(is_time_to_buy(q[4418:4418+50],
                                        [entry.cross_smas],
                                        [4,8,12], [4,8,12]),
                                         False)


    def test_is_time_to_exit(self):

        q = get_data_from_file("BTC-XRP", interval='10m')

        self.assertEqual(is_time_to_exit(q[4778:4778+50],
                                         [exit_.cross_smas],
                                         [4,8,12], [4,8,12]),
                                         False)
        self.assertEqual(is_time_to_exit(q[4779:4779+50],
                                         [exit_.cross_smas],
                                         [4,8,12], [4,8,12]),
                                         True)
        self.assertEqual(is_time_to_exit(q[4780:4780+50],
                                         [exit_.cross_smas],
                                         [4,8,12], [4,8,12]),
                                         False)


    def test_tick_by_tick(self):
        self.assertEqual(round(tick_by_tick("BTC-DGB",
                                entry.cross_smas,
                                exit_.cross_smas,
                                interval='10s',
                                from_file=True,
                                plot=False,
                                refresh_interval=0.01),
                            2),
                        -18.82)


    def test_backtest(self):
        self.assertEqual(round(backtest(["BTC-XRP","BTC-SRN"],
                                  entry.cross_smas,
                                  exit_.cross_smas,
                                  interval='10m',
                                  from_file=True,
                                  smas=[5,10,18]),
                            2),
                        -217.49)

        self.assertEqual(round(backtest("BTC-XRP",
                                  entry.cross_smas,
                                  exit_.cross_smas,
                                  interval='10m',
                                  from_file=True,
                                  smas=[5,10,18]),
                            2),
                        -43.4)

        self.assertEqual(backtest("BTC-XXX",
                                  entry.cross_smas,
                                  exit_.cross_smas,
                                  interval='10m',
                                  from_file=False,
                                  smas=[5,10,18]),
                        0)


    def test_backtest_market(self):
        self.assertEqual(round(backtest_market([entry.cross_smas],
                                               [exit_.cross_smas],
                                               '10m',
                                               [0,0],
                                               [5,10,18],
                                               [5,10,18],
                                               True,
                                               False,
                                               False,
                                               'bittrex',
                                               0,
					                           1,
                                               "BTC-XRP"),
                                            2),
                        -43.4)


if __name__ == '__main__':
    unittest.main()
