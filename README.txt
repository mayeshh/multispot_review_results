# 2018-01-04

NOTE: all measurements taken on this day were performed without
the slit for 532nm laser and with the slit for the 628nm laser (dumb of me...)

First single-molecule test with AS microfluidic chip using 
4x12 LCOS patterns. Success!!!

CONCLUSION: even while flowing sample through channel I get signal in the 
time trace. Promising, but lots of parameters to characterize including
laser intensity, Z-position, and input flow rate. 

# 2019-02-15 Analysis for Elsevier methods paper

After comparing the AS chip with flow to a measurement with no chip and no
flow, some conclusions can be made:

i) For the flow chip, a burst search using a moving threshold (F) would probably
be best.
ii) the background during Dex is not constant - it drops significantly towards the end of the measurement
iii) the burst ratio for the pooled data is 3x higher for the chip before selection.
After selection the ration increases to 9x, this could mean a) the the selection process for the AS chip with flow does not remove background bursts or b) there are way more bursts due to the flow rate and size selection indicates that the burst number is high... which doesn't make sense to me because I expect the burst number to decrease with flow. Perhaps there is significant scattering from the PDMS chip... not sure. 

# alex hist of pooled data
# superimpose plots 
# also include superimposed 48-spot plots 
# we observe more and larger bursts
# show a table or mean +/- std
# make a github repo and get a DOI
# hdf5 files go in figshare

##### number of bursts
# burst size
# burst duration
# CCF forumla: transit time (Gaussian waist of PSF / velocity) is ~10ms at the 10uL/hr flow rate this is compared to 200us
# - transit due to flow is dominated by diffusion 
  - at higher flow rates (5x faster) we reach a regime where the flow is one the same magnitude of flow and diffusion and at this point the bursts will go down

1. In appendix add burst size distribution analysis (right after burst statistics in the appendix)
- 48 histograms and then pooled one side-by-side 
- do we loose bursts with flow? --> NO! 

2. In appendix add burst duration distribution analysis (right after burst statistics in the appendix)
- 48 histograms and then pooled one side-by-side
- in the flow rate, burst duration is not affected by flow --> in fact it appears to be slightly higher in the pooled hist

3. Work on Appendix - see comments

4. can you autocomplete in texshop?? 
- can you split the screens? 
