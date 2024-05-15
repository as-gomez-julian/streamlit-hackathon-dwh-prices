MAIN_QUERY = """--sql
SELECT
  country_name,
  retailer_name,
  store_key,
  master_store_id,
  store_name,
  full_date,
  category_name,
  product_name,
  ean_sku_code,
  product_current_price,
FROM
  `prod-shelftia-as.flattening_data.dw_hktn_prices`
  LIMIT 100000
"""