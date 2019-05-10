---
layout: post
title:  "PC Engines apu coreboot Open Source Firmware v4.9.0.5"
date:   2019-05-10
categories: Firmware
---
# PC Engines apu coreboot Open Source Firmware v4.9.0.5

## Key changes

Mainline:

1. **Rebased** with official coreboot repository **commit** fe80bf2.
2. **Fixed MP table** creation. There were small **errors in entries** for PCI
   interrupts for **xHCI, SDHCI, PCIe bridges**. Also added entries for IOMMU
   and PCIe endpoint devices.
3. Removed redundant SVI2 message in sign-of-life during boot process.
4. Created **[theory of operation](https://github.com/pcengines/apu2-documentation/blob/master/docs/theory-of-operation.md)**
   for apu firmware features in order to help understand and properly utilize
   the features and advantages of the PC Engines firmware. They have been
   present in a form of asciinema records.
5. Researched **[USB compliance tests](https://github.com/pcengines/apu2-documentation/blob/master/docs/research/USB_compliance_test.md)**
   in order to leverage problems with USB stick detection in BIOS. It is a
   first step before analyzing USB protocol on low level to search for issues
   and possible fixes.
6. Prepared migration for platform to use postcar stage. Usage of postcar stage
   is a requirement to keep board in the main coreboot tree for next November
   release.

## Community

Patches sent for review:

* [Microcode update infrastructure for AMD family 16h processors](https://review.coreboot.org/c/coreboot/+/29272)

* [Migrate to postcar stage](https://review.coreboot.org/c/coreboot/+/32363)

## Statistics

![Files Changed](https://cloud.3mdeb.com/index.php/s/ysXTSd8kW5HX2b2/preview)

The chart shows the total files changed from release tag against the rebase
point of given release specified in CHANGELOG (CHANGELOG.md and gitlab-ci.yml
excluded from statistics). Check the statistics with:

```
git diff --stat fe80bf2 ':(exclude).gitlab-ci.yml' ':(exclude)CHANGELOG.md'
```

`76 files changed, 2102 insertions(+), 163 deletions(-)`

![Process of mainlining](https://cloud.3mdeb.com/index.php/s/yjJAC5m3m6DJBLF/preview)

The chart represents the total line added and deleted on the PC Engines
coreboot fork against the rebase point for a given release. Check the
statistics with:

```
git diff --stat fe80bf2 ':(exclude).gitlab-ci.yml' ':(exclude)CHANGELOG.md'
```

`76 files changed, 2102 insertions(+), 163 deletions(-)`

Two files have not been included in the diff as mentioned above since they are
not a part of coreboot tree.

## Testing

* [PC Engines hardware configuration matrix](https://cloud.3mdeb.com/index.php/s/wRi33Zo5sdgbpWn/preview) - hardware configurations available for testing in 3mdeb laboratory.

* [PC Engines release validation results](https://3mdeb.us16.list-manage.com/track/click?u=fce95b885fc13fbf1db611816&id=96d9b426c0&e=16ffa34a09) - please note there are separate sheets for each board-release.

Test changes in this release:

* **Added** TPM menu verification test (2 test-cases)
* **Added** Clear TPM validation test (1 test-case)
* **Added** TPM PCR banks verification (2 test-cases)
* **Improved** Sign of Life test with additional restrictions regarding SoL lines
* **Improved** stability of the hardware infrastructure with an additional
  isolated network

![Mainline test results](https://cloud.3mdeb.com/index.php/s/yR6BYof9fAKXFd2/preview)

* Mainline:
  * PASSED: **360** (+19)
  * FAILED: **12** (+1)
  * PASSED [%]: **96.77%** (-0.11%)

The small reduction of the PASSED tests coverage results from returning problem
with stable XEN/Core booting and USB sticks detection on apu5.

## Binaries

### Mainline

* [apu1 v4.9.0.5](https://3mdeb.com/open-source-firmware/pcengines/apu1/apu1_v4.9.0.5.rom)

  [SHA256 file](https://3mdeb.com/open-source-firmware/pcengines/apu1/apu1_v4.9.0.5.SHA256)

  [SHA256 sig](https://3mdeb.com/open-source-firmware/pcengines/apu1/apu1_v4.9.0.5.SHA256.sig)

* [apu2 v4.9.0.5](https://3mdeb.com/open-source-firmware/pcengines/apu2/apu2_v4.9.0.5.rom)

  [SHA256 file](https://3mdeb.com/open-source-firmware/pcengines/apu2/apu2_v4.9.0.5.SHA256)

  [SHA256 sig](https://3mdeb.com/open-source-firmware/pcengines/apu2/apu2_v4.9.0.5.SHA256.sig)

* [apu3 v4.9.0.5](https://3mdeb.com/open-source-firmware/pcengines/apu3/apu3_v4.9.0.5.rom)

  [SHA256 file](https://3mdeb.com/open-source-firmware/pcengines/apu3/apu3_v4.9.0.5.SHA256)

  [SHA256 sig](https://3mdeb.com/open-source-firmware/pcengines/apu3/apu3_v4.9.0.5.SHA256.sig)

* [apu4 v4.9.0.5](https://3mdeb.com/open-source-firmware/pcengines/apu4/apu4_v4.9.0.5.rom)

  [SHA256 file](https://3mdeb.com/open-source-firmware/pcengines/apu4/apu4_v4.9.0.5.SHA256)

  [SHA256 sig](https://3mdeb.com/open-source-firmware/pcengines/apu4/apu4_v4.9.0.5.SHA256.sig)

* [apu5 v4.9.0.5](https://3mdeb.com/open-source-firmware/pcengines/apu5/apu5_v4.9.0.5.rom)

  [SHA256 file](https://3mdeb.com/open-source-firmware/pcengines/apu5/apu5_v4.9.0.5.SHA256)

  [SHA256 sig](https://3mdeb.com/open-source-firmware/pcengines/apu5/apu5_v4.9.0.5.SHA256.sig)

See how to verify the signatures on [asciinema](https://asciinema.org/a/227035)

[1]: https://en.wikipedia.org/wiki/ROCA_vulnerability
[2]: https://github.com/pcengines/apu2-documentation/blob/master/docs/research/ROCA.md
[3]: https://github.com/pcengines/apu2-documentation/blob/master/docs/os-status.md

## Coming soon

Feature and improvements on the roadmap:

1. Verified and measured boot with vboot and TPM. Advantages:
   - signed firmware components; each boot stage is signed with keys, where
     public part of the key lies in recovery partition
   - possibility to lock recovery partition and protect the keys while keeping
     updatable partitions unlocked for firmware upgrades
   - measured boot stages and firmware components; ensure Your firmware was not
     tampered thanks to PCRs in TPM
2. coreboot image layout in flashmap allowing to have few CBFS images in one
   ROM. Advantages:
   - one recovery full firmware partition, one or two updatable
     partitions with full firmware. In case of failed update of one partition,
     other partitions still work and vboot will fall back to other working
     partition
3. Tianocore UEFI payload integration. Build image with UEFI payload instead of
   SeaBIOS payload and boot UEFI OSes.
4. Blog post presenting the state of Meltdown and Spectre on apu2 with and
   without microcode updates. Coming end of May.
5. ECC memory presence status in SMBIOS/DMI tables in legacy BIOS.
