---
layout: post
title:  "PC Engines apu coreboot Open Source Firmware v4.14.0.2"
date:   2021-06-30
categories: Firmware
---

# PC Engines apu coreboot Open Source Firmware v4.14.0.2

## Key changes

Mainline:

1. **Rebased** with official coreboot repository **commit** 1c43d92.

## Statistics

![Files Changed](TBD)

The chart shows the total files changed from release tag against the rebase
point of given release specified in CHANGELOG (CHANGELOG.md, gitlab-ci.yml
and regression.sh excluded from statistics). Check the statistics with:

```
git diff --stat 1c43d92 ':(exclude).gitlab-ci.yml' ':(exclude)CHANGELOG.md' ':(exclude).gitlab-ci/regression.sh'
```

`110 files changed, 4202 insertions(+), 340 deletions(-)`

![Process of mainlining](TBD)

The chart represents the total line added and deleted on the PC Engines
coreboot fork against the rebase point for a given release.

## Testing

* [PC Engines hardware configuration matrix](TBD) - hardware configurations
  available for testing in 3mdeb laboratory.

* [PC Engines release validation results](https://docs.google.com/spreadsheets/d/1_uRhVo9eYeZONnelymonYp444zYHT_Q_qmJEJ8_XqJc/edit#gid=0) -
  please note there are separate sheets for each board-release.

![Mainline test results](TBD)

* Mainline:
  * PASSED: **679** (-6)
  * FAILED: **18** (+13)
  * PASSED [%]: **97.42** (-1,86%)

Some OSes had problems to be installed on apu4 and apu6. Board status tests
which depend on them failed as well which resulted in the increased failures.

### Key Changes in testing

* Fixed the Debian installation tests by correcting the preseed files
* Added test for iPXE HTTPS support
* Corrected tests for UART C/D enabling after changes in the firmware
* Corrected IOMMU test configuration on apu3 and apu4

## Binaries

### Mainline

* [apu1 v4.14.0.2.zip](https://3mdeb.com/open-source-firmware/pcengines/apu1/apu1_v4.14.0.2.zip)

  [apu1 v4.14.0.2.rom](https://3mdeb.com/open-source-firmware/pcengines/apu1/apu1_v4.14.0.2.rom)

  [SHA256 file](https://3mdeb.com/open-source-firmware/pcengines/apu1/apu1_v4.14.0.2.SHA256)

  [SHA256 sig](https://3mdeb.com/open-source-firmware/pcengines/apu1/apu1_v4.14.0.2.SHA256.sig)

* [apu2 v4.14.0.2.zip](https://3mdeb.com/open-source-firmware/pcengines/apu2/apu2_v4.14.0.2.zip)

  [apu2 v4.14.0.2.rom](https://3mdeb.com/open-source-firmware/pcengines/apu2/apu2_v4.14.0.2.rom)

  [SHA256 file](https://3mdeb.com/open-source-firmware/pcengines/apu2/apu2_v4.14.0.2.SHA256)

  [SHA256 sig](https://3mdeb.com/open-source-firmware/pcengines/apu2/apu2_v4.14.0.2.SHA256.sig)

* [apu3 v4.14.0.2.zip](https://3mdeb.com/open-source-firmware/pcengines/apu3/apu3_v4.14.0.2.zip)

  [apu3 v4.14.0.2.rom](https://3mdeb.com/open-source-firmware/pcengines/apu3/apu3_v4.14.0.2.rom)

  [SHA256 file](https://3mdeb.com/open-source-firmware/pcengines/apu3/apu3_v4.14.0.2.SHA256)

  [SHA256 sig](https://3mdeb.com/open-source-firmware/pcengines/apu3/apu3_v4.14.0.2.SHA256.sig)

* [apu4 v4.14.0.2.zip](https://3mdeb.com/open-source-firmware/pcengines/apu4/apu4_v4.14.0.2.zip)

  [apu4 v4.14.0.2.rom](https://3mdeb.com/open-source-firmware/pcengines/apu4/apu4_v4.14.0.2.rom)

  [SHA256 file](https://3mdeb.com/open-source-firmware/pcengines/apu4/apu4_v4.14.0.2.SHA256)

  [SHA256 sig](https://3mdeb.com/open-source-firmware/pcengines/apu4/apu4_v4.14.0.2.SHA256.sig)

* [apu5 v4.14.0.2.zip](https://3mdeb.com/open-source-firmware/pcengines/apu5/apu5_v4.14.0.2.zip)

  [apu5 v4.14.0.2.rom](https://3mdeb.com/open-source-firmware/pcengines/apu5/apu5_v4.14.0.2.rom)

  [SHA256 file](https://3mdeb.com/open-source-firmware/pcengines/apu5/apu5_v4.14.0.2.SHA256)

  [SHA256 sig](https://3mdeb.com/open-source-firmware/pcengines/apu5/apu5_v4.14.0.2.SHA256.sig)

* [apu6 v4.14.0.2.zip](https://3mdeb.com/open-source-firmware/pcengines/apu6/apu6_v4.14.0.2.zip)

  [apu6 v4.14.0.2.rom](https://3mdeb.com/open-source-firmware/pcengines/apu6/apu6_v4.14.0.2.rom)

  [SHA256 file](https://3mdeb.com/open-source-firmware/pcengines/apu6/apu6_v4.14.0.2.SHA256)

  [SHA256 sig](https://3mdeb.com/open-source-firmware/pcengines/apu6/apu6_v4.14.0.2.SHA256.sig)

See how to verify the signatures on [asciinema](https://asciinema.org/a/417462)
