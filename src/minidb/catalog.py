from logging import root

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
        sql_raw = "select * from catalog_test1 where new_col1 is not null and new_col1 != 0 order by new_col1"
        self.tree = sqlglot.parse_one("select * from catalog_test1 where new_col1 is not null and new_col1 != 0 order by new_col1", dialect="postgres")


    def rules(self):
        qualified = qualify(tree, schema=optimizer_catalog, dialect="postgres")

        annotated_tree = annotate_types(tree, schema = optimizer_catalog, dialect="postgres")
        annotated_tree.expressions[0].type.this
        print(annotated_tree.expressions[0].type.this)

        pushdown_tree =pushdown_predicates(tree, dialect="postgres").__init__(sql_raw)

        normalized_tree = normalize(tree, dnf=True).__init__(sql_raw)

    def optimize_tree(self):
        self.optimized_tree = optimize(__init__(tree), 
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
        tree = sqlglot.parse_one("select * from catalog_test1 where new_col1 is not null and new_col1 != 0 order by new_col1", dialect="postgres")

        print(repr(tree))
        print(tree.sql(pretty=True))

        optimized_tree = optimize(tree, optimizer_catalog ,dialect="postgres")
        print(repr(optimized_tree))
        print(optimized_tree.sql(pretty=True))

if __name__ == "__main__":
        catalog_schema(),  test1()

class operators():

    def __init__(self, catalog_schema):
        self.catalog_schema = catalog_schema
        

    def From(self):
        self.op_From = self.catalog_schema.tree.find(exp.From)
        print("self.op_From", self.op_From)
        return self.op_From
    
    def filter(self):
        self.op_filter = self.catalog_schema.tree.find(exp.Where)
        print("self.op_filter", self.op_filter)
        return self.op_filter
    
    def project(self):
        self.op_select = self.catalog_schema.tree.find(exp.Select)
        print("self.op_select", self.op_select)
        return self.op_select

    def join(self):
        self.op_join = self.catalog_schema.tree.find(exp.Join)
        return self.op_join

    def aggregate(self):
        self.op_aggregate = self.catalog_schema.tree.find(exp.And)
        return self.op_aggregate
    
    def sort(self):
        self.op_orderby = self.catalog_schema.tree.find(exp.Order)
        return self.op_orderby
    
    def limit(self):
        self.op_limit = self.catalog_schema.tree.find(exp.Limit)
        return self.op_limit

    def distinct(self):
        self.op_distinct = self.catalog_schema.tree.find(exp.Distinct)
        return self.op_distinct

schema = catalog_schema()
ops = operators(schema)

class planner():
     def __init__(self, data):
        self.data = data
        self.children = []
        print("planner data", self.data)

        node_labels = {
            exp.From: "From",
            exp.Select : "Select",
            exp.Where: "Where",
            exp.Join: "Join",
            exp.And: "And",
            exp.Order: "Order",
            exp.Limit: "Limit",
            exp.Distinct: "Distinct"
        }

        for nodes in ops.catalog_schema.tree.walk():
            label = node_labels.get(type(nodes))
            if label is not None:
                print(label, nodes, "1")


root = planner(ops.From())
node_b = planner(ops.project())
node_c = planner(ops.filter())
node_d = planner(ops.join())
node_e = planner(ops.aggregate())
node_f = planner(ops.sort())

root.children.append(node_b)
root.children.append(node_c)
node_b.children.append(node_d)
node_b.children.append(node_e)
node_e.children.append(node_f)

print("root", root.data)

for child in root.children:
    print("child", child.data)

for child2 in node_b.children:
    print("child2", child2.data)


p = planner(ops)