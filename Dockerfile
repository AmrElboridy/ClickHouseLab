# Dockerfile
# Author: Amr Elboridy
# Date: 2025-09-25
# Description: ClickHouse Lab container for testing Columnar DB features

FROM clickhouse/clickhouse-server:latest

# Expose default ClickHouse ports
EXPOSE 8123 9000
