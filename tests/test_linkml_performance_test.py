import unittest
import os
import yaml
import json

from linkml_performance_test.model.benchconfig import BenchmarkConfig
from linkml_performance_test.runner import BenchmarkRunner
from linkml_runtime.dumpers import yaml_dumper, csv_dumper
from linkml_runtime.utils.introspection import package_schemaview

from tests import OUTPUT_DIR

WORKING_DIR = OUTPUT_DIR / 'test_run'
RESULTS = OUTPUT_DIR / 'results.tsv'


class TestPerformance(unittest.TestCase):
    """tests benchmark runner """

    def test_runner(self):
        runner = BenchmarkRunner()
        runner.schemaview = package_schemaview('linkml_performance_test.model.obograph')
        WORKING_DIR.mkdir(exist_ok=True, parents=True)
        config = BenchmarkConfig(entity_counts=[100, 200], working_directory=WORKING_DIR)
        result = runner.multi_run(config)
        print(yaml_dumper.dumps(result))
        sv = package_schemaview('linkml_performance_test.model.benchconfig')
        csv_dumper.dump(result, index_slot='runs', schemaview=sv, to_file=str(RESULTS))