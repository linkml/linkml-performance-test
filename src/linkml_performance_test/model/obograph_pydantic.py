# Auto generated from obograph.yaml by pythongen.py version: 0.9.0
# Generation date: 2022-03-20T17:30:27
# Schema: obographs_linkml_model
#
# id: https://github.com/geneontology/obographs
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
from linkml_runtime.linkml_model.types import Boolean, String
from linkml_runtime.utils.metamodelcore import Bool

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
DEFAULT_ = CurieNamespace('', 'https://github.com/geneontology/obographs/')


# Types

# Class references



@dataclass
class Graph(YAMLRoot):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = URIRef("https://github.com/geneontology/obographs/Graph")
    class_class_curie: ClassVar[str] = None
    class_name: ClassVar[str] = "Graph"
    class_model_uri: ClassVar[URIRef] = URIRef("https://github.com/geneontology/obographs/Graph")

    id: Optional[str] = None
    lbl: Optional[str] = None
    meta: Optional[Union[dict, "Meta"]] = None
    nodes: Optional[Union[Union[dict, "Node"], List[Union[dict, "Node"]]]] = empty_list()
    edges: Optional[Union[Union[dict, "Edge"], List[Union[dict, "Edge"]]]] = empty_list()
    equivalentNodesSets: Optional[Union[Union[dict, "EquivalentNodesSet"], List[Union[dict, "EquivalentNodesSet"]]]] = empty_list()
    logicalDefinitionAxioms: Optional[Union[Union[dict, "LogicalDefinitionAxiom"], List[Union[dict, "LogicalDefinitionAxiom"]]]] = empty_list()
    domainRangeAxioms: Optional[Union[Union[dict, "DomainRangeAxiom"], List[Union[dict, "DomainRangeAxiom"]]]] = empty_list()
    propertyChainAxioms: Optional[Union[Union[dict, "PropertyChainAxiom"], List[Union[dict, "PropertyChainAxiom"]]]] = empty_list()

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self.id is not None and not isinstance(self.id, str):
            self.id = str(self.id)

        if self.lbl is not None and not isinstance(self.lbl, str):
            self.lbl = str(self.lbl)

        if self.meta is not None and not isinstance(self.meta, Meta):
            self.meta = Meta(**as_dict(self.meta))

        if not isinstance(self.nodes, list):
            self.nodes = [self.nodes] if self.nodes is not None else []
        self.nodes = [v if isinstance(v, Node) else Node(**as_dict(v)) for v in self.nodes]

        if not isinstance(self.edges, list):
            self.edges = [self.edges] if self.edges is not None else []
        self.edges = [v if isinstance(v, Edge) else Edge(**as_dict(v)) for v in self.edges]

        if not isinstance(self.equivalentNodesSets, list):
            self.equivalentNodesSets = [self.equivalentNodesSets] if self.equivalentNodesSets is not None else []
        self.equivalentNodesSets = [v if isinstance(v, EquivalentNodesSet) else EquivalentNodesSet(**as_dict(v)) for v in self.equivalentNodesSets]

        if not isinstance(self.logicalDefinitionAxioms, list):
            self.logicalDefinitionAxioms = [self.logicalDefinitionAxioms] if self.logicalDefinitionAxioms is not None else []
        self.logicalDefinitionAxioms = [v if isinstance(v, LogicalDefinitionAxiom) else LogicalDefinitionAxiom(**as_dict(v)) for v in self.logicalDefinitionAxioms]

        if not isinstance(self.domainRangeAxioms, list):
            self.domainRangeAxioms = [self.domainRangeAxioms] if self.domainRangeAxioms is not None else []
        self.domainRangeAxioms = [v if isinstance(v, DomainRangeAxiom) else DomainRangeAxiom(**as_dict(v)) for v in self.domainRangeAxioms]

        if not isinstance(self.propertyChainAxioms, list):
            self.propertyChainAxioms = [self.propertyChainAxioms] if self.propertyChainAxioms is not None else []
        self.propertyChainAxioms = [v if isinstance(v, PropertyChainAxiom) else PropertyChainAxiom(**as_dict(v)) for v in self.propertyChainAxioms]

        super().__post_init__(**kwargs)


@dataclass
class Node(YAMLRoot):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = URIRef("https://github.com/geneontology/obographs/Node")
    class_class_curie: ClassVar[str] = None
    class_name: ClassVar[str] = "Node"
    class_model_uri: ClassVar[URIRef] = URIRef("https://github.com/geneontology/obographs/Node")

    id: Optional[str] = None
    label: Optional[str] = None
    type: Optional[str] = None
    meta: Optional[Union[dict, "Meta"]] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self.id is not None and not isinstance(self.id, str):
            self.id = str(self.id)

        if self.label is not None and not isinstance(self.label, str):
            self.label = str(self.label)

        if self.type is not None and not isinstance(self.type, str):
            self.type = str(self.type)

        if self.meta is not None and not isinstance(self.meta, Meta):
            self.meta = Meta(**as_dict(self.meta))

        super().__post_init__(**kwargs)


@dataclass
class Edge(YAMLRoot):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = URIRef("https://github.com/geneontology/obographs/Edge")
    class_class_curie: ClassVar[str] = None
    class_name: ClassVar[str] = "Edge"
    class_model_uri: ClassVar[URIRef] = URIRef("https://github.com/geneontology/obographs/Edge")

    sub: Optional[str] = None
    pred: Optional[str] = None
    obj: Optional[str] = None
    meta: Optional[Union[dict, "Meta"]] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self.sub is not None and not isinstance(self.sub, str):
            self.sub = str(self.sub)

        if self.pred is not None and not isinstance(self.pred, str):
            self.pred = str(self.pred)

        if self.obj is not None and not isinstance(self.obj, str):
            self.obj = str(self.obj)

        if self.meta is not None and not isinstance(self.meta, Meta):
            self.meta = Meta(**as_dict(self.meta))

        super().__post_init__(**kwargs)


@dataclass
class Meta(YAMLRoot):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = URIRef("https://github.com/geneontology/obographs/Meta")
    class_class_curie: ClassVar[str] = None
    class_name: ClassVar[str] = "Meta"
    class_model_uri: ClassVar[URIRef] = URIRef("https://github.com/geneontology/obographs/Meta")

    subsets: Optional[Union[str, List[str]]] = empty_list()
    version: Optional[str] = None
    comments: Optional[Union[str, List[str]]] = empty_list()
    definition: Optional[Union[dict, "DefinitionPropertyValue"]] = None
    xrefs: Optional[Union[str, List[str]]] = empty_list()
    synonyms: Optional[Union[Union[dict, "SynonymPropertyValue"], List[Union[dict, "SynonymPropertyValue"]]]] = empty_list()
    basicPropertyValues: Optional[Union[dict, "BasicPropertyValue"]] = None
    deprecated: Optional[Union[bool, Bool]] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if not isinstance(self.subsets, list):
            self.subsets = [self.subsets] if self.subsets is not None else []
        self.subsets = [v if isinstance(v, str) else str(v) for v in self.subsets]

        if self.version is not None and not isinstance(self.version, str):
            self.version = str(self.version)

        if not isinstance(self.comments, list):
            self.comments = [self.comments] if self.comments is not None else []
        self.comments = [v if isinstance(v, str) else str(v) for v in self.comments]

        if self.definition is not None and not isinstance(self.definition, DefinitionPropertyValue):
            self.definition = DefinitionPropertyValue(**as_dict(self.definition))

        if not isinstance(self.xrefs, list):
            self.xrefs = [self.xrefs] if self.xrefs is not None else []
        self.xrefs = [v if isinstance(v, str) else str(v) for v in self.xrefs]

        if not isinstance(self.synonyms, list):
            self.synonyms = [self.synonyms] if self.synonyms is not None else []
        self.synonyms = [v if isinstance(v, SynonymPropertyValue) else SynonymPropertyValue(**as_dict(v)) for v in self.synonyms]

        if self.basicPropertyValues is not None and not isinstance(self.basicPropertyValues, BasicPropertyValue):
            self.basicPropertyValues = BasicPropertyValue(**as_dict(self.basicPropertyValues))

        if self.deprecated is not None and not isinstance(self.deprecated, Bool):
            self.deprecated = Bool(self.deprecated)

        super().__post_init__(**kwargs)


@dataclass
class PropertyValue(YAMLRoot):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = URIRef("https://github.com/geneontology/obographs/PropertyValue")
    class_class_curie: ClassVar[str] = None
    class_name: ClassVar[str] = "PropertyValue"
    class_model_uri: ClassVar[URIRef] = URIRef("https://github.com/geneontology/obographs/PropertyValue")

    pred: Optional[str] = None
    val: Optional[str] = None
    xrefs: Optional[Union[str, List[str]]] = empty_list()
    meta: Optional[Union[dict, Meta]] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self.pred is not None and not isinstance(self.pred, str):
            self.pred = str(self.pred)

        if self.val is not None and not isinstance(self.val, str):
            self.val = str(self.val)

        if not isinstance(self.xrefs, list):
            self.xrefs = [self.xrefs] if self.xrefs is not None else []
        self.xrefs = [v if isinstance(v, str) else str(v) for v in self.xrefs]

        if self.meta is not None and not isinstance(self.meta, Meta):
            self.meta = Meta(**as_dict(self.meta))

        super().__post_init__(**kwargs)


class DefinitionPropertyValue(PropertyValue):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = URIRef("https://github.com/geneontology/obographs/DefinitionPropertyValue")
    class_class_curie: ClassVar[str] = None
    class_name: ClassVar[str] = "DefinitionPropertyValue"
    class_model_uri: ClassVar[URIRef] = URIRef("https://github.com/geneontology/obographs/DefinitionPropertyValue")


class BasicPropertyValue(PropertyValue):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = URIRef("https://github.com/geneontology/obographs/BasicPropertyValue")
    class_class_curie: ClassVar[str] = None
    class_name: ClassVar[str] = "BasicPropertyValue"
    class_model_uri: ClassVar[URIRef] = URIRef("https://github.com/geneontology/obographs/BasicPropertyValue")


class XrefPropertyValue(PropertyValue):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = URIRef("https://github.com/geneontology/obographs/XrefPropertyValue")
    class_class_curie: ClassVar[str] = None
    class_name: ClassVar[str] = "XrefPropertyValue"
    class_model_uri: ClassVar[URIRef] = URIRef("https://github.com/geneontology/obographs/XrefPropertyValue")


@dataclass
class SynonymPropertyValue(PropertyValue):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = URIRef("https://github.com/geneontology/obographs/SynonymPropertyValue")
    class_class_curie: ClassVar[str] = None
    class_name: ClassVar[str] = "SynonymPropertyValue"
    class_model_uri: ClassVar[URIRef] = URIRef("https://github.com/geneontology/obographs/SynonymPropertyValue")

    synonymType: Optional[str] = None
    isExact: Optional[Union[bool, Bool]] = None
    scope: Optional[Union[str, "ScopesEnum"]] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self.synonymType is not None and not isinstance(self.synonymType, str):
            self.synonymType = str(self.synonymType)

        if self.isExact is not None and not isinstance(self.isExact, Bool):
            self.isExact = Bool(self.isExact)

        if self.scope is not None and not isinstance(self.scope, ScopesEnum):
            self.scope = ScopesEnum(self.scope)

        super().__post_init__(**kwargs)


@dataclass
class Axiom(YAMLRoot):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = URIRef("https://github.com/geneontology/obographs/Axiom")
    class_class_curie: ClassVar[str] = None
    class_name: ClassVar[str] = "Axiom"
    class_model_uri: ClassVar[URIRef] = URIRef("https://github.com/geneontology/obographs/Axiom")

    meta: Optional[Union[dict, Meta]] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self.meta is not None and not isinstance(self.meta, Meta):
            self.meta = Meta(**as_dict(self.meta))

        super().__post_init__(**kwargs)


class DomainRangeAxiom(Axiom):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = URIRef("https://github.com/geneontology/obographs/DomainRangeAxiom")
    class_class_curie: ClassVar[str] = None
    class_name: ClassVar[str] = "DomainRangeAxiom"
    class_model_uri: ClassVar[URIRef] = URIRef("https://github.com/geneontology/obographs/DomainRangeAxiom")


@dataclass
class EquivalentNodesSet(Axiom):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = URIRef("https://github.com/geneontology/obographs/EquivalentNodesSet")
    class_class_curie: ClassVar[str] = None
    class_name: ClassVar[str] = "EquivalentNodesSet"
    class_model_uri: ClassVar[URIRef] = URIRef("https://github.com/geneontology/obographs/EquivalentNodesSet")

    representitiveNodeId: Optional[str] = None
    nodeIds: Optional[Union[str, List[str]]] = empty_list()

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self.representitiveNodeId is not None and not isinstance(self.representitiveNodeId, str):
            self.representitiveNodeId = str(self.representitiveNodeId)

        if not isinstance(self.nodeIds, list):
            self.nodeIds = [self.nodeIds] if self.nodeIds is not None else []
        self.nodeIds = [v if isinstance(v, str) else str(v) for v in self.nodeIds]

        super().__post_init__(**kwargs)


@dataclass
class ExistentialRestrictionExpression(YAMLRoot):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = URIRef("https://github.com/geneontology/obographs/ExistentialRestrictionExpression")
    class_class_curie: ClassVar[str] = None
    class_name: ClassVar[str] = "ExistentialRestrictionExpression"
    class_model_uri: ClassVar[URIRef] = URIRef("https://github.com/geneontology/obographs/ExistentialRestrictionExpression")

    fillerId: Optional[str] = None
    propertyId: Optional[str] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self.fillerId is not None and not isinstance(self.fillerId, str):
            self.fillerId = str(self.fillerId)

        if self.propertyId is not None and not isinstance(self.propertyId, str):
            self.propertyId = str(self.propertyId)

        super().__post_init__(**kwargs)


class LogicalDefinitionAxiom(Axiom):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = URIRef("https://github.com/geneontology/obographs/LogicalDefinitionAxiom")
    class_class_curie: ClassVar[str] = None
    class_name: ClassVar[str] = "LogicalDefinitionAxiom"
    class_model_uri: ClassVar[URIRef] = URIRef("https://github.com/geneontology/obographs/LogicalDefinitionAxiom")


class PropertyChainAxiom(Axiom):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = URIRef("https://github.com/geneontology/obographs/PropertyChainAxiom")
    class_class_curie: ClassVar[str] = None
    class_name: ClassVar[str] = "PropertyChainAxiom"
    class_model_uri: ClassVar[URIRef] = URIRef("https://github.com/geneontology/obographs/PropertyChainAxiom")


# Enumerations
class ScopesEnum(EnumDefinitionImpl):

    exact = PermissibleValue(text="exact")
    narrow = PermissibleValue(text="narrow")
    broad = PermissibleValue(text="broad")
    related = PermissibleValue(text="related")

    _defn = EnumDefinition(
        name="ScopesEnum",
    )

class PredsEnum(EnumDefinitionImpl):

    hasExactSynonym = PermissibleValue(text="hasExactSynonym")
    hasNarrowSynonym = PermissibleValue(text="hasNarrowSynonym")
    hasBroadSynonym = PermissibleValue(text="hasBroadSynonym")
    hasRelatedSynonym = PermissibleValue(text="hasRelatedSynonym")

    _defn = EnumDefinition(
        name="PredsEnum",
    )

# Slots
class slots:
    pass

slots.sub = Slot(uri=DEFAULT_.sub, name="sub", curie=DEFAULT_.curie('sub'),
                   model_uri=DEFAULT_.sub, domain=None, range=Optional[str])

slots.pred = Slot(uri=DEFAULT_.pred, name="pred", curie=DEFAULT_.curie('pred'),
                   model_uri=DEFAULT_.pred, domain=None, range=Optional[str])

slots.obj = Slot(uri=DEFAULT_.obj, name="obj", curie=DEFAULT_.curie('obj'),
                   model_uri=DEFAULT_.obj, domain=None, range=Optional[str])

slots.id = Slot(uri=DEFAULT_.id, name="id", curie=DEFAULT_.curie('id'),
                   model_uri=DEFAULT_.id, domain=None, range=Optional[str])

slots.val = Slot(uri=DEFAULT_.val, name="val", curie=DEFAULT_.curie('val'),
                   model_uri=DEFAULT_.val, domain=None, range=Optional[str])

slots.label = Slot(uri=DEFAULT_.label, name="label", curie=DEFAULT_.curie('label'),
                   model_uri=DEFAULT_.label, domain=None, range=Optional[str])

slots.type = Slot(uri=DEFAULT_.type, name="type", curie=DEFAULT_.curie('type'),
                   model_uri=DEFAULT_.type, domain=None, range=Optional[str])

slots.meta = Slot(uri=DEFAULT_.meta, name="meta", curie=DEFAULT_.curie('meta'),
                   model_uri=DEFAULT_.meta, domain=None, range=Optional[Union[dict, Meta]])

slots.definition = Slot(uri=DEFAULT_.definition, name="definition", curie=DEFAULT_.curie('definition'),
                   model_uri=DEFAULT_.definition, domain=None, range=Optional[Union[dict, DefinitionPropertyValue]])

slots.basicPropertyValues = Slot(uri=DEFAULT_.basicPropertyValues, name="basicPropertyValues", curie=DEFAULT_.curie('basicPropertyValues'),
                   model_uri=DEFAULT_.basicPropertyValues, domain=None, range=Optional[Union[dict, BasicPropertyValue]])

slots.comments = Slot(uri=DEFAULT_.comments, name="comments", curie=DEFAULT_.curie('comments'),
                   model_uri=DEFAULT_.comments, domain=None, range=Optional[Union[str, List[str]]])

slots.version = Slot(uri=DEFAULT_.version, name="version", curie=DEFAULT_.curie('version'),
                   model_uri=DEFAULT_.version, domain=None, range=Optional[str])

slots.deprecated = Slot(uri=DEFAULT_.deprecated, name="deprecated", curie=DEFAULT_.curie('deprecated'),
                   model_uri=DEFAULT_.deprecated, domain=None, range=Optional[Union[bool, Bool]])

slots.subsets = Slot(uri=DEFAULT_.subsets, name="subsets", curie=DEFAULT_.curie('subsets'),
                   model_uri=DEFAULT_.subsets, domain=None, range=Optional[Union[str, List[str]]])

slots.xrefs = Slot(uri=DEFAULT_.xrefs, name="xrefs", curie=DEFAULT_.curie('xrefs'),
                   model_uri=DEFAULT_.xrefs, domain=None, range=Optional[Union[str, List[str]]])

slots.lbl = Slot(uri=DEFAULT_.lbl, name="lbl", curie=DEFAULT_.curie('lbl'),
                   model_uri=DEFAULT_.lbl, domain=None, range=Optional[str])

slots.nodes = Slot(uri=DEFAULT_.nodes, name="nodes", curie=DEFAULT_.curie('nodes'),
                   model_uri=DEFAULT_.nodes, domain=None, range=Optional[Union[Union[dict, Node], List[Union[dict, Node]]]])

slots.edges = Slot(uri=DEFAULT_.edges, name="edges", curie=DEFAULT_.curie('edges'),
                   model_uri=DEFAULT_.edges, domain=None, range=Optional[Union[Union[dict, Edge], List[Union[dict, Edge]]]])

slots.equivalentNodesSets = Slot(uri=DEFAULT_.equivalentNodesSets, name="equivalentNodesSets", curie=DEFAULT_.curie('equivalentNodesSets'),
                   model_uri=DEFAULT_.equivalentNodesSets, domain=None, range=Optional[Union[Union[dict, EquivalentNodesSet], List[Union[dict, EquivalentNodesSet]]]])

slots.logicalDefinitionAxioms = Slot(uri=DEFAULT_.logicalDefinitionAxioms, name="logicalDefinitionAxioms", curie=DEFAULT_.curie('logicalDefinitionAxioms'),
                   model_uri=DEFAULT_.logicalDefinitionAxioms, domain=None, range=Optional[Union[Union[dict, LogicalDefinitionAxiom], List[Union[dict, LogicalDefinitionAxiom]]]])

slots.domainRangeAxioms = Slot(uri=DEFAULT_.domainRangeAxioms, name="domainRangeAxioms", curie=DEFAULT_.curie('domainRangeAxioms'),
                   model_uri=DEFAULT_.domainRangeAxioms, domain=None, range=Optional[Union[Union[dict, DomainRangeAxiom], List[Union[dict, DomainRangeAxiom]]]])

slots.propertyChainAxioms = Slot(uri=DEFAULT_.propertyChainAxioms, name="propertyChainAxioms", curie=DEFAULT_.curie('propertyChainAxioms'),
                   model_uri=DEFAULT_.propertyChainAxioms, domain=None, range=Optional[Union[Union[dict, PropertyChainAxiom], List[Union[dict, PropertyChainAxiom]]]])

slots.representitiveNodeId = Slot(uri=DEFAULT_.representitiveNodeId, name="representitiveNodeId", curie=DEFAULT_.curie('representitiveNodeId'),
                   model_uri=DEFAULT_.representitiveNodeId, domain=None, range=Optional[str])

slots.nodeIds = Slot(uri=DEFAULT_.nodeIds, name="nodeIds", curie=DEFAULT_.curie('nodeIds'),
                   model_uri=DEFAULT_.nodeIds, domain=None, range=Optional[Union[str, List[str]]])

slots.fillerId = Slot(uri=DEFAULT_.fillerId, name="fillerId", curie=DEFAULT_.curie('fillerId'),
                   model_uri=DEFAULT_.fillerId, domain=None, range=Optional[str])

slots.propertyId = Slot(uri=DEFAULT_.propertyId, name="propertyId", curie=DEFAULT_.curie('propertyId'),
                   model_uri=DEFAULT_.propertyId, domain=None, range=Optional[str])

slots.synonyms = Slot(uri=DEFAULT_.synonyms, name="synonyms", curie=DEFAULT_.curie('synonyms'),
                   model_uri=DEFAULT_.synonyms, domain=None, range=Optional[Union[Union[dict, SynonymPropertyValue], List[Union[dict, SynonymPropertyValue]]]])

slots.synonymType = Slot(uri=DEFAULT_.synonymType, name="synonymType", curie=DEFAULT_.curie('synonymType'),
                   model_uri=DEFAULT_.synonymType, domain=None, range=Optional[str])

slots.scope = Slot(uri=DEFAULT_.scope, name="scope", curie=DEFAULT_.curie('scope'),
                   model_uri=DEFAULT_.scope, domain=None, range=Optional[Union[str, "ScopesEnum"]])

slots.isExact = Slot(uri=DEFAULT_.isExact, name="isExact", curie=DEFAULT_.curie('isExact'),
                   model_uri=DEFAULT_.isExact, domain=None, range=Optional[Union[bool, Bool]])
