---
layout: post
title:  "PC Engines apu coreboot Open Source Firmware v4.12.0.2"
date:   2020-06-30
categories: Firmware
---
# PC Engines apu coreboot Open Source Firmware v4.12.0.2

## Key changes

Mainline:

1. **Rebased** with official coreboot repository **commit** f183626.
2. **New revisions** of apu3 and apu4 named **apu3d** and **apu4d** will come
   with TPM header. Thus **v4.12.0.2 enables TPM 2.0** on those platforms.
3. **Fixed incorrect serial number** in dmidecode for **apu1**.
4. With the new release of coreboot 4.12 **3mdeb has a new key used for signing
   release images**: [PC Engines Open Source Firmware Release 4.12 Signing Key](https://github.com/3mdeb/3mdeb-secpack/blob/master/customer-keys/pcengines/release-keys/pcengines-open-source-firmware-release-4.12-key.asc).
   Remember to import it to your GPG (or other key management software) before
   signature verification.
5. We are cleaning up the MP table and IRQ tables for apu2 from incorrect
   entries and non-existing devices (WIP):
   https://review.coreboot.org/c/coreboot/+/42097
6. We have released a **[new canary](https://github.com/3mdeb/3mdeb-secpack/blob/master/canaries/pcengines/canary-004-2020.txt)**
   which corrects an error with 3mdeb Master Key fingerprint. Previously the
   fingerprint was mistaken with PC Engines Open Source Firmware Release 4.9
   key fingerprint.

Legacy:
1. **Fixed watchdog** not causing reset after cold boot.

## coreboot community

Patches merged by community:

* [mb/pcengines/apu2/mainboard.c: unify hexadecimal notation using capital letters](https://review.coreboot.org/c/coreboot/+/42388)

Patches sent for review:

* [mb/pcengines/apu2/mptable.c: fix invalid MP table and IRQ table](https://review.coreboot.org/c/coreboot/+/42097)

**Total:**

* 3 lines added,
* 3 lines removed,

in official coreboot repository.

## Statistics

![Files Changed](https://cloud.3mdeb.com/index.php/s/fdzToSi8m4gQCPM/preview)

The chart shows the total files changed from release tag against the rebase
point of given release specified in CHANGELOG (CHANGELOG.md and gitlab-ci.yml
excluded from statistics). Check the statistics with:

```
git diff --stat f183626 ':(exclude).gitlab-ci.yml' ':(exclude)CHANGELOG.md'
```

`103 files changed, 3829 insertions(+), 415 deletions(-)`

![Process of mainlining](https://cloud.3mdeb.com/index.php/s/ajRRHg4LABdoRi3/preview)

The chart represents the total line added and deleted on the PC Engines
coreboot fork against the rebase point for a given release.

Two files have not been included in the diff as mentioned above since they are
not a part of coreboot tree.

The number of changes increased significantly, due to the TrenchBoot project development.

## Testing

* [PC Engines hardware configuration matrix](https://cloud.3mdeb.com/index.php/s/LMfrmjTgXc9tdxR/preview) - hardware configurations available for testing in 3mdeb laboratory.

* [PC Engines release validation results](https://3mdeb.us16.list-manage.com/track/click?u=fce95b885fc13fbf1db611816&id=96d9b426c0&e=16ffa34a09) - please note there are separate sheets for each board-release.

![Mainline test results](https://cloud.3mdeb.com/index.php/s/YAgKGmCqDPLXzkY/preview)

* Mainline:
  * PASSED: **440** (-3)
  * FAILED: **11** (+3)
  * PASSED [%]: **97.56** (-0.67%)

![Legacy test results](https://cloud.3mdeb.com/index.php/s/DtBTALCqrge4bPc/preview)

* Legacy:
  * PASSED: **385** (+6)
  * FAILED: **4** (-7)
  * PASSED [%]: **98.97** (+2.29%)

No particular changes in tests in this release. Regression didn't detect new
bugs. Decreased pass ratio for mainline has been caused by random Xen booting
problems. Legacy has increased pass percentage due to fixed cold boot watchdog
problem.

## Binaries

### Mainline

* [apu1 v4.12.0.2.zip](https://3mdeb.com/open-source-firmware/pcengines/apu1/apu1_v4.12.0.2.zip)

  [apu1 v4.12.0.2.rom](https://3mdeb.com/open-source-firmware/pcengines/apu1/apu1_v4.12.0.2.rom)

  [SHA256 file](https://3mdeb.com/open-source-firmware/pcengines/apu1/apu1_v4.12.0.2.SHA256)

  [SHA256 sig](https://3mdeb.com/open-source-firmware/pcengines/apu1/apu1_v4.12.0.2.SHA256.sig)

* [apu2 v4.12.0.2.zip](https://3mdeb.com/open-source-firmware/pcengines/apu2/apu2_v4.12.0.2.zip)

  [apu2 v4.12.0.2.rom](https://3mdeb.com/open-source-firmware/pcengines/apu2/apu2_v4.12.0.2.rom)

  [SHA256 file](https://3mdeb.com/open-source-firmware/pcengines/apu2/apu2_v4.12.0.2.SHA256)

  [SHA256 sig](https://3mdeb.com/open-source-firmware/pcengines/apu2/apu2_v4.12.0.2.SHA256.sig)

* [apu3 v4.12.0.2.zip](https://3mdeb.com/open-source-firmware/pcengines/apu3/apu3_v4.12.0.2.zip)

  [apu3 v4.12.0.2.rom](https://3mdeb.com/open-source-firmware/pcengines/apu3/apu3_v4.12.0.2.rom)

  [SHA256 file](https://3mdeb.com/open-source-firmware/pcengines/apu3/apu3_v4.12.0.2.SHA256)

  [SHA256 sig](https://3mdeb.com/open-source-firmware/pcengines/apu3/apu3_v4.12.0.2.SHA256.sig)

* [apu4 v4.12.0.2.zip](https://3mdeb.com/open-source-firmware/pcengines/apu4/apu4_v4.12.0.2.zip)

  [apu4 v4.12.0.2.rom](https://3mdeb.com/open-source-firmware/pcengines/apu4/apu4_v4.12.0.2.rom)

  [SHA256 file](https://3mdeb.com/open-source-firmware/pcengines/apu4/apu4_v4.12.0.2.SHA256)

  [SHA256 sig](https://3mdeb.com/open-source-firmware/pcengines/apu4/apu4_v4.12.0.2.SHA256.sig)

* [apu5 v4.12.0.2.zip](https://3mdeb.com/open-source-firmware/pcengines/apu5/apu5_v4.12.0.2.zip)

  [apu5 v4.12.0.2.rom](https://3mdeb.com/open-source-firmware/pcengines/apu5/apu5_v4.12.0.2.rom)

  [SHA256 file](https://3mdeb.com/open-source-firmware/pcengines/apu5/apu5_v4.12.0.2.SHA256)

  [SHA256 sig](https://3mdeb.com/open-source-firmware/pcengines/apu5/apu5_v4.12.0.2.SHA256.sig)

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
