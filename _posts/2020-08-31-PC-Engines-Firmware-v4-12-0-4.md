---
layout: post
title:  "PC Engines apu coreboot Open Source Firmware v4.12.0.4"
date:   2020-08-31
categories: Firmware
---
# PC Engines apu coreboot Open Source Firmware v4.12.0.4

## Key changes

Mainline:

1. **Rebased** with official coreboot repository **commit** 81a2f45.
2. **Fixed** TPM2 visibility in OS for apu3d and apu4d.
3. **Fixed** issues with IRQ vectors reported in Xen and Linux dmesg.
4. **Updated sortbootorder** to version **v4.6.20** adding minor build fix for
   mainline coreboot.


## Statistics

![Files Changed](https://cloud.3mdeb.com/index.php/s/C8kHB5AeZ3eaei3/preview)

The chart shows the total files changed from release tag against the rebase
point of given release specified in CHANGELOG (CHANGELOG.md, gitlab-ci.yml and
gitlab-ci/regression.sh excluded from statistics). Check the statistics with:

```
git diff --stat 81a2f45bd2 ':(exclude).gitlab-ci.yml' ':(exclude)CHANGELOG.md' ':(exclude).gitlab-ci/regression.sh'
```

`103 files changed, 4058 insertions(+), 422 deletions(-)`

![Process of mainlining](https://cloud.3mdeb.com/index.php/s/rAAmor4qzdSSe9c/preview)

The chart represents the total line added and deleted on the PC Engines
coreboot fork against the rebase point for a given release.

Three files have not been included in the diff as mentioned above since they are
not a part of coreboot tree.

## Testing

* [PC Engines hardware configuration matrix](https://cloud.3mdeb.com/index.php/s/sakiLj98Zxqz2D3/preview) - hardware configurations available for testing in 3mdeb laboratory.

Please notice that it has been significantly improved.

* [PC Engines release validation results](https://3mdeb.us16.list-manage.com/track/click?u=fce95b885fc13fbf1db611816&id=96d9b426c0&e=16ffa34a09) - please note there are separate sheets for each board-release.

![Mainline test results](https://cloud.3mdeb.com/index.php/s/4jDqGgS7iRJbJBW/preview)

* Mainline:
  * PASSED: **542** (+102)
  * FAILED: **6** (-6)
  * PASSED [%]: **98.91** (+1.56%)

### Key Changes in testing

1. PC Engines apu1d has been integrated into Automated Regression
   infrastructure. This immediately greatly increased the range of tests.

2. There were some hardware modifications, apu3d and apu4d has been added TPM2.

3. Some USB sticks has been replaced - this decreased the number some random
   issues.

4. Xen is still unstable - this is the cause of over a half of the failures.


## Binaries

### Mainline

* [apu1 v4.12.0.4.zip](https://3mdeb.com/open-source-firmware/pcengines/apu1/apu1_v4.12.0.4.zip)

  [apu1 v4.12.0.4.rom](https://3mdeb.com/open-source-firmware/pcengines/apu1/apu1_v4.12.0.4.rom)

  [SHA256 file](https://3mdeb.com/open-source-firmware/pcengines/apu1/apu1_v4.12.0.4.SHA256)

  [SHA256 sig](https://3mdeb.com/open-source-firmware/pcengines/apu1/apu1_v4.12.0.4.SHA256.sig)

* [apu2 v4.12.0.4.zip](https://3mdeb.com/open-source-firmware/pcengines/apu2/apu2_v4.12.0.4.zip)

  [apu2 v4.12.0.4.rom](https://3mdeb.com/open-source-firmware/pcengines/apu2/apu2_v4.12.0.4.rom)

  [SHA256 file](https://3mdeb.com/open-source-firmware/pcengines/apu2/apu2_v4.12.0.4.SHA256)

  [SHA256 sig](https://3mdeb.com/open-source-firmware/pcengines/apu2/apu2_v4.12.0.4.SHA256.sig)

* [apu3 v4.12.0.4.zip](https://3mdeb.com/open-source-firmware/pcengines/apu3/apu3_v4.12.0.4.zip)

  [apu3 v4.12.0.4.rom](https://3mdeb.com/open-source-firmware/pcengines/apu3/apu3_v4.12.0.4.rom)

  [SHA256 file](https://3mdeb.com/open-source-firmware/pcengines/apu3/apu3_v4.12.0.4.SHA256)

  [SHA256 sig](https://3mdeb.com/open-source-firmware/pcengines/apu3/apu3_v4.12.0.4.SHA256.sig)

* [apu4 v4.12.0.4.zip](https://3mdeb.com/open-source-firmware/pcengines/apu4/apu4_v4.12.0.4.zip)

  [apu4 v4.12.0.4.rom](https://3mdeb.com/open-source-firmware/pcengines/apu4/apu4_v4.12.0.4.rom)

  [SHA256 file](https://3mdeb.com/open-source-firmware/pcengines/apu4/apu4_v4.12.0.4.SHA256)

  [SHA256 sig](https://3mdeb.com/open-source-firmware/pcengines/apu4/apu4_v4.12.0.4.SHA256.sig)

* [apu5 v4.12.0.4.zip](https://3mdeb.com/open-source-firmware/pcengines/apu5/apu5_v4.12.0.4.zip)

  [apu5 v4.12.0.4.rom](https://3mdeb.com/open-source-firmware/pcengines/apu5/apu5_v4.12.0.4.rom)

  [SHA256 file](https://3mdeb.com/open-source-firmware/pcengines/apu5/apu5_v4.12.0.4.SHA256)

  [SHA256 sig](https://3mdeb.com/open-source-firmware/pcengines/apu5/apu5_v4.12.0.4.SHA256.sig)

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
