---
layout: post
title:  "PC Engines apu coreboot Open Source Firmware v4.12.0.3"
date:   2020-07-31
categories: Firmware
---
# PC Engines apu coreboot Open Source Firmware v4.12.0.3

## Key changes

Mainline:

1. **Rebased** with official coreboot repository **commit** 8d5cedf.
2. **Fixed** memory speed values in the DMI table. Previous values were the
speed of the bus not the memory thus it was 2 times smaller.
3. **Fixed** cbmem error caused by wrong ACPI table.
4. **Updated** sortbootorder to version 4.6.19 with an option in the runtime
configuration allowing to reverse PCI addressing order. Previously, if a new PCI
device was added to the PCIe slot, all other devices' addresses were incremented,
which could result in renaming the Ethernet interfaces.

Legacy:
1. **Updated** sortbootorder to version 4.6.19 with an option in the runtime
configuration allowing to reverse PCI addressing order. Previously, if a new PCI
device was added to the PCIe slot, all other devices' addresses were incremented,
which could result in renaming the Ethernet interfaces.


**Total:**

* 6 lines added

in official coreboot repository.

## Statistics

![Files Changed](https://cloud.3mdeb.com/index.php/s/JRiyzzy2se8mLaz/preview)

The chart shows the total files changed from release tag against the rebase
point of given release specified in CHANGELOG (CHANGELOG.md, gitlab-ci.yml and
gitlab-ci/regression.sh excluded from statistics). Check the statistics with:

```
git diff --stat 8d5cedf ':(exclude).gitlab-ci.yml' ':(exclude)CHANGELOG.md' ':(exclude).gitlab-ci/regression.sh'
```

`103 files changed, 4043 insertions(+), 422 deletions(-)`

![Process of mainlining](https://cloud.3mdeb.com/index.php/s/caZ45Mn9pwYTWsY/preview)

The chart represents the total line added and deleted on the PC Engines
coreboot fork against the rebase point for a given release.

Three files have not been included in the diff as mentioned above since they are
not a part of coreboot tree.

The number of changes increased significantly, due to the TrenchBoot project development.


## Testing

* [PC Engines hardware configuration matrix](https://cloud.3mdeb.com/index.php/s/LMfrmjTgXc9tdxR/preview) - hardware configurations available for testing in 3mdeb laboratory.

* [PC Engines release validation results](https://3mdeb.us16.list-manage.com/track/click?u=fce95b885fc13fbf1db611816&id=96d9b426c0&e=16ffa34a09) - please note there are separate sheets for each board-release.

![Mainline test results](https://cloud.3mdeb.com/index.php/s/sSPC8eeo8ioGfPT/preview)

* Mainline:
  * PASSED: **440** (0)
  * FAILED: **12** (+3)
  * PASSED [%]: **97.35** (-0.21%)

![Legacy test results](https://cloud.3mdeb.com/index.php/s/L9yb5jiQBZxNoap/preview)

* Legacy:
  * PASSED: **385** (0)
  * FAILED: **47** (+3)
  * PASSED [%]: **98.18** (-0.79%)

No particular changes in tests in this release. Regression didn't detect new
bugs. Decreased pass ratio for mainline has been caused by random Xen booting
problems. Legacy has increased pass percentage due to fixed cold boot watchdog
problem. There were some failures due to USD stick malfunction.

## Binaries

### Mainline

* [apu1 v4.12.0.3.zip](https://3mdeb.com/open-source-firmware/pcengines/apu1/apu1_v4.12.0.3.zip)

  [apu1 v4.12.0.3.rom](https://3mdeb.com/open-source-firmware/pcengines/apu1/apu1_v4.12.0.3.rom)

  [SHA256 file](https://3mdeb.com/open-source-firmware/pcengines/apu1/apu1_v4.12.0.3.SHA256)

  [SHA256 sig](https://3mdeb.com/open-source-firmware/pcengines/apu1/apu1_v4.12.0.3.SHA256.sig)

* [apu2 v4.12.0.3.zip](https://3mdeb.com/open-source-firmware/pcengines/apu2/apu2_v4.12.0.3.zip)

  [apu2 v4.12.0.3.rom](https://3mdeb.com/open-source-firmware/pcengines/apu2/apu2_v4.12.0.3.rom)

  [SHA256 file](https://3mdeb.com/open-source-firmware/pcengines/apu2/apu2_v4.12.0.3.SHA256)

  [SHA256 sig](https://3mdeb.com/open-source-firmware/pcengines/apu2/apu2_v4.12.0.3.SHA256.sig)

* [apu3 v4.12.0.3.zip](https://3mdeb.com/open-source-firmware/pcengines/apu3/apu3_v4.12.0.3.zip)

  [apu3 v4.12.0.3.rom](https://3mdeb.com/open-source-firmware/pcengines/apu3/apu3_v4.12.0.3.rom)

  [SHA256 file](https://3mdeb.com/open-source-firmware/pcengines/apu3/apu3_v4.12.0.3.SHA256)

  [SHA256 sig](https://3mdeb.com/open-source-firmware/pcengines/apu3/apu3_v4.12.0.3.SHA256.sig)

* [apu4 v4.12.0.3.zip](https://3mdeb.com/open-source-firmware/pcengines/apu4/apu4_v4.12.0.3.zip)

  [apu4 v4.12.0.3.rom](https://3mdeb.com/open-source-firmware/pcengines/apu4/apu4_v4.12.0.3.rom)

  [SHA256 file](https://3mdeb.com/open-source-firmware/pcengines/apu4/apu4_v4.12.0.3.SHA256)

  [SHA256 sig](https://3mdeb.com/open-source-firmware/pcengines/apu4/apu4_v4.12.0.3.SHA256.sig)

* [apu5 v4.12.0.3.zip](https://3mdeb.com/open-source-firmware/pcengines/apu5/apu5_v4.12.0.3.zip)

  [apu5 v4.12.0.3.rom](https://3mdeb.com/open-source-firmware/pcengines/apu5/apu5_v4.12.0.3.rom)

  [SHA256 file](https://3mdeb.com/open-source-firmware/pcengines/apu5/apu5_v4.12.0.3.SHA256)

  [SHA256 sig](https://3mdeb.com/open-source-firmware/pcengines/apu5/apu5_v4.12.0.3.SHA256.sig)

See how to verify the signatures on [asciinema](https://asciinema.org/a/335785)

### Legacy

* [apu2 v4.0.32.zip](https://3mdeb.com/open-source-firmware/pcengines/apu2/apu2_v4.0.32.zip)

  [apu2 v4.0.32.rom](https://3mdeb.com/open-source-firmware/pcengines/apu2/apu2_v4.0.32.rom)

  [SHA256 file](https://3mdeb.com/open-source-firmware/pcengines/apu2/apu2_v4.0.32.SHA256)

  [SHA256 sig](https://3mdeb.com/open-source-firmware/pcengines/apu2/apu2_v4.0.32.SHA256.sig)

* [apu3 v4.0.32.zip](https://3mdeb.com/open-source-firmware/pcengines/apu3/apu3_v4.0.32.zip)

  [apu3 v4.0.32.rom](https://3mdeb.com/open-source-firmware/pcengines/apu3/apu3_v4.0.32.rom)

  [SHA256 file](https://3mdeb.com/open-source-firmware/pcengines/apu3/apu3_v4.0.32.SHA256)

  [SHA256 sig](https://3mdeb.com/open-source-firmware/pcengines/apu3/apu3_v4.0.32.SHA256.sig)

* [apu4 v4.0.32.zip](https://3mdeb.com/open-source-firmware/pcengines/apu4/apu4_v4.0.32.zip)

  [apu4 v4.0.32.rom](https://3mdeb.com/open-source-firmware/pcengines/apu4/apu4_v4.0.32.rom)

  [SHA256 file](https://3mdeb.com/open-source-firmware/pcengines/apu4/apu4_v4.0.32.SHA256)

  [SHA256 sig](https://3mdeb.com/open-source-firmware/pcengines/apu4/apu4_v4.0.32.SHA256.sig)

* [apu5 v4.0.32.zip](https://3mdeb.com/open-source-firmware/pcengines/apu5/apu5_v4.0.32.zip)

  [apu5 v4.0.32.rom](https://3mdeb.com/open-source-firmware/pcengines/apu5/apu5_v4.0.32.rom)

  [SHA256 file](https://3mdeb.com/open-source-firmware/pcengines/apu5/apu5_v4.0.32.SHA256)

  [SHA256 sig](https://3mdeb.com/open-source-firmware/pcengines/apu5/apu5_v4.0.32.SHA256.sig)

See how to verify the signatures on [asciinema](https://asciinema.org/a/303584)

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
