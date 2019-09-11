---
layout: post
title:  "PC Engines apu coreboot Open Source Firmware v4.10.0.1"
date:   2019-09-10
categories: Firmware
---
# PC Engines apu coreboot Open Source Firmware v4.10.0.1

## Key changes

Mainline:

1. **Rebased** with official coreboot repository **commit** 22d66ef.
2. **Fixed watchdog** runtime option on **apu3**.
3. **Updated GPIOs** [documentation](https://github.com/pcengines/apu2-documentation/blob/master/docs/gpios.md)
   with known issue section and workaround.

Legacy:
1. **Fixed watchdog** runtime option on **apu3**.

There are little changes in this release because the effort was closely
focused on the runtime configuration reimplementation. The new runtime
configuration implementation will be based on VPD and will bring tools for
offline binary modification. It is planned to be introduced in v4.10.0.2.

## coreboot community

Patches merged:

* [MCFG ACPI table generation](https://review.coreboot.org/c/coreboot/+/35286)

Patches sent for review:

* [Enable AER and ACS for PCIe ports](https://review.coreboot.org/c/coreboot/+/35313)

## Statistics

![Files Changed](link1)

The chart shows the total files changed from release tag against the rebase
point of given release specified in CHANGELOG (CHANGELOG.md and gitlab-ci.yml
excluded from statistics). Check the statistics with:

```
git diff --stat 22d66ef ':(exclude).gitlab-ci.yml' ':(exclude)CHANGELOG.md'
```

`90 files changed, 2787 insertions(+), 208 deletions(-)`

![Process of mainlining](link2)

The chart represents the total line added and deleted on the PC Engines
coreboot fork against the rebase point for a given release. Check the
statistics with:

```
git diff --stat 22d66ef ':(exclude).gitlab-ci.yml' ':(exclude)CHANGELOG.md'
```

`90 files changed, 2787 insertions(+), 208 deletions(-)`

Two files have not been included in the diff as mentioned above since they are
not a part of coreboot tree.

## Testing

* [PC Engines hardware configuration matrix](https://cloud.3mdeb.com/index.php/s/ce829QADwA7sHx9/preview) - hardware configurations available for testing in 3mdeb laboratory.

* [PC Engines release validation results](https://3mdeb.us16.list-manage.com/track/click?u=fce95b885fc13fbf1db611816&id=96d9b426c0&e=16ffa34a09) - please note there are separate sheets for each board-release.

Test changes in this release:
* **improved** ATA boot perfomance tests for measuring "Loading Linux" time
* **replaced** APU3b2 testing platform with model **APU3c4**

![Mainline test results](https://cloud.3mdeb.com/index.php/s/LiG5NJszHQnXTKt/preview)

* Mainline:
  * PASSED: **406** (-2)
  * FAILED: **11** (-3)
  * PASSED [%]: **97.36%** (+0.68%)

The difference in the `PASSED`/`FAILED` aggregated statistics results from ATA
boot test improvement and minor platform problem (5 stable tests on apu4 were
not tested).

## Binaries

The signature files are not available yet. We are undergoing a new key
deployment for the new coreboot 4.10 release. Each release beginning with
v4.10.0.0 and v4.0.28 will be signed with PC Engines Open Source Firmware
Release 4.10 Signing Key instead of 4.9. A new key will be announced along with
a fresh canary publicly available at
[3mdeb-seckpack](https://github.com/3mdeb/3mdeb-secpack/tree/master/canaries/pcengines).
The signature files will be updated as soon as the new key will be deployed.

### Mainline

* [apu1 v4.10.0.1](https://3mdeb.com/open-source-firmware/pcengines/apu1/apu1_v4.10.0.1.rom)

  [SHA256 file](https://3mdeb.com/open-source-firmware/pcengines/apu1/apu1_v4.10.0.1.SHA256)

  [SHA256 sig](https://3mdeb.com/open-source-firmware/pcengines/apu1/apu1_v4.10.0.1.SHA256.sig)

* [apu2 v4.10.0.1](https://3mdeb.com/open-source-firmware/pcengines/apu2/apu2_v4.10.0.1.rom)

  [SHA256 file](https://3mdeb.com/open-source-firmware/pcengines/apu2/apu2_v4.10.0.1.SHA256)

  [SHA256 sig](https://3mdeb.com/open-source-firmware/pcengines/apu2/apu2_v4.10.0.1.SHA256.sig)

* [apu3 v4.10.0.1](https://3mdeb.com/open-source-firmware/pcengines/apu3/apu3_v4.10.0.1.rom)

  [SHA256 file](https://3mdeb.com/open-source-firmware/pcengines/apu3/apu3_v4.10.0.1.SHA256)

  [SHA256 sig](https://3mdeb.com/open-source-firmware/pcengines/apu3/apu3_v4.10.0.1.SHA256.sig)

* [apu4 v4.10.0.1](https://3mdeb.com/open-source-firmware/pcengines/apu4/apu4_v4.10.0.1.rom)

  [SHA256 file](https://3mdeb.com/open-source-firmware/pcengines/apu4/apu4_v4.10.0.1.SHA256)

  [SHA256 sig](https://3mdeb.com/open-source-firmware/pcengines/apu4/apu4_v4.10.0.1.SHA256.sig)

* [apu5 v4.10.0.1](https://3mdeb.com/open-source-firmware/pcengines/apu5/apu5_v4.10.0.1.rom)

  [SHA256 file](https://3mdeb.com/open-source-firmware/pcengines/apu5/apu5_v4.10.0.1.SHA256)

  [SHA256 sig](https://3mdeb.com/open-source-firmware/pcengines/apu5/apu5_v4.10.0.1.SHA256.sig)

### Legacy

* [apu2 v4.0.28](https://3mdeb.com/open-source-firmware/pcengines/apu2/apu2_v4.0.28.rom)

  [SHA256 file](https://3mdeb.com/open-source-firmware/pcengines/apu2/apu2_v4.0.28.SHA256)

  [SHA256 sig](https://3mdeb.com/open-source-firmware/pcengines/apu2/apu2_v4.0.28.SHA256.sig)

* [apu3 v4.0.27](https://3mdeb.com/open-source-firmware/pcengines/apu3/apu3_v4.0.28.rom)

  [SHA256 file](https://3mdeb.com/open-source-firmware/pcengines/apu3/apu3_v4.0.28.SHA256)

  [SHA256 sig](https://3mdeb.com/open-source-firmware/pcengines/apu3/apu3_v4.0.28.SHA256.sig)

* [apu4 v4.0.28](https://3mdeb.com/open-source-firmware/pcengines/apu4/apu4_v4.0.28.rom)

  [SHA256 file](https://3mdeb.com/open-source-firmware/pcengines/apu4/apu4_v4.0.28.SHA256)

  [SHA256 sig](https://3mdeb.com/open-source-firmware/pcengines/apu4/apu4_v4.0.28.SHA256.sig)

* [apu5 v4.0.28](https://3mdeb.com/open-source-firmware/pcengines/apu5/apu5_v4.0.28.rom)

  [SHA256 file](https://3mdeb.com/open-source-firmware/pcengines/apu5/apu5_v4.0.28.SHA256)

  [SHA256 sig](https://3mdeb.com/open-source-firmware/pcengines/apu5/apu5_v4.0.28.SHA256.sig)

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

   **WORK IN PROGRESS**

4. Reorganize runtime configuration by making it persistent across updates and
   accessible from user space. Also prepare a tool for offline binary
   modification.

   **WORK IN PROGRESS**

## Coming soon

Feature and improvements on the roadmap:

1. Improve the support of TPM2 in coreboot and SeaBIOS. Currently there is only
   the TCPA (TPM1.2) log support in coreboot. Additionally SeaBIOS overwrites
   existing entries in TPM2 log area. `cbmem` utility also lacks support for
   displaying TPM2 log area.
2. Validate ESXi 6.7. We have got information that booting ESXi 6.7 U2 fails on
   apu2 and are investigating the issue.
3. Fix bugs related to Nuvoton NCT5104D reset and implement GPIO access
   improvements.
4. Reorganize runtime configuration by making it persistent across updates and
   accessible from user space. Also prepare a tool for offline binary
   modification.
5. Vital Product Data (VPD) support. User will have possibility to store
   and change VPD configuration in Read-Write section of SPI flash. Moreover,
   default VPD keys and values will be stored in Read-Only region to protect
   data against corruption. Also, sortbootorder runtime configuration will be
   stored in VPD Read-Write section, so access to it will be possible in OS
   via dedicated util.
