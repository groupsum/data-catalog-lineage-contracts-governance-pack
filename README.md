# ssot-pack-data-catalog-lineage-contracts

Installable SSOT governance pack for data catalogs, analytics schemas, dataset metadata, lineage, export schemas, and evidence traceability.

This repository is an installable SSOT Registry governance pack. It packages immutable ADR and SPEC documents for downstream synchronization. It intentionally does not cross-link to other governance packs.

## Pack Metadata

- Pack ID: `pack:data-catalog-lineage-contracts`
- Priority: `P2.3`
- PyPI package: `ssot-pack-data-catalog-lineage-contracts`
- Import package: `ssot_pack_data_catalog_lineage_contracts`
- GitHub repository: `groupsum/data-catalog-lineage-contracts-governance-pack`
- Reservation owner: `extension-pack:ssot-pack-data-catalog-lineage-contracts`

## Domain Focus

Data Catalog, Lineage, And Analytics Contracts

## Authority Sources

- W3C DCAT v3
- JSON Schema 2020-12
- OpenLineage specification
- CloudEvents
- GA4 BigQuery Export schema

## Included ADRs

- `adr:data-catalog-lineage-boundary` - Data Catalog Lineage Boundary
- `adr:analytics-contract-evidence-lineage` - Analytics Contract Evidence Lineage

## Included SPECs

- `spc:json-schema-analytics-contract` - JSON Schema Analytics Contract
- `spc:dcat-dataset-contract` - DCAT Dataset Contract
- `spc:openlineage-processing-contract` - OpenLineage Processing Contract
- `spc:export-schema-evidence-contract` - Export Schema Evidence Contract

## Install With uv

```bash
uv add ssot-pack-data-catalog-lineage-contracts
uv add ssot-registry ssot-pack-data-catalog-lineage-contracts
```

## Use With The SSOT Registry CLI

```bash
uvx --from ssot-registry ssot pack install ssot-pack-data-catalog-lineage-contracts
uvx --from ssot-registry ssot pack sync . ssot-pack-data-catalog-lineage-contracts
uv run ssot adr list .
uv run ssot spec list .
```

## Programmatic Usage

```python
from ssot_pack_data_catalog_lineage_contracts import load_document_manifest

adr_manifest = load_document_manifest("adr")
spec_manifest = load_document_manifest("spec")
```

## Resources

- GitHub repository: https://github.com/groupsum/data-catalog-lineage-contracts-governance-pack
- PyPI package: https://pypi.org/project/ssot-pack-data-catalog-lineage-contracts/
- SSOT Registry: https://pypi.org/project/ssot-registry/
