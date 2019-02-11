---
layout: post
title:  "PC Engines apu coreboot Open Source Firmware v4.9.0.1"
date:   2019-01-20
categories: Firmware
---
# PC Engines apu coreboot Open Source Firmware v4.9.0.1

## Key changes

* Resolved issues with [rebooting on mainline firmware](https://3mdeb.us16.list-manage.com/track/click?u=fce95b885fc13fbf1db611816&id=279a83d9fd&e=16ffa34a09)
* **Enabled TPM** by default in apu1, apu2, and apu5. 
* **SeaBIOS** has been rebased on stable **1.12.0** release which brings correct detection of TPM2.0 modules.
* **Fixed** the problem with **hanging pfSense** on **legacy** firmware. EHCI0 seems to cause problems on apu2, where it is not populated. Option to enable EHCI0 on apu2 has been blocked to avoid problems in the future.
* **Fixed** the bug which caused AGESA to return **error on late init**.
* Introduced reproducible builds for whole binary. iPXE is no longer built with random build ID.
* coreboot 4.9 has been released before Christmas, thus **we moved to v4.9.0.x** naming.

 
## Statistics

![Files Changed](/assets/2019-01-20-chart-1.png) 

![Addition and Deletion](/assets/2019-01-20-chart-2.png)

Difference has grown a little, since some patches have not yet been merged (e.g. apu1 LPC TPM enabling)

## coreboot community

Patches merged:

* [Fix reboot hang](https://3mdeb.us16.list-manage.com/track/click?u=fce95b885fc13fbf1db611816&id=ab6b3c088b&e=16ffa34a09)
* [Fix AGESA bug in late init](https://3mdeb.us16.list-manage.com/track/click?u=fce95b885fc13fbf1db611816&id=847f88ee93&e=16ffa34a09)

Patches sent for review:

* [Enable LPC TPM on apu1](https://3mdeb.us16.list-manage.com/track/click?u=fce95b885fc13fbf1db611816&id=2e8eae089e&e=16ffa34a09)

## Testing

* [PC Engines hardware configuration matrix](https://3mdeb.us16.list-manage.com/track/click?u=fce95b885fc13fbf1db611816&id=486e98e016&e=16ffa34a09) - hardware configurations available for testing in 3mdeb laboratory.
* [PC Engines release validation results](https://3mdeb.us16.list-manage.com/track/click?u=fce95b885fc13fbf1db611816&id=96d9b426c0&e=16ffa34a09) - please note there are separate sheets for each board-release.

![Legacy test results](/assets/2019-01-20-chart-3.png)

![Mainline test results](/assets/2019-01-20-chart-4.png)

* Mainline
    * PASSED: 298 (-1)
    * FAILED: 14 (+3)
    * PASSED [%]: 95,51% (-0,94%)
         
* Legacy
    * PASSED: 280 (-3)
    * FAILED: 19 (0)
    * PASSED [%]: 93,65% (-0,06%)

