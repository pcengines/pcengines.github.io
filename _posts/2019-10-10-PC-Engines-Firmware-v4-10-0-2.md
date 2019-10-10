---
layout: post
title:  "PC Engines apu coreboot Open Source Firmware v4.10.0.2"
date:   2019-10-10
categories: Firmware
---
# PC Engines apu coreboot Open Source Firmware v4.10.0.2

## Key changes

Mainline:

1. **Rebased** with official coreboot repository **commit** 64c14b5.
2. Added **soft reset** feature for **SuperIO GPIOs**. With every platform boot
   **SuperIO GPIOs are set to default state**: input and open-drain.
3. **Support IO Base Address mode** for SuperIO GPIOs.
   SuperIO GPIOs can be controlled now in two ways:
   - through configuration registers
   - through direct access to I/O register with **base address 0x220**

   Both methods work in parallel without any disruptions.

Legacy:

1. Added **ACPI support for GPIOs**. Detailes are available in
[apu2-documentation](https://github.com/pcengines/apu2-documentation/blob/master/docs/gpios.md).
So far access to GPIOs was possible only via dedicated driver. Now, there is
support via Linux kernel sysfs including:
    - LEDs
    - S1 switch button with interrupts
    - SIMSWAP
2. **Fixed SD 3.0 mode** to be **runtime configurable** now.
3. Added **soft reset** feature for **SuperIO GPIOs**. With every platform boot
   **SuperIO GPIOs are set to default state**: input and open-drain.
4. **Support IO Base Address mode** for SuperIO GPIOs.
   SuperIO GPIOs can be controlled now in two ways:
   - through configuration registers
   - through direct access to I/O register with **base address 0x220**

   Both methods work in parallel without any disruptions.

## coreboot community

Patches sent for review:

* [Fix AMDFW outside CBFS](https://review.coreboot.org/c/coreboot/+/35853)
* [SuperIO Nuvoton NCT5104D GPIO soft reset](https://review.coreboot.org/c/coreboot/+/35482)
* [SuperIO Nuvoton NCT5104D enable Base Address mode](https://review.coreboot.org/c/coreboot/+/35849)
* [Fill PC Engines apu2 SMBIOS type 16 and 17](https://review.coreboot.org/c/coreboot/+/35889)
* [Adjust AGESA.h headers to AGESA version used in apu2](https://review.coreboot.org/c/coreboot/+/35906)
* [Default SATA in AHCI mode for apu2](https://review.coreboot.org/c/coreboot/+/35891)

## Statistics

![Files Changed](https://cloud.3mdeb.com/index.php/s/Sab6M8XJJ48GGbN/preview)

The chart shows the total files changed from release tag against the rebase
point of given release specified in CHANGELOG (CHANGELOG.md and gitlab-ci.yml
excluded from statistics). Check the statistics with:

```
git diff --stat 64c14b5 ':(exclude).gitlab-ci.yml' ':(exclude)CHANGELOG.md'
```

`93 files changed, 2899 insertions(+), 205 deletions(-)`

![Process of mainlining](https://cloud.3mdeb.com/index.php/s/rx2q4Cp2MtonQE6/preview)

The chart represents the total line added and deleted on the PC Engines
coreboot fork against the rebase point for a given release. Check the
statistics with:

```
git diff --stat 64c14b5 ':(exclude).gitlab-ci.yml' ':(exclude)CHANGELOG.md'
```

`93 files changed, 2899 insertions(+), 205 deletions(-)`

Two files have not been included in the diff as mentioned above since they are
not a part of coreboot tree.

## Testing

* [PC Engines hardware configuration matrix](https://cloud.3mdeb.com/index.php/s/ce829QADwA7sHx9/preview) - hardware configurations available for testing in 3mdeb laboratory.

* [PC Engines release validation results](https://3mdeb.us16.list-manage.com/track/click?u=fce95b885fc13fbf1db611816&id=96d9b426c0&e=16ffa34a09) - please note there are separate sheets for each board-release.

Test changes in this release:
* **added** GPIO driver (LED control) tests (3 test-cases)
* **added** GPIO driver (S1 switch handler) tests (1 test-case)
* **improved** Voyage installation test with regexp matches
* **improved** apu5 platform heat dissipation in the 3mdeb lab (CPB problems)

![Mainline test results](https://cloud.3mdeb.com/index.php/s/dRHMyDndi54aBLd/preview)

![Legacy test results](https://cloud.3mdeb.com/index.php/s/ZNEHy4FABxRpBJw/preview)

* Mainline:
  * PASSED: **425** (+19)
  * FAILED: **12** (+1)
  * PASSED [%]: **97.25%** (-0.11%)

* Legacy:
  * PASSED: **372** (+4)
  * FAILED: **10** (+1)
  * PASSED [%]: **97.38%** (-0.23%)

The difference in the `PASSED`/`FAILED` aggregated statistics results from the
apu3 watchdog fix, new GPIO driver tests and the returning USB detection problem.

## Binaries

### Mainline

* [apu1 v4.10.0.2](https://3mdeb.com/open-source-firmware/pcengines/apu1/apu1_v4.10.0.2.rom)

  [SHA256 file](https://3mdeb.com/open-source-firmware/pcengines/apu1/apu1_v4.10.0.2.SHA256)

  [SHA256 sig](https://3mdeb.com/open-source-firmware/pcengines/apu1/apu1_v4.10.0.2.SHA256.sig)

* [apu2 v4.10.0.2](https://3mdeb.com/open-source-firmware/pcengines/apu2/apu2_v4.10.0.2.rom)

  [SHA256 file](https://3mdeb.com/open-source-firmware/pcengines/apu2/apu2_v4.10.0.2.SHA256)

  [SHA256 sig](https://3mdeb.com/open-source-firmware/pcengines/apu2/apu2_v4.10.0.2.SHA256.sig)

* [apu3 v4.10.0.2](https://3mdeb.com/open-source-firmware/pcengines/apu3/apu3_v4.10.0.2.rom)

  [SHA256 file](https://3mdeb.com/open-source-firmware/pcengines/apu3/apu3_v4.10.0.2.SHA256)

  [SHA256 sig](https://3mdeb.com/open-source-firmware/pcengines/apu3/apu3_v4.10.0.2.SHA256.sig)

* [apu4 v4.10.0.2](https://3mdeb.com/open-source-firmware/pcengines/apu4/apu4_v4.10.0.2.rom)

  [SHA256 file](https://3mdeb.com/open-source-firmware/pcengines/apu4/apu4_v4.10.0.2.SHA256)

  [SHA256 sig](https://3mdeb.com/open-source-firmware/pcengines/apu4/apu4_v4.10.0.2.SHA256.sig)

* [apu5 v4.10.0.2](https://3mdeb.com/open-source-firmware/pcengines/apu5/apu5_v4.10.0.2.rom)

  [SHA256 file](https://3mdeb.com/open-source-firmware/pcengines/apu5/apu5_v4.10.0.2.SHA256)

  [SHA256 sig](https://3mdeb.com/open-source-firmware/pcengines/apu5/apu5_v4.10.0.2.SHA256.sig)

### Legacy

* [apu2 v4.0.29](https://3mdeb.com/open-source-firmware/pcengines/apu2/apu2_v4.0.29.rom)

  [SHA256 file](https://3mdeb.com/open-source-firmware/pcengines/apu2/apu2_v4.0.29.SHA256)

  [SHA256 sig](https://3mdeb.com/open-source-firmware/pcengines/apu2/apu2_v4.0.29.SHA256.sig)

* [apu3 v4.0.29](https://3mdeb.com/open-source-firmware/pcengines/apu3/apu3_v4.0.29.rom)

  [SHA256 file](https://3mdeb.com/open-source-firmware/pcengines/apu3/apu3_v4.0.29.SHA256)

  [SHA256 sig](https://3mdeb.com/open-source-firmware/pcengines/apu3/apu3_v4.0.29.SHA256.sig)

* [apu4 v4.0.29](https://3mdeb.com/open-source-firmware/pcengines/apu4/apu4_v4.0.29.rom)

  [SHA256 file](https://3mdeb.com/open-source-firmware/pcengines/apu4/apu4_v4.0.29.SHA256)

  [SHA256 sig](https://3mdeb.com/open-source-firmware/pcengines/apu4/apu4_v4.0.29.SHA256.sig)

* [apu5 v4.0.29](https://3mdeb.com/open-source-firmware/pcengines/apu5/apu5_v4.0.29.rom)

  [SHA256 file](https://3mdeb.com/open-source-firmware/pcengines/apu5/apu5_v4.0.29.SHA256)

  [SHA256 sig](https://3mdeb.com/open-source-firmware/pcengines/apu5/apu5_v4.0.29.SHA256.sig)

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

3. Fix bugs related to Nuvoton NCT5104D reset and implement GPIO access
   improvements.

   **DONE**

4. Reorganize runtime configuration by making it persistent across updates and
   accessible from user space. Also prepare a tool for offline binary
   modification.

   **WORK IN PROGRESS**

5. Vital Product Data (VPD) support. User will have possibility to store
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
