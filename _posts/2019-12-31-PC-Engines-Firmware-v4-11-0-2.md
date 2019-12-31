---
layout: post
title:  "PC Engines apu coreboot Open Source Firmware v4.11.0.2"
date:   2019-12-31
categories: Firmware
---
# PC Engines apu coreboot Open Source Firmware v4.11.0.2

## Key changes

Mainline:

1. **Rebased** with official coreboot repository **commit** 536799d.
2. **Updated** sortbootorder to **v4.6.16** bringing **IOMMU runtime**
   **configuration** and **board autodetection** in the top banner of setup
   menu.
3. **Fixed** [issue](https://github.com/pcengines/coreboot/issues/356) with booting
   **OpenBSD 6.6** on v4.11.0.1 firmware.
4. PC Engines **platforms reached** all the **requirements** necessary to **stay in the**
   official **coreboot tree**.

## coreboot community

Patches sent for review:

* [amd/agesa/state_machine: Add BeforeInitLate hooks](https://review.coreboot.org/c/coreboot/+/37998)

* [nb/amd/pi/00730F01/state_machine: Add lost options](https://review.coreboot.org/c/coreboot/+/37999)

Patches merged by community:

* [AGESA, binaryPI: implement C bootblock](https://review.coreboot.org/c/coreboot/+/36914)

* [pcengines/apu2: Switch away from ROMCC_BOOTBLOCK](https://review.coreboot.org/c/coreboot/+/36915)

* [pcengines/apu1: Switch away from ROMCC_BOOTBLOCK](https://review.coreboot.org/c/coreboot/+/37332)

* [amdblocks/pci: add common implementation of MMCONF enabling](https://review.coreboot.org/c/coreboot/+/37552)

* [AMD {SoC, AGESA, binaryPI}: Don't use both of _ADR and _HID](https://review.coreboot.org/c/coreboot/+/37835)

## Statistics

![Files Changed](https://cloud.3mdeb.com/index.php/s/yTQrwdqCfsjLYqL/preview)

The chart shows the total files changed from release tag against the rebase
point of given release specified in CHANGELOG (CHANGELOG.md and gitlab-ci.yml
excluded from statistics). Check the statistics with:

```
git diff --stat 536799d ':(exclude).gitlab-ci.yml' ':(exclude)CHANGELOG.md'
```

`100 files changed, 3252 insertions(+), 424 deletions(-)`

![Process of mainlining](https://cloud.3mdeb.com/index.php/s/szWeD85ggoHikdY/preview)

The chart represents the total line added and deleted on the PC Engines
coreboot fork against the rebase point for a given release. Check the
statistics with:

```
git diff --stat 536799d ':(exclude).gitlab-ci.yml' ':(exclude)CHANGELOG.md'
```

`100 files changed, 3252 insertions(+), 424 deletions(-)`

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

* [apu1 v4.11.0.2.zip](https://3mdeb.com/open-source-firmware/pcengines/apu1/apu1_v4.11.0.2.zip)

  [apu1 v4.11.0.2.rom](https://3mdeb.com/open-source-firmware/pcengines/apu1/apu1_v4.11.0.2.rom)

  [SHA256 file](https://3mdeb.com/open-source-firmware/pcengines/apu1/apu1_v4.11.0.2.SHA256)

  [SHA256 sig](https://3mdeb.com/open-source-firmware/pcengines/apu1/apu1_v4.11.0.2.SHA256.sig)

* [apu2 v4.11.0.2.zip](https://3mdeb.com/open-source-firmware/pcengines/apu2/apu2_v4.11.0.2.zip)

  [apu2 v4.11.0.2.rom](https://3mdeb.com/open-source-firmware/pcengines/apu2/apu2_v4.11.0.2.rom)

  [SHA256 file](https://3mdeb.com/open-source-firmware/pcengines/apu2/apu2_v4.11.0.2.SHA256)

  [SHA256 sig](https://3mdeb.com/open-source-firmware/pcengines/apu2/apu2_v4.11.0.2.SHA256.sig)

* [apu3 v4.11.0.2.zip](https://3mdeb.com/open-source-firmware/pcengines/apu3/apu3_v4.11.0.2.zip)

  [apu3 v4.11.0.2.rom](https://3mdeb.com/open-source-firmware/pcengines/apu3/apu3_v4.11.0.2.rom)

  [SHA256 file](https://3mdeb.com/open-source-firmware/pcengines/apu3/apu3_v4.11.0.2.SHA256)

  [SHA256 sig](https://3mdeb.com/open-source-firmware/pcengines/apu3/apu3_v4.11.0.2.SHA256.sig)

* [apu4 v4.11.0.2.zip](https://3mdeb.com/open-source-firmware/pcengines/apu4/apu4_v4.11.0.2.zip)

  [apu4 v4.11.0.2.rom](https://3mdeb.com/open-source-firmware/pcengines/apu4/apu4_v4.11.0.2.rom)

  [SHA256 file](https://3mdeb.com/open-source-firmware/pcengines/apu4/apu4_v4.11.0.2.SHA256)

  [SHA256 sig](https://3mdeb.com/open-source-firmware/pcengines/apu4/apu4_v4.11.0.2.SHA256.sig)

* [apu5 v4.11.0.2.zip](https://3mdeb.com/open-source-firmware/pcengines/apu5/apu5_v4.11.0.2.zip)

  [apu5 v4.11.0.2.rom](https://3mdeb.com/open-source-firmware/pcengines/apu5/apu5_v4.11.0.2.rom)

  [SHA256 file](https://3mdeb.com/open-source-firmware/pcengines/apu5/apu5_v4.11.0.2.SHA256)

  [SHA256 sig](https://3mdeb.com/open-source-firmware/pcengines/apu5/apu5_v4.11.0.2.SHA256.sig)

See how to verify the signatures on [asciinema](https://asciinema.org/a/227035)

## What we planned

1. Improve the support of TPM2 in coreboot and SeaBIOS. Currently there is only
   the TCPA (TPM1.2) log support in coreboot. Additionally SeaBIOS overwrites
   existing entries in TPM2 log area. `cbmem` utility also lacks support for
   displaying TPM2 log area.

   **WORK IN PROGRESS**

2. Validate ESXi 6.7. We have got information that booting ESXi 6.7 U2 fails on
   apu2 and are investigating the issue.

   **DONE**

   The problem lies in the incorrectly written bootloader by VMWare. An issue
   has been created with explanation of the problem:
   https://github.com/vmware/esx-boot/issues/4

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
2. Reorganize runtime configuration by making it persistent across updates and
   accessible from user space. Also prepare a tool for offline binary
   modification.
3. Vital Product Data (VPD) support. User will have possibility to store
   and change VPD configuration in Read-Write section of SPI flash. Moreover,
   default VPD keys and values will be stored in Read-Only region to protect
   data against corruption. Also, sortbootorder runtime configuration will be
   stored in VPD Read-Write section, so access to it will be possible in OS
   via dedicated util.
