# 13.12.2018 - i go by the book and "play" with the examples at hand

import thinkstats2  #import dependencies

# define a function to import 
# a stata dictionary file and
# turn it into a dataframe

def ReadFemPreg(dct_file='2002FemPreg.dct', dat_file= '2002FemPreg.dat.gz' ):
    dct = thinkstats2.ReadStataDct(dct_file)
    df = dct.ReadFixedWidth(dat_file,compression='gzip')
    CleanFemPreg(df)
    return df
    