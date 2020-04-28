---
layout: post
title:  "PC Engines apu coreboot Open Source Firmware v4.11.0.6"
date:   2020-03-31
categories: Firmware
---
# PC Engines apu coreboot Open Source Firmware v4.11.0.6

## Key changes

Mainline:

1. **Rebased** with official coreboot repository **commit** d6f7ec5.
2. **Updated sortbootorder** to **v4.6.18** bringing the PCI Express power
   management features runtime option. For details refer to
   [sortbootorder documentation](https://github.com/pcengines/sortbootorder#settings-description).
   When PCI Express power management features features are enabled, the network
   controllers (NICs and WIFi cards) may have reduced performance at the cost
   of reduced power consumption. By default this option will be disabled to not
   [impact the network performance](https://github.com/pcengines/coreboot/issues/387).
3. **Reverted changes to ACPI CPU definitions** causing BSD systems to
   [not probe CPU frequency driver](https://github.com/pcengines/coreboot/issues/389).
   **The ACPI compliance of current BSD systems is not up to date**, the
   situation should improve when the distribution will start to use FreeBSD
   12.x, which works well with most recent rules of defining processors in
   ACPI.
4. **Reverted changes with PCIe reset logic** causing
   [mPCIe2 slot connected modules to not appear in OS](https://github.com/pcengines/coreboot/issues/388).
   The change did more harm than good. We are working to improve the PCIe
   modules detection in firmware, which is dependent on the AGESA.
5. **Added IOMMU IVRS generation expanded with IVHD type 11h for newer Xen**.
   This change should allow newer Xen images to utilize more IOMMU features.
6. **Fixed memtest hang on apu1**.
7. **Fixed TPM2 detection on FreeBSD 12.1**. Since FreeBSD 12.1 the TPM2
   support is available along with FreeBSD ports offering TPM2 tools. We will
   provide documentation how to install and utilize those tools on FreeBSD
   systems soon.

## coreboot community

Patches merged by community:

* [drivers/pc80/tpm/tis.c: change the _HID and _CID for TPM2 device](https://review.coreboot.org/c/coreboot/+/39699)
* [arch/x86/acpi: add definitions for IVHD type 11h](https://review.coreboot.org/c/coreboot/+/40041)
* [nb/amd/pi/00730F01/northbridge.c: refactor IVRS generation](https://review.coreboot.org/c/coreboot/+/40042)
* [Revert "mb/pcengines/apu2: add reset logic for PCIe slots"](https://review.coreboot.org/c/coreboot/+/40147)

**Total:**

* 308 lines added,
* 245 lines removed,

in official coreboot repository.

## Other news

3mdeb is co-developing [TrenchBoot project](http://trenchboot.org/) and is
responsible for developing AMD part of Dynamic Root of Trust for Measurement
(DRTM). The DRTM requires a special security instruction available on the AMD
GX-412TC SoC called `SKINIT`. The effort is founded by [NLNet Foundation](https://nlnet.nl/discovery/)
under the name:
`Open Source DRTM implementation with TrenchBoot for AMD processors project`.
The project aims to provide easy access to the tools and software that can
provably verify the security of the system. An important part of the reliable
and trustworthy Next Generation Internet (NGI).

To read more, please visit our blog describing the details and progress of our
work which is based on the flagship PC Engines apu2 model:

* [Introductory post](https://blog.3mdeb.com/2020/2020-03-28-trenchboot-nlnet-introduction/)
* [Project basics](https://blog.3mdeb.com/2020/2020-03-31-trenchboot-nlnet-lz/)
* [Validating the DRTM functionality](https://blog.3mdeb.com/2020/2020-04-03-trenchboot-nlnet-lz-validation/)

If you are interested in the project follow us on our blog and [Twitter](https://twitter.com/3mdeb_com),
or contact us directly over [email](mailto:contact@3mdeb.com).

## Statistics

![Files Changed](https://cloud.3mdeb.com/index.php/s/gXtePkQ3fdz2a9C/preview)

The chart shows the total files changed from release tag against the rebase
point of given release specified in CHANGELOG (CHANGELOG.md and gitlab-ci.yml
excluded from statistics). Check the statistics with:

```
git diff --stat d6f7ec5 ':(exclude).gitlab-ci.yml' ':(exclude)CHANGELOG.md'
```

`93 files changed, 3279 insertions(+), 379 deletions(-)`

![Process of mainlining](https://cloud.3mdeb.com/index.php/s/Q3y7tAN78DMbPnw/preview)

The chart represents the total line added and deleted on the PC Engines
coreboot fork against the rebase point for a given release. Check the
statistics with:

```
git diff --stat d6f7ec5 ':(exclude).gitlab-ci.yml' ':(exclude)CHANGELOG.md'
```

`93 files changed, 3279 insertions(+), 379 deletions(-)`

Two files have not been included in the diff as mentioned above since they are
not a part of coreboot tree.

The number of changes significantly increased, because we had to revert many
changes locally on our fork repository.

## Testing

* [PC Engines hardware configuration matrix](https://cloud.3mdeb.com/index.php/s/ce829QADwA7sHx9/preview) - hardware configurations available for testing in 3mdeb laboratory.

* [PC Engines release validation results](https://3mdeb.us16.list-manage.com/track/click?u=fce95b885fc13fbf1db611816&id=96d9b426c0&e=16ffa34a09) - please note there are separate sheets for each board-release.

![Mainline test results](https://cloud.3mdeb.com/index.php/s/F9SZtab5bErgyXg/preview)

* Mainline:
  * PASSED: **433** (+0)
  * FAILED: **22** (+0)
  * PASSED [%]: **95.16** (+0%)

No particular changes in tests in this release. Regression didn't detect new
bugs.

## Binaries

### Mainline

* [apu1 v4.11.0.6.zip](https://3mdeb.com/open-source-firmware/pcengines/apu1/apu1_v4.11.0.6.zip)

  [apu1 v4.11.0.6.rom](https://3mdeb.com/open-source-firmware/pcengines/apu1/apu1_v4.11.0.6.rom)

  [SHA256 file](https://3mdeb.com/open-source-firmware/pcengines/apu1/apu1_v4.11.0.6.SHA256)

  [SHA256 sig](https://3mdeb.com/open-source-firmware/pcengines/apu1/apu1_v4.11.0.6.SHA256.sig)

* [apu2 v4.11.0.6.zip](https://3mdeb.com/open-source-firmware/pcengines/apu2/apu2_v4.11.0.6.zip)

  [apu2 v4.11.0.6.rom](https://3mdeb.com/open-source-firmware/pcengines/apu2/apu2_v4.11.0.6.rom)

  [SHA256 file](https://3mdeb.com/open-source-firmware/pcengines/apu2/apu2_v4.11.0.6.SHA256)

  [SHA256 sig](https://3mdeb.com/open-source-firmware/pcengines/apu2/apu2_v4.11.0.6.SHA256.sig)

* [apu3 v4.11.0.6.zip](https://3mdeb.com/open-source-firmware/pcengines/apu3/apu3_v4.11.0.6.zip)

  [apu3 v4.11.0.6.rom](https://3mdeb.com/open-source-firmware/pcengines/apu3/apu3_v4.11.0.6.rom)

  [SHA256 file](https://3mdeb.com/open-source-firmware/pcengines/apu3/apu3_v4.11.0.6.SHA256)

  [SHA256 sig](https://3mdeb.com/open-source-firmware/pcengines/apu3/apu3_v4.11.0.6.SHA256.sig)

* [apu4 v4.11.0.6.zip](https://3mdeb.com/open-source-firmware/pcengines/apu4/apu4_v4.11.0.6.zip)

  [apu4 v4.11.0.6.rom](https://3mdeb.com/open-source-firmware/pcengines/apu4/apu4_v4.11.0.6.rom)

  [SHA256 file](https://3mdeb.com/open-source-firmware/pcengines/apu4/apu4_v4.11.0.6.SHA256)

  [SHA256 sig](https://3mdeb.com/open-source-firmware/pcengines/apu4/apu4_v4.11.0.6.SHA256.sig)

* [apu5 v4.11.0.6.zip](https://3mdeb.com/open-source-firmware/pcengines/apu5/apu5_v4.11.0.6.zip)

  [apu5 v4.11.0.6.rom](https://3mdeb.com/open-source-firmware/pcengines/apu5/apu5_v4.11.0.6.rom)

  [SHA256 file](https://3mdeb.com/open-source-firmware/pcengines/apu5/apu5_v4.11.0.6.SHA256)

  [SHA256 sig](https://3mdeb.com/open-source-firmware/pcengines/apu5/apu5_v4.11.0.6.SHA256.sig)

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
