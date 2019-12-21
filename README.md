# sqltemplate
Database query tool based on SQL templates

## Development status

* Alpha
* API may be radically changed until first Beta release
* Not tested automatically yet
 
### Roadmap

* 0.6 - drop django-sqltemplate compatibility layer
* 0.7 - automated tests, first beta release
* 0.8 - stable API
* 0.9,<1.0 - minor improvements without API changes, bugfixes
* 1.0 - first stable release

## Introduction

SQL is a great and poweruful DSL, which is easeier in maintenance 
when you're working on complext queries (i.e. reporting queries).
But the main problem of raw SQL is a commonly used "spaghetti" anti-pattern, 
when you're embedding/building SQLs directly in your code.

The solution comes from templating SQLs idea and `sqltemplate` 
is a simple implementation of it.

## Template system / database agnostic

The `sqltemplate` provides an abstraction layer for templating SQL
queries and working with query results. It requires an adapter to work.

For example - if you want to use `sqltemplate` together with Django
templates and database management, use [django-sqltemplate](https://github.com/marcinn/django-sqltemplate) adapter
directly.


## Backward compatibilty with `django-template`

The 0.5.x branch contains a compatibility layer with `django-template`.
The layer provides Django adapter and necessary imports.


## Building an adapter


Adapter must implement few callables required by `sqltemplate` core.
The adapter may be as a class instance or pure Python module providing
such functions. These functions are defined as:

`load_template(template_name)`

Must load template by name and return some kind of template object,
which will be passed to `render_template()` as an argument.


`create_template_from_string(string)`

Creates template object from provided string.


`render_template(template, context)`

Must render the template object using provided context (a dict).


`do_query(sql, query_params, using=None)`

Must execute a `sql` query with `query_params` applied.

Optional `using` argument specifies database connection identifier.
This may be any object dependent on how your adapter recognizes 
particular connections. For Django adapter, for example, this is a 
string with a connection name.


## Dependencies

* sqlparse
* flatdict

## License

BSD
