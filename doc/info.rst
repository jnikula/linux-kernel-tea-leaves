.. SPDX-License-Identifier: AGPL-3.0-or-later
.. SPDX-FileCopyrightText: 2025 Jani Nikula <jani@nikula.org>

====
Info
====

Background info on the Linux kernel development process and notes on the
predictions.

Kernel Process
==============

For the longest time, the Linux kernel development cycles have followed the
pattern:

- Upon release of the previous kernel version, a two-week merge window opens for
  features heading to the next release.

- The release candidate -rc1 closes the merge window, and marks the beginning of
  the stabilization period aiming for release.

- There are seven or eight release candidates, more commonly seven.

- The release candidates and releases happen on a weekly basis, almost
  invariably on a Sunday.

- The release cycle length is thus nine or ten weeks.

Notes on Predictions
====================

This project predicts the current and upcoming development cycle release
candidate and release dates based on the latest tag in the upstream Linux git
repository, i.e. a single data point.

- Whether -rc8 occurs or not is the main source of uncertainty in the
  predictions.

- -rc8 is only included if it has actually occurred; otherwise it increases
  uncertainty in the following predictions by a week.

- Uncertainty is expressed as a date range.

- The date and date range format follows `ISO-8601`_.

- Dates not landing on a Sunday are rounded to the nearest Sunday for
  simplicity. Very rarely this leads to incorrect tagging dates being presented.

Completely accurate and trustworthy, right?

.. _ISO-8601: https://en.wikipedia.org/wiki/ISO_8601
