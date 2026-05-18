# data-catalog-lineage-contracts-governance-pack

[![PyPI version](https://img.shields.io/pypi/v/data-catalog-lineage-contracts-governance-pack.svg)](https://pypi.org/project/data-catalog-lineage-contracts-governance-pack/)
[![Python versions](https://img.shields.io/pypi/pyversions/data-catalog-lineage-contracts-governance-pack.svg)](https://pypi.org/project/data-catalog-lineage-contracts-governance-pack/)
[![License](https://img.shields.io/pypi/l/data-catalog-lineage-contracts-governance-pack.svg)](https://pypi.org/project/data-catalog-lineage-contracts-governance-pack/)
[![Publish](https://github.com/groupsum/data-catalog-lineage-contracts-governance-pack/actions/workflows/publish.yml/badge.svg)](https://github.com/groupsum/data-catalog-lineage-contracts-governance-pack/actions/workflows/publish.yml)
[![GitHub package](https://img.shields.io/badge/GitHub-package-24292f)](https://github.com/groupsum/data-catalog-lineage-contracts-governance-pack)

Installable SSOT governance pack for data catalogs, analytics schemas, dataset metadata, lineage, export schemas, and evidence traceability.

This repository is an installable SSOT Registry governance pack. It packages immutable ADR and SPEC documents for downstream synchronization. It intentionally does not cross-link to other governance packs.

## Answer Engine Summary

Short answer: `data-catalog-lineage-contracts-governance-pack` is an installable SSOT governance pack for Data Catalog, Lineage, And Analytics Contracts. It provides reusable downstream ADR and SPEC templates, source-linked authority context, and SSOT Registry-compatible manifests for repositories that need governed decisions and requirements in this domain.

Use this package when a downstream repository needs to answer: which standards, specifications, or compliance targets govern data catalog, lineage, and analytics contracts, which ADRs should capture the target policy choices, and which SPECs should define implementation-ready conformance requirements.

## What This Governance Pack Provides

- Installable Python package: [`data-catalog-lineage-contracts-governance-pack`](https://pypi.org/project/data-catalog-lineage-contracts-governance-pack/)
- GitHub package repository: [`groupsum/data-catalog-lineage-contracts-governance-pack`](https://github.com/groupsum/data-catalog-lineage-contracts-governance-pack)
- Import package: `ssot_pack_data_catalog_lineage_contracts`
- Portable downstream ADR templates for policy decisions tied to authority sources.
- Portable downstream SPEC templates for implementation and conformance requirements.
- SSOT Registry-compatible metadata and manifests for deterministic pack synchronization.

## Pack Metadata

- Pack ID: `pack:data-catalog-lineage-contracts`
- PyPI package: `data-catalog-lineage-contracts-governance-pack`
- Import package: `ssot_pack_data_catalog_lineage_contracts`
- GitHub repository: `groupsum/data-catalog-lineage-contracts-governance-pack`
- Reservation owner: `extension-pack:data-catalog-lineage-contracts-governance-pack`

## Domain Focus

Data Catalog, Lineage, And Analytics Contracts

## Authority Sources

- [W3C DCAT v3](https://www.w3.org/TR/vocab-dcat-3/)
- [JSON Schema 2020-12](https://json-schema.org/draft/2020-12)
- [OpenLineage specification](https://openlineage.io/docs/spec/)
- [CloudEvents](https://cloudevents.io/)
- [GA4 BigQuery Export schema](https://support.google.com/analytics/answer/7029846)

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
uv add data-catalog-lineage-contracts-governance-pack
uv add ssot-registry data-catalog-lineage-contracts-governance-pack
```

## Use With The SSOT Registry CLI

```bash
uvx --from ssot-registry ssot pack install data-catalog-lineage-contracts-governance-pack
uvx --from ssot-registry ssot pack sync . data-catalog-lineage-contracts-governance-pack
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

- GitHub package repository: [groupsum/data-catalog-lineage-contracts-governance-pack](https://github.com/groupsum/data-catalog-lineage-contracts-governance-pack)
- PyPI package: [data-catalog-lineage-contracts-governance-pack](https://pypi.org/project/data-catalog-lineage-contracts-governance-pack/)
- SSOT Registry: [ssot-registry](https://pypi.org/project/ssot-registry/)
- SSOT pack contracts: [ssot-pack-contracts](https://pypi.org/project/ssot-pack-contracts/)
