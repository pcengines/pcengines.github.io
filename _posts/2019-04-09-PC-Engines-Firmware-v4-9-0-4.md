---
layout: post
title:  "PC Engines apu coreboot Open Source Firmware v4.9.0.4"
date:   2019-04-09
categories: Firmware
---
# PC Engines apu coreboot Open Source Firmware v4.9.0.4

## Key changes

Mainline:

1. **Added possibility** to reboot platform with coldboot path to ensure full
   platform reset during **remote firmware update**, option is intended to
   mitigate reboot issue when migrating from BIOS version older than v4.9.0.x.
   For detail how to safely update firmware remotely, please refer to
   the [documentation](https://github.com/pcengines/apu2-documentation/blob/master/docs/firmware_flashing.md#corebootrom-flashing).
2. **Updated SeaBIOS** to rel-1.12.1.1 with **new TPM menu** option. For
   details **how to use** the menu options for **TPM** please refer to the
   [documentation](https://github.com/pcengines/apu2-documentation/blob/master/docs/tpm_menu.md).
3. **Rebased** with official coreboot repository **commit** 28def8b.
4. Created a **repository structure** for [apu2-documentatation](https://github.com/pcengines/apu2-documentation#repository-structure)
   repository for **better overview** of the contents inside the
   **documentation** repository.
5. Performed comprehensive **research** of **fastboot** capability for PC
   Engines platforms. The outcome is available [here](https://github.com/pcengines/apu2-documentation/blob/master/docs/research/fast_boot.md).
   In short, it is **not possible** to achieve Intel like fastboot feature,
   which allows **to skip full memory training** during boot using stored
   configuration in MRC cache. That is also an official **AMD statement**, that
   the **fastboot** is possible **only** during **S3 wakeup**.
6. We have been reached by our customers with a question about
   **ROCA TPM vulnerability** for Infineon SLB9665 chips present on
   **TPM1a modules**. The engineers verified that the **TPMs are vulnerable**.
   For details and mitigation refer to the [documentation](https://github.com/pcengines/apu2-documentation/blob/master/docs/research/ROCA.md).
   The document describes how to **upgrade TPM firmware** and
   **get rid of the vulnerability**.
7. Added a [list of supported and verified mPCIe modules](https://github.com/pcengines/apu2-documentation/blob/master/docs/mpcie_modules.md).
   The list also describes **known issues** with modules and **workarounds** to get the **modules working** properly. Please check the list when
   encountered any issues with mPCIe modules. Contribution is welcome. Also be
   sure to check whether the slot is compatible with the module. In order to do so, look at the interfaces connected to each mPCIe slot [here](https://github.com/pcengines/apu2-documentation/blob/master/docs/APU_mPCIe_capabilities.md) and the interfaces required by the module in its
   product specification etc.

## Statistics

![Files Changed]()

The chart shows the total files changed from release tag against the rebase
point of given release specified in CHANGELOG (CHANGELOG.md and gitlab-ci.yml
excluded from statistics). Check the statistics with:

```
git diff --stat 7a732b4 ':(exclude)gitlab-ci.yml' ':(exclude)CHANGELOG.md'
```

`72 files changed, 2240 insertions(+), 138 deletions(-)`

![Addition and Deletion]()

The chart represents the total line added and deleted on the PC Engines
corebootÂ fork against the rebase point for given release. Check the statistics
with:

```
git diff --stat 7a732b4 ':(exclude)gitlab-ci.yml' ':(exclude)CHANGELOG.md'
```

`72 files changed, 2240 insertions(+), 138 deletions(-)`

Two files have not been included in the diff as mentioned above since they are
not a part of coreboot tree.

## Testing

* [PC Engines hardware configuration matrix](https://cloud.3mdeb.com/index.php/s/wRi33Zo5sdgbpWn/preview) - hardware configurations available for testing in 3mdeb laboratory.

* [PC Engines release validation results](https://3mdeb.us16.list-manage.com/track/click?u=fce95b885fc13fbf1db611816&id=96d9b426c0&e=16ffa34a09) - please note there are separate sheets for each board-release.

Test changes in this release:

TBD

![Mainline test results]()

* Mainline:
  * PASSED: 318 (+12)
  * FAILED: 14 (-2)
  * PASSED [%]: 95,78% (+0.75%)

(Description)

## Binaries

### Mainline

* [apu1 v4.9.0.4](https://3mdeb.com/open-source-firmware/pcengines/apu1/apu1_v4.9.0.4.rom)

  [SHA256 file](https://3mdeb.com/open-source-firmware/pcengines/apu1/apu1_v4.9.0.4.SHA256)

  [SHA256 sig](https://3mdeb.com/open-source-firmware/pcengines/apu1/apu1_v4.9.0.4.SHA256.sig)

* [apu2 v4.9.0.4](https://3mdeb.com/open-source-firmware/pcengines/apu2/apu2_v4.9.0.4.rom)

  [SHA256 file](https://3mdeb.com/open-source-firmware/pcengines/apu2/apu2_v4.9.0.4.SHA256)

  [SHA256 sig](https://3mdeb.com/open-source-firmware/pcengines/apu2/apu2_v4.9.0.4.SHA256.sig)

* [apu3 v4.9.0.4](https://3mdeb.com/open-source-firmware/pcengines/apu3/apu3_v4.9.0.4.rom)

  [SHA256 file](https://3mdeb.com/open-source-firmware/pcengines/apu3/apu3_v4.9.0.4.SHA256)

  [SHA256 sig](https://3mdeb.com/open-source-firmware/pcengines/apu3/apu3_v4.9.0.4.SHA256.sig)

* [apu4 v4.9.0.4](https://3mdeb.com/open-source-firmware/pcengines/apu4/apu4_v4.9.0.4.rom)

  [SHA256 file](https://3mdeb.com/open-source-firmware/pcengines/apu4/apu4_v4.9.0.4.SHA256)

  [SHA256 sig](https://3mdeb.com/open-source-firmware/pcengines/apu4/apu4_v4.9.0.4.SHA256.sig)

* [apu5 v4.9.0.4](https://3mdeb.com/open-source-firmware/pcengines/apu5/apu5_v4.9.0.4.rom)

  [SHA256 file](https://3mdeb.com/open-source-firmware/pcengines/apu5/apu5_v4.9.0.4.SHA256)

  [SHA256 sig](https://3mdeb.com/open-source-firmware/pcengines/apu5/apu5_v4.9.0.4.SHA256.sig)

See how to verify the signatures on [asciinema](https://asciinema.org/a/227035)
