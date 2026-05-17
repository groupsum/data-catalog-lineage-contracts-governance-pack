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

- `adr:dcat-dataset-catalog-metadata-policy` - DCAT Dataset Catalog Metadata Policy
- `adr:json-schema-analytics-contract-policy` - JSON Schema Analytics Contract Policy
- `adr:json-schema-compatibility-and-versioning-policy` - JSON Schema Compatibility And Versioning Policy
- `adr:openlineage-job-run-lineage-policy` - OpenLineage Job Run Lineage Policy
- `adr:cloudevents-analytics-envelope-policy` - CloudEvents Analytics Envelope Policy
- `adr:ga4-bigquery-export-schema-policy` - GA4 BigQuery Export Schema Policy
- `adr:analytics-export-evidence-lineage-policy` - Analytics Export Evidence Lineage Policy
- `adr:data-contract-audit-evidence-policy` - Data Contract Audit Evidence Policy

## Included SPECs

- `spc:dcat-dataset-metadata-requirements` - DCAT Dataset Metadata Requirements
- `spc:dcat-distribution-and-data-service-requirements` - DCAT Distribution And Data Service Requirements
- `spc:json-schema-document-identity-requirements` - JSON Schema Document Identity Requirements
- `spc:json-schema-payload-validation-requirements` - JSON Schema Payload Validation Requirements
- `spc:json-schema-contract-versioning-requirements` - JSON Schema Contract Versioning Requirements
- `spc:openlineage-run-event-requirements` - OpenLineage Run Event Requirements
- `spc:openlineage-dataset-facet-requirements` - OpenLineage Dataset Facet Requirements
- `spc:cloudevents-core-attribute-requirements` - CloudEvents Core Attribute Requirements
- `spc:cloudevents-json-http-binding-requirements` - CloudEvents JSON HTTP Binding Requirements
- `spc:ga4-bigquery-export-event-schema-requirements` - GA4 BigQuery Export Event Schema Requirements
- `spc:analytics-export-reconciliation-requirements` - Analytics Export Reconciliation Requirements
- `spc:data-contract-lineage-audit-evidence-requirements` - Data Contract Lineage Audit Evidence Requirements

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
