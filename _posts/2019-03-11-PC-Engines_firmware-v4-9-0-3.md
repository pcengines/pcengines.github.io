---
layout: post
title:  "PC Engines apu coreboot Open Source Firmware v4.9.0.3"
date:   2019-03-11
categories: Firmware
---
# PC Engines apu coreboot Open Source Firmware v4.9.0.3

## Key changes

Mainline:

1. **Enabled** CPU **boost** feature in **runtime** configuration. Some
   platforms seem to have problems with boost thus we decided to make CPU boost
   runtime configurable.
2. We have **upgraded** to coreboot **SDK 1.52** in mainline releases.
3. Configured **pull-ups** on **WLAN_DISABLE#** pins on the mPCIe connectors
   which could cause issues with certain modems (e.g. Quectel EP06) when
   floating.
4. **Reproducible builds limiation** has been **eliminated** by setting iPXE
   and Memtest86+ fixed revisions. More details [here](https://github.com/pcengines/coreboot/issues/267)
5. Uploaded SHA256 and signatures of all previous firmware releases. SHA256
   files and signatures have been uploaded to pcengines.github.io.
6. **Fixed microcode update** feature, which broke due to the upstream changes
   in coreboot. More details [here](https://github.com/pcengines/apu2-documentation/issues/75#issuecomment-463067220)
7. **Added** information about **ECC** memory capability in **SMBIOS tables**
   on 4GB platforms. `Physical Memory Array` structure in `dmidecode` should
   report `Multi-bit ECC` in `Error Correction Type` field. Note: the ECC is
   present only on 4GB platforms. Check [how to verify](https://asciinema.org/a/233041)
8. **Added interrupt** configuration entries for **PCIe bridge** devices 2.4
   and 2.5. The interrupt ocnfiguration for 2 PCIe bridges were not programmed
   in BIOS. Kernel/OS will not always program it by itself, thus rely on BIOS
   programmed values in case kernel will not handle that.
9. **Rebased** with official coreboot repository **commit** 7a732b4.

Legacy:

1. **Enabled** CPU **boost** feature in **runtime** configuration. Some
   platforms seem to have problems with boost thus we decided to make CPU boost
   runtime configurable.
2. **Reproducible builds limiation** has been **eliminated** by setting iPXE
   and Memtest86+ fixed revisions. More details [here](https://github.com/pcengines/coreboot/issues/267)
3. Uploaded SHA256 and signatures of all previous firmware releases. SHA256
   files and signatures have been uploaded to pcengines.github.io.

## Statistics

![Files Changed](https://cloud.3mdeb.com/index.php/s/5TXiKGgiZSnWJ5m/preview)

The chart shows the total files changed from release tag against the rebase
point of given release specified in CHANGELOG (CHANGELOG.md and gitlab-ci.yml
excluded from statistics). Check the statistics with:

```
git diff --stat 7a732b4 ':(exclude)gitlab-ci.yml' ':(exclude)CHANGELOG.md'
```

![Addition and Deletion](https://cloud.3mdeb.com/index.php/s/JGj2bTDdw3xo7wg/preview)

The chart represents the total line added and deleted on the PC Engines
corebootÂ fork against the rebase point for given release. Check the statistics
with:

```
git diff --stat 7a732b4 ':(exclude)gitlab-ci.yml' ':(exclude)CHANGELOG.md'
```

Two files have not been included in the diff as mentioned above since they are
not a part of coreboot tree.

## Testing

* [PC Engines hardware configuration matrix](https://cloud.3mdeb.com/index.php/s/wRi33Zo5sdgbpWn/preview) - hardware configurations available for testing in 3mdeb laboratory.

* [PC Engines release validation results](https://3mdeb.us16.list-manage.com/track/click?u=fce95b885fc13fbf1db611816&id=96d9b426c0&e=16ffa34a09) - please note there are separate sheets for each board-release.

Test changes in this release:

* **Added** Verify ECC Presence test (1 test-case)
* **Added** Install Debian amd64 on SATA storage test (2 test-cases)
* **Fixed** ATA kernel boot time measurement automated test regarding missing
  tools on the booted OS
* **Updated** apu5 hardware configuration with `Quectel_EP06` LTE module and
  `WLE1216V5-20` WiFi module
* **Verified** (manually) OPNsense installation on apu3 platform
* **Verified** that USB modem (TL-WN722N) on apu2 USB3.0 port is initialized correctly
* **Verified** CPU boost load in terms of hard-locks (38h apu2 stress testing
  according to [blog post method](https://3mdeb.com/firmware/amd-cpu-boost/))

![Mainline test results](https://cloud.3mdeb.com/index.php/s/xr4zCeHwPtw97kq/preview)

![Legacy test results](https://cloud.3mdeb.com/index.php/s/7Jng9M8QE5DkPco/preview)

* Mainline:
  * PASSED: 318 (+12)
  * FAILED: 14 (-2)
  * PASSED [%]: 95,78% (+0.75%)
* Legacy:
  * PASSED: 293 (+11)
  * FAILED: 4 (-11)
  * PASSED [%]: 98.65% (+3.7%)

The improvement of the PASSED tests coverage results from adding 3 test-cases
and fixing ATA kernel boot time test (resolved [#220](https://github.com/pcengines/coreboot/issues/220)
issue). The difference in `mainline` and `legacy` FAILED tests statistics is
caused mainly by XEN tests problems, that are not supported in `legacy` testing.

## Binaries

### Mainline

* [apu1 v4.9.0.3](https://cloud.3mdeb.com/index.php/s/Xxcsxyb5T6gq4Zb/download)

  [SHA256 file](https://cloud.3mdeb.com/index.php/s/JdGFFEqnqSz7zmF/download)

  [SHA256 sig](https://cloud.3mdeb.com/index.php/s/eimcQrPTtw7C7mQ/download)

* [apu2 v4.9.0.3](https://cloud.3mdeb.com/index.php/s/aroRiaaRfoXsRJE/download)

  [SHA256 file](https://cloud.3mdeb.com/index.php/s/739Y6cg6E23bpzn/download)

  [SHA256 sig](https://cloud.3mdeb.com/index.php/s/cy37owiFs8ZWaMN/download)

* [apu3 v4.9.0.3](https://cloud.3mdeb.com/index.php/s/AbEX3keWGtGMFdD/download)

  [SHA256 file](https://cloud.3mdeb.com/index.php/s/CgdpBDx3jXqAaS4/download)

  [SHA256 sig](https://cloud.3mdeb.com/index.php/s/EggEQaLZmH3edDE/download)

* [apu4 v4.9.0.3](https://cloud.3mdeb.com/index.php/s/HmYYgQNnXCyyxD7/download)

  [SHA256 file](https://cloud.3mdeb.com/index.php/s/cgdyNNtQndCZRjK/download)

  [SHA256 sig](https://cloud.3mdeb.com/index.php/s/PapaR2daNrDjZ9r/download)

* [apu5 v4.9.0.2](https://cloud.3mdeb.com/index.php/s/Yotxg6WRoDCHHgp/download)

  [SHA256 file](https://cloud.3mdeb.com/index.php/s/FTHNN3g4mYwwkWw/download)

  [SHA256 sig](https://cloud.3mdeb.com/index.php/s/tARS2XqEafCQaDb/download)

### Legacy

* [apu2 v4.0.24](https://cloud.3mdeb.com/index.php/s/dpKqXzooprK6aJr/download)

  [SHA256 file](https://cloud.3mdeb.com/index.php/s/NfBptrfx9B56iJb/download)

  [SHA256 sig](https://cloud.3mdeb.com/index.php/s/EKfJTccSYTrwDt6/download)

* [apu3 v4.0.24](https://cloud.3mdeb.com/index.php/s/ACK32Wy6QtZbyNs/download)

  [SHA256 file](https://cloud.3mdeb.com/index.php/s/HyFkRnj3zmKHod3/download)

  [SHA256 sig](https://cloud.3mdeb.com/index.php/s/7WXMWAoWrAdWFz9/download)

* [apu4 v4.0.24](https://cloud.3mdeb.com/index.php/s/nzSMyApkKimzsEf/download)

  [SHA256 file](https://cloud.3mdeb.com/index.php/s/2W4EjpTii7LmwrC/download)

  [SHA256 sig](https://cloud.3mdeb.com/index.php/s/4wzJRPZ9FszRNYy/download)

* [apu5 v4.0.24](https://cloud.3mdeb.com/index.php/s/ito92SCGrn4pEyq/download)

  [SHA256 file](https://cloud.3mdeb.com/index.php/s/5DdxdmmzsCxSrkf/download)

  [SHA256 sig](https://cloud.3mdeb.com/index.php/s/jnaKWRBz7XWBxWA/download)

See how to verify the signatures on [asciinema](https://asciinema.org/a/227035)
