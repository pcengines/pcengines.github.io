---
layout: post
title:  "PC Engines apu coreboot Open Source Firmware v4.17.0.3"
date:   2022-08-24
categories: Firmware
---
# PC Engines apu coreboot Open Source Firmware v4.17.0.3

## Key changes

Mainline:

### Changed

- **Rebased** with official coreboot repository **commit** e173f2b
- Changed sign of life date format from YYYY-DD-MM to YYYY-MM-DD

## Statistics


![Files Changed](https://cloud.3mdeb.com/index.php/s/SmZGQBnfR94xQif/preview)

The chart shows the total files changed from release tag against the rebase
point of given release specified in CHANGELOG (CHANGELOG.md, gitlab-ci.yml
and regression.sh excluded from statistics). Check the statistics with:

```
git diff --stat e173f2b ':(exclude).gitlab-ci.yml' ':(exclude)CHANGELOG.md' ':(exclude).gitlab-ci/regression.sh'
```

`116 files changed, 4402 insertions(+), 215 deletions(-)`

![Process of mainlining](https://cloud.3mdeb.com/index.php/s/zTozsLdMR5YaTpT/preview)

The chart represents the total line added and deleted on the PC Engines
coreboot fork against the rebase point for a given release.

## Testing

* [PC Engines hardware configuration matrix](https://cloud.3mdeb.com/index.php/s/GYecq2SHidoFZ8A/preview) -
  hardware configurations available for testing in 3mdeb laboratory.

* [PC Engines release validation results](https://docs.google.com/spreadsheets/d/1_uRhVo9eYeZONnelymonYp444zYHT_Q_qmJEJ8_XqJc/edit#gid=2507399) -
  please note there are separate sheets for each board-release.

![Mainline test results](https://cloud.3mdeb.com/index.php/s/HWRgLeSj4A9jEX2/preview)

* Mainline:
  * PASSED: 768 (**+4**)
  * FAILED: 7 (**-2**)
  * PASSED [%]: 98,97 (**+0,26%**)

Fails are related to
[USB](https://github.com/pcengines/apu2-documentation/issues/277),
[Xen](https://github.com/pcengines/apu2-documentation/issues/109) and
[Checking CPU temperature in pfSense](https://github.com/pcengines/apu2-documentation/issues/281).

## Binaries

### Mainline

* [apu1 v4.17.0.3.zip](https://3mdeb.com/open-source-firmware/pcengines/apu1/apu1_v4.17.0.3.zip)

  [apu1 v4.17.0.3.rom](https://3mdeb.com/open-source-firmware/pcengines/apu1/apu1_v4.17.0.3.rom)

  [SHA256 file](https://3mdeb.com/open-source-firmware/pcengines/apu1/apu1_v4.17.0.3.SHA256)

  [SHA256 sig](https://3mdeb.com/open-source-firmware/pcengines/apu1/apu1_v4.17.0.3.SHA256.sig)

* [apu2 v4.17.0.3.zip](https://3mdeb.com/open-source-firmware/pcengines/apu2/apu2_v4.17.0.3.zip)

  [apu2 v4.17.0.3.rom](https://3mdeb.com/open-source-firmware/pcengines/apu2/apu2_v4.17.0.3.rom)

  [SHA256 file](https://3mdeb.com/open-source-firmware/pcengines/apu2/apu2_v4.17.0.3.SHA256)

  [SHA256 sig](https://3mdeb.com/open-source-firmware/pcengines/apu2/apu2_v4.17.0.3.SHA256.sig)

* [apu3 v4.17.0.3.zip](https://3mdeb.com/open-source-firmware/pcengines/apu3/apu3_v4.17.0.3.zip)

  [apu3 v4.17.0.3.rom](https://3mdeb.com/open-source-firmware/pcengines/apu3/apu3_v4.17.0.3.rom)

  [SHA256 file](https://3mdeb.com/open-source-firmware/pcengines/apu3/apu3_v4.17.0.3.SHA256)

  [SHA256 sig](https://3mdeb.com/open-source-firmware/pcengines/apu3/apu3_v4.17.0.3.SHA256.sig)

* [apu4 v4.17.0.3.zip](https://3mdeb.com/open-source-firmware/pcengines/apu4/apu4_v4.17.0.3.zip)

  [apu4 v4.17.0.3.rom](https://3mdeb.com/open-source-firmware/pcengines/apu4/apu4_v4.17.0.3.rom)

  [SHA256 file](https://3mdeb.com/open-source-firmware/pcengines/apu4/apu4_v4.17.0.3.SHA256)

  [SHA256 sig](https://3mdeb.com/open-source-firmware/pcengines/apu4/apu4_v4.17.0.3.SHA256.sig)

* [apu5 v4.17.0.3.zip](https://3mdeb.com/open-source-firmware/pcengines/apu5/apu5_v4.17.0.3.zip)

  [apu5 v4.17.0.3.rom](https://3mdeb.com/open-source-firmware/pcengines/apu5/apu5_v4.17.0.3.rom)

  [SHA256 file](https://3mdeb.com/open-source-firmware/pcengines/apu5/apu5_v4.17.0.3.SHA256)

  [SHA256 sig](https://3mdeb.com/open-source-firmware/pcengines/apu5/apu5_v4.17.0.3.SHA256.sig)

* [apu6 v4.17.0.3.zip](https://3mdeb.com/open-source-firmware/pcengines/apu6/apu6_v4.17.0.3.zip)

  [apu6 v4.17.0.3.rom](https://3mdeb.com/open-source-firmware/pcengines/apu6/apu6_v4.17.0.3.rom)

  [SHA256 file](https://3mdeb.com/open-source-firmware/pcengines/apu6/apu6_v4.17.0.3.SHA256)

  [SHA256 sig](https://3mdeb.com/open-source-firmware/pcengines/apu6/apu6_v4.17.0.3.SHA256.sig)

* [apu7 v4.17.0.3.zip](https://3mdeb.com/open-source-firmware/pcengines/apu7/apu7_v4.17.0.3.zip)

  [apu7 v4.17.0.3.rom](https://3mdeb.com/open-source-firmware/pcengines/apu7/apu7_v4.17.0.3.rom)

  [SHA256 file](https://3mdeb.com/open-source-firmware/pcengines/apu7/apu7_v4.17.0.3.SHA256)

  [SHA256 sig](https://3mdeb.com/open-source-firmware/pcengines/apu7/apu7_v4.17.0.3.SHA256.sig)

See how to verify the signatures on [asciinema](https://asciinema.org/a/504899)
