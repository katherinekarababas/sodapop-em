# sodapop
Tools for neutron star population modeling and inference with gravitational-wave and electromagnetic observations.

### Scripts

* reweight-masses /path/to/samples.csv -c m1_source m2_source dL z -o /path/to/samples_reweighted.csv -p flat_m1m2det_quad_dL -r flat_m1m2 -v

Reweight posterior samples according to flat-in-source-frame-component-mass prior to make them likelihood samples.

* INFER-NS-MASS

Specify observations, population models and hyperparameter priors, then infer the neutron-star mass distribution. Relies on sample-pop-params, infer-pop-params and build-ppd.

### Examples

sample-pop-params unif_mass -n 10 -p mmin,mmax+flat12,1.,1.2,1.8,2.4 -o sodapop-em/dat/unif_mass_prior.csv -v

infer-pop-params-em sodapop-em/dat/unif_mass_prior.csv $(ls -m sodapop-em/etc/*.csv | tr -d ',') -p unif_mass -C psr psr psr psr psr psr psr psr psr psr psr psr psr psr psr psr psr psr psr psr psr psr psr psr psr psr psr psr psr psr psr psr psr psr psr psr psr psr psr psr psr psr psr psr psr psr psr psr psr psr psr psr psr psr psr psr psr psr psr psr psr psr psr psr psr psr psr psr psr psr psr psr psr psr psr -c m -l 100 -P mmin,mmax+flat12,1.,1.5,1.5,3. -B 3. 60. 0. -f False -s 5000 -t 10000 -w 10 -b 1000 -o sodapop-em/dat/unif_mass.csv --diag -v

build-ppd-em sodapop-em/dat/unif_mass.csv -p unif_mass -s 5000 -f False -m 5000 -o sodapop-em/dat/unif_mass_ppd.csv -v


sample-pop-params peakcut_mass -n 36 -p mmin,mmax+flat12,1.,1.2,1.8,2.4 mu+flat,1.,3. sigma+flat,0.01,2. -o sodapop-em/dat/peakcut_mass_prior.csv -v

infer-pop-params-em sodapop-em/dat/peakcut_mass_prior.csv $(ls -m sodapop-em/etc/*.csv | tr -d ',') -p peakcut_mass -C psr psr psr psr psr psr psr psr psr psr psr psr psr psr psr psr psr psr psr psr psr psr psr psr psr psr psr psr psr psr psr psr psr psr psr psr psr psr psr psr psr psr psr psr psr psr psr psr psr psr psr psr psr psr psr psr psr psr psr psr psr psr psr psr psr psr psr psr psr psr psr psr psr psr psr -c m -l 100 -P mmin,mmax+flat12,1.,1.5,1.5,3. mu+flat,1.,3. sigma+flat,0.01,2. -B 3. 60. 0. -f False -s 5000 -t 10000 -w 36 -b 1000 -o sodapop-em/dat/peakcut_mass.csv --diag -v

build-ppd-em sodapop-em/dat/peakcut_mass.csv -p peakcut_mass -s 5000 -f False -m 5000 -o sodapop-em/dat/peakcut_mass_ppd.csv -v


sample-pop-params bimodcut_mass -n 105 -p mmin,mmax,mu1,mu2+flat1234,1.,1.2,1.8,2.4,1.2,1.5,1.5,1.8 sigma1+flat,0.01,2. sigma2+flat,0.01,2. w+flat,0.,1. -o sodapop-em/dat/bimodcut_mass_prior.csv -v -g 1000000

infer-pop-params-em sodapop-em/dat/bimodcut_mass_prior.csv $(ls -m sodapop-em/etc/*.csv | tr -d ',') -p bimodcut_mass -C psr psr psr psr psr psr psr psr psr psr psr psr psr psr psr psr psr psr psr psr psr psr psr psr psr psr psr psr psr psr psr psr psr psr psr psr psr psr psr psr psr psr psr psr psr psr psr psr psr psr psr psr psr psr psr psr psr psr psr psr psr psr psr psr psr psr psr psr psr psr psr psr psr psr psr -c m -l 100 -P mmin,mmax,mu1,mu2+flat1234,1.,1.5,1.5,3.,1.,3.,1.,3. sigma1+flat,0.01,2. sigma2+flat,0.01,2. w+flat,0.,1. -B 3. 60. 0. -f False -s 5000 -t 10000 -w 105 -b 1000 -o sodapop-em/dat/bimodcut_mass.csv --diag -v

build-ppd-em sodapop-em/dat/bimodcut_mass.csv -p bimodcut_mass -s 5000 -f False -m 5000 -o sodapop-em/dat/bimodcut_mass_ppd.csv -v
