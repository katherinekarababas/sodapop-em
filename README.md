# sodapop
Tools for neutron star population modeling and inference with gravitational-wave and electromagnetic observations.

### Scripts

* reweight-masses /path/to/samples.csv -c m1_source m2_source dL z -o /path/to/samples_reweighted.csv -p flat_m1m2det_quad_dL -r flat_m1m2 -v

Reweight posterior samples according to flat-in-source-frame-component-mass prior to make them likelihood samples.

* INFER-NS-MASS

Specify observations, population models and hyperparameter priors, then infer the neutron-star mass distribution. Relies on sample-pop-params, infer-pop-params and build-ppd.

### Examples

sample-pop-params unif_mass -n 10 -p mmin,mmax+flat12,1.,1.2,1.8,2.4 -o sodapop-em/dat/unif_mass_prior.csv -v

infer-pop-params sodapop-em/dat/unif_mass_prior.csv $(ls -m sodapop-em/etc/gw/*.csv | tr -d ',') $(ls -m sodapop-em/etc/psr/*.csv | tr -d ',') -p unif_m1m2 unif_m1_unif_m2 unif_mass -C bns bns bns bns bns bns bns bns bns bns bns bns bns bns bns bns bns bns bns bns psr psr psr psr psr psr psr psr psr psr psr psr psr psr psr psr psr psr psr psr psr psr psr psr psr psr psr psr psr psr psr psr psr psr psr psr psr psr psr psr psr psr psr psr psr psr psr psr psr psr psr psr psr psr psr psr psr psr psr psr psr psr psr psr psr psr psr psr psr psr psr psr psr psr psr -c m1_source m2_source dL z m likelihood -l 100 -P mmin,mmax+flat12,1.,1.5,1.5,3. -B 3. 60. 0. -f chirpmass52 -s 5000 -t 10000 -w 10 -b 100 -o sodapop-em/dat/unif_mass.csv --diag -v

build-ppd sodapop-em/dat/unif_mass.csv -p unif_mass -s 5000 -f False -m 5000 -o sodapop-em/dat/unif_mass_ppd.csv -v

