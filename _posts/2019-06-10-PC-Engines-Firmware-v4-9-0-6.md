---
layout: post
title:  "PC Engines apu coreboot Open Source Firmware v4.9.0.6"
date:   2019-06-10
categories: Firmware
---
# PC Engines apu coreboot Open Source Firmware v4.9.0.6

## Key changes

Mainline:

1. **Rebased** with official coreboot repository **commit** 3b4d0e0.
2. Added initial **support** of **vboot** with measured boot mode on APU2.
   This feature brings the FMAP layout of SPI flash, 3 fully bootable firmware
   volumes (which may act as a recovery fallback) and the TPM measurement of
   the BIOS components used during boot process. Details on how to build an
   image available in [apu2-documentation](https://github.com/pcengines/apu2-documentation/blob/master/docs/apu2_vboot.md)
3. **Updated SeaBIOS** to **rel-1.12.1.2** introducing small **fixes** for
   **SD 3.0** mode and **hard disk fallback boot** functionality. From now on
   platform will always try to boot hard disks first according to bootorder
   (or iPXE if set and enabled). When the first device is not bootable (i.e.
   contains invalid MBR signature), SeaBIOS will try next device in boot order
   until all storage devices have been tried. If no bootable device found,
   reboot after minute. Secondary payloads will not boot automatically from
   now. If one desires to launch setup or memtest, it requires physical
   presence in order to explicitly select the payload in the boot menu.
4. Published a **blog post** presenting the status of **Meltdown and Spectre**
   on **apu2**. Visit [3mdeb blog to read](https://blog.3mdeb.com/2019/2019-05-29-spectre-and-meltdown-on-apu2/)
5. **Enabled SD 3.0** mode allowing transfers of **~100MB/s**. All **UHS-I**
   capable cards should be able to be detected as **SDR104 or SDR50** (depending on the
   card). Tested SD cards were able to **reach 80MB/s** read transfer for SDR104
   (the manufacturer of the card guaranteed the transfers up to 80MB/s).
   Currently the SD 3.0 mode is disabled by default, because the operating
   system sometimes detected SDR104 capable card as SDR50 or as SD 2.0
   compliant card. So far no issues with SD card detection in SeaBIOS. For
   those interested in SD 3.0 mode, the option is available in setup menu as
   **runtime configurable**.
6. Enabled **runtime configuration** of **watchdog**. By default the timeout is
   set to 0 seconds (disabled state). To enable watchdog, enter setup menu and
   toggle watchdog option. You will be prompted to specify the timeout after
   which the platform should reset. [Options description](https://github.com/pcengines/sortbootorder#settings-description)
   **WARNING** do not set short timeouts! It may lead to a reset loop and
   brick Your platform. Please take into consideration that platform boot time
   and OS boot time also counts to the overall timeout time, so set at least
   few minutes timeout to still be able to enter setup menu to disable the
   watchdog! The operating system has to support the watchdog, otherwise the
   platform will constantly reboot. For Linux OSes the driver is `sp5100_tco`,
   however it conflicts with `i2c_piix4` leaving the watchdog driver unloaded
   completely. One has to properly blacklist the `i2c_piix4` driver in order
   to get the watchdog working.
7. Added a hidden **flash lockdown menu** in sortbootorder. Its purpose is to
   freely choose the **protection** of **BIOS** SPI flash offered by a Winbond
   W25Q64*V chip. The menu supports all block protection ranges and the status
   register protection. NOTE: the permanent lock does not work for the Winbond
   chips, this feature is available only on demand after contacting Winbond.
   For details how to use menu, see the [sortbootorder documentation](https://github.com/pcengines/sortbootorder#hidden-flash-lockdown-menu)
8. All USB devices (either external plugged to front USB 3.0 connector or
   attached to USb internal headers) have a single boot order entry. Previously
   the USb devices connected via headers did not have any boot order and landed
   at the end of boot device list despite USB was set to a high priority.
9. According to a [customer using FreeBSD](http://pcengines.info/forums/?page=post&fid=6D8DBBA4-9D40-4C87-B471-80CB5D9BD945&lastp=1&id=776921E8-222D-45F7-A234-910DEBBDA767)
   the serial ports were not configured automatically because, they were not
   present in the APCI namespace. Added entries for both serial ports to ACPI.

Legacy:

1. **Updated SeaBIOS** to **rel-1.12.1.2** introducing small **fixes** for
   **SD 3.0** mode and **hard disk fallback boot** functionality. From now on
   platform will always try to boot hard disks first according to bootorder
   (or iPXE if set and enabled). When the first device is not bootable (i.e.
   contains invalid MBR signature), SeaBIOS will try next device in boot order
   until all storage devices have been tried. If no bootable device found,
   reboot after minute. Secondary payloads will not boot automatically from
   now. If one desires to launch setup or memtest, it requires physical
   presence in order to explicitly select the payload in the boot menu.
2. **Enabled SD 3.0** mode allowing transfers of **~100MB/s**. All **UHS-I**
   capable cards should be able to be detected as **SDR104 or SDR50** (depending on the
   card). Tested SD cards were able to **reach 80MB/s** read transfer for SDR104
   (the manufacturer of the card guaranteed the transfers up to 80MB/s).
   Currently the SD 3.0 mode is disabled by default, because the operating
   system sometimes detected SDR104 capable card as SDR50 or as SD 2.0
   compliant card. So far no issues with SD card detection in SeaBIOS. For
   those interested in SD 3.0 mode, the option is available in setup menu as
   **runtime configurable**.
3. Enabled **runtime configuration** of **watchdog**. By default the timeout is
   set to 0 seconds (disabled state). To enable watchdog, enter setup menu and
   toggle watchdog option. You will be prompted to specify the timeout after
   which the platform should reset. [Options description](https://github.com/pcengines/sortbootorder#settings-description)
   **WARNING** do not set short timeouts! It may lead to a reset loop and
   brick Your platform. Please take into consideration that platform boot time
   and OS boot time also counts to the overall timeout time, so set at least
   few minutes timeout to still be able to enter setup menu to disable the
   watchdog! The operating system has to support the watchdog, otherwise the
   platform will constantly reboot. For Linux OSes the driver is `sp5100_tco`,
   however it conflicts with `i2c_piix4` leaving the watchdog driver unloaded
   completely. One has to properly blacklist the `i2c_piix4` driver in order
   to get the watchdog working.
4. Added a hidden **flash lockdown menu** in sortbootorder. Its purpose is to
   freely choose the **protection** of **BIOS** SPI flash offered by a Winbond
   W25Q64*V chip. The menu supports all block protection ranges and the status
   register protection. NOTE: the permanent lock does not work for the Winbond
   chips, this feature is available only on demand after contacting Winbond.
   For details how to use menu, see the [sortbootorder documentation](https://github.com/pcengines/sortbootorder#hidden-flash-lockdown-menu)
5. All USB devices (either external plugged to front USB 3.0 connector or
   attached to USb internal headers) have a single boot order entry. Previously
   the USB devices connected via headers did not have any boot order and landed
   at the end of boot device list despite USB was set to a high priority.
6. **ECC presence** is reported **in SMBIOS tables**. It is a backport from
   mainline versions.

## Community

Patches sent for review:

* [APU1 documentation](https://review.coreboot.org/c/coreboot/+/32907)

* [APU2 documentation](https://review.coreboot.org/c/coreboot/+/33146)

* [Describe serial ports in ACPI](https://review.coreboot.org/c/coreboot/+/32989)

## Statistics

![Files Changed](https://cloud.3mdeb.com/index.php/s/yFZx4T78w9QXZ9K/preview)

The chart shows the total files changed from release tag against the rebase
point of given release specified in CHANGELOG (CHANGELOG.md and gitlab-ci.yml
excluded from statistics). Check the statistics with:

```
git diff --stat 3b4d0e0 ':(exclude).gitlab-ci.yml' ':(exclude)CHANGELOG.md'
```

`88 files changed, 2573 insertions(+), 178 deletions(-)`

![Process of mainlining](https://cloud.3mdeb.com/index.php/s/aJnsJH4PGYyZo7e/preview)

The chart represents the total line added and deleted on the PC Engines
coreboot fork against the rebase point for a given release. Check the
statistics with:

```
git diff --stat 3b4d0e0 ':(exclude).gitlab-ci.yml' ':(exclude)CHANGELOG.md'
```

`88 files changed, 2573 insertions(+), 178 deletions(-)`

Two files have not been included in the diff as mentioned above since they are
not a part of coreboot tree.

The statistics has grown significantly due to two many configuration
options introduced in this version.

## Testing

* [PC Engines hardware configuration matrix](https://cloud.3mdeb.com/index.php/s/ce829QADwA7sHx9/preview) - hardware configurations available for testing in 3mdeb laboratory.

* [PC Engines release validation results](https://3mdeb.us16.list-manage.com/track/click?u=fce95b885fc13fbf1db611816&id=96d9b426c0&e=16ffa34a09) - please note there are separate sheets for each board-release.

Test changes in this release:

* **Added** SD card detect in BIOS test-suite (3 test-cases)
* **Improved** Voyage installation test with partitioning error-check
* **Replaced** HDD disk in the apu3 hardware configuration for better stability
* **Implemented** full automated regression testing:
  From now on regression tests start automatically by Jenkins machine that is
  integrated with pcengines/coreboot build system on GitHub

![Mainline test results](https://cloud.3mdeb.com/index.php/s/wkXxXY4zTnzMbTp/preview)

![Legacy test results](https://cloud.3mdeb.com/index.php/s/pkeNPqEN6XAWqJD/preview)

* Mainline:
  * PASSED: **373** (+13)
  * FAILED: **11** (-1)
  * PASSED [%]: **97.14%** (+0.37%)

* Legacy:
  * PASSED: **333** (+40)
  * FAILED: **5** (+1)
  * PASSED [%]: **98.52%** (-0.13%)

Improvement in the PASS aggregated statistics results from new SD card test and
adding SD card to the apu3 hardware matrix configuration enabling some of the
`NOT-SUPPORTED` tests before.

## Binaries

### Mainline

* [apu1 v4.9.0.6](https://3mdeb.com/open-source-firmware/pcengines/apu1/apu1_v4.9.0.6.rom)

  [SHA256 file](https://3mdeb.com/open-source-firmware/pcengines/apu1/apu1_v4.9.0.6.SHA256)

  [SHA256 sig](https://3mdeb.com/open-source-firmware/pcengines/apu1/apu1_v4.9.0.6.SHA256.sig)

* [apu2 v4.9.0.6](https://3mdeb.com/open-source-firmware/pcengines/apu2/apu2_v4.9.0.6.rom)

  [SHA256 file](https://3mdeb.com/open-source-firmware/pcengines/apu2/apu2_v4.9.0.6.SHA256)

  [SHA256 sig](https://3mdeb.com/open-source-firmware/pcengines/apu2/apu2_v4.9.0.6.SHA256.sig)

* [apu3 v4.9.0.6](https://3mdeb.com/open-source-firmware/pcengines/apu3/apu3_v4.9.0.6.rom)

  [SHA256 file](https://3mdeb.com/open-source-firmware/pcengines/apu3/apu3_v4.9.0.6.SHA256)

  [SHA256 sig](https://3mdeb.com/open-source-firmware/pcengines/apu3/apu3_v4.9.0.6.SHA256.sig)

* [apu4 v4.9.0.6](https://3mdeb.com/open-source-firmware/pcengines/apu4/apu4_v4.9.0.6.rom)

  [SHA256 file](https://3mdeb.com/open-source-firmware/pcengines/apu4/apu4_v4.9.0.6.SHA256)

  [SHA256 sig](https://3mdeb.com/open-source-firmware/pcengines/apu4/apu4_v4.9.0.6.SHA256.sig)

* [apu5 v4.9.0.6](https://3mdeb.com/open-source-firmware/pcengines/apu5/apu5_v4.9.0.6.rom)

  [SHA256 file](https://3mdeb.com/open-source-firmware/pcengines/apu5/apu5_v4.9.0.6.SHA256)

  [SHA256 sig](https://3mdeb.com/open-source-firmware/pcengines/apu5/apu5_v4.9.0.6.SHA256.sig)

### Legacy

* [apu2 v4.0.26](https://3mdeb.com/open-source-firmware/pcengines/apu2/apu2_v4.0.26.rom)

  [SHA256 file](https://3mdeb.com/open-source-firmware/pcengines/apu2/apu2_v4.0.26.SHA256)

  [SHA256 sig](https://3mdeb.com/open-source-firmware/pcengines/apu2/apu2_v4.0.26.SHA256.sig)

* [apu3 v4.0.26](https://3mdeb.com/open-source-firmware/pcengines/apu3/apu3_v4.0.26.rom)

  [SHA256 file](https://3mdeb.com/open-source-firmware/pcengines/apu3/apu3_v4.0.26.SHA256)

  [SHA256 sig](https://3mdeb.com/open-source-firmware/pcengines/apu3/apu3_v4.0.26.SHA256.sig)

* [apu4 v4.0.26](https://3mdeb.com/open-source-firmware/pcengines/apu4/apu4_v4.0.26.rom)

  [SHA256 file](https://3mdeb.com/open-source-firmware/pcengines/apu4/apu4_v4.0.26.SHA256)

  [SHA256 sig](https://3mdeb.com/open-source-firmware/pcengines/apu4/apu4_v4.0.26.SHA256.sig)

* [apu5 v4.0.26](https://3mdeb.com/open-source-firmware/pcengines/apu5/apu5_v4.0.26.rom)

  [SHA256 file](https://3mdeb.com/open-source-firmware/pcengines/apu5/apu5_v4.0.26.SHA256)

  [SHA256 sig](https://3mdeb.com/open-source-firmware/pcengines/apu5/apu5_v4.0.26.SHA256.sig)


See how to verify the signatures on [asciinema](https://asciinema.org/a/227035)

[1]: https://en.wikipedia.org/wiki/ROCA_vulnerability
[2]: https://github.com/pcengines/apu2-documentation/blob/master/docs/research/ROCA.md
[3]: https://github.com/pcengines/apu2-documentation/blob/master/docs/os-status.md

## What we planned

On v4.9.0.5 release we have announced:

1. Verified and measured boot with vboot and TPM. Advantages:
   - signed firmware components; each boot stage is signed with keys, where
     public part of the key lies in recovery partition
   - possibility to lock recovery partition and protect the keys while keeping
     updatable partitions unlocked for firmware upgrades
   - measured boot stages and firmware components; ensure Your firmware was not
     tampered thanks to PCRs in TPM

**DONE**

2. coreboot image layout in flashmap allowing to have few CBFS images in one
   ROM. Advantages:
   - one recovery full firmware partition, one or two updatable
     partitions with full firmware. In case of failed update of one partition,
     other partitions still work and vboot will fall back to other working
     partition

**DONE**

3. Tianocore UEFI payload integration. Build image with UEFI payload instead of
   SeaBIOS payload and boot UEFI OSes.

**WORK IN PROGRESS**

4. Blog post presenting the state of Meltdown and Spectre on apu2 with and
   without microcode updates. Coming end of May.

**DONE**

5. ECC memory presence status in SMBIOS/DMI tables in legacy BIOS.

**DONE**

4 out of 5 items has been addressed. Due to the preparations to the
[Open Source Firmware Conference (OSFC) 2019](https://osfc.io/) we did not manage to
check the recent Tianocore payload on apu2. If You are interested in PC Engines
firmware, would like to design something special or have some ideas in mind
contact us or see us directly at OSFC 2019.

## Coming soon

Feature and improvements on the roadmap:

1. Tianocore UEFI payload integration. Build image with UEFI payload instead of
   SeaBIOS payload and boot UEFI OSes.
2. PXE autoboot from the starting from the last interface with Wake on LAN
   support.
3. Improve the support of TPM2 in coreboot and SeaBIOS. Currently the is only
   the TCPA (TPM1.2) log support in coreboot. Additionally SeaBIOS overwrites
   existing entries in TPM2 log area. `cbmem` utility also lacks support for
   displaying TPM2 log area.
4. Validate ESXi 6.7. We have got information that booting ESXi 6.7 U2 fails on
   apu2 and are investigating the issue.
5. Linux GPIO support via ACPI tables. It will allow to control certain GPIOs
   via kernel sysfs (LEDs, S1 button, SIMSWAP).
6. Improve the iPXE performance. The DHCP autoconfiguration is very slow and
   sometimes fails (link autoconfiguration has to be repeated in iPXE shell).
