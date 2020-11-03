---
layout: post
title:  "PC Engines apu coreboot Open Source Firmware v4.12.0.6"
date:   2020-11-03
categories: Firmware
---
# PC Engines apu coreboot Open Source Firmware v4.12.0.6

## Key changes

Mainline:

1. **Rebased** with official coreboot repository **commit** 43439f6.
2. **Fixed** runtime configuration allowing to reverse PCI addressing order.
   Previously it changed only addressing of mPCIe devices, now NICs are
   reversed as well. Which means that NIC with WoL should be the first booting
   in iPXE.

Legacy:

1. **Fixed** runtime configuration allowing to reverse PCI addressing order.
   Previously it changed only addressing of mPCIe devices, now NICs are
   reversed as well. Which means that NIC with WoL should be the first booting
   in iPXE.


## Statistics

![Files Changed](https://cloud.3mdeb.com/index.php/s/ZKafJdJojiitT8n/preview)

The chart shows the total files changed from release tag against the rebase
point of given release specified in CHANGELOG (CHANGELOG.md and gitlab-ci.yml
excluded from statistics). Check the statistics with:

```
git diff --stat 43439f6 ':(exclude).gitlab-ci.yml' ':(exclude)CHANGELOG.md' ':(exclude).gitlab-ci/regression.sh'
```

`108 files changed, 4214 insertions(+), 452 deletions(-)`

![Process of mainlining](https://cloud.3mdeb.com/index.php/s/qfAyiq5B42BaTcH/preview)

The chart represents the total line added and deleted on the PC Engines
coreboot fork against the rebase point for a given release.

Three files have not been included in the diff as mentioned above since they
are not a part of coreboot tree.


## Testing

* [PC Engines hardware configuration matrix](https://cloud.3mdeb.com/index.php/s/sakiLj98Zxqz2D3/preview) - hardware configurations available for testing in 3mdeb laboratory.

* [PC Engines release validation results](https://3mdeb.us16.list-manage.com/track/click?u=fce95b885fc13fbf1db611816&id=96d9b426c0&e=16ffa34a09) - please note there are separate sheets for each board-release.

![Mainline test results](https://cloud.3mdeb.com/index.php/s/cyjGHt3RXTgTtN2/preview)

* Mainline:
  * PASSED: **574** (-43)
  * FAILED: **13** (+6)
  * PASSED [%]: **97.74** (-1.15%)

![Legacy test results](https://cloud.3mdeb.com/index.php/s/FtpH5DTRDx5nDDn/preview)

* Legacy:
  * PASSED: **389** (+4)
  * FAILED: **4** (-3)
  * PASSED [%]: **98.97** (+0.79%)

### Key Changes in testing

1. Validation infrastructure has been updated. Robot Framework has been rebased
   with official **commit** 535d9a1.

2. apu6a has not been tested in this iteration, which significantly decreased
   the total number of tests.

3. New USB sticks has had been added, which not necessarily have a good impact
   on the regression tests results. Increased FAIL rate is caused mainly by this
   change.

## Binaries

### Mainline

* [apu1 v4.12.0.6.zip](https://3mdeb.com/open-source-firmware/pcengines/apu1/apu1_v4.12.0.6.zip)

  [apu1 v4.12.0.6.rom](https://3mdeb.com/open-source-firmware/pcengines/apu1/apu1_v4.12.0.6.rom)

  [SHA256 file](https://3mdeb.com/open-source-firmware/pcengines/apu1/apu1_v4.12.0.6.SHA256)

  [SHA256 sig](https://3mdeb.com/open-source-firmware/pcengines/apu1/apu1_v4.12.0.6.SHA256.sig)

* [apu2 v4.12.0.6.zip](https://3mdeb.com/open-source-firmware/pcengines/apu2/apu2_v4.12.0.6.zip)

  [apu2 v4.12.0.6.rom](https://3mdeb.com/open-source-firmware/pcengines/apu2/apu2_v4.12.0.6.rom)

  [SHA256 file](https://3mdeb.com/open-source-firmware/pcengines/apu2/apu2_v4.12.0.6.SHA256)

  [SHA256 sig](https://3mdeb.com/open-source-firmware/pcengines/apu2/apu2_v4.12.0.6.SHA256.sig)

* [apu3 v4.12.0.6.zip](https://3mdeb.com/open-source-firmware/pcengines/apu3/apu3_v4.12.0.6.zip)

  [apu3 v4.12.0.6.rom](https://3mdeb.com/open-source-firmware/pcengines/apu3/apu3_v4.12.0.6.rom)

  [SHA256 file](https://3mdeb.com/open-source-firmware/pcengines/apu3/apu3_v4.12.0.6.SHA256)

  [SHA256 sig](https://3mdeb.com/open-source-firmware/pcengines/apu3/apu3_v4.12.0.6.SHA256.sig)

* [apu4 v4.12.0.6.zip](https://3mdeb.com/open-source-firmware/pcengines/apu4/apu4_v4.12.0.6.zip)

  [apu4 v4.12.0.6.rom](https://3mdeb.com/open-source-firmware/pcengines/apu4/apu4_v4.12.0.6.rom)

  [SHA256 file](https://3mdeb.com/open-source-firmware/pcengines/apu4/apu4_v4.12.0.6.SHA256)

  [SHA256 sig](https://3mdeb.com/open-source-firmware/pcengines/apu4/apu4_v4.12.0.6.SHA256.sig)

* [apu5 v4.12.0.6.zip](https://3mdeb.com/open-source-firmware/pcengines/apu5/apu5_v4.12.0.6.zip)

  [apu5 v4.12.0.6.rom](https://3mdeb.com/open-source-firmware/pcengines/apu5/apu5_v4.12.0.6.rom)

  [SHA256 file](https://3mdeb.com/open-source-firmware/pcengines/apu5/apu5_v4.12.0.6.SHA256)

  [SHA256 sig](https://3mdeb.com/open-source-firmware/pcengines/apu5/apu5_v4.12.0.6.SHA256.sig)

See how to verify the signatures on [asciinema](https://asciinema.org/a/335785)

### Legacy

* [apu2 v4.0.33.zip](https://3mdeb.com/open-source-firmware/pcengines/apu2/apu2_v4.0.33.zip)

  [apu2 v4.0.33.rom](https://3mdeb.com/open-source-firmware/pcengines/apu2/apu2_v4.0.33.rom)

  [SHA256 file](https://3mdeb.com/open-source-firmware/pcengines/apu2/apu2_v4.0.33.SHA256)

  [SHA256 sig](https://3mdeb.com/open-source-firmware/pcengines/apu2/apu2_v4.0.33.SHA256.sig)

* [apu3 v4.0.33.zip](https://3mdeb.com/open-source-firmware/pcengines/apu3/apu3_v4.0.33.zip)

  [apu3 v4.0.33.rom](https://3mdeb.com/open-source-firmware/pcengines/apu3/apu3_v4.0.33.rom)

  [SHA256 file](https://3mdeb.com/open-source-firmware/pcengines/apu3/apu3_v4.0.33.SHA256)

  [SHA256 sig](https://3mdeb.com/open-source-firmware/pcengines/apu3/apu3_v4.0.33.SHA256.sig)

* [apu4 v4.0.33.zip](https://3mdeb.com/open-source-firmware/pcengines/apu4/apu4_v4.0.33.zip)

  [apu4 v4.0.33.rom](https://3mdeb.com/open-source-firmware/pcengines/apu4/apu4_v4.0.33.rom)

  [SHA256 file](https://3mdeb.com/open-source-firmware/pcengines/apu4/apu4_v4.0.33.SHA256)

  [SHA256 sig](https://3mdeb.com/open-source-firmware/pcengines/apu4/apu4_v4.0.33.SHA256.sig)

* [apu5 v4.0.33.zip](https://3mdeb.com/open-source-firmware/pcengines/apu5/apu5_v4.0.33.zip)

  [apu5 v4.0.33.rom](https://3mdeb.com/open-source-firmware/pcengines/apu5/apu5_v4.0.33.rom)

  [SHA256 file](https://3mdeb.com/open-source-firmware/pcengines/apu5/apu5_v4.0.33.SHA256)

  [SHA256 sig](https://3mdeb.com/open-source-firmware/pcengines/apu5/apu5_v4.0.33.SHA256.sig)

See how to verify the signatures on [asciinema](https://asciinema.org/a/335785)

## What we planned

1. Improve the support of TPM2 in coreboot and SeaBIOS. Currently there is only
   the TCPA (TPM1.2) log support in coreboot. Additionally SeaBIOS overwrites
   existing entries in TPM2 log area. `cbmem` utility also lacks support for
   displaying TPM2 log area.

   **WORK IN PROGRESS**

2. Reorganize runtime configuration by making it persistent across updates and
   accessible from user space. Also prepare a tool for offline binary
   modification.

   **VERIFICATION**

3. Vital Product Data (VPD) support. User will have possibility to store
   and change VPD configuration in Read-Write section of SPI flash. Moreover,
   default VPD keys and values will be stored in Read-Only region to protect
   data against corruption. Also, sortbootorder runtime configuration will be
   stored in VPD Read-Write section, so access to it will be possible in OS
   via dedicated util.

   **VERIFICATION**

## Coming soon

Feature and improvements on the roadmap:

1. Improve the support of TPM2 in coreboot and SeaBIOS. Currently there is only
   the TCPA (TPM1.2) log support in coreboot. Additionally SeaBIOS overwrites
   existing entries in TPM2 log area. `cbmem` utility also lacks support for
   displaying TPM2 log area.
2. Reorganize runtime configuration by making it persistent across updates and
   accessible from user space. Also prepare a tool for offline binary
   modification.
3. Vital Product Data (VPD) support. User will have possibility to store
   and change VPD configuration in Read-Write section of SPI flash. Moreover,
   default VPD keys and values will be stored in Read-Only region to protect
   data against corruption. Also, sortbootorder runtime configuration will be
   stored in VPD Read-Write section, so access to it will be possible in OS
   via dedicated util.
