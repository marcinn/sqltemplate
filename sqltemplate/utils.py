try:
    import sqlparse
except ImportError:
    from . import dummy_sqlparse as sqlparse


def prettify(sql):
    return sqlparse.format(sql, reindent=True, keyword_case='upper')
