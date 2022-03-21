import logging
import random
import time
import unittest
import os
from copy import deepcopy
from pathlib import Path

import click
import yaml
import json

import linkml
import linkml_runtime
from linkml_runtime import SchemaView
from linkml_runtime.dumpers import json_dumper, yaml_dumper, rdflib_dumper, csv_dumper
from linkml_runtime.loaders import json_loader, yaml_loader, rdflib_loader
from linkml_performance_test.model.obograph import *
from linkml_performance_test.model.benchconfig import *
from linkml_runtime.utils.introspection import package_schemaview

from linkml_runtime.utils.yamlutils import YAMLRoot, as_json_object


@dataclass
class BenchmarkRunner:
    event: Event = None
    schemaview: SchemaView = None

    def multi_run(self, config: BenchmarkConfig) -> BenchmarkResultSet:
        config.linkml_runtime_version = linkml_runtime.__version__
        #config.linkml_version = linkml.__version__
        runs = []
        for n in config.entity_counts:
            runs.append(self.execute(config, n))
        return BenchmarkResultSet(runs=runs)

    def execute(self, config:  BenchmarkConfig, entity_count: int):
        """Test that perf tests works."""
        node_list = []
        edge_list = []
        run = BenchmarkRun(entity_count=entity_count, config=config)
        run.create_object_event = self.start()
        for ni in range(1, entity_count):
            meta = Meta(definition=DefinitionPropertyValue(val='my def'))
            n = Node(id=f'N:{ni}', label=f'node {ni}', meta=meta)
            node_list.append(n)
        def random_node():
            ni = int(random.random() * entity_count)
            return f'N:{ni}'
        for ei in range(1, entity_count * 4):
            e = Edge(sub=random_node(), obj=random_node(), pred='is_a')
            edge_list.append(e)
        g = Graph(nodes=node_list, edges=edge_list)
        self.end()
        logging.info(f'graph nodes = {len(g.nodes)}')
        tmp_file = str(Path(config.working_directory) / 'tmp')
        # as-json
        #json_obj = json.dumps(g.dict)
        #print(json_obj)
        #json_obj = as_json_object(g, inject_type=False)
        #print(json_obj)
        #assert isinstance(json_obj, JsonObj)
        # JSON
        run.json_dump_event = self.start()
        #json_dumper.dump(g, to_file=tmp_file, inject_type=False)
        json_dumper.dump(g, to_file=tmp_file)
        self.end()
        run.json_load_event = self.start()
        g2 = json_loader.load(target_class=Graph, source=tmp_file)
        self.end()
        # YAML
        run.yaml_dump_event = self.start()
        yaml_dumper.dump(g, to_file=tmp_file)
        self.end()
        run.yaml_load_event = self.start()
        g2 = yaml_loader.load(target_class=Graph, source=tmp_file)
        self.end()
        # RDF
        run.rdf_dump_event = self.start()
        rdflib_dumper.dump(g, schemaview=self.schemaview, to_file=tmp_file)
        self.end()
        run.rdf_load_event = self.start()
        g2 = rdflib_loader.load(schemaview=self.schemaview, target_class=Graph, source=tmp_file)
        self.end()
        # DICT
        run.to_dict_event = self.start()
        as_obj = json_dumper.to_dict(g)
        self.end()
        assert isinstance(as_obj, dict)
        # PLAIN JSON
        run.plain_json_dump_event = self.start()
        with open(tmp_file, 'w', encoding='utf-8') as stream:
            json.dump(as_obj, stream)
        self.end()
        run.plain_json_load_event = self.start()
        with open(tmp_file) as stream:
            as_obj2 = json.load(stream)
        self.end()
        # PLAIN YAML
        run.plain_yaml_dump_event = self.start()
        with open(tmp_file, 'w', encoding='utf-8') as stream:
            yaml.dump(as_obj, stream)
        self.end()
        run.plain_yaml_load_event = self.start()
        with open(tmp_file) as stream:
            as_obj2 = yaml.load(stream)
        self.end()

        return run

    def start(self) -> Event:
        self.event = Event(start=time.time())
        return self.event

    def end(self) -> Event:
        event = self.event
        event.end = time.time()
        event.duration = event.end - event.start
        return event

@click.command()
@click.option('-E', '--entity-counts',
              type=int,
              default=(10, 100),
              show_default=True,
              multiple=True,
              help="list of sizes of each graph to be used in test")
@click.option('-d', '--working-directory',
              required=True)
@click.option('-o', '--output-file',
              required=True,
              help="path to TSV to store results")
def main(entity_counts, working_directory, output_file):
    runner = BenchmarkRunner()
    runner.schemaview = package_schemaview('linkml_performance_test.model.obograph')
    config = BenchmarkConfig(entity_counts=list(entity_counts), working_directory=working_directory)
    print(config)
    result = runner.multi_run(config)
    print(yaml_dumper.dumps(result))
    sv = package_schemaview('linkml_performance_test.model.benchconfig')
    csv_dumper.dump(result, index_slot='runs', schemaview=sv, to_file=str(output_file))

if __name__ == "__main__":
    main()





