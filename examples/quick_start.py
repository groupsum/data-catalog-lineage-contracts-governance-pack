"""Inspect the installed pack identity."""

from ssot_pack_data_catalog_lineage_contracts import load_pack_metadata

metadata = load_pack_metadata()
assert metadata["origin"]["id"] == "pack:data-catalog-lineage-contracts"
print(metadata["origin"]["id"])
