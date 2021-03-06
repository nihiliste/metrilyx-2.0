Roadmap
=======

##### v2.3.3 - v2.4.0
- Metric operatorations i.e. perform math against different series.

##### v2.3.2
- Complex annotation tag queries in particular the OR operator.
- Site analytics
- Toggle annotation detail visibility.

##### v2.3.1
- Enable/Disable cache layer.
- Performance related configuration changes.
- Angularjs unit tests.

##### v2.3.0
- Event annotations for both adhoc and dashboard view.
- Cleaner URL params for user readability.
- Auto updates when viewing adhoc graphs.
- Regex support for metric, tag-key and tag-value searches.
- Additional graph types: spline, area, stacked, pie, line.
- UI changes and fixes.
- Overall performance improvements.

##### v2.2.0
- Major performance improvements.
	- Data delivery system now completely **asynchronous**.
	- Data provided through **websockets**.
	- In flight data **compression** (permessage-deflate).
- **Nginx** used as reverse proxy rather than apache.
- Support for **distributed** and **HA** setup.

##### v2.1.0
- Ability to group pages based on tags.
- Ability to generate heatmaps against a metric.
- Ability to import and export pages.
- Updated graphing library to Highstock 2.0.1
- Improved the ability to move pods around on a page.
- Various performance improvements and bug fixes.
