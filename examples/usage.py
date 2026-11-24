"""Find a specification and its downstream path in the installed manifest."""

from ssot_pack_data_catalog_lineage_contracts import load_document_manifest

specification = next(
    row for row in load_document_manifest("spec")
    if row["id"] == "spc:dcat-dataset-metadata-requirements"
)
assert specification["target_path"] == ".ssot/specs/SPEC-2001-dcat-dataset-metadata-requirements.yaml"
