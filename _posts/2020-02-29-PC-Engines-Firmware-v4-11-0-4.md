---
layout: post
title:  "PC Engines apu coreboot Open Source Firmware v4.11.0.4"
date:   2020-02-29
categories: Firmware
---
# PC Engines apu coreboot Open Source Firmware v4.11.0.4

## Key changes

Mainline:

1. **Rebased** with official coreboot repository **commit** e53f8c9.
2. Fixed **SD card boot order** on apu5.
3. Added **ARM management controller interaction** on apu5.
4. The **new PC Engines Open Source Firmware Release 4.10 Signing Key** has
   been enrolled and all coreboot v4.11.0.x versions are signed by this key.
   See how to verify the image with new key on [asciinema.](https://asciinema.org/a/303584)

Legacy:

1. Fixed **SD card boot order** on apu5.
2. Added **ARM management controller interaction** on apu5.
3. The **new PC Engines Open Source Firmware Release 4.10 Signing Key** has
   been enrolled and coreboot v4.0.30 and later versions will be signed by this key.
   See how to verify the image with new key on [asciinema.](https://asciinema.org/a/303584)

## coreboot community

Patches sent for review:

* [mb/pcengines/*/devicetree: remove non-existing NCT5104d LDN 0xe](https://review.coreboot.org/c/coreboot/+/38851)
* [nb/amd/{agesa,pi}/acpi: include thermal zone](https://review.coreboot.org/c/coreboot/+/38755)
* [superio/nuvoton/nct5104d: add chip config option to reset GPIOs](https://review.coreboot.org/c/coreboot/+/38850)

Patches merged by community:

* [mb/pcengines/apu2: use AGESA 1.0.0.4 with adjusted AGESA header](https://review.coreboot.org/c/coreboot/+/35906)
* [sb/amd/{agesa,pi}/hudson/Kconfig: Change default SATA mode to AHCI](https://review.coreboot.org/c/coreboot/+/35891)
* [nb/amd/pi/00730F01: enable ACS and AER for PCIe ports](https://review.coreboot.org/c/coreboot/+/35313)

**Total:**

* 51 lines added,
* 2 lines removed,

to official coreboot repository.

## Statistics

![Files Changed](https://3mdeb.com/open-source-firmware/files-changed-v4.11.0.4.png)

The chart shows the total files changed from release tag against the rebase
point of given release specified in CHANGELOG (CHANGELOG.md and gitlab-ci.yml
excluded from statistics). Check the statistics with:

```
git diff --stat e53f8c9 ':(exclude).gitlab-ci.yml' ':(exclude)CHANGELOG.md'
```

`93 files changed, 3158 insertions(+), 366 deletions(-)`

![Process of mainlining](https://3mdeb.com/open-source-firmware/process-of-mainlining-v4.11.0.4.png)

The chart represents the total line added and deleted on the PC Engines
coreboot fork against the rebase point for a given release. Check the
statistics with:

```
git diff --stat e53f8c9 ':(exclude).gitlab-ci.yml' ':(exclude)CHANGELOG.md'
```

`93 files changed, 3158 insertions(+), 366 deletions(-)`

Two files have not been included in the diff as mentioned above since they are
not a part of coreboot tree.

The number of changes increased due to SD boot order fix on apu5.

## Testing

* [PC Engines hardware configuration matrix](https://cloud.3mdeb.com/index.php/s/ce829QADwA7sHx9/preview) - hardware configurations available for testing in 3mdeb laboratory.

* [PC Engines release validation results](https://3mdeb.us16.list-manage.com/track/click?u=fce95b885fc13fbf1db611816&id=96d9b426c0&e=16ffa34a09) - please note there are separate sheets for each board-release.

Test changes in this release:
* enabled SD cards tests on apu5

![Mainline test results](https://3mdeb.com/open-source-firmware/mainline-test-results-v4.11.0.4.png)

* Mainline:
  * PASSED: **433** (+4)
  * FAILED: **22** (+2)
  * PASSED [%]: **95.16%** (-0.39%)

Slightly worse overall `PASSED` tests percentage results from the on-going
random USB detection problem and TinyCore boot stability. The increased number
of PASSED tests is a result of enabling SD card tests on apu5.

![Legacy test results](https://3mdeb.com/open-source-firmware/legacy-test-results-v4.0.30.png)

* Legacy:
  * PASSED: **379** (+7)
  * FAILED: **13** (+3)
  * PASSED [%]: **96.68%%** (-0.7%)

Slightly worse overall `PASSED` tests percentage results from the on-going
random USB detection problem and TinyCore boot stability. The increased number
of PASSED tests is a result of enabling SD card tests on apu5.

## Binaries

### Mainline

* [apu1 v4.11.0.4.zip](https://3mdeb.com/open-source-firmware/pcengines/apu1/apu1_v4.11.0.4.zip)

  [apu1 v4.11.0.4.rom](https://3mdeb.com/open-source-firmware/pcengines/apu1/apu1_v4.11.0.4.rom)

  [SHA256 file](https://3mdeb.com/open-source-firmware/pcengines/apu1/apu1_v4.11.0.4.SHA256)

  [SHA256 sig](https://3mdeb.com/open-source-firmware/pcengines/apu1/apu1_v4.11.0.4.SHA256.sig)

* [apu2 v4.11.0.4.zip](https://3mdeb.com/open-source-firmware/pcengines/apu2/apu2_v4.11.0.4.zip)

  [apu2 v4.11.0.4.rom](https://3mdeb.com/open-source-firmware/pcengines/apu2/apu2_v4.11.0.4.rom)

  [SHA256 file](https://3mdeb.com/open-source-firmware/pcengines/apu2/apu2_v4.11.0.4.SHA256)

  [SHA256 sig](https://3mdeb.com/open-source-firmware/pcengines/apu2/apu2_v4.11.0.4.SHA256.sig)

* [apu3 v4.11.0.4.zip](https://3mdeb.com/open-source-firmware/pcengines/apu3/apu3_v4.11.0.4.zip)

  [apu3 v4.11.0.4.rom](https://3mdeb.com/open-source-firmware/pcengines/apu3/apu3_v4.11.0.4.rom)

  [SHA256 file](https://3mdeb.com/open-source-firmware/pcengines/apu3/apu3_v4.11.0.4.SHA256)

  [SHA256 sig](https://3mdeb.com/open-source-firmware/pcengines/apu3/apu3_v4.11.0.4.SHA256.sig)

* [apu4 v4.11.0.4.zip](https://3mdeb.com/open-source-firmware/pcengines/apu4/apu4_v4.11.0.4.zip)

  [apu4 v4.11.0.4.rom](https://3mdeb.com/open-source-firmware/pcengines/apu4/apu4_v4.11.0.4.rom)

  [SHA256 file](https://3mdeb.com/open-source-firmware/pcengines/apu4/apu4_v4.11.0.4.SHA256)

  [SHA256 sig](https://3mdeb.com/open-source-firmware/pcengines/apu4/apu4_v4.11.0.4.SHA256.sig)

* [apu5 v4.11.0.4.zip](https://3mdeb.com/open-source-firmware/pcengines/apu5/apu5_v4.11.0.4.zip)

  [apu5 v4.11.0.4.rom](https://3mdeb.com/open-source-firmware/pcengines/apu5/apu5_v4.11.0.4.rom)

  [SHA256 file](https://3mdeb.com/open-source-firmware/pcengines/apu5/apu5_v4.11.0.4.SHA256)

  [SHA256 sig](https://3mdeb.com/open-source-firmware/pcengines/apu5/apu5_v4.11.0.4.SHA256.sig)

See how to verify the signatures on [asciinema](https://asciinema.org/a/303584)

### Legacy

* [apu2 v4.0.30.zip](https://3mdeb.com/open-source-firmware/pcengines/apu2/apu2_v4.0.30.zip)

  [apu2 v4.0.30.rom](https://3mdeb.com/open-source-firmware/pcengines/apu2/apu2_v4.0.30.rom)

  [SHA256 file](https://3mdeb.com/open-source-firmware/pcengines/apu2/apu2_v4.0.30.SHA256)

  [SHA256 sig](https://3mdeb.com/open-source-firmware/pcengines/apu2/apu2_v4.0.30.SHA256.sig)

* [apu3 v4.0.30.zip](https://3mdeb.com/open-source-firmware/pcengines/apu3/apu3_v4.0.30.zip)

  [apu3 v4.0.30.rom](https://3mdeb.com/open-source-firmware/pcengines/apu3/apu3_v4.0.30.rom)

  [SHA256 file](https://3mdeb.com/open-source-firmware/pcengines/apu3/apu3_v4.0.30.SHA256)

  [SHA256 sig](https://3mdeb.com/open-source-firmware/pcengines/apu3/apu3_v4.0.30.SHA256.sig)

* [apu4 v4.0.30.zip](https://3mdeb.com/open-source-firmware/pcengines/apu4/apu4_v4.0.30.zip)

  [apu4 v4.0.30.rom](https://3mdeb.com/open-source-firmware/pcengines/apu4/apu4_v4.0.30.rom)

  [SHA256 file](https://3mdeb.com/open-source-firmware/pcengines/apu4/apu4_v4.0.30.SHA256)

  [SHA256 sig](https://3mdeb.com/open-source-firmware/pcengines/apu4/apu4_v4.0.30.SHA256.sig)

* [apu5 v4.0.30.zip](https://3mdeb.com/open-source-firmware/pcengines/apu5/apu5_v4.0.30.zip)

  [apu5 v4.0.30.rom](https://3mdeb.com/open-source-firmware/pcengines/apu5/apu5_v4.0.30.rom)

  [SHA256 file](https://3mdeb.com/open-source-firmware/pcengines/apu5/apu5_v4.0.30.SHA256)

  [SHA256 sig](https://3mdeb.com/open-source-firmware/pcengines/apu5/apu5_v4.0.30.SHA256.sig)

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

   **WORK IN PROGRESS**

3. Vital Product Data (VPD) support. User will have possibility to store
   and change VPD configuration in Read-Write section of SPI flash. Moreover,
   default VPD keys and values will be stored in Read-Only region to protect
   data against corruption. Also, sortbootorder runtime configuration will be
   stored in VPD Read-Write section, so access to it will be possible in OS
   via dedicated util.

   **VERIFICATION**

4. ACPI Thermal Zones implementation. BSD systems suffer from lack of Thermal
   Zones and lack of temperature status on the dashboards of router
   distributions of BSD systems.

   **PATCH SENT TO COREBOOT**

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
