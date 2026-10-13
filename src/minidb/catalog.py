from sqlglot import exp
from sqlglot.optimizer.optimizer import DialectType
from sqlglot.optimizer import optimize
from sqlglot.optimizer.annotate_types import annotate_types
from sqlglot.optimizer.qualify import qualify
from sqlglot.optimizer.normalize import normalize
from sqlglot.optimizer.pushdown_predicates import pushdown_predicates
import sqlglot
from sqlglot import parse_one



class catalog_schema():

    def __init__(self):
        optimizer_catalog = {"catalog_test1": {"new_col1": "TEXT"}}
        sql_raw = "select * from catalog_test1"
        tree = sqlglot.parse_one("select * from catalog_test1", dialect="postgres")
        return tree

    def rules(self):
        qualified = qualify(tree, schema=optimizer_catalog, dialect="postgres")

        annotated_tree = annotate_types(tree, schema = optimizer_catalog, dialect="postgres")
        annotated_tree.expressions[0].type.this
        print(annotated_tree.expressions[0].type.this)

        pushdown_tree =pushdown_predicates(tree, dialect="postgres").__init__(sql_raw)

        normalized_tree = normalize(tree, dnf=True).__init__(sql_raw)

    def optimize_tree(self):
        optimized_tree = optimize(__init__(tree), 
                                  __init__(optimizer_catalog) ,
                                  dialect="postgres",
                                  rules=[rules(qualified), rules(annotated_tree), rules(pushdown_tree), rules(normalized_tree)]
                                  )
    
    #def add_table(self, table_name: exp.Table | str, dialect: DialectType = postgres) -> None:
    #    pass

    #def column_names(self, table: exp.Table | str, dialect: DialectType = postgres, ) -> Sequence[str]:
    #    pass

    #def get_column_type(self, table: exp.Table | str, column: exp.Column | str, dialect: DialectType = postgres,) -> exp.DataType:
    #    pass

def test1():
        optimizer_catalog = {"catalog_test1": {"new_col1": "TEXT"}}
        tree = sqlglot.parse_one("select * from catalog_test1", dialect="postgres")

        print(repr(tree))
        print(tree.sql(pretty=True))

        optimized_tree = optimize(tree, optimizer_catalog ,dialect="postgres")
        print(repr(optimized_tree))
        print(optimized_tree.sql(pretty=True))

if __name__ == "__main__":
        catalog_schema(),  test1()

class operators():

    def __init__(self, catalog_schema):
        self.catalog_schema = op_tree

    def scan(self, op_scan):
        op_scan = __init__(op_tree).find(exp.scan)

    def filter(self, op_filter):
        op_filter = __init__(op_tree).find(exp.filter)

    def project(self, op_select):
        op_select = __init__(op_tree).find(exp.select)

    def join(self, op_join):
        op_join = __init__(op_tree).find(exp.join)

    def aggregate(self, op_aggregate):
        op_aggregate = __init__(op_tree).find(exp.aggregate)

    def sort(self, op_orderby):
        op_orderby = __init__(op_tree).find(exp.orderby)

    def limit(self, op_limit):
        op_limit = __init__(op_tree).find(exp.limit)

    def distinct(self, op_distinct):
        op_distinct = __init__(op_tree).find(exp.distinct)

class planner(operators):
     def __init__(self, value):
        self.value = value
        self.children = []

     def children(self):
         root = planner(operators.join())
        


     