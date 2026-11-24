"""Resolve and read a packaged specification without synchronizing it."""

from ssot_pack_data_catalog_lineage_contracts import load_document_manifest, read_packaged_document_text

spec = next(row for row in load_document_manifest("spec") if row["id"] == "spc:dcat-dataset-metadata-requirements")
document = read_packaged_document_text("spec", spec["filename"])
assert spec["id"] in document
