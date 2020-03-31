---
layout: post
title:  "PC Engines apu coreboot Open Source Firmware v4.11.0.5"
date:   2020-03-31
categories: Firmware
---
# PC Engines apu coreboot Open Source Firmware v4.11.0.5

## Key changes

Mainline:

1. **Rebased** with official coreboot repository **commit** 90557f4.
2. **Fixed** processors definitions and scope in **ACPI**. Partially fixed
   processor entries in ACPI previously caused issues with
   [thermal sensors on OPNSense](https://github.com/pcengines/coreboot/issues/351)
   and now it is fixed.
3. **Northbridge interrupt controller** was **not** being **initialized** in
   coreboot. Proper **initialization routine** has been **added** for this
   controller.
4. **Enabled PCIe power management capabilities**: ASPM L0s and L1, CommonClock
   and ClockPowerManagement. This should result in **lower power consumption**
   of the **apu devices**. The measurements of the power consumption and
   comparison report how the changes affect the power consumption will be
   available soon.
5. AGESA allows to reset the PCI Express endpoint during silicon
   initialization. Since apu2 has GPIOs connected to PCI Express reset signals,
   the reset logic has been implemented to reset single PCI Express devices.
   This should **improve the detection of PCI Express modules**. Test results
   of problematic modules and their detection will be published soon.
6. **Added thermal zone** definition to **ACPI** in order for operating systems
   to **automatically probe for thermal sensors** on apu2 devices.
7. **Implemented SMBIOS memory tables for apu1**.
8. **Added** missing **northbridge interrupt controller to MP table.**

## coreboot community

Patches sent for review:

* [drivers/pc80/tpm/tis.c: change the _HID and _CID for TPM2 device](https://review.coreboot.org/c/coreboot/+/39699)

Patches merged by community:

* [mb/pcengines/*/devicetree: remove non-existing NCT5104d LDN 0xe](https://review.coreboot.org/c/coreboot/+/38851)
* [nb/amd/{agesa,pi}/acpi: include thermal zone](https://review.coreboot.org/c/coreboot/+/38755)
* [superio/nuvoton/nct5104d: add chip config option to reset GPIOs](https://review.coreboot.org/c/coreboot/+/38850)
* [mb/pcengines/apu1/mainboard.c: Add SMBIOS type 16 and 17 entries](https://review.coreboot.org/c/coreboot/+/38343/)
* [nb/amd/pi/00730F01: initialize GNB IOAPIC](https://review.coreboot.org/c/coreboot/+/39700/)
* [nb/amd/pi/00730F01/state_machine.c: unhardcode IOAPIC2 address](https://review.coreboot.org/c/coreboot/+/39701)
* [mb/pcengines/apu2/mptable.c: add GNB IOAPIC to MP Table](https://review.coreboot.org/c/coreboot/+/39702/)
* [mb/pcengines/apu2: add reset logic for PCIe slots](https://review.coreboot.org/c/coreboot/+/39703/)
* [mb/pcengines/apu2: enable PCIe power management features](https://review.coreboot.org/c/coreboot/+/39704/)
* [acpi: correct the processor devices scope](https://review.coreboot.org/c/coreboot/+/39698)
* [amd/common/acpi: move thermal zone to common location](https://review.coreboot.org/c/coreboot/+/39779)
* [nb/amd/agesa/family14: Improve HTC threshold handling](https://review.coreboot.org/c/coreboot/+/39697)
* [mb/pcengines/apu2: do not pass enabled PCIe ClockPM to AGESA](https://review.coreboot.org/c/coreboot/+/39970)

**Total:**

* 492 lines added,
* 131 lines removed,

in official coreboot repository.

## Statistics

![Files Changed](https://cloud.3mdeb.com/index.php/s/rBiiDSd4annFnGG/preview)

The chart shows the total files changed from release tag against the rebase
point of given release specified in CHANGELOG (CHANGELOG.md and gitlab-ci.yml
excluded from statistics). Check the statistics with:

```
git diff --stat 90557f4 ':(exclude).gitlab-ci.yml' ':(exclude)CHANGELOG.md'
```

`88 files changed, 2840 insertions(+), 166 deletions(-)`

![Process of mainlining](https://cloud.3mdeb.com/index.php/s/co4WnMBsrw4p44R/preview)

The chart represents the total line added and deleted on the PC Engines
coreboot fork against the rebase point for a given release. Check the
statistics with:

```
git diff --stat 90557f4 ':(exclude).gitlab-ci.yml' ':(exclude)CHANGELOG.md'
```

`88 files changed, 2840 insertions(+), 166 deletions(-)`

Two files have not been included in the diff as mentioned above since they are
not a part of coreboot tree.

The number of changes significantly reduced due to many patches merged by
community.

## Testing

* [PC Engines hardware configuration matrix](https://cloud.3mdeb.com/index.php/s/ce829QADwA7sHx9/preview) - hardware configurations available for testing in 3mdeb laboratory.

* [PC Engines release validation results](https://3mdeb.us16.list-manage.com/track/click?u=fce95b885fc13fbf1db611816&id=96d9b426c0&e=16ffa34a09) - please note there are separate sheets for each board-release.

![Mainline test results](https://cloud.3mdeb.com/index.php/s/B4imeoGmrLCmzoY/preview)

* Mainline:
  * PASSED: **433** (+0)
  * FAILED: **22** (+0)
  * PASSED [%]: **95.16** (+0%)

No particular changes in tests in this release. Regression didn't detect new
bugs.

## Binaries

### Mainline

* [apu1 v4.11.0.5.zip](https://3mdeb.com/open-source-firmware/pcengines/apu1/apu1_v4.11.0.5.zip)

  [apu1 v4.11.0.5.rom](https://3mdeb.com/open-source-firmware/pcengines/apu1/apu1_v4.11.0.5.rom)

  [SHA256 file](https://3mdeb.com/open-source-firmware/pcengines/apu1/apu1_v4.11.0.5.SHA256)

  [SHA256 sig](https://3mdeb.com/open-source-firmware/pcengines/apu1/apu1_v4.11.0.5.SHA256.sig)

* [apu2 v4.11.0.5.zip](https://3mdeb.com/open-source-firmware/pcengines/apu2/apu2_v4.11.0.5.zip)

  [apu2 v4.11.0.5.rom](https://3mdeb.com/open-source-firmware/pcengines/apu2/apu2_v4.11.0.5.rom)

  [SHA256 file](https://3mdeb.com/open-source-firmware/pcengines/apu2/apu2_v4.11.0.5.SHA256)

  [SHA256 sig](https://3mdeb.com/open-source-firmware/pcengines/apu2/apu2_v4.11.0.5.SHA256.sig)

* [apu3 v4.11.0.5.zip](https://3mdeb.com/open-source-firmware/pcengines/apu3/apu3_v4.11.0.5.zip)

  [apu3 v4.11.0.5.rom](https://3mdeb.com/open-source-firmware/pcengines/apu3/apu3_v4.11.0.5.rom)

  [SHA256 file](https://3mdeb.com/open-source-firmware/pcengines/apu3/apu3_v4.11.0.5.SHA256)

  [SHA256 sig](https://3mdeb.com/open-source-firmware/pcengines/apu3/apu3_v4.11.0.5.SHA256.sig)

* [apu4 v4.11.0.5.zip](https://3mdeb.com/open-source-firmware/pcengines/apu4/apu4_v4.11.0.5.zip)

  [apu4 v4.11.0.5.rom](https://3mdeb.com/open-source-firmware/pcengines/apu4/apu4_v4.11.0.5.rom)

  [SHA256 file](https://3mdeb.com/open-source-firmware/pcengines/apu4/apu4_v4.11.0.5.SHA256)

  [SHA256 sig](https://3mdeb.com/open-source-firmware/pcengines/apu4/apu4_v4.11.0.5.SHA256.sig)

* [apu5 v4.11.0.5.zip](https://3mdeb.com/open-source-firmware/pcengines/apu5/apu5_v4.11.0.5.zip)

  [apu5 v4.11.0.5.rom](https://3mdeb.com/open-source-firmware/pcengines/apu5/apu5_v4.11.0.5.rom)

  [SHA256 file](https://3mdeb.com/open-source-firmware/pcengines/apu5/apu5_v4.11.0.5.SHA256)

  [SHA256 sig](https://3mdeb.com/open-source-firmware/pcengines/apu5/apu5_v4.11.0.5.SHA256.sig)

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

4. ACPI Thermal Zones implementation. BSD systems suffer from lack of Thermal
   Zones and lack of temperature status on the dashboards of router
   distributions of BSD systems.

   **DONE**

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
