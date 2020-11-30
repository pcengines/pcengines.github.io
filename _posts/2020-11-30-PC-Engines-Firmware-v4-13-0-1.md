---
layout: post
title:  "PC Engines apu coreboot Open Source Firmware v4.13.0.1"
date:   2020-11-30
categories: Firmware
---
# PC Engines apu coreboot Open Source Firmware v4.13.0.1

## Key changes

Mainline:

1. **Rebased** with official coreboot repository **commit** 9b7dc76.

## Statistics

![Files Changed](https://cloud.3mdeb.com/index.php/s/gDfnpETCC9zQr8K/preview)

The chart shows the total files changed from release tag against the rebase
point of given release specified in CHANGELOG (CHANGELOG.md and gitlab-ci.yml
excluded from statistics). Check the statistics with:

```
git diff --stat 9b7dc76 ':(exclude).gitlab-ci.yml' ':(exclude)CHANGELOG.md' ':(exclude).gitlab-ci/regression.sh'
```

`107 files changed, 4333 insertions(+), 422 deletions(-)`

![Process of mainlining](https://cloud.3mdeb.com/index.php/s/73aERKHeNCdTTJ7/preview)

The chart represents the total line added and deleted on the PC Engines
coreboot fork against the rebase point for a given release.

Three files have not been included in the diff as mentioned above since they
are not a part of coreboot tree.

## Testing

* [PC Engines hardware configuration matrix](https://cloud.3mdeb.com/index.php/s/sakiLj98Zxqz2D3/preview) - hardware configurations available for testing in 3mdeb laboratory.

* [PC Engines release validation results](https://3mdeb.us16.list-manage.com/track/click?u=fce95b885fc13fbf1db611816&id=96d9b426c0&e=16ffa34a09) - please note there are separate sheets for each board-release.

![Mainline test results](https://cloud.3mdeb.com/index.php/s/eZS28Jro7HZrbqT/preview)

* Mainline:
  * PASSED: **567** (+2)
  * FAILED: **7** (-2)
  * PASSED [%]: **98.78** (+0.35%)

### Key Changes in testing

1. Introduced new way of backup the regression logs in case of external
   CI errors.
2. Changed pyte library to a fork that ignores bad escape code errors.
3. Some SD cards has been exchanged.

## Binaries

### Mainline

* [apu1 v4.13.0.1.zip](https://3mdeb.com/open-source-firmware/pcengines/apu1/apu1_v4.13.0.1.zip)

  [apu1 v4.13.0.1.rom](https://3mdeb.com/open-source-firmware/pcengines/apu1/apu1_v4.13.0.1.rom)

  [SHA256 file](https://3mdeb.com/open-source-firmware/pcengines/apu1/apu1_v4.13.0.1.SHA256)

  [SHA256 sig](https://3mdeb.com/open-source-firmware/pcengines/apu1/apu1_v4.13.0.1.SHA256.sig)

* [apu2 v4.13.0.1.zip](https://3mdeb.com/open-source-firmware/pcengines/apu2/apu2_v4.13.0.1.zip)

  [apu2 v4.13.0.1.rom](https://3mdeb.com/open-source-firmware/pcengines/apu2/apu2_v4.13.0.1.rom)

  [SHA256 file](https://3mdeb.com/open-source-firmware/pcengines/apu2/apu2_v4.13.0.1.SHA256)

  [SHA256 sig](https://3mdeb.com/open-source-firmware/pcengines/apu2/apu2_v4.13.0.1.SHA256.sig)

* [apu3 v4.13.0.1.zip](https://3mdeb.com/open-source-firmware/pcengines/apu3/apu3_v4.13.0.1.zip)

  [apu3 v4.13.0.1.rom](https://3mdeb.com/open-source-firmware/pcengines/apu3/apu3_v4.13.0.1.rom)

  [SHA256 file](https://3mdeb.com/open-source-firmware/pcengines/apu3/apu3_v4.13.0.1.SHA256)

  [SHA256 sig](https://3mdeb.com/open-source-firmware/pcengines/apu3/apu3_v4.13.0.1.SHA256.sig)

* [apu4 v4.13.0.1.zip](https://3mdeb.com/open-source-firmware/pcengines/apu4/apu4_v4.13.0.1.zip)

  [apu4 v4.13.0.1.rom](https://3mdeb.com/open-source-firmware/pcengines/apu4/apu4_v4.13.0.1.rom)

  [SHA256 file](https://3mdeb.com/open-source-firmware/pcengines/apu4/apu4_v4.13.0.1.SHA256)

  [SHA256 sig](https://3mdeb.com/open-source-firmware/pcengines/apu4/apu4_v4.13.0.1.SHA256.sig)

* [apu5 v4.13.0.1.zip](https://3mdeb.com/open-source-firmware/pcengines/apu5/apu5_v4.13.0.1.zip)

  [apu5 v4.13.0.1.rom](https://3mdeb.com/open-source-firmware/pcengines/apu5/apu5_v4.13.0.1.rom)

  [SHA256 file](https://3mdeb.com/open-source-firmware/pcengines/apu5/apu5_v4.13.0.1.SHA256)

  [SHA256 sig](https://3mdeb.com/open-source-firmware/pcengines/apu5/apu5_v4.13.0.1.SHA256.sig)

* [apu6 v4.13.0.1.zip](https://3mdeb.com/open-source-firmware/pcengines/apu6/apu6_v4.13.0.1.zip)

  [apu6 v4.13.0.1.rom](https://3mdeb.com/open-source-firmware/pcengines/apu6/apu6_v4.13.0.1.rom)

  [SHA256 file](https://3mdeb.com/open-source-firmware/pcengines/apu6/apu6_v4.13.0.1.SHA256)

  [SHA256 sig](https://3mdeb.com/open-source-firmware/pcengines/apu6/apu6_v4.13.0.1.SHA256.sig)

See how to verify the signatures on [asciinema](https://asciinema.org/a/376207)

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
