---
layout: post
title:  "PC Engines apu coreboot Open Source Firmware v4.19.0.1"
date:   2023-02-02
categories: Firmware
---
# PC Engines apu coreboot Open Source Firmware v4.19.0.1

## Key changes

Mainline:

### Changed

- **Rebased** with official coreboot repository **commit** 2ccbcc5
- Removed configuration and mainboard files for apu1 due to the board being
  dropped from upstream coreboot

## Statistics


![Files Changed](https://cloud.3mdeb.com/index.php/s/Djd8gQ3P6Hb3r3L/preview)

The chart shows the total files changed from release tag against the rebase
point of given release specified in CHANGELOG (CHANGELOG.md, gitlab-ci.yml
and regression.sh excluded from statistics). Check the statistics with:

```
git diff --stat 2ccbcc5 ':(exclude).gitlab-ci.yml' ':(exclude)CHANGELOG.md' ':(exclude).gitlab-ci/regression.sh'
```

`97 files changed, 3960 insertions(+), 174 deletions(-)`

![Process of mainlining](https://cloud.3mdeb.com/index.php/s/iqAHtaRiGBCyyw7/preview)

The chart represents the total line added and deleted on the PC Engines
coreboot fork against the rebase point for a given release.

## Testing

* [PC Engines hardware configuration matrix](https://cloud.3mdeb.com/index.php/s/GYecq2SHidoFZ8A/preview) -
  hardware configurations available for testing in 3mdeb laboratory.

* [PC Engines release validation results](https://docs.google.com/spreadsheets/d/1_uRhVo9eYeZONnelymonYp444zYHT_Q_qmJEJ8_XqJc/edit#gid=2507399) -
  please note there are separate sheets for each board-release.

![Mainline test results](https://cloud.3mdeb.com/index.php/s/A9fKnqmYmrsxoWB/preview)

* Mainline:
  * PASSED: 679 (**-87**)
  * FAILED: 7 (**+/-0**)
  * PASSED [%]: 98.84 (**-0.13%**)

The overall number of tests as well as the number of successful tests has
decreased due to the stopping release for apu1 mainboard.

Fails are related to
[USB](https://github.com/pcengines/apu2-documentation/issues/277),
[Xen](https://github.com/pcengines/apu2-documentation/issues/109) and
[Checking CPU temperature in pfSense](https://github.com/pcengines/apu2-documentation/issues/281).

## Binaries

### Mainline

* [apu1 v4.19.0.1.zip](https://3mdeb.com/open-source-firmware/pcengines/apu1/apu1_v4.19.0.1.zip)

  [apu1 v4.19.0.1.rom](https://3mdeb.com/open-source-firmware/pcengines/apu1/apu1_v4.19.0.1.rom)

  [SHA256 file](https://3mdeb.com/open-source-firmware/pcengines/apu1/apu1_v4.19.0.1.SHA256)

  [SHA256 sig](https://3mdeb.com/open-source-firmware/pcengines/apu1/apu1_v4.19.0.1.SHA256.sig)

* [apu2 v4.19.0.1.zip](https://3mdeb.com/open-source-firmware/pcengines/apu2/apu2_v4.19.0.1.zip)

  [apu2 v4.19.0.1.rom](https://3mdeb.com/open-source-firmware/pcengines/apu2/apu2_v4.19.0.1.rom)

  [SHA256 file](https://3mdeb.com/open-source-firmware/pcengines/apu2/apu2_v4.19.0.1.SHA256)

  [SHA256 sig](https://3mdeb.com/open-source-firmware/pcengines/apu2/apu2_v4.19.0.1.SHA256.sig)

* [apu3 v4.19.0.1.zip](https://3mdeb.com/open-source-firmware/pcengines/apu3/apu3_v4.19.0.1.zip)

  [apu3 v4.19.0.1.rom](https://3mdeb.com/open-source-firmware/pcengines/apu3/apu3_v4.19.0.1.rom)

  [SHA256 file](https://3mdeb.com/open-source-firmware/pcengines/apu3/apu3_v4.19.0.1.SHA256)

  [SHA256 sig](https://3mdeb.com/open-source-firmware/pcengines/apu3/apu3_v4.19.0.1.SHA256.sig)

* [apu4 v4.19.0.1.zip](https://3mdeb.com/open-source-firmware/pcengines/apu4/apu4_v4.19.0.1.zip)

  [apu4 v4.19.0.1.rom](https://3mdeb.com/open-source-firmware/pcengines/apu4/apu4_v4.19.0.1.rom)

  [SHA256 file](https://3mdeb.com/open-source-firmware/pcengines/apu4/apu4_v4.19.0.1.SHA256)

  [SHA256 sig](https://3mdeb.com/open-source-firmware/pcengines/apu4/apu4_v4.19.0.1.SHA256.sig)

* [apu5 v4.19.0.1.zip](https://3mdeb.com/open-source-firmware/pcengines/apu5/apu5_v4.19.0.1.zip)

  [apu5 v4.19.0.1.rom](https://3mdeb.com/open-source-firmware/pcengines/apu5/apu5_v4.19.0.1.rom)

  [SHA256 file](https://3mdeb.com/open-source-firmware/pcengines/apu5/apu5_v4.19.0.1.SHA256)

  [SHA256 sig](https://3mdeb.com/open-source-firmware/pcengines/apu5/apu5_v4.19.0.1.SHA256.sig)

* [apu6 v4.19.0.1.zip](https://3mdeb.com/open-source-firmware/pcengines/apu6/apu6_v4.19.0.1.zip)

  [apu6 v4.19.0.1.rom](https://3mdeb.com/open-source-firmware/pcengines/apu6/apu6_v4.19.0.1.rom)

  [SHA256 file](https://3mdeb.com/open-source-firmware/pcengines/apu6/apu6_v4.19.0.1.SHA256)

  [SHA256 sig](https://3mdeb.com/open-source-firmware/pcengines/apu6/apu6_v4.19.0.1.SHA256.sig)

* [apu7 v4.19.0.1.zip](https://3mdeb.com/open-source-firmware/pcengines/apu7/apu7_v4.19.0.1.zip)

  [apu7 v4.19.0.1.rom](https://3mdeb.com/open-source-firmware/pcengines/apu7/apu7_v4.19.0.1.rom)

  [SHA256 file](https://3mdeb.com/open-source-firmware/pcengines/apu7/apu7_v4.19.0.1.SHA256)

  [SHA256 sig](https://3mdeb.com/open-source-firmware/pcengines/apu7/apu7_v4.19.0.1.SHA256.sig)

See how to verify the signatures on [asciinema](https://asciinema.org/a/556754)
