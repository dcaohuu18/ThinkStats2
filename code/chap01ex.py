"""This file contains code for use with "Think Stats",
by Allen B. Downey, available from greenteapress.com

Copyright 2014 Allen B. Downey
License: GNU GPLv3 http://www.gnu.org/licenses/gpl.html
"""

from __future__ import print_function

import numpy as np
import sys

import nsfg
import thinkstats2


def ReadFemResp(dct_file='2002FemResp.dct', dat_file='2002FemResp.dat.gz'):
	dct = thinkstats2.ReadStataDct(dct_file) 
	df = dct.ReadFixedWidth(dat_file, compression='gzip') 
	CleanFemResp(df) 
	return df


def CleanFemResp(df):
    pass


def ValidatePregnum(resp_df, preg_df):
	preg_map = nsfg.MakePregMap(preg_df)

	for index, caseid in preg_df.caseid.iteritems(): 
		pregnum = preg_df.pregnum[index]

		if len(preg_map[caseid]) != pregnum:
			return False 

	return True


def main(script):
    """Tests the functions in this module.

    script: string script name
    """

    resp_df = ReadFemResp()
    preg_df = nsfg.ReadFemPreg()

    assert(len(resp_df) == 7643)
    assert(resp_df.pregnum.value_counts()[1] == 1267)
    assert(ValidatePregnum(resp_df, preg_df))

    print('%s: All tests passed.' % script)


if __name__ == '__main__':
    main(*sys.argv)
