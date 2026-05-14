from airflow.sdk import Asset
from src.env import ENV

saturn_slc_ready_asset = Asset(f"{ENV}_saturn_slc_ready_asset")
segment_EQU_ready_asset = Asset(f"{ENV}_segment_EQU_ready_asset")
segment_WAR_ready_asset = Asset(f"{ENV}_segment_WAR_ready_asset")
segment_BLK_ready_asset = Asset(f"{ENV}_segment_BLK_ready_asset")
segment_FXI_ready_asset = Asset(f"{ENV}_segment_FXI_ready_asset")
segment_ETF_ready_asset = Asset(f"{ENV}_segment_ETF_ready_asset")