---
layout: post
title:  "PC Engines apu coreboot Open Source Firmware v4.13.0.6"
date:   2021-05-05
categories: Firmware
---

# PC Engines apu coreboot Open Source Firmware v4.13.0.6

## Key changes

Mainline:

1. **Rebased** with official coreboot repository **commit** a4c09c5.

## coreboot community

Patches sent for review:

* [nb/amd/{agesa,pi}: Avoid overflows during DRAM calculation](https://review.coreboot.org/c/coreboot/+/52922)
* [nb/amd/pi/00730F01/northbridge.c: Use generic allocation functions](https://review.coreboot.org/c/coreboot/+/52926)
* [nb/amd/pi/00730F01/northbridge.c: Report missing resources](https://review.coreboot.org/c/coreboot/+/52927)
* [nb/amd/pi/00730F01: enable RESOURCE_ALLOCATOR_V4](https://review.coreboot.org/c/coreboot/+/52761)
* [cpu/amd/pi/00730F01/model_16_init.c: create correct MTRR solution](https://review.coreboot.org/c/coreboot/+/52762)
* [nb/amd/agesa/family14/northbridge.c: Use generic allocation functions](https://review.coreboot.org/c/coreboot/+/52934)
* [nb/amd/agesa/family14/northbridge.c:  Report missing resources](https://review.coreboot.org/c/coreboot/+/52935)
* [northbridge/amd/agesa/family14: enable RESOURCE_ALLOCATOR_V4](https://review.coreboot.org/c/coreboot/+/52780)
* [cpu/amd/agesa/family14/model_14_init.c: create correct MTRR solution](https://review.coreboot.org/c/coreboot/+/52781)
* [mainboard/pcengines/apu1/OemCustomize.c: make AGESA AmdInitPost happy](https://review.coreboot.org/c/coreboot/+/52779)
* [mb/pcengines/apu2/OemCustomize.c: make AGESA AmdInitPost happy](https://review.coreboot.org/c/coreboot/+/52759)

Total:

* Lines added: 329
* Lines removed: 618

## Statistics

![Files Changed](https://cloud.3mdeb.com/index.php/s/4mrBz3eRSyDyrms/preview)

The chart shows the total files changed from release tag against the rebase
point of given release specified in CHANGELOG (CHANGELOG.md and gitlab-ci.yml
excluded from statistics). Check the statistics with:

```
git diff --stat a4c09c5 ':(exclude).gitlab-ci.yml' ':(exclude)CHANGELOG.md' ':(exclude).gitlab-ci/regression.sh'
```

`106 files changed, 4422 insertions(+), 404 deletions(-)`

![Process of mainlining](https://cloud.3mdeb.com/index.php/s/3eRBCMfW2jjdWxs/preview)

The chart represents the total line added and deleted on the PC Engines
coreboot fork against the rebase point for a given release.

## Testing

* [PC Engines hardware configuration matrix](https://cloud.3mdeb.com/index.php/s/oWDDFxNDZBtJDQP/preview) - hardware configurations available for testing in 3mdeb laboratory.

* [PC Engines release validation results](https://3mdeb.us16.list-manage.com/track/click?u=fce95b885fc13fbf1db611816&id=96d9b426c0&e=16ffa34a09) - please note there are separate sheets for each board-release.

![Mainline test results](https://cloud.3mdeb.com/index.php/s/qBaSnEptzSWTeHE/preview)

* Mainline:
  * PASSED: **685** (+23)
  * FAILED: **5**
  * PASSED [%]: **99.28** (+0,03%)

### Key Changes in testing

1. Enabled more automatic tests for apu6a setup.

## Binaries

### Mainline

* [apu1 v4.13.0.6.zip](https://3mdeb.com/open-source-firmware/pcengines/apu1/apu1_v4.13.0.6.zip)

  [apu1 v4.13.0.6.rom](https://3mdeb.com/open-source-firmware/pcengines/apu1/apu1_v4.13.0.6.rom)

  [SHA256 file](https://3mdeb.com/open-source-firmware/pcengines/apu1/apu1_v4.13.0.6.SHA256)

  [SHA256 sig](https://3mdeb.com/open-source-firmware/pcengines/apu1/apu1_v4.13.0.6.SHA256.sig)

* [apu2 v4.13.0.6.zip](https://3mdeb.com/open-source-firmware/pcengines/apu2/apu2_v4.13.0.6.zip)

  [apu2 v4.13.0.6.rom](https://3mdeb.com/open-source-firmware/pcengines/apu2/apu2_v4.13.0.6.rom)

  [SHA256 file](https://3mdeb.com/open-source-firmware/pcengines/apu2/apu2_v4.13.0.6.SHA256)

  [SHA256 sig](https://3mdeb.com/open-source-firmware/pcengines/apu2/apu2_v4.13.0.6.SHA256.sig)

* [apu3 v4.13.0.6.zip](https://3mdeb.com/open-source-firmware/pcengines/apu3/apu3_v4.13.0.6.zip)

  [apu3 v4.13.0.6.rom](https://3mdeb.com/open-source-firmware/pcengines/apu3/apu3_v4.13.0.6.rom)

  [SHA256 file](https://3mdeb.com/open-source-firmware/pcengines/apu3/apu3_v4.13.0.6.SHA256)

  [SHA256 sig](https://3mdeb.com/open-source-firmware/pcengines/apu3/apu3_v4.13.0.6.SHA256.sig)

* [apu4 v4.13.0.6.zip](https://3mdeb.com/open-source-firmware/pcengines/apu4/apu4_v4.13.0.6.zip)

  [apu4 v4.13.0.6.rom](https://3mdeb.com/open-source-firmware/pcengines/apu4/apu4_v4.13.0.6.rom)

  [SHA256 file](https://3mdeb.com/open-source-firmware/pcengines/apu4/apu4_v4.13.0.6.SHA256)

  [SHA256 sig](https://3mdeb.com/open-source-firmware/pcengines/apu4/apu4_v4.13.0.6.SHA256.sig)

* [apu5 v4.13.0.6.zip](https://3mdeb.com/open-source-firmware/pcengines/apu5/apu5_v4.13.0.6.zip)

  [apu5 v4.13.0.6.rom](https://3mdeb.com/open-source-firmware/pcengines/apu5/apu5_v4.13.0.6.rom)

  [SHA256 file](https://3mdeb.com/open-source-firmware/pcengines/apu5/apu5_v4.13.0.6.SHA256)

  [SHA256 sig](https://3mdeb.com/open-source-firmware/pcengines/apu5/apu5_v4.13.0.6.SHA256.sig)

* [apu6 v4.13.0.6.zip](https://3mdeb.com/open-source-firmware/pcengines/apu6/apu6_v4.13.0.6.zip)

  [apu6 v4.13.0.6.rom](https://3mdeb.com/open-source-firmware/pcengines/apu6/apu6_v4.13.0.6.rom)

  [SHA256 file](https://3mdeb.com/open-source-firmware/pcengines/apu6/apu6_v4.13.0.6.SHA256)

  [SHA256 sig](https://3mdeb.com/open-source-firmware/pcengines/apu6/apu6_v4.13.0.6.SHA256.sig)

See how to verify the signatures on [asciinema](https://asciinema.org/a/376207)

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

## Coming soon

Feature and improvements on the roadmap:

1. Improve the support of TPM2 in coreboot and SeaBIOS. Currently there is only
   the TCPA (TPM1.2) log support in coreboot. Additionally SeaBIOS overwrites
   existing entries in TPM2 log area. `cbmem` utility also lacks support for
   displaying TPM2 log area.
2. Reorganize runtime configuration by making it persistent across updates and
   accessible from user space. Also prepare a tool for offline binary
   modification.
