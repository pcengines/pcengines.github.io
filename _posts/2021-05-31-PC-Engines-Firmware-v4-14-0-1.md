---
layout: post
title:  "PC Engines apu coreboot Open Source Firmware v4.14.0.1"
date:   2021-06-01
categories: Firmware
---

# PC Engines apu coreboot Open Source Firmware v4.14.0.1

## Key changes

Mainline:

1. **Rebased** with official coreboot repository **commit** 6a936fc.
2. **Fixed** inconsistent MTTRs warning in Linux.
3. **Added persistent bootorder and runtime configuration** in separate FMAP
   region **for apu2-apu6** platforms.

## coreboot community

Patches sent for review:

* [nb/amd/agesa/family14/northbridge.c: Use generic allocation functions](https://review.coreboot.org/c/coreboot/+/52934)
* [nb/amd/agesa/family14/northbridge.c:  Report missing resources](https://review.coreboot.org/c/coreboot/+/52935)
* [northbridge/amd/agesa/family14: enable RESOURCE_ALLOCATOR_V4](https://review.coreboot.org/c/coreboot/+/52780)
* [cpu/amd/agesa/family14/model_14_init.c: create correct MTRR solution](https://review.coreboot.org/c/coreboot/+/52781)

Patches merged by community:

* [nb/amd/{agesa,pi}: Avoid overflows during DRAM calculation](https://review.coreboot.org/c/coreboot/+/52922)
* [nb/amd/pi/00730F01: Use generic allocation functions for northbridge](https://review.coreboot.org/c/coreboot/+/52926)
* [nb/amd/pi/00730F01: Use generic allocation functions for PCI domain](https://review.coreboot.org/c/coreboot/+/53955)
* [nb/amd/pi/00730F01/northbridge.c: Report missing resources](https://review.coreboot.org/c/coreboot/+/52927)
* [nb/amd/pi/00730F01: enable RESOURCE_ALLOCATOR_V4](https://review.coreboot.org/c/coreboot/+/52761)
* [cpu/amd/pi/00730F01/model_16_init.c: create correct MTRR solution](https://review.coreboot.org/c/coreboot/+/52762)
* [mainboard/pcengines/apu1/OemCustomize.c: make AGESA AmdInitPost happy](https://review.coreboot.org/c/coreboot/+/52779)
* [mb/pcengines/apu2/OemCustomize.c: make AGESA AmdInitPost happy](https://review.coreboot.org/c/coreboot/+/52759)

Total:

* Lines added: 235
* Lines removed: 506

## Statistics

![Files Changed](https://cloud.3mdeb.com/index.php/s/cXrbXz6ESMzQA6p/preview)

The chart shows the total files changed from release tag against the rebase
point of given release specified in CHANGELOG (CHANGELOG.md and gitlab-ci.yml
excluded from statistics). Check the statistics with:

```
git diff --stat 6a936fc ':(exclude).gitlab-ci.yml' ':(exclude)CHANGELOG.md' ':(exclude).gitlab-ci/regression.sh'
```

`111 files changed, 4215 insertions(+), 356 deletions(-)`

![Process of mainlining](https://cloud.3mdeb.com/index.php/s/s7Qa48m2rmrAddj/preview)

The chart represents the total line added and deleted on the PC Engines
coreboot fork against the rebase point for a given release.

## Testing

* [PC Engines hardware configuration matrix](https://cloud.3mdeb.com/index.php/s/oWDDFxNDZBtJDQP/preview) - hardware configurations available for testing in 3mdeb laboratory.

* [PC Engines release validation results](https://3mdeb.us16.list-manage.com/track/click?u=fce95b885fc13fbf1db611816&id=96d9b426c0&e=16ffa34a09) - please note there are separate sheets for each board-release.

![Mainline test results](https://cloud.3mdeb.com/index.php/s/qBaSnEptzSWTeHE/preview)

* Mainline:
  * PASSED: **TBD**
  * FAILED: **TBD**
  * PASSED [%]: **TBD**

### Key Changes in testing

No changes.

## Binaries

### Mainline

* [apu1 v4.14.0.1.zip](https://3mdeb.com/open-source-firmware/pcengines/apu1/apu1_v4.14.0.1.zip)

  [apu1 v4.14.0.1.rom](https://3mdeb.com/open-source-firmware/pcengines/apu1/apu1_v4.14.0.1.rom)

  [SHA256 file](https://3mdeb.com/open-source-firmware/pcengines/apu1/apu1_v4.14.0.1.SHA256)

  [SHA256 sig](https://3mdeb.com/open-source-firmware/pcengines/apu1/apu1_v4.14.0.1.SHA256.sig)

* [apu2 v4.14.0.1.zip](https://3mdeb.com/open-source-firmware/pcengines/apu2/apu2_v4.14.0.1.zip)

  [apu2 v4.14.0.1.rom](https://3mdeb.com/open-source-firmware/pcengines/apu2/apu2_v4.14.0.1.rom)

  [SHA256 file](https://3mdeb.com/open-source-firmware/pcengines/apu2/apu2_v4.14.0.1.SHA256)

  [SHA256 sig](https://3mdeb.com/open-source-firmware/pcengines/apu2/apu2_v4.14.0.1.SHA256.sig)

* [apu3 v4.14.0.1.zip](https://3mdeb.com/open-source-firmware/pcengines/apu3/apu3_v4.14.0.1.zip)

  [apu3 v4.14.0.1.rom](https://3mdeb.com/open-source-firmware/pcengines/apu3/apu3_v4.14.0.1.rom)

  [SHA256 file](https://3mdeb.com/open-source-firmware/pcengines/apu3/apu3_v4.14.0.1.SHA256)

  [SHA256 sig](https://3mdeb.com/open-source-firmware/pcengines/apu3/apu3_v4.14.0.1.SHA256.sig)

* [apu4 v4.14.0.1.zip](https://3mdeb.com/open-source-firmware/pcengines/apu4/apu4_v4.14.0.1.zip)

  [apu4 v4.14.0.1.rom](https://3mdeb.com/open-source-firmware/pcengines/apu4/apu4_v4.14.0.1.rom)

  [SHA256 file](https://3mdeb.com/open-source-firmware/pcengines/apu4/apu4_v4.14.0.1.SHA256)

  [SHA256 sig](https://3mdeb.com/open-source-firmware/pcengines/apu4/apu4_v4.14.0.1.SHA256.sig)

* [apu5 v4.14.0.1.zip](https://3mdeb.com/open-source-firmware/pcengines/apu5/apu5_v4.14.0.1.zip)

  [apu5 v4.14.0.1.rom](https://3mdeb.com/open-source-firmware/pcengines/apu5/apu5_v4.14.0.1.rom)

  [SHA256 file](https://3mdeb.com/open-source-firmware/pcengines/apu5/apu5_v4.14.0.1.SHA256)

  [SHA256 sig](https://3mdeb.com/open-source-firmware/pcengines/apu5/apu5_v4.14.0.1.SHA256.sig)

* [apu6 v4.14.0.1.zip](https://3mdeb.com/open-source-firmware/pcengines/apu6/apu6_v4.14.0.1.zip)

  [apu6 v4.14.0.1.rom](https://3mdeb.com/open-source-firmware/pcengines/apu6/apu6_v4.14.0.1.rom)

  [SHA256 file](https://3mdeb.com/open-source-firmware/pcengines/apu6/apu6_v4.14.0.1.SHA256)

  [SHA256 sig](https://3mdeb.com/open-source-firmware/pcengines/apu6/apu6_v4.14.0.1.SHA256.sig)

See how to verify the signatures on [asciinema](https://asciinema.org/a/417462)
