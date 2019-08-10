---
layout: post
title:  "PC Engines apu coreboot Open Source Firmware v4.10.0.0"
date:   2019-08-10
categories: Firmware
---
# PC Engines apu coreboot Open Source Firmware v4.10.0.0

## Key changes

Mainline:

1. **Rebased** with official coreboot repository **commit** 2a20d13.
2. Added ACPI support for GPIOs. Detailes are available in
[apu2-documentation](https://github.com/pcengines/apu2-documentation/blob/master/docs/gpios.md).
So far access to GPIOs was possible only via dedicated driver. Now, there is
support via Linux kernel sysfs including:
    - LEDs
    - S1 switch button with interrupts
    - SIMSWAP
1. Validated problem with ESXi v6.7 U2 installation. We have located the source
   of the issue and now we are working to resolve it.
2. Added [documentation](https://github.com/pcengines/apu2-documentation/blob/master/docs/apu_CPU_boost.md)
   about APU Core Performance Boost.
3. Updated WLE200NX [documentation](https://github.com/pcengines/apu2-documentation/blob/master/docs/mpcie_modules.md#wle200nx)
   with issue workarounds.
4. Updated the pcengines.github.io site with new section containing useful
   documentation from apu2-documentation repository. Also the link to the
   repository is now accessible in the top panel. Below the binaries section
   for each release we have added a note with link how to verify signatures of
   the binaries.

## Statistics

![Files Changed](https://cloud.3mdeb.com/index.php/s/cfKkNEZXs43NfQG/preview)

The chart shows the total files changed from release tag against the rebase
point of given release specified in CHANGELOG (CHANGELOG.md and gitlab-ci.yml
excluded from statistics). Check the statistics with:

```
git diff --stat 2a20d13 ':(exclude).gitlab-ci.yml' ':(exclude)CHANGELOG.md'
```

`88 files changed, 2784 insertions(+), 196 deletions(-)`

![Process of mainlining](https://cloud.3mdeb.com/index.php/s/Gad3L44ZEW6wEgP/preview)

The chart represents the total line added and deleted on the PC Engines
coreboot fork against the rebase point for a given release. Check the
statistics with:

```
git diff --stat 2a20d13 ':(exclude).gitlab-ci.yml' ':(exclude)CHANGELOG.md'
```

`88 files changed, 2784 insertions(+), 196 deletions(-)`

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

### Mainline

* [apu1 v4.10.0.0](https://3mdeb.com/open-source-firmware/pcengines/apu1/apu1_v4.10.0.0.rom)

  [SHA256 file](https://3mdeb.com/open-source-firmware/pcengines/apu1/apu1_v4.10.0.0.SHA256)

  [SHA256 sig](https://3mdeb.com/open-source-firmware/pcengines/apu1/apu1_v4.10.0.0.SHA256.sig)

* [apu2 v4.10.0.0](https://3mdeb.com/open-source-firmware/pcengines/apu2/apu2_v4.10.0.0.rom)

  [SHA256 file](https://3mdeb.com/open-source-firmware/pcengines/apu2/apu2_v4.10.0.0.SHA256)

  [SHA256 sig](https://3mdeb.com/open-source-firmware/pcengines/apu2/apu2_v4.10.0.0.SHA256.sig)

* [apu3 v4.10.0.0](https://3mdeb.com/open-source-firmware/pcengines/apu3/apu3_v4.10.0.0.rom)

  [SHA256 file](https://3mdeb.com/open-source-firmware/pcengines/apu3/apu3_v4.10.0.0.SHA256)

  [SHA256 sig](https://3mdeb.com/open-source-firmware/pcengines/apu3/apu3_v4.10.0.0.SHA256.sig)

* [apu4 v4.10.0.0](https://3mdeb.com/open-source-firmware/pcengines/apu4/apu4_v4.10.0.0.rom)

  [SHA256 file](https://3mdeb.com/open-source-firmware/pcengines/apu4/apu4_v4.10.0.0.SHA256)

  [SHA256 sig](https://3mdeb.com/open-source-firmware/pcengines/apu4/apu4_v4.10.0.0.SHA256.sig)

* [apu5 v4.10.0.0](https://3mdeb.com/open-source-firmware/pcengines/apu5/apu5_v4.10.0.0.rom)

  [SHA256 file](https://3mdeb.com/open-source-firmware/pcengines/apu5/apu5_v4.10.0.0.SHA256)

  [SHA256 sig](https://3mdeb.com/open-source-firmware/pcengines/apu5/apu5_v4.10.0.0.SHA256.sig)

See how to verify the signatures on [asciinema](https://asciinema.org/a/227035)

[1]: https://en.wikipedia.org/wiki/ROCA_vulnerability
[2]: https://github.com/pcengines/apu2-documentation/blob/master/docs/research/ROCA.md
[3]: https://github.com/pcengines/apu2-documentation/blob/master/docs/os-status.md

## What we planned

1. Improve the support of TPM2 in coreboot and SeaBIOS. Currently the is only
   the TCPA (TPM1.2) log support in coreboot. Additionally SeaBIOS overwrites
   existing entries in TPM2 log area. `cbmem` utility also lacks support for
   displaying TPM2 log area.

   **WORK IN PROGRESS**

2. Validate ESXi 6.7. We have got information that booting ESXi 6.7 U2 fails on
   apu2 and are investigating the issue.

   **WORK IN PROGRESS**

3. Linux GPIO support via ACPI tables. It will allow to control certain GPIOs
   via kernel sysfs (LEDs, S1 button, SIMSWAP).

   **DONE**

4. Fix bugs related to Nuvoton NCT5104D reset and implement GPIO access
   improvements.

   **WORK IN PROGRESS**

5. Reorganize runtime configuration by making it persistent across updates and
   accessible from user space. Also prepare a tool for offline binary
   modification.

   **WORK IN PROGRESS**

## Coming soon

Feature and improvements on the roadmap:

1. Improve the support of TPM2 in coreboot and SeaBIOS. Currently the is only
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
