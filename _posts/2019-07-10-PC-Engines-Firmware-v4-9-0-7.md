---
layout: post
title:  "PC Engines apu coreboot Open Source Firmware v4.9.0.7"
date:   2019-07-10
categories: Firmware
---
# PC Engines apu coreboot Open Source Firmware v4.9.0.7

## Key changes

Mainline:

1. **Rebased** with official coreboot repository **commit** c32ccb7.
2. Added support for tianocore payload integration. Tianocore payload with
   coreboot package allows booting UEFI aware operating systems. How to build
   an image containing tianocore as a main payload instead of SeaBIOS is
   explained in [apu2-documentation](https://github.com/pcengines/apu2-documentation/blob/master/docs/tianocore_build.md)
3. **Updated SeaBIOS** to **rel-1.12.1.3** introducing small **fixes** for
   **hard disk fallback boot** functionality corner cases:
    - CBFS payloads were still booting when no HD media found (fixed)
    - CBFS payloads can be loaded only explicitly when entered to boot menu
      with F10 key
    - if no HD media present and PXE is disabled, after boot menu wait timeout
      SeaBIOS will print that no bootable device has been found and will reboot
      after 60 seconds, unless entered to boot menu to choose a CBFS payload
   Also cleaned up unused and obsolete code from older SeaBIOS versions.
4. **Updated sortbootorder** to **v4.6.15** introducing small fix to SPI
   lockdown menu, where IF statements had bad condition formulas.
5. **Disabled IPv6** in **iPXE** payload. This option often caused timeouts on
   dhcp/autoboot commands. Now the link configuration is much faster. This also
   resolves following [issue.](https://github.com/pcengines/coreboot/issues/181)
6. **Removed incorrectly assigned clock request mappings.** The clock request
   signals are either hardwired to on for NICs or routed to mPCIe connectors.
   However the mappings were not correctly set. They have been removed for now
   and clocks set to always on for all PCIe lanes. The mPCIe2 clock forcing
   does not change anything for now. The correct mappings will be implemented
   in next release to save the energy.

Legacy:

1. **Updated SeaBIOS** to **rel-1.12.1.3** introducing small **fixes** for
   **hard disk fallback boot** functionality corner cases:
    - CBFS payloads were still booting when no HD media found (fixed)
    - CBFS payloads can be loaded only explicitly when entered to boot menu
      with F10 key
    - if no HD media present and PXE is disabled, after boot menu wait timeout
      SeaBIOS will print that no bootable device has been found and will reboot
      after 60 seconds, unless entered to boot menu to choose a CBFS payload
   Also cleaned up unused and obsolete code from older SeaBIOS versions.
2. **Updated sortbootorder** to **v4.6.15** introducing small fix to SPI
   lockdown menu, where IF statements had bad condition formulas.
3. **Disabled IPv6** in **iPXE** payload. This option often caused timeouts on
   dhcp/autoboot commands. Now the link configuration is much faster. This also
   resolves following [issue.](https://github.com/pcengines/coreboot/issues/181)
4. **Updated iPXE** revision to **2019.3** (iPXE in mainline got updated along
   with rebase).

## Community

Patches merged by community:

* [APU1 documentation](https://review.coreboot.org/c/coreboot/+/32907)

* [APU2 documentation](https://review.coreboot.org/c/coreboot/+/33146)

* [microcode update infrastructure](https://review.coreboot.org/c/coreboot/+/29272)

## Statistics

![Files Changed](https://cloud.3mdeb.com/index.php/s/rfrq6FaxNLCLzSa/preview)

The chart shows the total files changed from release tag against the rebase
point of given release specified in CHANGELOG (CHANGELOG.md and gitlab-ci.yml
excluded from statistics). Check the statistics with:

```
git diff --stat c32ccb7 ':(exclude).gitlab-ci.yml' ':(exclude)CHANGELOG.md'
```

`87 files changed, 2589 insertions(+), 184 deletions(-)`

![Process of mainlining](https://cloud.3mdeb.com/index.php/s/Mew82wtGox4iKR8/preview)

The chart represents the total line added and deleted on the PC Engines
coreboot fork against the rebase point for a given release. Check the
statistics with:

```
git diff --stat c32ccb7 ':(exclude).gitlab-ci.yml' ':(exclude)CHANGELOG.md'
```

`87 files changed, 2589 insertions(+), 184 deletions(-)`

Two files have not been included in the diff as mentioned above since they are
not a part of coreboot tree.

The statistics has grown significantly due to two many configuration
options introduced in this version.

## Testing

* [PC Engines hardware configuration matrix](https://cloud.3mdeb.com/index.php/s/ce829QADwA7sHx9/preview) - hardware configurations available for testing in 3mdeb laboratory.

* [PC Engines release validation results](https://3mdeb.us16.list-manage.com/track/click?u=fce95b885fc13fbf1db611816&id=96d9b426c0&e=16ffa34a09) - please note there are separate sheets for each board-release.

Test changes in this release:

* **added** SeaBIOS verification test for unbootable devices (4 test cases)
* **added** Watchdog verification tests (4 test cases)
* **added** SD3.0 enable/disable mode verification (2 test cases)
* **added** SD3.0 performance test (1 test case)
* **upgraded** pfSense stick installer to version `2.4.4-RELEASE-p3`
* **improved** autoregression testing on Jenkins machine

![Mainline test results](https://cloud.3mdeb.com/index.php/s/94yRGRnaJGi83Mk/preview)

![Legacy test results](https://cloud.3mdeb.com/index.php/s/dxx7B6T9CKprsJ6/preview)

* Mainline:
  * PASSED: **410** (+37)
  * FAILED: **14** (+3)
  * PASSED [%]: **96.70%** (-0.44%)

* Legacy:
  * PASSED: **368** (+35)
  * FAILED: **9** (+4)
  * PASSED [%]: **97.61%** (-0.91%)

Improvement in the `PASSED` aggregated statistics results from the new 11
test-cases and enabling ECC tests on legacy. Summary of `FAILED` tests increased
due to [#321](https://github.com/pcengines/coreboot/issues/321) issue.

## Binaries

### Mainline

* [apu1 v4.9.0.7](https://3mdeb.com/open-source-firmware/pcengines/apu1/apu1_v4.9.0.7.rom)

  [SHA256 file](https://3mdeb.com/open-source-firmware/pcengines/apu1/apu1_v4.9.0.7.SHA256)

  [SHA256 sig](https://3mdeb.com/open-source-firmware/pcengines/apu1/apu1_v4.9.0.7.SHA256.sig)

* [apu2 v4.9.0.7](https://3mdeb.com/open-source-firmware/pcengines/apu2/apu2_v4.9.0.7.rom)

  [SHA256 file](https://3mdeb.com/open-source-firmware/pcengines/apu2/apu2_v4.9.0.7.SHA256)

  [SHA256 sig](https://3mdeb.com/open-source-firmware/pcengines/apu2/apu2_v4.9.0.7.SHA256.sig)

* [apu3 v4.9.0.7](https://3mdeb.com/open-source-firmware/pcengines/apu3/apu3_v4.9.0.7.rom)

  [SHA256 file](https://3mdeb.com/open-source-firmware/pcengines/apu3/apu3_v4.9.0.7.SHA256)

  [SHA256 sig](https://3mdeb.com/open-source-firmware/pcengines/apu3/apu3_v4.9.0.7.SHA256.sig)

* [apu4 v4.9.0.7](https://3mdeb.com/open-source-firmware/pcengines/apu4/apu4_v4.9.0.7.rom)

  [SHA256 file](https://3mdeb.com/open-source-firmware/pcengines/apu4/apu4_v4.9.0.7.SHA256)

  [SHA256 sig](https://3mdeb.com/open-source-firmware/pcengines/apu4/apu4_v4.9.0.7.SHA256.sig)

* [apu5 v4.9.0.7](https://3mdeb.com/open-source-firmware/pcengines/apu5/apu5_v4.9.0.7.rom)

  [SHA256 file](https://3mdeb.com/open-source-firmware/pcengines/apu5/apu5_v4.9.0.7.SHA256)

  [SHA256 sig](https://3mdeb.com/open-source-firmware/pcengines/apu5/apu5_v4.9.0.7.SHA256.sig)

### Legacy

* [apu2 v4.0.27](https://3mdeb.com/open-source-firmware/pcengines/apu2/apu2_v4.0.27.rom)

  [SHA256 file](https://3mdeb.com/open-source-firmware/pcengines/apu2/apu2_v4.0.27.SHA256)

  [SHA256 sig](https://3mdeb.com/open-source-firmware/pcengines/apu2/apu2_v4.0.27.SHA256.sig)

* [apu3 v4.0.27](https://3mdeb.com/open-source-firmware/pcengines/apu3/apu3_v4.0.27.rom)

  [SHA256 file](https://3mdeb.com/open-source-firmware/pcengines/apu3/apu3_v4.0.27.SHA256)

  [SHA256 sig](https://3mdeb.com/open-source-firmware/pcengines/apu3/apu3_v4.0.27.SHA256.sig)

* [apu4 v4.0.27](https://3mdeb.com/open-source-firmware/pcengines/apu4/apu4_v4.0.27.rom)

  [SHA256 file](https://3mdeb.com/open-source-firmware/pcengines/apu4/apu4_v4.0.27.SHA256)

  [SHA256 sig](https://3mdeb.com/open-source-firmware/pcengines/apu4/apu4_v4.0.27.SHA256.sig)

* [apu5 v4.0.27](https://3mdeb.com/open-source-firmware/pcengines/apu5/apu5_v4.0.27.rom)

  [SHA256 file](https://3mdeb.com/open-source-firmware/pcengines/apu5/apu5_v4.0.27.SHA256)

  [SHA256 sig](https://3mdeb.com/open-source-firmware/pcengines/apu5/apu5_v4.0.27.SHA256.sig)

See how to verify the signatures on [asciinema](https://asciinema.org/a/227035)

[1]: https://en.wikipedia.org/wiki/ROCA_vulnerability
[2]: https://github.com/pcengines/apu2-documentation/blob/master/docs/research/ROCA.md
[3]: https://github.com/pcengines/apu2-documentation/blob/master/docs/os-status.md

## What we planned

On v4.9.0.6 release we have announced:

1. Tianocore UEFI payload integration. Build image with UEFI payload instead of
   SeaBIOS payload and boot UEFI OSes.

**DONE**

2. PXE autoboot from the starting from the last interface with Wake on LAN
   support.

**WORK IN REVIEW**

3. Improve the support of TPM2 in coreboot and SeaBIOS. Currently the is only
   the TCPA (TPM1.2) log support in coreboot. Additionally SeaBIOS overwrites
   existing entries in TPM2 log area. `cbmem` utility also lacks support for
   displaying TPM2 log area.

**WORK IN PROGRESS**

4. Validate ESXi 6.7. We have got information that booting ESXi 6.7 U2 fails on
   apu2 and are investigating the issue.

**WORK IN PROGRESS**

5. Linux GPIO support via ACPI tables. It will allow to control certain GPIOs
   via kernel sysfs (LEDs, S1 button, SIMSWAP).

**WORK IN PROGRESS**

6. Improve the iPXE performance. The DHCP autoconfiguration is very slow and
   sometimes fails (link autoconfiguration has to be repeated in iPXE shell).

**DONE**

## Coming soon

Feature and improvements on the roadmap:

1. Improve the support of TPM2 in coreboot and SeaBIOS. Currently the is only
   the TCPA (TPM1.2) log support in coreboot. Additionally SeaBIOS overwrites
   existing entries in TPM2 log area. `cbmem` utility also lacks support for
   displaying TPM2 log area.
2. Validate ESXi 6.7. We have got information that booting ESXi 6.7 U2 fails on
   apu2 and are investigating the issue.
3. Linux GPIO support via ACPI tables. It will allow to control certain GPIOs
   via kernel sysfs (LEDs, S1 button, SIMSWAP).
4. Fix bugs related to Nuvoton NCT5104D reset and implement GPIO access
   improvements.
5. Reorganize runtime configuration by making it persistent across updates and
   accessible from user space. Also prepare a tool for offline binary modification.
