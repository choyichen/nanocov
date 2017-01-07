GTEx data
=========

* Source: dbGaP
* Version: v6
* Download date: Oct. 7, 2015

dbGaP
-----

GTEx raw data downloaded from dbGaP.

meta
----

Metadata parsed from raw data, including lists of variables to use.

Subject phenotype & sample attribute variable information were parsed from the XML files from dbGaP by `py/parse_var_list.py`. (Number of variables were computed by `wc -l`.)

  Var Path
  173 `meta/subj_var_list.tsv`
   75 `meta/samp_var_list.tsv`
  248 total

The lists were later manually reviewed and edited to select only those informative variables. Notes, comments, units, and other invariant variables (e.g., Tru-Seq v1, totoal RNA) were removed from analysis. Variables w/ more than 50% missing values were also exlucded (DTHLUCODD, DTHRFGD, TRAMP, TRCCLMPD). SMRDLGTH (Read Length: maximum detected read length found) was removed because almost all of the samples were done with 76 bp (only 8 samples were done with 101 bp). SMUNPDRD (Unpaired Reads: number of reads lacking a pair mate) was removed becaasue most of the samples (99%) have 0 values. (This step left us 208-1=207 variables for analysis. (`SAMPID` not included for analysis).

  Var Path
  146 `meta/subj_var_list.selected.tsv`
   62 `meta/samp_var_list.selected.tsv`
  208 total

Use `diff` command to know what variables were excluded.

py
--

Python scripts to process the data.
