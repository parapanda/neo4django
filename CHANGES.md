### Changes

#### 0.2.0 (2016-4-10)

* Renamed project to neo4django2 to avoid confusion w/ original project
* Added Neo4j Docker example 
* Upgraded to django 1.9+
* Upgraded to httplib2 0.9+
* Upgraded to decorator 4+
* Upgraded to python-dateutil 2.5+
* Upgraded to lucene-querybuilder 0.2+
* Upgraded to neo4jrestclient 2+
* Upgraded test requirments
* Added support for fixed-point number
* Added support for floating-point number

#### 0.1.8 (2013-4-18)

* Now supports Neo4j 1.8.2 and 1.9.RC1. Older versions are no longer supported.
* Docs have been expanded and moved to Sphinx for hosting by RTD (#144).
* In-graph Django user auth is now supported (#147).
* RelationshipQuerySet now inherits from neo4django's regular QuerySet.  `object.related.all()` can now be safely filtered against, deleted, etc, and supports all methods type-wide queries support (#141).
* QuerySet.order_by(), exists(), and count() (#140, #60).
* QuerySet aggregation support (Avg, Count...) (#53).
* QuerySet.delete() now does the hard work DB-side (#79).
* DateTimeProperty and DateTimeTZProperty were merged to handle timezones the Django way (#148).
* NodeModels are now pickleable (#46).
* Bug fixes - #150 and #151.

#### 0.1.7 (2012-9-12)

* Updated to support Neo4j 1.7.2 & 1.8.M07 (issue #110)
* select_related() performance improvements (issue #125)
* More RelationshipQuerySet functionality (issues #111, #81, #91, #92, #93)
* Better "internal" Cypher support with connection.cypher()
* REST auth support.
* More closely matches existing Django ORM (eg issue #103)
* All sorts of other performance improvements (eg issue #122)
* Bug fixes and stability improvements (issues #129, #67, #86, #62, #84, #127, #14, #88, #107, #56, #61, #66, #54, #51) helped along by integration with Travis CI.

#### 0.1.5 (2011-12-11)

* select_related() and model caching (issue #42)
* Small benchmark suite (issue #22)
* 'contains' field lookup (issue #3)
* Query by node id (id__exact, id__in - issue #28)
* AutoProperty values guaranteed transactional (issue #38)
* Index/query array property members individually (the 'member' field lookup, issue #37)
* in_bulk() object access (issue #31)
* Fixed the objects.all() "AttributeError" foolishness that shows up in interpreters.
* Bug fixes galore.

#### 0.1.4 (2011-09-23)

* Relationships can now target strings as well as model classes.

#### 0.1.3 (2011-09-20)

* Refactored model access to be more like traditional Django. To define models, import `from neo4django.db import models`.
* Added a database router to allow mixing of neo4django/Django ORM in one project.

#### 0.1.2 (2011-09-01)

* Model to model casting. (issue #7)

#### 0.1.1 (2011-08-30)

* One-to-one relationship support. (issue #10)
* Fixed a major bug where `NodeQueryset`s weren't returning models without filtering. Improved the test to catch a regression.
