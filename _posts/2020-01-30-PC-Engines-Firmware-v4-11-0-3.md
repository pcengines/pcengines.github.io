---
layout: post
title:  "PC Engines apu coreboot Open Source Firmware v4.11.0.3"
date:   2020-01-30
categories: Firmware
---
# PC Engines apu coreboot Open Source Firmware v4.11.0.3

## Key changes

Mainline:

1. **Rebased** with official coreboot repository **commit** 98eeb96.
2. **Updated** sortbootorder to **v4.6.17** fixing PS2 keyboard error.

## coreboot community

Patches sent for review:

* [mb/pcengines/apu1/mainboard.c: Add SMBIOS type 16 and 17 entries](https://review.coreboot.org/c/coreboot/+/38343)

Patches merged by community:

* [sb/amd/{agesa,pi}: use ACPIMMIO common block wherever possible](https://review.coreboot.org/c/coreboot/+/37400)

* [amd/agesa/state_machine: Add BeforeInitLate hooks](https://review.coreboot.org/c/coreboot/+/37998)

* [nb/amd/pi/00730F01/state_machine: Add lost options](https://review.coreboot.org/c/coreboot/+/37999)

* [mb/pcengines/apu1/bootblock.c: Add possibility to redirect output to COM2](https://review.coreboot.org/c/coreboot/+/29791)

* [mb/*/*: use ACPIMMIO common block wherever possible](https://review.coreboot.org/c/coreboot/+/37401)

* [superio/nuvoton/nct5104d: Add soft reset GPIO functionality](https://review.coreboot.org/c/coreboot/+/35482)

* [mb/pcengines: Enable SuperIO LDN 0xf for GPIO soft reset](https://review.coreboot.org/c/coreboot/+/38274)

* [superio/nuvoton/nct5104d: Add virtual LDN for simple GPIO IO control](https://review.coreboot.org/c/coreboot/+/35849)

* [mb/pcengines/*: enable simple IO-based GPIO control](https://review.coreboot.org/c/coreboot/+/38275)

* [mb/pcengines/apu2/mainboard.c: Add SMBIOS type 16 and 17 entries](https://review.coreboot.org/c/coreboot/+/38342)

* [amdblocks/acpimmio: add missing MMIO functions](https://review.coreboot.org/c/coreboot/+/37813)

**Total:**

* 1131 lines added,
* 829 lines removed,

to official coreboot repository.

## Statistics

![Files Changed](https://cloud.3mdeb.com/index.php/s/6Kcnsa5pdiMHZye/preview)

The chart shows the total files changed from release tag against the rebase
point of given release specified in CHANGELOG (CHANGELOG.md and gitlab-ci.yml
excluded from statistics). Check the statistics with:

```
git diff --stat 98eeb96 ':(exclude).gitlab-ci.yml' ':(exclude)CHANGELOG.md'
```

`93 files changed, 3073 insertions(+), 395 deletions(-)`

![Process of mainlining](https://cloud.3mdeb.com/index.php/s/cdSCMYPar85DfRC/preview)

The chart represents the total line added and deleted on the PC Engines
coreboot fork against the rebase point for a given release. Check the
statistics with:

```
git diff --stat 98eeb96 ':(exclude).gitlab-ci.yml' ':(exclude)CHANGELOG.md'
```

`93 files changed, 3073 insertions(+), 395 deletions(-)`

Two files have not been included in the diff as mentioned above since they are
not a part of coreboot tree.

The number of changed files and lines decreased due to certain changes merged
by community.

## Testing

* [PC Engines hardware configuration matrix](https://cloud.3mdeb.com/index.php/s/ce829QADwA7sHx9/preview) - hardware configurations available for testing in 3mdeb laboratory.

* [PC Engines release validation results](https://3mdeb.us16.list-manage.com/track/click?u=fce95b885fc13fbf1db611816&id=96d9b426c0&e=16ffa34a09) - please note there are separate sheets for each board-release.

Test changes in this release:
* added test for Watchdog triggering reboot verification after coldboot (1 test
  case)

![Mainline test results](https://cloud.3mdeb.com/index.php/s/ffdPGTXk6mBJTiX/preview)

* Mainline:
  * PASSED: **429** (-2)
  * FAILED: **20** (+6)
  * PASSED [%]: **95.55%** (-1.30%)

Slightly worse overall `PASSED` tests percentage results from the on-going
random USB detection problem and TinyCore boot stability.

## Binaries

### Mainline

* [apu1 v4.11.0.3.zip](https://3mdeb.com/open-source-firmware/pcengines/apu1/apu1_v4.11.0.3.zip)

  [apu1 v4.11.0.3.rom](https://3mdeb.com/open-source-firmware/pcengines/apu1/apu1_v4.11.0.3.rom)

  [SHA256 file](https://3mdeb.com/open-source-firmware/pcengines/apu1/apu1_v4.11.0.3.SHA256)

  [SHA256 sig](https://3mdeb.com/open-source-firmware/pcengines/apu1/apu1_v4.11.0.3.SHA256.sig)

* [apu2 v4.11.0.3.zip](https://3mdeb.com/open-source-firmware/pcengines/apu2/apu2_v4.11.0.3.zip)

  [apu2 v4.11.0.3.rom](https://3mdeb.com/open-source-firmware/pcengines/apu2/apu2_v4.11.0.3.rom)

  [SHA256 file](https://3mdeb.com/open-source-firmware/pcengines/apu2/apu2_v4.11.0.3.SHA256)

  [SHA256 sig](https://3mdeb.com/open-source-firmware/pcengines/apu2/apu2_v4.11.0.3.SHA256.sig)

* [apu3 v4.11.0.3.zip](https://3mdeb.com/open-source-firmware/pcengines/apu3/apu3_v4.11.0.3.zip)

  [apu3 v4.11.0.3.rom](https://3mdeb.com/open-source-firmware/pcengines/apu3/apu3_v4.11.0.3.rom)

  [SHA256 file](https://3mdeb.com/open-source-firmware/pcengines/apu3/apu3_v4.11.0.3.SHA256)

  [SHA256 sig](https://3mdeb.com/open-source-firmware/pcengines/apu3/apu3_v4.11.0.3.SHA256.sig)

* [apu4 v4.11.0.3.zip](https://3mdeb.com/open-source-firmware/pcengines/apu4/apu4_v4.11.0.3.zip)

  [apu4 v4.11.0.3.rom](https://3mdeb.com/open-source-firmware/pcengines/apu4/apu4_v4.11.0.3.rom)

  [SHA256 file](https://3mdeb.com/open-source-firmware/pcengines/apu4/apu4_v4.11.0.3.SHA256)

  [SHA256 sig](https://3mdeb.com/open-source-firmware/pcengines/apu4/apu4_v4.11.0.3.SHA256.sig)

* [apu5 v4.11.0.3.zip](https://3mdeb.com/open-source-firmware/pcengines/apu5/apu5_v4.11.0.3.zip)

  [apu5 v4.11.0.3.rom](https://3mdeb.com/open-source-firmware/pcengines/apu5/apu5_v4.11.0.3.rom)

  [SHA256 file](https://3mdeb.com/open-source-firmware/pcengines/apu5/apu5_v4.11.0.3.SHA256)

  [SHA256 sig](https://3mdeb.com/open-source-firmware/pcengines/apu5/apu5_v4.11.0.3.SHA256.sig)

See how to verify the signatures on [asciinema](https://asciinema.org/a/269426)

## What we planned

1. Improve the support of TPM2 in coreboot and SeaBIOS. Currently there is only
   the TCPA (TPM1.2) log support in coreboot. Additionally SeaBIOS overwrites
   existing entries in TPM2 log area. `cbmem` utility also lacks support for
   displaying TPM2 log area.

   **WORK IN PROGRESS**

2. Reorganize runtime configuration by making it persistent across updates and
   accessible from user space. Also prepare a tool for offline binary
   modification.

   **WORK IN PROGRESS**

3. Vital Product Data (VPD) support. User will have possibility to store
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
4. ACPI Thermal Zones implementation. BSD systems suffer from lack of Thermal
   Zones and lack of temperature status on the dashboards of router
   distributions of BSD systems.
