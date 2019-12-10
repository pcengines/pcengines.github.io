---
layout: post
title:  "PC Engines apu coreboot Open Source Firmware v4.11.0.1"
date:   2019-12-10
categories: Firmware
---
# PC Engines apu coreboot Open Source Firmware v4.11.0.1

## Key changes

Mainline:

1. **Rebased** with official coreboot repository **commit** 9f56eed.
2. **Temperature** is now being **showed in pfSense** dashboard.

## coreboot community

Recent month was focused mainly on contribution to official coreboot repository
in order to keep PC Engines boards in the tree. Recent coreboot release is
enforcing certain features that board/silicon must support in order to be
maintained on the master branch. Here is the list of patches sent for review
and merged in order to achieve the goal.

Patches sent for review:

* [AGESA, binaryPI: implement C bootblock](https://review.coreboot.org/c/coreboot/+/36914)

* [sb/amd/{agesa,pi}: use ACPIMMIO common block wherever possible](https://review.coreboot.org/c/coreboot/+/37400)

* [pcengines/apu2: Switch away from ROMCC_BOOTBLOCK](https://review.coreboot.org/c/coreboot/+/36915)

* [pcengines/apu1: Switch away from ROMCC_BOOTBLOCK](https://review.coreboot.org/c/coreboot/+/37332)

* [amdblocks/pci: add common implementation of MMCONF enabling](https://review.coreboot.org/c/coreboot/+/37552)

* [mb/\*/\*: use ACPIMMIO common block wherever possible](https://review.coreboot.org/c/coreboot/+/37401)

Patches merged by community:

* [cpu/amd/{agesa,pi}/Kconfig: select SSE2](https://review.coreboot.org/c/coreboot/+/37292)

* [sb/amd/{agesa,pi}/hudson: enable support for AMD common ACPIMMIO blocks](https://review.coreboot.org/c/coreboot/+/37177)

* [binaryPI: Use Kconfig to define the number of IOAPICs](https://review.coreboot.org/c/coreboot/+/37169)

* [amd/pi/00730F01: Add support without BINARYPI_LEGACY_WRAPPER](https://review.coreboot.org/c/coreboot/+/32421)

* [vendorcode/amd/pi/Makefile.inc: remove -fno-zero-initialized-in-bss](https://review.coreboot.org/c/coreboot/+/36976)

* [pcengines/apu2: Switch away from BINARYPI_LEGACY_WRAPPER](https://review.coreboot.org/c/coreboot/+/32363)

* [sb/amd/{agesa,pi}/hudson: add southbridge C bootblock initialization](https://review.coreboot.org/c/coreboot/+/37168)

* [sb/amd/cimx/sb800: add C bootblock southbridge initialization](https://review.coreboot.org/c/coreboot/+/37329)

* [amdblocks/acpimmio: add common functions for AP entry](https://review.coreboot.org/c/coreboot/+/37416)

* [amdblocks/acpimmio: Unify BIOSRAM usage](https://review.coreboot.org/c/coreboot/+/37402)

* [soc/amd/common/block/acpimmio: fix ACPIMMIO decode enable function](https://review.coreboot.org/c/coreboot/+/37178)

* [sb/amd/cimx: replace cimx_util with common ACPIMMIO AMD block](https://review.coreboot.org/c/coreboot/+/37328)

* [AGESA,binaryPI: Fix stack location on entry to romstage](https://review.coreboot.org/c/coreboot/+/37351)

* [AGESA,binaryPI: Remove \_\_x86_64\_\_ long mode in CAR](https://review.coreboot.org/c/coreboot/+/37350)

* [AGESA,binaryPI: Remove redundant SSE enable](https://review.coreboot.org/c/coreboot/+/37349)

## Statistics

![Files Changed](https://cloud.3mdeb.com/index.php/s/fx55cpRb2ScwLgf/preview)

The chart shows the total files changed from release tag against the rebase
point of given release specified in CHANGELOG (CHANGELOG.md and gitlab-ci.yml
excluded from statistics). Check the statistics with:

```
git diff --stat 9f56eed ':(exclude).gitlab-ci.yml' ':(exclude)CHANGELOG.md'
```

`97 files changed, 3219 insertions(+), 413 deletions(-)`

![Process of mainlining](https://cloud.3mdeb.com/index.php/s/95MLrFL7g2TpDJD/preview)

The chart represents the total line added and deleted on the PC Engines
coreboot fork against the rebase point for a given release. Check the
statistics with:

```
git diff --stat 9f56eed ':(exclude).gitlab-ci.yml' ':(exclude)CHANGELOG.md'
```

`97 files changed, 3219 insertions(+), 413 deletions(-)`

Two files have not been included in the diff as mentioned above since they are
not a part of coreboot tree.

## Testing

* [PC Engines hardware configuration matrix](https://cloud.3mdeb.com/index.php/s/ce829QADwA7sHx9/preview) - hardware configurations available for testing in 3mdeb laboratory.

* [PC Engines release validation results](https://3mdeb.us16.list-manage.com/track/click?u=fce95b885fc13fbf1db611816&id=96d9b426c0&e=16ffa34a09) - please note there are separate sheets for each board-release.

There are no test changes in this release.

![Mainline test results](https://cloud.3mdeb.com/index.php/s/Mx69zQBScReaDtK/preview)

* Mainline:
  * PASSED: **427** (-1)
  * FAILED: **10** (+1)
  * PASSED [%]: **97.71%** (-0.23%)

This release does not have tests changes, therefore there is slight difference
in the aggregated statistics. Slightly worse overall `PASSED` tests percentage
results from the on-going random USB detection problem and TinyCore boot
stability, whether it will affect the current iteration or not.

## Binaries

### Mainline

* [apu1 v4.11.0.1.zip](https://3mdeb.com/open-source-firmware/pcengines/apu1/apu1_v4.11.0.1.zip)

  [apu1 v4.11.0.1.rom](https://3mdeb.com/open-source-firmware/pcengines/apu1/apu1_v4.11.0.1.rom)

  [SHA256 file](https://3mdeb.com/open-source-firmware/pcengines/apu1/apu1_v4.11.0.1.SHA256)

  [SHA256 sig](https://3mdeb.com/open-source-firmware/pcengines/apu1/apu1_v4.11.0.1.SHA256.sig)

* [apu2 v4.11.0.1.zip](https://3mdeb.com/open-source-firmware/pcengines/apu2/apu2_v4.11.0.1.zip)

  [apu2 v4.11.0.1.rom](https://3mdeb.com/open-source-firmware/pcengines/apu2/apu2_v4.11.0.1.rom)

  [SHA256 file](https://3mdeb.com/open-source-firmware/pcengines/apu2/apu2_v4.11.0.1.SHA256)

  [SHA256 sig](https://3mdeb.com/open-source-firmware/pcengines/apu2/apu2_v4.11.0.1.SHA256.sig)

* [apu3 v4.11.0.1.zip](https://3mdeb.com/open-source-firmware/pcengines/apu3/apu3_v4.11.0.1.zip)

  [apu3 v4.11.0.1.rom](https://3mdeb.com/open-source-firmware/pcengines/apu3/apu3_v4.11.0.1.rom)

  [SHA256 file](https://3mdeb.com/open-source-firmware/pcengines/apu3/apu3_v4.11.0.1.SHA256)

  [SHA256 sig](https://3mdeb.com/open-source-firmware/pcengines/apu3/apu3_v4.11.0.1.SHA256.sig)

* [apu4 v4.11.0.1.zip](https://3mdeb.com/open-source-firmware/pcengines/apu4/apu4_v4.11.0.1.zip)

  [apu4 v4.11.0.1.rom](https://3mdeb.com/open-source-firmware/pcengines/apu4/apu4_v4.11.0.1.rom)

  [SHA256 file](https://3mdeb.com/open-source-firmware/pcengines/apu4/apu4_v4.11.0.1.SHA256)

  [SHA256 sig](https://3mdeb.com/open-source-firmware/pcengines/apu4/apu4_v4.11.0.1.SHA256.sig)

* [apu5 v4.11.0.1.zip](https://3mdeb.com/open-source-firmware/pcengines/apu5/apu5_v4.11.0.1.zip)

  [apu5 v4.11.0.1.rom](https://3mdeb.com/open-source-firmware/pcengines/apu5/apu5_v4.11.0.1.rom)

  [SHA256 file](https://3mdeb.com/open-source-firmware/pcengines/apu5/apu5_v4.11.0.1.SHA256)

  [SHA256 sig](https://3mdeb.com/open-source-firmware/pcengines/apu5/apu5_v4.11.0.1.SHA256.sig)

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
