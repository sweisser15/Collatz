#!/usr/bin/env python3

# -------------------------------
# projects/collatz/TestCollatz.py
# Copyright (C) 2016
# Glenn P. Downing
# -------------------------------

# https://docs.python.org/3.4/reference/simple_stmts.html#grammar-token-assert_stmt

# -------
# imports
# -------

from io import StringIO
from unittest import main, TestCase

from Collatz import collatz_read, collatz_eval, collatz_print, collatz_solve

# -----------
# TestCollatz
# -----------


class TestCollatz (TestCase):
    # ----
    # read
    # ----

    def test_read_1(self):
        s = "1 10\n"
        i, j = collatz_read(s)
        self.assertEqual(i,  1)
        self.assertEqual(j, 10)

    def test_read_2(self):
        s = "67844 63902\n"
        i, j = collatz_read(s)
        self.assertEqual(i, 67844)
        self.assertEqual(j, 63902)

    def test_read_3(self):
        s = "1 999999\n"
        i, j = collatz_read(s)
        self.assertEqual(i, 1)
        self.assertEqual(j, 999999)

    def test_read_4(self):
        s = "12 140\n"
        i, j = collatz_read(s)
        self.assertEqual(i, 12)
        self.assertEqual(j, 140)

    # ----
    # eval
    # ----

    def test_eval_1(self):
        v = collatz_eval(1, 10)
        self.assertEqual(v, 20)

    def test_eval_2(self):
        v = collatz_eval(100, 200)
        self.assertEqual(v, 125)

    def test_eval_3(self):
        v = collatz_eval(201, 210)
        self.assertEqual(v, 89)

    def test_eval_4(self):
        v = collatz_eval(900, 1000)
        self.assertEqual(v, 174)

    def test_eval_5(self):
        v = collatz_eval(67844, 63902)
        self.assertEqual(v, 312)

    def test_eval_6(self):
        v = collatz_eval(1, 999999)
        self.assertEqual(v, 525)

    def test_eval_7(self):
        v = collatz_eval(999999, 999999)
        self.assertEqual(v, 259)

    def test_eval_8(self):
        v = collatz_eval(134000, 287000)
        self.assertEqual(v, 443)

    # -----
    # print
    # -----

    def test_print_1(self):
        w = StringIO()
        collatz_print(w, 1, 10, 20)
        self.assertEqual(w.getvalue(), "1 10 20\n")

    def test_print_2(self):
        w = StringIO()
        collatz_print(w, 78777, 74090, 351)
        self.assertEqual(w.getvalue(), "78777 74090 351\n")

    def test_print_3(self):
        w = StringIO()
        collatz_print(w, 812000, 814575, 375)
        self.assertEqual(w.getvalue(), "812000 814575 375\n")

    def test_print_4(self):
        w = StringIO()
        collatz_print(w, 3000, 8000, 262)
        self.assertEqual(w.getvalue(), "3000 8000 262\n")

    # -----
    # solve
    # -----

    def test_solve_1(self):
        r = StringIO("1 10\n100 200\n201 210\n900 1000\n")
        w = StringIO()
        collatz_solve(r, w)
        self.assertEqual(
            w.getvalue(), "1 10 20\n100 200 125\n201 210 89\n900 1000 174\n")

    def test_solve_2(self):
        r = StringIO("2000 24356\n13001 14000\n904000 915766\n34000 35999\n")
        w = StringIO()
        collatz_solve(r, w)
        self.assertEqual(
            w.getvalue(), "2000 24356 282\n13001 14000 276\n904000 915766 476\n34000 35999 324\n")

    def test_solve_3(self):
        r = StringIO("300 400\n19 1\n31 7\n812000 235000\n")
        w = StringIO()
        collatz_solve(r, w)
        self.assertEqual(
            w.getvalue(), "300 400 144\n19 1 21\n31 7 112\n812000 235000 509\n")

    def test_solve_4(self):
        r = StringIO("990999 990000\n34000 35999\n345001 346000\n560 120\n")
        w = StringIO()
        collatz_solve(r, w)
        self.assertEqual(
            w.getvalue(), "990999 990000 321\n34000 35999 324\n345001 346000 441\n560 120 144\n")

# ----
# main
# ----


if __name__ == "__main__":
    main()

""" #pragma: no cover
% coverage run --branch TestCollatz.py >  TestCollatz.out 2>&1


% cat TestCollatz.out
.......
----------------------------------------------------------------------
Ran 7 tests in 0.000s
OK


% coverage report -m                   >> TestCollatz.out



% cat TestCollatz.out
.......
----------------------------------------------------------------------
Ran 7 tests in 0.000s
OK
Name             Stmts   Miss Branch BrPart  Cover   Missing
------------------------------------------------------------
Collatz.py          12      0      2      0   100%
TestCollatz.py      32      0      0      0   100%
------------------------------------------------------------
TOTAL               44      0      2      0   100%
"""
