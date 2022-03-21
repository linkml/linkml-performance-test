from __future__ import annotations
from datetime import datetime, date
from enum import Enum
from typing import List, Dict, Optional, Any
from pydantic import BaseModel, Field
from pydantic.dataclasses import dataclass

metamodel_version = "None"
version = "0.0.1"

# Pydantic config and validators
class PydanticConfig:
    """ Pydantic config https://pydantic-docs.helpmanual.io/usage/model_config/ """

    validate_assignment = True
    validate_all = True
    underscore_attrs_are_private = True
    extra = 'forbid'
    arbitrary_types_allowed = True  # TODO re-evaluate this


class ScopesEnum(str, Enum):
    
    exact = "exact"
    narrow = "narrow"
    broad = "broad"
    related = "related"
    
    

class PredsEnum(str, Enum):
    
    hasExactSynonym = "hasExactSynonym"
    hasNarrowSynonym = "hasNarrowSynonym"
    hasBroadSynonym = "hasBroadSynonym"
    hasRelatedSynonym = "hasRelatedSynonym"
    
    

@dataclass(config=PydanticConfig)
class Graph:
    
    id: Optional[str] = Field(None)
    lbl: Optional[str] = Field(None)
    meta: Optional[Meta] = Field(None)
    nodes: Optional[List[Node]] = Field(None)
    edges: Optional[List[Edge]] = Field(None)
    equivalentNodesSets: Optional[List[EquivalentNodesSet]] = Field(None)
    logicalDefinitionAxioms: Optional[List[LogicalDefinitionAxiom]] = Field(None)
    domainRangeAxioms: Optional[List[DomainRangeAxiom]] = Field(None)
    propertyChainAxioms: Optional[List[PropertyChainAxiom]] = Field(None)
    


@dataclass(config=PydanticConfig)
class Node:
    
    id: Optional[str] = Field(None)
    label: Optional[str] = Field(None)
    type: Optional[str] = Field(None)
    meta: Optional[Meta] = Field(None)
    


@dataclass(config=PydanticConfig)
class Edge:
    
    sub: Optional[str] = Field(None)
    pred: Optional[str] = Field(None)
    obj: Optional[str] = Field(None)
    meta: Optional[Meta] = Field(None)
    


@dataclass(config=PydanticConfig)
class Meta:
    
    subsets: Optional[List[str]] = Field(None)
    version: Optional[str] = Field(None)
    comments: Optional[List[str]] = Field(None)
    definition: Optional[DefinitionPropertyValue] = Field(None)
    xrefs: Optional[List[str]] = Field(None)
    synonyms: Optional[List[SynonymPropertyValue]] = Field(None)
    basicPropertyValues: Optional[BasicPropertyValue] = Field(None)
    deprecated: Optional[bool] = Field(None)
    


@dataclass(config=PydanticConfig)
class PropertyValue:
    
    pred: Optional[str] = Field(None)
    val: Optional[str] = Field(None)
    xrefs: Optional[List[str]] = Field(None)
    meta: Optional[Meta] = Field(None)
    


@dataclass(config=PydanticConfig)
class DefinitionPropertyValue(PropertyValue):
    
    pred: Optional[str] = Field(None)
    val: Optional[str] = Field(None)
    xrefs: Optional[List[str]] = Field(None)
    meta: Optional[Meta] = Field(None)
    


@dataclass(config=PydanticConfig)
class BasicPropertyValue(PropertyValue):
    
    pred: Optional[str] = Field(None)
    val: Optional[str] = Field(None)
    xrefs: Optional[List[str]] = Field(None)
    meta: Optional[Meta] = Field(None)
    


@dataclass(config=PydanticConfig)
class XrefPropertyValue(PropertyValue):
    
    pred: Optional[str] = Field(None)
    val: Optional[str] = Field(None)
    xrefs: Optional[List[str]] = Field(None)
    meta: Optional[Meta] = Field(None)
    


@dataclass(config=PydanticConfig)
class SynonymPropertyValue(PropertyValue):
    
    synonymType: Optional[str] = Field(None)
    isExact: Optional[bool] = Field(None)
    scope: Optional[ScopesEnum] = Field(None)
    pred: Optional[str] = Field(None)
    val: Optional[str] = Field(None)
    xrefs: Optional[List[str]] = Field(None)
    meta: Optional[Meta] = Field(None)
    


@dataclass(config=PydanticConfig)
class Axiom:
    
    meta: Optional[Meta] = Field(None)
    


@dataclass(config=PydanticConfig)
class DomainRangeAxiom(Axiom):
    
    meta: Optional[Meta] = Field(None)
    


@dataclass(config=PydanticConfig)
class EquivalentNodesSet(Axiom):
    
    representitiveNodeId: Optional[str] = Field(None)
    nodeIds: Optional[List[str]] = Field(None)
    meta: Optional[Meta] = Field(None)
    


@dataclass(config=PydanticConfig)
class ExistentialRestrictionExpression:
    
    fillerId: Optional[str] = Field(None)
    propertyId: Optional[str] = Field(None)
    


@dataclass(config=PydanticConfig)
class LogicalDefinitionAxiom(Axiom):
    
    meta: Optional[Meta] = Field(None)
    


@dataclass(config=PydanticConfig)
class PropertyChainAxiom(Axiom):
    
    meta: Optional[Meta] = Field(None)
    



# Update forward refs
# see https://pydantic-docs.helpmanual.io/usage/postponed_annotations/
Graph.__pydantic_model__.update_forward_refs()
Node.__pydantic_model__.update_forward_refs()
Edge.__pydantic_model__.update_forward_refs()
Meta.__pydantic_model__.update_forward_refs()
PropertyValue.__pydantic_model__.update_forward_refs()
DefinitionPropertyValue.__pydantic_model__.update_forward_refs()
BasicPropertyValue.__pydantic_model__.update_forward_refs()
XrefPropertyValue.__pydantic_model__.update_forward_refs()
SynonymPropertyValue.__pydantic_model__.update_forward_refs()
Axiom.__pydantic_model__.update_forward_refs()
DomainRangeAxiom.__pydantic_model__.update_forward_refs()
EquivalentNodesSet.__pydantic_model__.update_forward_refs()
ExistentialRestrictionExpression.__pydantic_model__.update_forward_refs()
LogicalDefinitionAxiom.__pydantic_model__.update_forward_refs()
PropertyChainAxiom.__pydantic_model__.update_forward_refs()

