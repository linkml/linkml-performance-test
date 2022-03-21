# Auto generated from benchconfig.yaml by pythongen.py version: 0.9.0
# Generation date: 2022-03-20T18:15:47
# Schema: benchconfig
#
# id: https://github.com/geneontology/benchconfig
# description:
# license: https://creativecommons.org/publicdomain/zero/1.0/

import dataclasses
import sys
import re
from jsonasobj2 import JsonObj, as_dict
from typing import Optional, List, Union, Dict, ClassVar, Any
from dataclasses import dataclass
from linkml_runtime.linkml_model.meta import EnumDefinition, PermissibleValue, PvFormulaOptions

from linkml_runtime.utils.slot import Slot
from linkml_runtime.utils.metamodelcore import empty_list, empty_dict, bnode
from linkml_runtime.utils.yamlutils import YAMLRoot, extended_str, extended_float, extended_int
from linkml_runtime.utils.dataclass_extensions_376 import dataclasses_init_fn_with_kwargs
from linkml_runtime.utils.formatutils import camelcase, underscore, sfx
from linkml_runtime.utils.enumerations import EnumDefinitionImpl
from rdflib import Namespace, URIRef
from linkml_runtime.utils.curienamespace import CurieNamespace
from linkml_runtime.linkml_model.types import Float, Integer, String

metamodel_version = "1.7.0"
version = "0.0.1"

# Overwrite dataclasses _init_fn to add **kwargs in __init__
dataclasses._init_fn = dataclasses_init_fn_with_kwargs

# Namespaces
LINKML = CurieNamespace('linkml', 'https://w3id.org/linkml/')
RDF = CurieNamespace('rdf', 'http://www.w3.org/1999/02/22-rdf-syntax-ns#')
RDFS = CurieNamespace('rdfs', 'http://www.w3.org/2000/01/rdf-schema#')
SDO = CurieNamespace('sdo', 'https://schema.org/')
SKOS = CurieNamespace('skos', 'http://www.w3.org/2004/02/skos/core#')
XSD = CurieNamespace('xsd', 'http://www.w3.org/2001/XMLSchema#')
DEFAULT_ = CurieNamespace('', 'https://github.com/geneontology/benchconfig/')


# Types

# Class references



@dataclass
class Event(YAMLRoot):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = URIRef("https://github.com/geneontology/benchconfig/Event")
    class_class_curie: ClassVar[str] = None
    class_name: ClassVar[str] = "Event"
    class_model_uri: ClassVar[URIRef] = URIRef("https://github.com/geneontology/benchconfig/Event")

    duration: Optional[float] = None
    start: Optional[float] = None
    end: Optional[float] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self.duration is not None and not isinstance(self.duration, float):
            self.duration = float(self.duration)

        if self.start is not None and not isinstance(self.start, float):
            self.start = float(self.start)

        if self.end is not None and not isinstance(self.end, float):
            self.end = float(self.end)

        super().__post_init__(**kwargs)


@dataclass
class BenchmarkResultSet(YAMLRoot):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = URIRef("https://github.com/geneontology/benchconfig/BenchmarkResultSet")
    class_class_curie: ClassVar[str] = None
    class_name: ClassVar[str] = "BenchmarkResultSet"
    class_model_uri: ClassVar[URIRef] = URIRef("https://github.com/geneontology/benchconfig/BenchmarkResultSet")

    runs: Optional[Union[Union[dict, "BenchmarkRun"], List[Union[dict, "BenchmarkRun"]]]] = empty_list()
    config: Optional[Union[dict, "BenchmarkConfig"]] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if not isinstance(self.runs, list):
            self.runs = [self.runs] if self.runs is not None else []
        self.runs = [v if isinstance(v, BenchmarkRun) else BenchmarkRun(**as_dict(v)) for v in self.runs]

        if self.config is not None and not isinstance(self.config, BenchmarkConfig):
            self.config = BenchmarkConfig(**as_dict(self.config))

        super().__post_init__(**kwargs)


@dataclass
class BenchmarkConfig(YAMLRoot):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = URIRef("https://github.com/geneontology/benchconfig/BenchmarkConfig")
    class_class_curie: ClassVar[str] = None
    class_name: ClassVar[str] = "BenchmarkConfig"
    class_model_uri: ClassVar[URIRef] = URIRef("https://github.com/geneontology/benchconfig/BenchmarkConfig")

    linkml_version: Optional[str] = None
    linkml_runtime_version: Optional[str] = None
    python_version: Optional[str] = None
    datamodel_generator: Optional[str] = None
    entity_counts: Optional[Union[int, List[int]]] = empty_list()
    working_directory: Optional[str] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self.linkml_version is not None and not isinstance(self.linkml_version, str):
            self.linkml_version = str(self.linkml_version)

        if self.linkml_runtime_version is not None and not isinstance(self.linkml_runtime_version, str):
            self.linkml_runtime_version = str(self.linkml_runtime_version)

        if self.python_version is not None and not isinstance(self.python_version, str):
            self.python_version = str(self.python_version)

        if self.datamodel_generator is not None and not isinstance(self.datamodel_generator, str):
            self.datamodel_generator = str(self.datamodel_generator)

        if not isinstance(self.entity_counts, list):
            self.entity_counts = [self.entity_counts] if self.entity_counts is not None else []
        self.entity_counts = [v if isinstance(v, int) else int(v) for v in self.entity_counts]

        if self.working_directory is not None and not isinstance(self.working_directory, str):
            self.working_directory = str(self.working_directory)

        super().__post_init__(**kwargs)


@dataclass
class BenchmarkRun(YAMLRoot):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = URIRef("https://github.com/geneontology/benchconfig/BenchmarkRun")
    class_class_curie: ClassVar[str] = None
    class_name: ClassVar[str] = "BenchmarkRun"
    class_model_uri: ClassVar[URIRef] = URIRef("https://github.com/geneontology/benchconfig/BenchmarkRun")

    config: Optional[Union[dict, BenchmarkConfig]] = None
    entity_count: Optional[int] = None
    create_object_event: Optional[Union[dict, Event]] = None
    json_dump_event: Optional[Union[dict, Event]] = None
    json_load_event: Optional[Union[dict, Event]] = None
    yaml_dump_event: Optional[Union[dict, Event]] = None
    yaml_load_event: Optional[Union[dict, Event]] = None
    rdf_dump_event: Optional[Union[dict, Event]] = None
    rdf_load_event: Optional[Union[dict, Event]] = None
    to_dict_event: Optional[Union[dict, Event]] = None
    plain_yaml_dump_event: Optional[Union[dict, Event]] = None
    plain_yaml_load_event: Optional[Union[dict, Event]] = None
    plain_json_dump_event: Optional[Union[dict, Event]] = None
    plain_json_load_event: Optional[Union[dict, Event]] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self.config is not None and not isinstance(self.config, BenchmarkConfig):
            self.config = BenchmarkConfig(**as_dict(self.config))

        if self.entity_count is not None and not isinstance(self.entity_count, int):
            self.entity_count = int(self.entity_count)

        if self.create_object_event is not None and not isinstance(self.create_object_event, Event):
            self.create_object_event = Event(**as_dict(self.create_object_event))

        if self.json_dump_event is not None and not isinstance(self.json_dump_event, Event):
            self.json_dump_event = Event(**as_dict(self.json_dump_event))

        if self.json_load_event is not None and not isinstance(self.json_load_event, Event):
            self.json_load_event = Event(**as_dict(self.json_load_event))

        if self.yaml_dump_event is not None and not isinstance(self.yaml_dump_event, Event):
            self.yaml_dump_event = Event(**as_dict(self.yaml_dump_event))

        if self.yaml_load_event is not None and not isinstance(self.yaml_load_event, Event):
            self.yaml_load_event = Event(**as_dict(self.yaml_load_event))

        if self.rdf_dump_event is not None and not isinstance(self.rdf_dump_event, Event):
            self.rdf_dump_event = Event(**as_dict(self.rdf_dump_event))

        if self.rdf_load_event is not None and not isinstance(self.rdf_load_event, Event):
            self.rdf_load_event = Event(**as_dict(self.rdf_load_event))

        if self.to_dict_event is not None and not isinstance(self.to_dict_event, Event):
            self.to_dict_event = Event(**as_dict(self.to_dict_event))

        if self.plain_yaml_dump_event is not None and not isinstance(self.plain_yaml_dump_event, Event):
            self.plain_yaml_dump_event = Event(**as_dict(self.plain_yaml_dump_event))

        if self.plain_yaml_load_event is not None and not isinstance(self.plain_yaml_load_event, Event):
            self.plain_yaml_load_event = Event(**as_dict(self.plain_yaml_load_event))

        if self.plain_json_dump_event is not None and not isinstance(self.plain_json_dump_event, Event):
            self.plain_json_dump_event = Event(**as_dict(self.plain_json_dump_event))

        if self.plain_json_load_event is not None and not isinstance(self.plain_json_load_event, Event):
            self.plain_json_load_event = Event(**as_dict(self.plain_json_load_event))

        super().__post_init__(**kwargs)


# Enumerations


# Slots
class slots:
    pass

slots.event__duration = Slot(uri=DEFAULT_.duration, name="event__duration", curie=DEFAULT_.curie('duration'),
                   model_uri=DEFAULT_.event__duration, domain=None, range=Optional[float])

slots.event__start = Slot(uri=DEFAULT_.start, name="event__start", curie=DEFAULT_.curie('start'),
                   model_uri=DEFAULT_.event__start, domain=None, range=Optional[float])

slots.event__end = Slot(uri=DEFAULT_.end, name="event__end", curie=DEFAULT_.curie('end'),
                   model_uri=DEFAULT_.event__end, domain=None, range=Optional[float])

slots.benchmarkResultSet__runs = Slot(uri=DEFAULT_.runs, name="benchmarkResultSet__runs", curie=DEFAULT_.curie('runs'),
                   model_uri=DEFAULT_.benchmarkResultSet__runs, domain=None, range=Optional[Union[Union[dict, BenchmarkRun], List[Union[dict, BenchmarkRun]]]])

slots.benchmarkResultSet__config = Slot(uri=DEFAULT_.config, name="benchmarkResultSet__config", curie=DEFAULT_.curie('config'),
                   model_uri=DEFAULT_.benchmarkResultSet__config, domain=None, range=Optional[Union[dict, BenchmarkConfig]])

slots.benchmarkConfig__linkml_version = Slot(uri=DEFAULT_.linkml_version, name="benchmarkConfig__linkml_version", curie=DEFAULT_.curie('linkml_version'),
                   model_uri=DEFAULT_.benchmarkConfig__linkml_version, domain=None, range=Optional[str])

slots.benchmarkConfig__linkml_runtime_version = Slot(uri=DEFAULT_.linkml_runtime_version, name="benchmarkConfig__linkml_runtime_version", curie=DEFAULT_.curie('linkml_runtime_version'),
                   model_uri=DEFAULT_.benchmarkConfig__linkml_runtime_version, domain=None, range=Optional[str])

slots.benchmarkConfig__python_version = Slot(uri=DEFAULT_.python_version, name="benchmarkConfig__python_version", curie=DEFAULT_.curie('python_version'),
                   model_uri=DEFAULT_.benchmarkConfig__python_version, domain=None, range=Optional[str])

slots.benchmarkConfig__datamodel_generator = Slot(uri=DEFAULT_.datamodel_generator, name="benchmarkConfig__datamodel_generator", curie=DEFAULT_.curie('datamodel_generator'),
                   model_uri=DEFAULT_.benchmarkConfig__datamodel_generator, domain=None, range=Optional[str])

slots.benchmarkConfig__entity_counts = Slot(uri=DEFAULT_.entity_counts, name="benchmarkConfig__entity_counts", curie=DEFAULT_.curie('entity_counts'),
                   model_uri=DEFAULT_.benchmarkConfig__entity_counts, domain=None, range=Optional[Union[int, List[int]]])

slots.benchmarkConfig__working_directory = Slot(uri=DEFAULT_.working_directory, name="benchmarkConfig__working_directory", curie=DEFAULT_.curie('working_directory'),
                   model_uri=DEFAULT_.benchmarkConfig__working_directory, domain=None, range=Optional[str])

slots.benchmarkRun__config = Slot(uri=DEFAULT_.config, name="benchmarkRun__config", curie=DEFAULT_.curie('config'),
                   model_uri=DEFAULT_.benchmarkRun__config, domain=None, range=Optional[Union[dict, BenchmarkConfig]])

slots.benchmarkRun__entity_count = Slot(uri=DEFAULT_.entity_count, name="benchmarkRun__entity_count", curie=DEFAULT_.curie('entity_count'),
                   model_uri=DEFAULT_.benchmarkRun__entity_count, domain=None, range=Optional[int])

slots.benchmarkRun__create_object_event = Slot(uri=DEFAULT_.create_object_event, name="benchmarkRun__create_object_event", curie=DEFAULT_.curie('create_object_event'),
                   model_uri=DEFAULT_.benchmarkRun__create_object_event, domain=None, range=Optional[Union[dict, Event]])

slots.benchmarkRun__json_dump_event = Slot(uri=DEFAULT_.json_dump_event, name="benchmarkRun__json_dump_event", curie=DEFAULT_.curie('json_dump_event'),
                   model_uri=DEFAULT_.benchmarkRun__json_dump_event, domain=None, range=Optional[Union[dict, Event]])

slots.benchmarkRun__json_load_event = Slot(uri=DEFAULT_.json_load_event, name="benchmarkRun__json_load_event", curie=DEFAULT_.curie('json_load_event'),
                   model_uri=DEFAULT_.benchmarkRun__json_load_event, domain=None, range=Optional[Union[dict, Event]])

slots.benchmarkRun__yaml_dump_event = Slot(uri=DEFAULT_.yaml_dump_event, name="benchmarkRun__yaml_dump_event", curie=DEFAULT_.curie('yaml_dump_event'),
                   model_uri=DEFAULT_.benchmarkRun__yaml_dump_event, domain=None, range=Optional[Union[dict, Event]])

slots.benchmarkRun__yaml_load_event = Slot(uri=DEFAULT_.yaml_load_event, name="benchmarkRun__yaml_load_event", curie=DEFAULT_.curie('yaml_load_event'),
                   model_uri=DEFAULT_.benchmarkRun__yaml_load_event, domain=None, range=Optional[Union[dict, Event]])

slots.benchmarkRun__rdf_dump_event = Slot(uri=DEFAULT_.rdf_dump_event, name="benchmarkRun__rdf_dump_event", curie=DEFAULT_.curie('rdf_dump_event'),
                   model_uri=DEFAULT_.benchmarkRun__rdf_dump_event, domain=None, range=Optional[Union[dict, Event]])

slots.benchmarkRun__rdf_load_event = Slot(uri=DEFAULT_.rdf_load_event, name="benchmarkRun__rdf_load_event", curie=DEFAULT_.curie('rdf_load_event'),
                   model_uri=DEFAULT_.benchmarkRun__rdf_load_event, domain=None, range=Optional[Union[dict, Event]])

slots.benchmarkRun__to_dict_event = Slot(uri=DEFAULT_.to_dict_event, name="benchmarkRun__to_dict_event", curie=DEFAULT_.curie('to_dict_event'),
                   model_uri=DEFAULT_.benchmarkRun__to_dict_event, domain=None, range=Optional[Union[dict, Event]])

slots.benchmarkRun__plain_yaml_dump_event = Slot(uri=DEFAULT_.plain_yaml_dump_event, name="benchmarkRun__plain_yaml_dump_event", curie=DEFAULT_.curie('plain_yaml_dump_event'),
                   model_uri=DEFAULT_.benchmarkRun__plain_yaml_dump_event, domain=None, range=Optional[Union[dict, Event]])

slots.benchmarkRun__plain_yaml_load_event = Slot(uri=DEFAULT_.plain_yaml_load_event, name="benchmarkRun__plain_yaml_load_event", curie=DEFAULT_.curie('plain_yaml_load_event'),
                   model_uri=DEFAULT_.benchmarkRun__plain_yaml_load_event, domain=None, range=Optional[Union[dict, Event]])

slots.benchmarkRun__plain_json_dump_event = Slot(uri=DEFAULT_.plain_json_dump_event, name="benchmarkRun__plain_json_dump_event", curie=DEFAULT_.curie('plain_json_dump_event'),
                   model_uri=DEFAULT_.benchmarkRun__plain_json_dump_event, domain=None, range=Optional[Union[dict, Event]])

slots.benchmarkRun__plain_json_load_event = Slot(uri=DEFAULT_.plain_json_load_event, name="benchmarkRun__plain_json_load_event", curie=DEFAULT_.curie('plain_json_load_event'),
                   model_uri=DEFAULT_.benchmarkRun__plain_json_load_event, domain=None, range=Optional[Union[dict, Event]])
