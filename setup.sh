mkdir -p ~/.streamlit/
echo "[theme]
primaryColor='#F05F40'
backgroundColor='#f6f6f6'
secondaryBackgroundColor='#ececec'
textColor='#171717'
font = 'sans serif'
[server]
headless = true
port = $PORT
enableCORS = false
" > ~/.streamlit/config.toml
