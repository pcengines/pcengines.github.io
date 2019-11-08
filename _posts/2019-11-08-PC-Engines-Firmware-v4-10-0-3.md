---
layout: post
title:  "PC Engines apu coreboot Open Source Firmware v4.10.0.3"
date:   2019-11-08
categories: Firmware
---
# PC Engines apu coreboot Open Source Firmware v4.10.0.3

## Key changes

Mainline:

1. **Rebased** with official coreboot repository **commit** 2d90cb1.

## coreboot community

Patches sent for review:

* [Default SATA in AHCI mode for apu2](https://review.coreboot.org/c/coreboot/+/35891)
* [Handle USB keyboards function keys in Memtest86+](https://review.coreboot.org/c/memtest86plus/+/36630)
* [Implement bootblock in C environment](https://review.coreboot.org/c/coreboot/+/35754)
* [Adapt romstage to bootblock in C environment](https://review.coreboot.org/c/coreboot/+/35755)
* [Fix firmware table lookup for AMD FW](https://review.coreboot.org/c/blobs/+/35969)
* [Move AMD FW higher in CBFS](https://review.coreboot.org/c/coreboot/+/35970)

## Statistics

![Files Changed](https://cloud.3mdeb.com/index.php/s/2gwAPC6LwD3CQx9/preview)

The chart shows the total files changed from release tag against the rebase
point of given release specified in CHANGELOG (CHANGELOG.md and gitlab-ci.yml
excluded from statistics). Check the statistics with:

```
git diff --stat 2d90cb1 ':(exclude).gitlab-ci.yml' ':(exclude)CHANGELOG.md'
```

`93 files changed, 2901 insertions(+), 213 deletions(-)`

![Process of mainlining](https://cloud.3mdeb.com/index.php/s/kdk7PX3HCfzb4N6/preview)

The chart represents the total line added and deleted on the PC Engines
coreboot fork against the rebase point for a given release. Check the
statistics with:

```
git diff --stat 2d90cb1 ':(exclude).gitlab-ci.yml' ':(exclude)CHANGELOG.md'
```

`93 files changed, 2901 insertions(+), 213 deletions(-)`

Two files have not been included in the diff as mentioned above since they are
not a part of coreboot tree.

## Testing

* [PC Engines hardware configuration matrix](https://cloud.3mdeb.com/index.php/s/ce829QADwA7sHx9/preview) - hardware configurations available for testing in 3mdeb laboratory.

* [PC Engines release validation results](https://3mdeb.us16.list-manage.com/track/click?u=fce95b885fc13fbf1db611816&id=96d9b426c0&e=16ffa34a09) - please note there are separate sheets for each board-release.

Test changes in this release:
* **improved** coreboot flashing test with FTP server option
* **fixed** the python modules deprecation warning in the test infrastructure
* **started** the migration of test infrastructure to python3

![Mainline test results](https://cloud.3mdeb.com/index.php/s/bfFnytdiXA5oBJq/preview)

![Legacy test results](https://cloud.3mdeb.com/index.php/s/DGLG6wdX9E33A4o/preview)

* Mainline:
  * PASSED: **424** (-1)
  * FAILED: **13** (+1)
  * PASSED [%]: **97.03%** (-0.22%)

* Legacy:
  * PASSED: **372** (no changes)
  * FAILED: **10** (no changes)
  * PASSED [%]: **97.38%** (no changes)

This release does not have tests changes, therefore there is nearly no
difference in the aggregated statistics. Slightly worse tests performance on
`FAILED` tests results from the on-going USB detection problem.

## Binaries

### Mainline

* [apu1 v4.10.0.3.zip](https://3mdeb.com/open-source-firmware/pcengines/apu1/apu1_v4.10.0.3.zip)

  [apu1 v4.10.0.3.rom](https://3mdeb.com/open-source-firmware/pcengines/apu1/apu1_v4.10.0.3.rom)

  [SHA256 file](https://3mdeb.com/open-source-firmware/pcengines/apu1/apu1_v4.10.0.3.SHA256)

  [SHA256 sig](https://3mdeb.com/open-source-firmware/pcengines/apu1/apu1_v4.10.0.3.SHA256.sig)

* [apu2 v4.10.0.3.zip](https://3mdeb.com/open-source-firmware/pcengines/apu2/apu2_v4.10.0.3.zip)

  [apu2 v4.10.0.3.rom](https://3mdeb.com/open-source-firmware/pcengines/apu2/apu2_v4.10.0.3.rom)

  [SHA256 file](https://3mdeb.com/open-source-firmware/pcengines/apu2/apu2_v4.10.0.3.SHA256)

  [SHA256 sig](https://3mdeb.com/open-source-firmware/pcengines/apu2/apu2_v4.10.0.3.SHA256.sig)

* [apu3 v4.10.0.3.zip](https://3mdeb.com/open-source-firmware/pcengines/apu3/apu3_v4.10.0.3.zip)

  [apu3 v4.10.0.3.rom](https://3mdeb.com/open-source-firmware/pcengines/apu3/apu3_v4.10.0.3.rom)

  [SHA256 file](https://3mdeb.com/open-source-firmware/pcengines/apu3/apu3_v4.10.0.3.SHA256)

  [SHA256 sig](https://3mdeb.com/open-source-firmware/pcengines/apu3/apu3_v4.10.0.3.SHA256.sig)

* [apu4 v4.10.0.3.zip](https://3mdeb.com/open-source-firmware/pcengines/apu4/apu4_v4.10.0.3.zip)

  [apu4 v4.10.0.3.rom](https://3mdeb.com/open-source-firmware/pcengines/apu4/apu4_v4.10.0.3.rom)

  [SHA256 file](https://3mdeb.com/open-source-firmware/pcengines/apu4/apu4_v4.10.0.3.SHA256)

  [SHA256 sig](https://3mdeb.com/open-source-firmware/pcengines/apu4/apu4_v4.10.0.3.SHA256.sig)

* [apu5 v4.10.0.3.zip](https://3mdeb.com/open-source-firmware/pcengines/apu5/apu5_v4.10.0.3.zip)

  [apu5 v4.10.0.3.rom](https://3mdeb.com/open-source-firmware/pcengines/apu5/apu5_v4.10.0.3.rom)

  [SHA256 file](https://3mdeb.com/open-source-firmware/pcengines/apu5/apu5_v4.10.0.3.SHA256)

  [SHA256 sig](https://3mdeb.com/open-source-firmware/pcengines/apu5/apu5_v4.10.0.3.SHA256.sig)

See how to verify the signatures on [asciinema](https://asciinema.org/a/227035)

[1]: https://en.wikipedia.org/wiki/ROCA_vulnerability
[2]: https://github.com/pcengines/apu2-documentation/blob/master/docs/research/ROCA.md
[3]: https://github.com/pcengines/apu2-documentation/blob/master/docs/os-status.md

## What we planned

1. Improve the support of TPM2 in coreboot and SeaBIOS. Currently there is only
   the TCPA (TPM1.2) log support in coreboot. Additionally SeaBIOS overwrites
   existing entries in TPM2 log area. `cbmem` utility also lacks support for
   displaying TPM2 log area.

   **WORK IN PROGRESS**

2. Validate ESXi 6.7. We have got information that booting ESXi 6.7 U2 fails on
   apu2 and are investigating the issue.

   **WORK IN PROGRESS**

3. Reorganize runtime configuration by making it persistent across updates and
   accessible from user space. Also prepare a tool for offline binary
   modification.

   **WORK IN PROGRESS**

4. Vital Product Data (VPD) support. User will have possibility to store
   and change VPD configuration in Read-Write section of SPI flash. Moreover,
   default VPD keys and values will be stored in Read-Only region to protect
   data against corruption. Also, sortbootorder runtime configuration will be
   stored in VPD Read-Write section, so access to it will be possible in OS
   via dedicated util.

   **WORK IN PROGRESS**

## Coming soon

Feature and improvements on the roadmap:

1. Improve the support of TPM2 in coreboot and SeaBIOS. Currently there is only
   the TCPA (TPM1.2) log support in coreboot. Additionally SeaBIOS overwrites
   existing entries in TPM2 log area. `cbmem` utility also lacks support for
   displaying TPM2 log area.
2. Validate ESXi 6.7. We have got information that booting ESXi 6.7 U2 fails on
   apu2 and are investigating the issue.
3. Reorganize runtime configuration by making it persistent across updates and
   accessible from user space. Also prepare a tool for offline binary
   modification.
4. Vital Product Data (VPD) support. User will have possibility to store
   and change VPD configuration in Read-Write section of SPI flash. Moreover,
   default VPD keys and values will be stored in Read-Only region to protect
   data against corruption. Also, sortbootorder runtime configuration will be
   stored in VPD Read-Write section, so access to it will be possible in OS
   via dedicated util.
